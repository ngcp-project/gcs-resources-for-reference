from codecs import decode
import os
import subprocess 

WEBSITE_URL = "https://ngcp-project.github.io"
ROOT_DIR = decode(subprocess.check_output(["sh", "-c", "git rev-parse --show-toplevel"]))[:-1]


def main():
    dirs_dict = {}
    content = ""
    for (root, _, files) in os.walk(ROOT_DIR):
        md_list = [f for f in files if ".md" in f]
        if len(md_list) > 0: dirs_dict[root.replace(ROOT_DIR, "")] = md_list

    with open(f"{ROOT_DIR}/README.md", "r") as file:
        content = file.read()
    for (root, files) in dirs_dict.items():
        layers = root.count("/")

        index_page_name = root.split("/")[-1]
        if root != "":
            if "index.md" in files:
                files.remove("index.md")
                content += "\t"*(layers-1) + f"- [{index_page_name}]({WEBSITE_URL}{root})\n"
            else:
                content += "\t"*(layers-1) + f"- {index_page_name}\n" 

        for f in files:
            file_name = f.replace(".md", "")
            content += "\t"*layers + f"- [{file_name}]({WEBSITE_URL}{root}/{file_name})" + "\n"

    with open("../README.md", "w") as file:
        file.write(content)

if __name__ == '__main__':
    main()