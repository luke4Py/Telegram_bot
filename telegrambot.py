"""
@author: SAMUEL LUKE
"""


import sqlalchemy
import json 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from sqlalchemy import *
import time
from cric_api import *

TOKEN = "****************"  #Enter your telegram Token
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(msg, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(msg, chat_id)
    get_url(url)




#text, chat = get_last_chat_id_and_text(get_updates())
#send_message('hello', get_last_chat_id_and_text(get_updates())[1])




def main():
    last_textchat = (None, None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:
            if text == "Live":
                send_message(live_score(), chat)
            elif text == "Gone":
                send_message(Gone_score(), chat)
            else:
                send_message("please enter 'Live' or 'Gone' for results", chat)
            last_textchat = (text, chat)
        time.sleep(0)


if __name__ == '__main__':
    main()




"""

get_updates()["result"][0]["update_id"]
get_updates()["result"][0]["message"]['message_id']


x = pd.DataFrame(columns = ["update_id","message_id","id","is_bot","first_name","language_code","date","text"], index = range(1,100))

get_updates()["result"][0]["update_id"]
get_updates()["result"][0]["message"]["message_id"]
get_updates()["result"][0]["message"]["from"]["id"]
get_updates()["result"][0]["message"]["from"]["is_bot"]
get_updates()["result"][0]["message"]["from"]["first_name"]
get_updates()["result"][0]["message"]["from"]["language_code"]
get_updates()["result"][0]["message"]["date"]
get_updates()["result"][0]["message"]["text"]
"""












