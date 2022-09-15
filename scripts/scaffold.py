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

        for sec in data["section"]:
            print(sec["title"])

            table_content = utils.get_content(
                md_str,
                Config.START_COMMENT.format(sec["title"]),
                Config.END_COMMENT.format(sec["title"]),
            )

            yaml_content = {sec["title"]: utils.mdtable_to_yaml(table_content)}

            data.update(yaml_content)

        utils.write_yaml(yaml_file, data)

    def yaml_to_mdtable(self, yaml_file, md_file):
        pass

    def clear(self):
        data = utils.read_yaml(Config.YAML_PATH)
        data_ = {}
        data_["section"] = data["section"]
        utils.write_yaml(Config.YAML_PATH, data_)
