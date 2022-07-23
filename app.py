from flask import Flask, redirect, render_template, request, flash, session
from flask_session import Session
from game import RPS
app = Flask(__name__)
app.secret_key = 'aAbBcD'
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=["GET", "POST"])
def index():
    session.clear()
    return render_template("index.html")

@app.route('/rps', methods=["GET", "POST"])
def rps():
    if request.method == "POST":
        pchoice = request.form['button']
        if pchoice == "clear":
            session.clear()
            flash("Points cleared", 'clear')
            session['B'] = 0
            session['P'] = 0
            return redirect("/rps")

        if not pchoice in ['R', 'P', 'S']:
            flash("WRONG INPUT!", 'lost')
            return redirect("/rps")
        else:
            status, bchoice = RPS(pchoice)
            P = int(session.get('P'))
            B = int(session.get('B'))
            P += {0:0, 1:1, 2:0}[status]
            B += {0:1, 1:0, 2:0}[status]
            session['P'] = P
            session['B'] = B
            bottxt = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}[bchoice]
            resulttxt = {0:'lost', 1:'won', 2:'tied'}[status]
            result = "Bot choice is {}, you {}!".format(bottxt, resulttxt)
            flash(result, resulttxt)
            return redirect("/rps")
    else:
        if not session.get('B'):
            session['B'] = 0
            session['P'] = 0
        return render_template("rps.html", bot = session.get('B'), player = session.get('P'))

@app.route('/merge', methods=["GET", "POST"])
def merge():
    session.clear()
    return render_template("merge.html")