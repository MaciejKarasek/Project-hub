from flask import Flask, redirect, render_template, request, flash
from game import RPS
app = Flask(__name__)
app.secret_key = 'aAbBcD'

@app.route('/', methods=["GET", "POST"])
def index():
    color = 0
    if request.method == "POST":
        pchoice = request.form['button']
        if not pchoice in ['R', 'P', 'S']:
            flash("WRONG INPUT!", lost)
            return redirect("/")
        else:
            status, bchoice = RPS(pchoice)
            color = status
            bottxt = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}[bchoice]
            resulttxt = {0:'lost', 1:'won', 2:'tied'}[status]
            result = "Bot choice is {}, you {}!".format(bottxt, resulttxt)
            flash(result, resulttxt)
            return redirect("/")
    else:
        return render_template("index.html")
