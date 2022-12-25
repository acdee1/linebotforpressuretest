import os
import sys
from flask import Flask, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,MessageTemplateAction
from utils import send_text_message,send_button_message
from fsm import TocMachine
load_dotenv()

machine = TocMachine(
    states=['user','test','question1','question2','question3','question4','question5','question6','question7','question8','question9','question10','result','familyquestion1','familyquestion2','familyquestion3','familyquestion4','familyquestion5','familyquestion6','familyquestion7','familyquestion8','familyquestion9','familyquestion10','familyresult','workquestion1','workquestion2','workquestion3','workquestion4','workquestion5','workquestion6','workquestion7','workquestion8','workquestion9','workquestion10','workresult'],
    transitions=[{'trigger': 'advance', 'source': 'user', 'dest':'test', 'conditions':'is_going_to_test'},
                 {'trigger': 'advance', 'source': 'test', 'dest':'question1', 'conditions':'is_going_to_question1'},
                 {'trigger': 'advance', 'source': 'question1', 'dest':'question2', 'conditions':'is_going_to_question2'},
                 {'trigger': 'advance', 'source': 'question2', 'dest':'question1', 'conditions':'back_to_question1'},
                 {'trigger': 'advance', 'source': 'question2', 'dest':'question3', 'conditions':'is_going_to_question3'},
                 {'trigger': 'advance', 'source': 'question3', 'dest':'question2', 'conditions':'back_to_question2'},
                 {'trigger': 'advance', 'source': 'question3', 'dest':'question4', 'conditions':'is_going_to_question4'},
                 {'trigger': 'advance', 'source': 'question4', 'dest':'question3', 'conditions':'back_to_question3'},
                 {'trigger': 'advance', 'source': 'question4', 'dest':'question5', 'conditions':'is_going_to_question5'},
                 {'trigger': 'advance', 'source': 'question5', 'dest':'question4', 'conditions':'back_to_question4'},
                 {'trigger': 'advance', 'source': 'question5', 'dest':'question6', 'conditions':'is_going_to_question6'},
                 {'trigger': 'advance', 'source': 'question6', 'dest':'question5', 'conditions':'back_to_question5'},
                 {'trigger': 'advance', 'source': 'question6', 'dest':'question7', 'conditions':'is_going_to_question7'},
                 {'trigger': 'advance', 'source': 'question7', 'dest':'question6', 'conditions':'back_to_question6'},
                 {'trigger': 'advance', 'source': 'question7', 'dest':'question8', 'conditions':'is_going_to_question8'},
                 {'trigger': 'advance', 'source': 'question8', 'dest':'question7', 'conditions':'back_to_question7'},
                 {'trigger': 'advance', 'source': 'question8', 'dest':'question9', 'conditions':'is_going_to_question9'},
                 {'trigger': 'advance', 'source': 'question9', 'dest':'question8', 'conditions':'back_to_question8'},
                 {'trigger': 'advance', 'source': 'question9', 'dest':'question10', 'conditions':'is_going_to_question10'},
                 {'trigger': 'advance', 'source': 'question10', 'dest':'question9', 'conditions':'back_to_question9'},
                 {'trigger': 'advance', 'source': 'question10', 'dest':'result', 'conditions':'is_going_to_result'},
                 {'trigger': 'advance', 'source': 'result', 'dest':'user', 'conditions':'is_going_to_user'},
                 {'trigger': 'advance', 'source': 'test', 'dest':'familyquestion1', 'conditions':'is_going_to_familyquestion1'},
                 {'trigger': 'advance', 'source': 'familyquestion1', 'dest':'familyquestion2', 'conditions':'is_going_to_familyquestion2'},
                 {'trigger': 'advance', 'source': 'familyquestion2', 'dest':'familyquestion1', 'conditions':'back_to_familyquestion1'},
                 {'trigger': 'advance', 'source': 'familyquestion2', 'dest':'familyquestion3', 'conditions':'is_going_to_familyquestion3'},
                 {'trigger': 'advance', 'source': 'familyquestion3', 'dest':'familyquestion2', 'conditions':'back_to_familyquestion2'},
                 {'trigger': 'advance', 'source': 'familyquestion3', 'dest':'familyquestion4', 'conditions':'is_going_to_familyquestion4'},
                 {'trigger': 'advance', 'source': 'familyquestion4', 'dest':'familyquestion3', 'conditions':'back_to_familyquestion3'},
                 {'trigger': 'advance', 'source': 'familyquestion4', 'dest':'familyquestion5', 'conditions':'is_going_to_familyquestion5'},
                 {'trigger': 'advance', 'source': 'familyquestion5', 'dest':'familyquestion4', 'conditions':'back_to_familyquestion4'},
                 {'trigger': 'advance', 'source': 'familyquestion5', 'dest':'familyquestion6', 'conditions':'is_going_to_familyquestion6'},
                 {'trigger': 'advance', 'source': 'familyquestion6', 'dest':'familyquestion5', 'conditions':'back_to_familyquestion5'},
                 {'trigger': 'advance', 'source': 'familyquestion6', 'dest':'familyquestion7', 'conditions':'is_going_to_familyquestion7'},
                 {'trigger': 'advance', 'source': 'familyquestion7', 'dest':'familyquestion6', 'conditions':'back_to_familyquestion6'},
                 {'trigger': 'advance', 'source': 'familyquestion7', 'dest':'familyquestion8', 'conditions':'is_going_to_familyquestion8'},
                 {'trigger': 'advance', 'source': 'familyquestion8', 'dest':'familyquestion7', 'conditions':'back_to_familyquestion7'},
                 {'trigger': 'advance', 'source': 'familyquestion8', 'dest':'familyquestion9', 'conditions':'is_going_to_familyquestion9'},
                 {'trigger': 'advance', 'source': 'familyquestion9', 'dest':'familyquestion8', 'conditions':'back_to_familyquestion8'},
                 {'trigger': 'advance', 'source': 'familyquestion9', 'dest':'familyquestion10', 'conditions':'is_going_to_familyquestion10'},
                 {'trigger': 'advance', 'source': 'familyquestion10', 'dest':'familyquestion9', 'conditions':'back_to_familyquestion9'},
                 {'trigger': 'advance', 'source': 'familyquestion10', 'dest':'familyresult', 'conditions':'is_going_to_familyresult'},
                 {'trigger': 'advance', 'source': 'familyresult', 'dest':'user', 'conditions':'is_going_to_user'},
                 {'trigger': 'advance', 'source': 'test', 'dest':'workquestion1', 'conditions':'is_going_to_workquestion1'},
                 {'trigger': 'advance', 'source': 'workquestion1', 'dest':'workquestion2', 'conditions':'is_going_to_workquestion2'},
                 {'trigger': 'advance', 'source': 'workquestion2', 'dest':'workquestion1', 'conditions':'back_to_workquestion1'},
                 {'trigger': 'advance', 'source': 'workquestion2', 'dest':'workquestion3', 'conditions':'is_going_to_workquestion3'},
                 {'trigger': 'advance', 'source': 'workquestion3', 'dest':'workquestion2', 'conditions':'back_to_workquestion2'},
                 {'trigger': 'advance', 'source': 'workquestion3', 'dest':'workquestion4', 'conditions':'is_going_to_workquestion4'},
                 {'trigger': 'advance', 'source': 'workquestion4', 'dest':'workquestion3', 'conditions':'back_to_workquestion3'},
                 {'trigger': 'advance', 'source': 'workquestion4', 'dest':'workquestion5', 'conditions':'is_going_to_workquestion5'},
                 {'trigger': 'advance', 'source': 'workquestion5', 'dest':'workquestion4', 'conditions':'back_to_workquestion4'},
                 {'trigger': 'advance', 'source': 'workquestion5', 'dest':'workquestion6', 'conditions':'is_going_to_workquestion6'},
                 {'trigger': 'advance', 'source': 'workquestion6', 'dest':'workquestion5', 'conditions':'back_to_workquestion5'},
                 {'trigger': 'advance', 'source': 'workquestion6', 'dest':'workquestion7', 'conditions':'is_going_to_workquestion7'},
                 {'trigger': 'advance', 'source': 'workquestion7', 'dest':'workquestion6', 'conditions':'back_to_workquestion6'},
                 {'trigger': 'advance', 'source': 'workquestion7', 'dest':'workquestion8', 'conditions':'is_going_to_workquestion8'},
                 {'trigger': 'advance', 'source': 'workquestion8', 'dest':'workquestion7', 'conditions':'back_to_workquestion7'},
                 {'trigger': 'advance', 'source': 'workquestion8', 'dest':'workquestion9', 'conditions':'is_going_to_workquestion9'},
                 {'trigger': 'advance', 'source': 'workquestion9', 'dest':'workquestion8', 'conditions':'back_to_workquestion8'},
                 {'trigger': 'advance', 'source': 'workquestion9', 'dest':'workquestion10', 'conditions':'is_going_to_workquestion10'},
                 {'trigger': 'advance', 'source': 'workquestion10', 'dest':'workquestion9', 'conditions':'back_to_workquestion9'},
                 {'trigger': 'advance', 'source': 'workquestion10', 'dest':'workresult', 'conditions':'is_going_to_workresult'},
                 {'trigger': 'advance', 'source': 'workresult', 'dest':'user', 'conditions':'is_going_to_user'},
                 
                ],
    initial="user",
    auto_transitions=False,
    show_conditions=True
)

app = Flask(__name__, static_url_path='')
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token =os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")    
        response = machine.advance(event)
        if response == False:
            if machine.state == 'user':
                send_text_message(event.reply_token, '輸入開始即可以進行測試')

    return "OK"
   
@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port, debug=True)

