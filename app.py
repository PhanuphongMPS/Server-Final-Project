from asyncio import events
import json
import re
from tkinter.messagebox import NO
from traceback import print_tb
import requests

from flask import Flask, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from textwrap import indent
from cgi import print_form
from dataclasses import field

import getdata


def sendReplyMessage(replyToken, text, Brand):
    CBrand, CName, CUrl, CImg = getdata.run(Brand)
    payload = json.dumps({
        "replyToken": replyToken,
        "messages": [
            {
                "type": "flex",
                "altText": "Flex Message",
                "contents": {
                    "type": "carousel",
                    "contents": [
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": CImg[0],
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": CUrl[0]
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": CBrand[0],
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": CName[0],
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "ข้อมูลรถยนต์เพิ่มเติม",
                                            "uri":CUrl[0],
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": CImg[1],
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": CUrl[1]
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": CBrand[1],
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": CName[1],
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "ข้อมูลรถยนต์เพิ่มเติม",
                                            "uri": CUrl[1],
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": CImg[2],
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": CUrl[2]
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": CBrand[2],
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": CName[2],
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "ข้อมูลรถยนต์เพิ่มเติม",
                                            "uri": CUrl[2],
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": CImg[3],
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": CUrl[3]
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": CBrand[3],
                                        "weight": "bold",
                                        "size": "xl",
                                        "contents": []
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "margin": "md",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": CName[3],
                                                "size": "sm",
                                                "color": "#999999",
                                                "flex": 0,
                                                "margin": "md",
                                                "contents": []
                                            }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "ข้อมูลรถยนต์เพิ่มเติม",
                                            "uri": CUrl[3],
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "backgroundColor": "#000000FF",
                                "borderColor": "#000000FF",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "ดูรถยนต์เพิ่มเติม",
                                            "uri": "http://www.spyderautoimport.com/premium-used-car/"
                                        },
                                        "flex": 1,
                                        "color": "#FFFFFFFF",
                                        "gravity": "center"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer dGSnvznud6Ikb6NhNfP0NPqNbSnf9VYWKLQ84jRZgSkredsIZqw1H7WjuDJ4mz8cYHmlyZ+S/pRXuhGpinJUXTW7ytU7V2ymMJjxPB3oVtEzZWVbKxk+Ch/mn82bGR765c1gSin0ToaP5fXM7DRgiAdB04t89/1O/w1cDnyilFU='
    }
    response = requests.request(
        "POST", "https://api.line.me/v2/bot/message/reply", headers=headers, data=payload)
    print(response.text)

app = Flask(__name__)

@ app.route("/webhook", methods=["POST"])

def callback():
    request_json = request.get_json(silent=True, force=True)
    print(request_json)

    try:
        print(request_json["events"][0]["replyToken"])
    except:
        None

    try:
        if request_json["events"][0]["message"]["type"] == "text":
            headers = dict(request.headers)
            headers.update({"Host": "dialogflow.cloud.google.com"})
            requests.post("https://bots.dialogflow.com/line/feee7085-d5e1-4afe-a3b3-593afc0ddf56/webhook",
                          data=request.data, headers=headers)
    except:
        None
    try:
        replyToken = request_json["originalDetectIntentRequest"]["payload"]["data"]["replyToken"]
        if request_json["queryResult"]["intent"]["displayName"] == "BrandSearch - name - Brand":
            Brand = request_json["queryResult"]["parameters"]["Brand"]
            name = request_json["queryResult"]["parameters"]["name"]
            text = Brand+","+name
            sendReplyMessage(replyToken, text, Brand)
    except:
        None

if __name__ == "__main__":
    app.run()
