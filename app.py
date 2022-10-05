from asyncio import events
import json
from traceback import print_tb
import requests
from flask import Flask, request
from flask_restful import Api,Resource


app = Flask(__name__)
api=Api(app)

@app.route("/webhook", methods=["POST"])

# class TypeCar(Resource):
#     def get(self):
#         return{"data":"name car"}
# #call
# api.add_resource(TypeCar,"Car")

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
def search_answer(question_from_dailogflow_dict):
    print(json.dumps(question_from_dailogflow_dict, indent=4 , ensure_ascil=False))
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"]

    if intent_group_question_str == 'Searchcar':
        answer_str = namecar()
    

def namecar():
    database_ref = firestore.client().document('spyderpremiumcar/Car')
    database_dict = database_ref.get().to_dict()
    # database_list = list(database_dict.values())
    # premiumcar = randint(0, len(database_list)-1)
    #car_data = database_list(premiumcar)
    answer_function = car_data
    return answer_function

if __name__ == "main":
    app.run()



