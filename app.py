import json
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def callback():
    request_json = request.get_json(silent=True, force=True)
    print(request_json)
    try:
        if request_json["events"][0]["message"]["type"] == "text":
            headers = dict(request.headers)
            headers.update({"Host": "dialogflow.cloud.google.com"})
            requests.post("https://dialogflow.cloud.google.com/v1/integrations/line/webhook/feee7085-d5e1-4afe-a3b3-593afc0ddf56",
                          data=request.data, headers=headers)
    except:
        None


if __name__ == "main":
    app.run()
