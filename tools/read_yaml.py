import os

import yaml

from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    arr = []
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f).values()
        for a in data:
            arr.append(tuple(a.values()))

    return arr


if __name__ == "__main__":
    print(read_yaml("mp_login.yaml"))
