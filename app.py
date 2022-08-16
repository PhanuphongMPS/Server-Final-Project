from asyncio import events
import json
from traceback import print_tb
import requests
from flask import Flask, request
#test
#from random import randint
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
#cred = credentials.Certificate("supcar-85c0a-firebase-adminsdk-o10rd-ccdceef4b1.json")
#firebase_admin.initialize_app(cred)

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])

#test
#def Carname():
   # database_ref = firestore.client().document('Carname/Car')
    #database_dict = database_ref.get().to.dict()
    #database_list = list(database_dict.values())
   # ran_manu = randint(0, len(database_list)-1)
   # menu_name = database_list[ran_manu]
   # answer_function = menu_name + 'ไม่มีสินค้าในขณะนี้'
   # return answer_function


def callback():
    request_json = request.get_json(silent=True, force=True)
    print(request_json)

    ##test
    print(request_json["events"][0]["replyToken"]) 

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

