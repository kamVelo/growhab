from flask import Flask,render_template, session,request, redirect

app = Flask(__name__)
app.secret_key = "dsdnkdso£*4492r4_2398u"

@app.route('/', methods=['GET'])
def home():
    return render_template('test_index.html')

@app.route('/', methods=["POST"])
def decision():
    session["on"] = "LOW"
    try:
        if request.form["LEDon"]: session["on"] = "HIGH"
    except KeyError:
        pass
    return redirect('/')

@app.route('/decision', methods=["GET"])
def returnDecision():
    return session["on"]