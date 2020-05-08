# coding=utf-8
import requests
import json
import datetime
import time

today = datetime.datetime
today = today.now()
date = today.strftime("%a %b %d %Y %H:%M:%S")
base_api = "https://api.exchangeratesapi.io/latest?base="

while True:
    print date.center(50, "*")

    user_currency = raw_input("Please enter a currency that you would like to buy: \n")

    result = requests.get(base_api + user_currency)
    result = result.text
    result = json.loads(result)

    if result["base"] == user_currency:
        user_buying_currency = raw_input("Enter the currency to buy your desired currency: \n")
        for buying_currency in result["rates"]:
            if buying_currency == user_buying_currency:
                user_amount = input("Enter the amount: \n")
                time.sleep(1)
                print "1", user_currency, "=", user_buying_currency, result["rates"][user_buying_currency]
                time.sleep(1)
                print user_amount, user_currency, "=", user_buying_currency, user_amount * result["rates"][user_buying_currency]
                print "Returning back..."
                time.sleep(3)
