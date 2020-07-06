import requests
import csv
import json
from flask import Flask, render_template, request, redirect

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
#dotarłam do listy rated
rates = data[0]['rates']
#utworzyłam plik csv
with open ('rates.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(["currency", "code", "bid", "ask"])
    for item in rates:
        writer.writerow([item['currency'], item['code'], item['bid'], item['ask']])
#zaczynam tworzyć aplikacje Kalkulator 
app = Flask(__name__)
@app.route("/", methods=['GET'])
def calc():
    return redirect("/calculator")

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template("data.html", curr=rates)
    elif request.method == 'POST':
        
        #ponizej sa zmienne tylko dla mojego potwierdzenia, ze wybierana waluta i wartosc wyswietla sie w terminalu 
        value_response = float(request.form['value'])
        currency_response = request.form['currency']
        for currency in rates:
            if currency_response == currency['code']:
                ask= float(currency['ask'])
                result = ask * value_response
                result=round(result, 3)
                return render_template("data.html", ask=ask, vr=value_response, curr=rates,  val=result)
        

if __name__=='__main__':
    app.run(debug=True)