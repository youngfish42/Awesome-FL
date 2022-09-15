import os


class Config:
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    README_PATH = os.path.join(ROOT_PATH, "README.md")
    YAML_PATH = os.path.join(ROOT_PATH, "data.yaml")
    START_COMMENT = "<!-- START:{} -->"
    END_COMMENT = "<!-- END:{} -->"
