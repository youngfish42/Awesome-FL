import subprocess
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
    """Read yaml file"""
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def write_yaml(yaml_file, data):
    """Write yaml file"""
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


def get_substr_before(src: str, split_str: str):
    """Get substring before split_str"""
    idx = src.find(split_str)
    if idx == -1:
        return src
    return src[:idx]


def get_substr_after(src: str, split_str: str):
    """Get substring after split_str"""
    idx = src.find(split_str)
    if idx == -1:
        return src
    return src[idx + len(split_str) :]


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
    """Parse header string to yaml key"""
    # to lower case || TL;DR -> tldr || " " -> "_"
    return header_str.strip().lower().replace(" ", "_").replace(";", "")


def mdtable_to_yaml(table_content: str, md_ref: dict):
    """Convert markdown table to yaml"""

    # parse table to list
    table_list = []
    for line in table_content.splitlines():
        if line.startswith("|"):  # skip empty line
            table_list.append(line.strip("|").strip().split("|"))

    # check table exist
    if len(table_list) == 0:
        return {}, md_ref

    # get table header and body
    table_header = table_list[0]  # header
    table_line = table_list[1]  # line length
    table_body = table_list[2:]  # body

    header_alias = {}
    for i, header in enumerate(table_header):
        # parse header to yaml key
        header_alias[i] = parse_header(header)

    # parse table body to dict
    data = {}
    data["header"] = {}
    for i, header in enumerate(table_header):
        # save header
        data["header"][header_alias[i]] = header

    data["length"] = {}
    for i, line in enumerate(table_line):
        # count and save line length
        data["length"][header_alias[i]] = len(line.strip())

    data["body"] = []
    for line in table_body:
        line_dict = {}
        for i, item in enumerate(line):
            if header_alias[i] == "tldr" and len(item.strip()) > 0:
                # special handle for tldr
                # abbr[^abbr] -> abbr || " " -> "-" || "+" -> "plus"
                abbr = (
                    item.strip()
                    .split("[")[0]
                    .strip()
                    .replace(" ", "-")
                    .replace("+", "plus")
                )
                if not abbr in md_ref:
                    # can not find abbr in md_ref
                    print(f"can not find {abbr} in md_ref")
                    # default value
                    md_ref[abbr] = "TBC"

                # save content
                line_dict[header_alias[i]] = f"{abbr}: {md_ref[abbr]}"
                continue

            if header_alias[i] == "materials":
                # special handle for materials

                # get links in materials
                get_links = re.findall(r"\[.*?\]\(.*?\)", item.strip())

                links = {}
                for link in get_links:
                    # parse link to dict, split by "]("
                    # [[link]](url) || [[link](url)] || [link](url) -> {link: url}
                    text = get_substr_before(link, "](").strip("[]").strip()
                    url = get_substr_after(link, "](").strip(")").strip()
                    # to upper case
                    links[text.upper()] = url

                line_dict[header_alias[i]] = links
                continue

            # other cases
            line_dict[header_alias[i]] = item.strip()

        data["body"].append(line_dict)

    return data, md_ref


def yaml_to_mdtable(yaml_data: dict, md_ref: str):
    """Convert yaml to markdown table"""

    # check yaml data exist
    if len(yaml_data) == 0:
        return "", md_ref

    # get table header and body
    table_header = yaml_data["header"]  # header
    table_line = yaml_data["length"]  # line length
    table_body = yaml_data["body"]  # body

    # parse table body to dict
    table_list = []

    # header
    table_list.append("|" + "|".join(table_header.values()) + "|")

    # line length
    table_list.append(
        "| " + " | ".join(["-" * line for line in table_line.values()]) + " |"
    )

    for line in table_body:
        for key in table_header.keys():
            if key == "tldr":
                # special handle for tldr
                # split by first ":"
                abbr = get_substr_before(line[key], ":").strip()

                if len(abbr) > 0:
                    # save abbr to md_ref
                    md_ref += f"[^{abbr}]: {get_substr_after(line[key], ':').strip()}\n"
                    # revert "plus" to "+"
                    line[key] = f"{abbr.replace('plus', '+')}[^{abbr}]"
                else:
                    # empty abbr
                    line[key] = ""

            if key == "materials":
                # special handle for materials
                links = []

                if type(line[key]) is not dict:
                    # wrong type
                    print(f"materials is str, please check it: {line[key]}")
                else:
                    # parse dict to str
                    for text, url in line[key].items():
                        links.append(f"[[{text}]({url})]")
                line[key] = " ".join(links)

        # other cases
        table_list.append("| " + " | ".join(line.values()) + " |")

    return "\n".join(table_list), md_ref


def get_mdref(md_str: str, start_comment: str, end_comment: str):
    """Get md ref from md_str"""
    ref_content = get_content(md_str, start_comment, end_comment)

    ref_dict = {}
    for line in ref_content.splitlines():
        # skip empty line
        if line.startswith("["):
            # get abbr and content
            # [^abbr]: content -> {abbr: content}
            # abbr: " " -> "-" || "+" -> "plus" || "^" -> "" || "[]" -> ""
            # split by first "]:"
            abbr = (
                get_substr_before(line, "]:")
                .strip("[]")
                .replace("^", "")
                .strip()
                .replace(" ", "-")
                .replace("+", "plus")
            )
            # split by first "]:"
            cont = get_substr_after(line, "]:").strip()
            if len(cont) == 0:
                # empty content
                print(f"can not find content for {abbr}")
                # default value
                cont = "TBC"
            ref_dict[abbr] = cont

    return ref_dict


def write_mdref(md_ref: dict):
    """Write md ref to README.md"""
    ref_list = []
    for key, value in md_ref.items():
        # parse [^abbr]: content
        ref_list.append(f"[^{key}]: {value}")

    return "\n".join(ref_list)


def get_git_log_time(file_path: str):
    """Get git log time"""
    cmd = f"git log -1 --format=%cd --date=iso {file_path}"
    resp = subprocess.check_output(cmd, shell=True)
    return resp.decode("utf-8").strip()
