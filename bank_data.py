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

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template("data.html", curr=rates)
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        #ponizej sa zmienne tylko dla mojego potwierdzenia, ze wybierana waluta i wartosc wyswietla sie w terminalu 
        value_response = request.form['value']
        currency_response = request.form['currency']
        return render_template("data.html", curr=rates)
        
#teraz mam jedynie problem z utworzeniem kalkulora



if __name__=='__main__':
    app.run(debug=True)