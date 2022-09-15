import yaml
import os
import re


def read_mdfile(md_file: str):
    """Read markdown file"""
    with open(md_file, "r", encoding="utf-8") as f:
        md_str = f.read()
    return md_str


def read_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def write_yaml(yaml_file, data):
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


def get_content(src: str, start_comment: str, end_comment: str):
    """Get content between start and end comment"""
    pattern = f"{start_comment}[\\s\\S]+{end_comment}"

    if re.search(pattern, src) is None:
        print(
            f"can not find comment in src, please check it, it should be {start_comment} and {end_comment}"
        )

    return re.search(pattern, src).group(0)


def replace_content(src: str, content: str, start_comment: str, end_comment: str):
    """Replace content between start and end comment"""
    pattern = f"{start_comment}[\\s\\S]+{end_comment}"
    repl = f"{start_comment}\n\n{content}\n\n{end_comment}"

    if re.search(pattern, src) is None:
        print(
            f"can not find comment in src, please check it, it should be {start_comment} and {end_comment}"
        )

    return re.sub(pattern, repl, src)


def parse_header(header_str: str):
    return header_str.strip().lower().replace(" ", "_").replace(";", "")


def mdtable_to_yaml(table_content: str):
    """Convert markdown table to yaml"""

    # parse table to list
    table_list = []
    for line in table_content.splitlines():
        if line.startswith("|"):
            table_list.append(line.strip("|").strip().split("|"))

    # check table exist
    if len(table_list) == 0:
        return {}

    # get table header and body
    table_header = table_list[0]
    table_line = table_list[1]
    table_body = table_list[2:]

    header_alias = {}
    for i, header in enumerate(table_header):
        header_alias[i] = parse_header(header)

    # parse table body to dict
    data = {}
    data["header"] = {}
    for i, header in enumerate(table_header):
        data["header"][header_alias[i]] = header

    data["length"] = {}
    for i, line in enumerate(table_line):
        data["length"][header_alias[i]] = len(line.strip())

    data["body"] = []
    for line in table_body:
        line_dict = {}
        for i, item in enumerate(line):
            line_dict[header_alias[i]] = item.strip()
        data["body"].append(line_dict)

    return data
