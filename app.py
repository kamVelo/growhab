from flask import Flask,render_template, session,request, redirect
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = "dsdnkdso£*4492r4_2398u"

@app.route('/', methods=['GET'])
def home():
    return render_template('test_index.html')

@app.route('/', methods=["POST"])
def decision():
    conn = sql.connect("./static/test.db", isolation_level=None)
    cursor = conn.cursor()
    var = cursor.execute("SELECT * FROM LEDON").fetchall()[0][0]
    
    try:
        on = request.form["LEDon"]
        cursor.execute(f"UPDATE LEDON SET LEDon='HIGH' WHERE LEDon='{var}'")
    except KeyError:
        print("low")
        cursor.execute(f"UPDATE LEDON SET LEDon='LOW' WHERE LEDon='{var}'")
    return redirect('/')

@app.route('/decision', methods=["GET"])
def returnDecision():
    conn = sql.connect("test.db", isolation_level=None)
    cursor = conn.cursor()
    var = cursor.execute("SELECT * FROM LEDON").fetchall()[0][0]
    print(var)
    return var