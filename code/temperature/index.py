from flask import Flask, render_template, jsonify, Response
import sqlite3 as sql
import json

app = Flask(__name__)

@app.route("/")
def index():
    # copy or find a way to get last entery of table and set it = to temp
    con = sql.connect("temperature.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tempData ORDER BY date_time DESC LIMIT 1")
    result = cursor.fetchone()
    print(result[2])
    temp = result[2]
    return render_template('index.html', temp = temp)


@app.route("/fetch")
def data():
    con = sql.connect("temperature.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM tempData")

    entry = cur.fetchall()
    data = []
    for row in entry:
        data.append(list(row))

    return Response(json.dumps(data),  mimetype='application/json')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)