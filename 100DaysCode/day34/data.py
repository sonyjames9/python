import requests


def question_data():
    parameters = {
        "amount": 10,
        "type": "boolean"
    }

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    questions_data = data["results"]
    # print(questions_data)
    return questions_data
