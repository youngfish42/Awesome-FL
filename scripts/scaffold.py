import os
from config import Config
import utils


class Scaffold:
    def __init__(self):
        pass

    def mdtable_to_yaml(self, md_file=None, yaml_file=None):
        md_file = md_file or Config.README_PATH
        yaml_file = yaml_file or Config.YAML_PATH

        md_str = utils.read_mdfile(md_file)
        data = utils.read_yaml(yaml_file)

        md_ref = utils.get_mdref(
            md_str,
            Config.START_COMMENT.format("reference-section"),
            Config.END_COMMENT.format("reference-section"),
        )

        for sec in data["section"]:
            print(sec["title"])

            table_content = utils.get_content(
                md_str,
                Config.START_COMMENT.format(sec["title"]),
                Config.END_COMMENT.format(sec["title"]),
            )

            yaml_content, md_ref = utils.mdtable_to_yaml(table_content, md_ref)

            data[sec["title"]] = yaml_content

        utils.write_yaml(yaml_file, data)

    def yaml_to_mdtable(self, yaml_file=None, md_file=None):
        yaml_file = yaml_file or Config.YAML_PATH
        md_file = md_file or Config.README_PATH

        data = utils.read_yaml(yaml_file)
        md_str = utils.read_mdfile(md_file)
        md_ref = ""

        for sec in data["section"]:
            print(sec["title"])

            table_content, md_ref = utils.yaml_to_mdtable(data[sec["title"]], md_ref)

            md_str = utils.replace_content(
                md_str,
                table_content,
                Config.START_COMMENT.format(sec["title"]),
                Config.END_COMMENT.format(sec["title"]),
            )

        md_str = utils.replace_content(
            md_str,
            md_ref,
            Config.START_COMMENT.format("reference-section"),
            Config.END_COMMENT.format("reference-section"),
        )

        utils.write_mdfile(md_file, md_str)

    def clear(self):
        data = utils.read_yaml(Config.YAML_PATH)
        data_ = {}
        data_["section"] = data["section"]
        utils.write_yaml(Config.YAML_PATH, data_)

    def merge_md_yaml(self, md_file=None, yaml_file=None, env="prod"):
        md_file = md_file or Config.README_PATH
        yaml_file = yaml_file or Config.YAML_PATH

        # get latest file
        priority = [Config.README_PATH, Config.YAML_PATH]

        if env == "dev":
            priority.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        # else:
        #     priority.sort(key=lambda x: utils.get_git_log_time(x), reverse=True)

        for file in priority:
            print(file, os.path.getmtime(file), utils.get_git_log_time(file))

        if priority[0] == Config.README_PATH:
            print("merge md to yaml")
            self.mdtable_to_yaml(md_file, yaml_file)

        self.yaml_to_mdtable(yaml_file, md_file)
