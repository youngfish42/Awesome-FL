import contextlib
import importlib
import io
import json
import os
import runpy
import sys
import tempfile
import types
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT_DIR / "add_dependent.py"


class MockHTTPError(Exception):
    def __init__(self, response):
        super().__init__(f"HTTP {response.status_code}")
        self.response = response


class MockResponse:
    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise MockHTTPError(self)

    def json(self):
        return self.payload


def run_add_dependent(readme_links, routes):
    requests_module = types.ModuleType("requests")
    requests_module.exceptions = types.SimpleNamespace(HTTPError=MockHTTPError)

    def get(url, headers=None):
        if url not in routes:
            raise AssertionError(f"unexpected URL requested: {url}")
        route = routes[url]
        return MockResponse(route["json"], route.get("status_code", 200))

    requests_module.get = get

    real_time = importlib.import_module("time")
    time_module = types.ModuleType("time")
    for name in dir(real_time):
        setattr(time_module, name, getattr(real_time, name))
    time_module.sleep = lambda *_args, **_kwargs: None

    old_requests = sys.modules.get("requests")
    old_time = sys.modules.get("time")
    cwd = os.getcwd()

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        (tmpdir_path / "README.md").write_text(
            "\n".join(f"({link})" for link in readme_links) + "\n",
            encoding="utf-8",
        )

        sys.modules["requests"] = requests_module
        sys.modules["time"] = time_module
        os.chdir(tmpdir_path)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                runpy.run_path(str(SCRIPT_PATH), run_name="__main__")
            return {
                "go_mod": (tmpdir_path / "go.mod").read_text(encoding="utf-8"),
                "provenance": json.loads(
                    (tmpdir_path / "go.mod.provenance.json").read_text(encoding="utf-8")
                ),
            }
        finally:
            os.chdir(cwd)
            if old_requests is None:
                sys.modules.pop("requests", None)
            else:
                sys.modules["requests"] = old_requests
            if old_time is None:
                sys.modules.pop("time", None)
            else:
                sys.modules["time"] = old_time


def test_writes_full_commit_provenance_for_dependency_identity():
    result = run_add_dependent(
        ["https://github.com/trusted/acme-lib"],
        {
            "https://api.github.com/repos/trusted/acme-lib/commits/main": {
                "json": {
                    "sha": "deadbeefcafebabefeed11111111111111111111",
                    "commit": {
                        "committer": {
                            "date": "2024-05-01T12:30:00Z",
                        },
                    },
                },
            },
            "https://api.github.com/repos/trusted/acme-lib/tags": {
                "json": [
                    {
                        "name": "v1.2.3",
                    },
                ],
            },
        },
    )

    assert (
        "github.com/trusted/acme-lib v1.2.3-20240501123000-deadbeefcafe // indirect"
        in result["go_mod"]
    )
    assert result["provenance"]["schema_version"] == 1
    assert result["provenance"]["dependencies"] == [
        {
            "module": "github.com/trusted/acme-lib",
            "version": "v1.2.3",
            "commit_timestamp": "20240501123000",
            "short_commit_sha": "deadbeefcafe",
            "full_commit_sha": "deadbeefcafebabefeed11111111111111111111",
            "resolved_ref": "main",
        },
    ]


def test_records_master_fallback_ref_in_provenance():
    result = run_add_dependent(
        ["https://github.com/trusted/acme-lib"],
        {
            "https://api.github.com/repos/trusted/acme-lib/commits/main": {
                "status_code": 422,
                "json": {},
            },
            "https://api.github.com/repos/trusted/acme-lib/commits/master": {
                "json": {
                    "sha": "deadbeefcafe9999222222222222222222222222",
                    "commit": {
                        "committer": {
                            "date": "2024-05-01T12:30:00Z",
                        },
                    },
                },
            },
            "https://api.github.com/repos/trusted/acme-lib/tags": {
                "json": [
                    {
                        "name": "v1.2.3",
                    },
                ],
            },
        },
    )

    dependency = result["provenance"]["dependencies"][0]
    assert dependency["resolved_ref"] == "master"
    assert dependency["full_commit_sha"] == "deadbeefcafe9999222222222222222222222222"
