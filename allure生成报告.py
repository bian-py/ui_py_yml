import json
import os

# os.system("allure serve report")
os.system("allure generate ./temp -o ./report --clean ")


# os.system(r"xcopy .\allure-report\history .\allure-results\history /e /Y /I")
def display_trends():
    with open("./report/widgets/history-trend.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    try:
        with open("./data/allure_history.json", "r", encoding="utf-8") as f:
            arr = json.load(f)
        data.extend(arr)
        with open("./data/allure_history.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
    except:
        with open("./data/allure_history.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

    with open("./data/allure_history.json", "r", encoding="utf-8") as f:
        result = json.load(f)
    with open("./report/widgets/history-trend.json", "w", encoding="utf-8") as f:
        json.dump(result, f)


display_trends()
