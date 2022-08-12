from flask import Flask, render_template, request

import mysql.connector 

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

@app.route("/")
def index():
    q = request.args.get("q")
    rows = db.execute("SELECT * FROM registrants WHERE name = :name", name=q)
    return render_template("index.html", rows=rows)