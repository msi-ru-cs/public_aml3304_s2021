import slack
import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask
from slackeventsapi import SlackEventAdapter


env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

# clint.chat_postMessage(channel='#channel_bot_3304', text="Welcome to the Bot channel!!!")

@ slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text.upper() + " " + user_id)

if __name__ == "__main__":
    app.run(debug=True)