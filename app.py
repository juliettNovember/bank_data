from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse.html", items=items, errors=errors)

