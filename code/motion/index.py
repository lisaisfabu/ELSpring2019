from flask import Flask, render_template, jsonify, Response
import sqlite3 as mydb
import json

app = Flask(__name__)

@app.route("/")
def index():
    con = mydb.connect("motion.db")
    cur = con.cursor()
    # cur.execute("SELECT * FROM inAndOut ORDER BY total DESC LIMIT 10")
    # result = cur.fetchone()
    # print(result[4])
    return render_template('index.html')

#get data from db
@app.route("/catch")
def data():
    con = mydb.connect("motion.db")
    con.row_factory = mydb.Row

    cur = con.cursor()
    cur.execute("SELECT * from inAndOut ORDER BY rowid DESC LIMIT 10")

    getAll = cur.fetchall()
    data = []
    for row in getAll:
        data.append(list(row))

    return Response(json.dumps(data), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)