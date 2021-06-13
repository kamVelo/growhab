from flask import Flask,render_template, session,request, redirect

app = Flask(__name__)
app.secret_key = "dsdnkdso£*4492r4_2398u"

@app.route('/', methods=['GET'])
def home():
    return render_template('test_index.html')

@app.route('/', methods=["POST"])
def decision():
    file = open("decision.txt", "w")
    try:
        if request.form["LEDon"]: file.write("HIGH")
    except KeyError:
        file.write("LOW")
    file.close()
    return redirect('/')

@app.route('/decision', methods=["GET"])
def returnDecision():
    file = open("decision.txt", "r")
    var = file.readline()
    file.close()
    print(var)
    return var