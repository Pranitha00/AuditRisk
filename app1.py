from flask import Flask,redirect,url_for,render_template,request
from audit_risk_detection1 import check
app = Flask(__name__)

lst = ['Sector_score', 'PARA_A', 'Score_A', 'PARA_B', 'Score_B', 'numbers',
       'Money_Value', 'Score_MV', 'District_Loss', 'PROB', 'History']
d = {}

@app.route("/",methods = ["POST","GET"])
def predict():
    global d
    global lst
    if request.method == "POST":
        for x in lst:
            d[x] = request.form[str(x)]
        return redirect(url_for("result"))
    return render_template("index.html",content=lst)

@app.route("/result",methods = ["POST","GET"])
def result():
    global d
    if request.method == "POST":
        return redirect(url_for("predict"))
    return render_template("result.html",content=check(d))

if __name__ == "__main__":
    app.run(debug = True)