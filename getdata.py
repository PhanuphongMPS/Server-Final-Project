
from cgi import print_form
from dataclasses import field
from urllib import request
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import bs4
import time
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from textwrap import indent

import json

cred = credentials.Certificate('supcar-85c0a-firebase-adminsdk-o10rd-e6722e0084.json')
firebase_admin.initialize_app(cred)
firebase_admin.get_app(name='[DEFAULT]')
db = firestore.client()

def run(x):
    doc_ref = db.collection(u'Spyder').document(x)
    doc = doc_ref.get()
    if doc.exists:
        CImg =[]
        CBrand =[]
        CName =[]
        CUrl =[]
        CWeb =[]
        count = 0
        for d in doc.to_dict():
            
            if count == 5:
                break
            else:
                CBrand.append(doc.to_dict()[d]['Brand'])
                CName.append(doc.to_dict()[d]['Name'])
                CImg.append(doc.to_dict()[d]['Img'])
                CUrl.append(doc.to_dict()[d]['Url'])
                count +=1
        return CBrand,CName,CUrl,CImg
    else:
        print(u'ขออภัยไม่มีรถยนต์ที่ท่านต้องการ')