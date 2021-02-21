import dotenv
import os
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter


dotenv.load_dotenv()

slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events')

client = WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel='test-bot', text="hello again")
@slack_event_adapter.on('message')
def message(payload):
    print("Hello")
    text = "Hello there!"
    client.chat_postMessage(channel='test-bot', text=text)

slack_event_adapter.start(port=5000)