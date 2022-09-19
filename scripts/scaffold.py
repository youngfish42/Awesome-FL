import os
from config import Config
import utils


class Scaffold:
    def __init__(self):
        pass

    def mdtable_to_yaml(self, md_file=None, yaml_file=None):
        """convert markdown table to yaml file"""
        md_file = md_file or Config.README_PATH  # README.md
        yaml_file = yaml_file or Config.YAML_PATH  # data.yaml

        md_str = utils.read_mdfile(md_file)  # read README.md
        data = utils.read_yaml(yaml_file)  # read data.yaml

        # get reference section
        md_ref = utils.get_mdref(
            md_str,
            Config.START_COMMENT.format("reference-section"),
            Config.END_COMMENT.format("reference-section"),
        )

        # iterate section
        for sec in data["section"]:
            print(sec["title"])

            # get table content
            table_content = utils.get_content(
                md_str,
                Config.START_COMMENT.format(sec["title"]),
                Config.END_COMMENT.format(sec["title"]),
            )
            # parse table to yaml
            yaml_content, md_ref = utils.mdtable_to_yaml(table_content, md_ref)
            # update yaml
            data[sec["title"]] = yaml_content

        # save yaml
        utils.write_yaml(yaml_file, data)

    def yaml_to_mdtable(self, yaml_file=None, md_file=None):
        """convert yaml file to markdown table"""
        yaml_file = yaml_file or Config.YAML_PATH  # data.yaml
        md_file = md_file or Config.README_PATH  # README.md

        # read yaml
        data = utils.read_yaml(yaml_file)
        # read md
        md_str = utils.read_mdfile(md_file)
        # get reference section
        md_ref = ""

        for sec in data["section"]:
            print(sec["title"])

            # get markdown table content
            table_content, md_ref = utils.yaml_to_mdtable(data[sec["title"]], md_ref)

            # update markdown
            md_str = utils.replace_content(
                md_str,
                table_content,
                Config.START_COMMENT.format(sec["title"]),
                Config.END_COMMENT.format(sec["title"]),
            )

        # update reference section
        md_str = utils.replace_content(
            md_str,
            md_ref,
            Config.START_COMMENT.format("reference-section"),
            Config.END_COMMENT.format("reference-section"),
        )

        # save md
        utils.write_mdfile(md_file, md_str)

    def clear(self):
        """clear all data"""

        data = utils.read_yaml(Config.YAML_PATH)  # read yaml

        data_ = {}
        data_["section"] = data["section"]  # only keep section
        utils.write_yaml(Config.YAML_PATH, data_)

    def merge_md_yaml(self, md_file=None, yaml_file=None, env="prod"):
        """Merge markdown table to yaml file"""
        md_file = md_file or Config.README_PATH  # README.md
        yaml_file = yaml_file or Config.YAML_PATH  # data.yaml

        # file priority
        priority = [Config.README_PATH, Config.YAML_PATH]

        if env == "dev":
            # local mode | dev: sort by file modify time
            priority.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        else:
            # prod mode | sort by file modify time in git
            priority.sort(key=lambda x: utils.get_git_log_time(x), reverse=True)

        # log file priority
        for file in priority:
            print(file, os.path.getmtime(file), utils.get_git_log_time(file))

        if priority[0] == Config.README_PATH:
            # markdown table is newer, merge to yaml
            print("merge md to yaml")
            self.mdtable_to_yaml(md_file, yaml_file)

        # format markdown table
        self.yaml_to_mdtable(yaml_file, md_file)
