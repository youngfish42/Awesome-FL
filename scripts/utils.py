import yaml
import os
import re


def read_mdfile(md_file: str):
    """Read markdown file"""
    with open(md_file, "r", encoding="utf-8") as f:
        md_str = f.read()
    return md_str


def write_mdfile(md_file: str, md_str: str):
    """Write markdown file"""
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_str)


def read_yaml(yaml_file):
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def write_yaml(yaml_file, data):
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


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


def mdtable_to_yaml(table_content: str, md_ref: dict):
    """Convert markdown table to yaml"""

    # parse table to list
    table_list = []
    for line in table_content.splitlines():
        if line.startswith("|"):
            table_list.append(line.strip("|").strip().split("|"))

    # check table exist
    if len(table_list) == 0:
        return {}, md_ref

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
            if header_alias[i] == "tldr" and len(item.strip()) > 0:
                abbr = item.strip().split("[")[0].strip().replace(" ", "-")
                if not abbr in md_ref:
                    print(f"can not find {abbr} in md_ref")
                    md_ref[abbr] = "TBC"
                line_dict[header_alias[i]] = f"{abbr}: {md_ref[abbr]}"
                continue

            if header_alias[i] == "materials":
                get_links = re.findall(r"\[.*?\]\(.*?\)", item.strip())
                links = {}
                for link in get_links:
                    text = link.split("]")[0].strip("[").strip()
                    url = link.split("(")[1].strip(")").strip()
                    links[text.upper()] = url
                line_dict[header_alias[i]] = links
                continue

            line_dict[header_alias[i]] = item.strip()

        data["body"].append(line_dict)

    return data, md_ref


def yaml_to_mdtable(yaml_data: dict):
    """Convert yaml to markdown table"""

    # check yaml data exist
    if len(yaml_data) == 0:
        return ""

    # get table header and body
    table_header = yaml_data["header"]
    table_line = yaml_data["length"]
    table_body = yaml_data["body"]

    # parse table body to dict
    table_list = []
    table_list.append("| " + " | ".join(table_header.values()) + " |")
    table_list.append(
        "| " + " | ".join(["-" * line for line in table_line.values()]) + " |"
    )
    for line in table_body:
        for key in table_header.keys():
            if key == "tldr":
                abbr = line[key].split(":")[0].strip()
                if len(abbr) > 0:
                    line[key] = f"{abbr}[^{abbr}]"
                else:
                    line[key] = ""

            if key == "materials":
                links = []
                if type(line[key]) is not dict:
                    print(f"materials is str, please check it: {line[key]}")
                else:
                    for text, url in line[key].items():
                        links.append(f"[[{text}]({url})]")
                line[key] = " ".join(links)

        table_list.append("| " + " | ".join(line.values()) + " |")

    return "\n".join(table_list)


def get_mdref(md_str: str, start_comment: str, end_comment: str):
    ref_content = get_content(md_str, start_comment, end_comment)

    ref_dict = {}
    for line in ref_content.splitlines():
        if line.startswith("["):
            abbr = (
                line.split("]:")[0]
                .strip("[]")
                .replace("^", "")
                .strip()
                .replace(" ", "")
            )
            cont = line.split("]:")[1].strip()
            if len(cont) == 0:
                print(f"can not find content for {abbr}")
                cont = "TBC"
            ref_dict[abbr] = cont

    return ref_dict


def write_mdref(md_ref: dict):
    ref_list = []
    for key, value in md_ref.items():
        ref_list.append(f"[^{key}]: {value}")

    return "\n".join(ref_list)
