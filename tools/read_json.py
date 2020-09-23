import json


class ReadJson:
    @staticmethod
    def read_json(filename):
        with open("./data/" + filename, "r", encoding='utf-8') as f:
            data = json.load(f)

        return data


if __name__ == '__main__':
    print(ReadJson.read_json('mp_login.json'))
