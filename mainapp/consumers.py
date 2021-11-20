import datetime
import json
from random import *
from time import sleep

import pytz
import requests
from channels.generic.websocket import WebsocketConsumer

from .top25 import top25


class StockConsumer(WebsocketConsumer):

    def connect(self):

        self.accept()

        query_string = self.scope["query_string"].decode()

        query_string = query_string.replace("+", " ")

        query_string = query_string.replace("pickstocks=", "")

        selectedStocks = query_string.split('&')

        print("\n\nThese are the Selected Stocks : \n\n")

        print(selectedStocks, end="\n\n")

        while self.connect:

            Prices = []

            for stocks in selectedStocks:

                url = "https://twelve-data1.p.rapidapi.com/price"

                querystring = {
                    "symbol": top25[stocks],
                    "format": "json",
                    "outputsize": "30"
                }

                headers = {
                    'x-rapidapi-host': "twelve-data1.p.rapidapi.com",
                    'x-rapidapi-key': "be54dfd69fmsh47add16c3c47959p1d8339jsnbff1e5a80706"
                }

                response = requests.request(
                    "GET", url, headers=headers, params=querystring)

                rawstr = response.text

                newstr = ""

                for i in range(10, len(rawstr)-2):

                    newstr += rawstr[i]

                Prices.append(newstr)

            my_dict = {i: Prices[i] for i in range(0, len(Prices))}

            nyc_datetime = datetime.datetime.now(
                pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M")

            my_dict['nyctime'] = nyc_datetime

            self.send(json.dumps(my_dict, default=str))

            sleep(61)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
