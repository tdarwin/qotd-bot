import requests
import json
import os

slack_url = os.getenv("SLACK_URL")
slack_channel = os.getenv("SLACK_CHANNEL")
convo_starter_url = os.getenv("CONVO_STARTER_URL")
rapidapi_key = os.getenv("RAPIDAPI_KEY")
rapidapi_host = os.getenv("RAPIDAPI_HOST")


def get_question(url):
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": rapidapi_host
    }
    r = requests.request("GET", url, headers=headers)
    response = json.loads(r.text)
    return response['question']


def post_to_slack(question, channel, url):
    p = {
        "channel": str(channel),
        "username": "QOTD",
        "icon_emoji": ":interrobang:",
        "attachments": [
            {
                "fallback": "Here's the question of the day, respond in channel:",
                "pretext": "Here's the question of the day, respond in channel:",
                "color": "#00FF00",
                "fields": [
                    {
                        "title": "Question",
                        "value": str(question),
                        "short": False
                    }
                ]
            }
        ]
    }
    payload = json.dumps(p)

    s = requests.post(url, data=payload)
    return s.status_code


question = get_question(convo_starter_url)
print(question)

post_to_slack(question, slack_channel, slack_url)
