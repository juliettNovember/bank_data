import requests
import csv
import json
from flask import Flask, render_template, request

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

rates = data[0]['rates']

with open ('rates.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(["currency", "code", "bid", "ask"])
    for item in rates:
        writer.writerow([item['currency'], item['code'], item['bid'], item['ask']])

app = Flask(__name__)

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    curr = item['code']
    return render_template("data.html", curr=rates)


if __name__=='__main__':
    app.run(debug=True)