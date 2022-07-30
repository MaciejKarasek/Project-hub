from flask import Flask, redirect, render_template, request, flash, session
from flask_session import Session
from game import RPS
from numpy import random
import sort
import time
import os
import csv
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'UPLOAD'
ALLOWED_EXTENSIONS = {'csv'}


app = Flask(__name__)
#app.config["SESSION_PERMANENT"] = False
app.secret_key = 'aAbBcD'
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["GET", "POST"])
def index():
    session.clear()
    session['val'] = 5000
    return render_template("index.html")

@app.route('/rps', methods=["GET", "POST"])
def rps():
    if request.method == "POST":
        pchoice = request.form['button']
        if pchoice == "clear":
            session.clear()
            session['val'] = 5000
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

@app.route('/sorting', methods=["GET", "POST"])
def sorting():
    if request.method == "POST":
        print('request.form: {}'.format(request.form.keys()))
        print('request.files: {}'.format(request.files.keys()))
        if request.form['file']:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                array = open(path)
                csvreader = csv.reader(array)
                arr = []
                for row in csvreader:  # Read uploaded file
                    #print(row[0])
                    arr.append(int(row[0]))
                    if not row[0].isnumeric():
                        flash('Number has to be integer', 'lost')
                        return redirect('/sorting')
                array.close()
                arr=list(arr)
                os.remove(path)
                #print(arr)
                session['val'] = len(arr)

                unsorted = arr.copy()
                st = time.time()
                sorted = sort.insertsort(arr.copy())
                inserttime = time.time() - st

                st = time.time()
                sorted = sort.mergesort(arr.copy())
                mergetime = time.time() - st

                st = time.time()
                sorted = sort.select(arr.copy())
                selecttime = time.time() - st

                st = time.time()
                sorted = sort.bubblesort(arr.copy())
                bubbletime = time.time() - st

                st = time.time()
                sort.quicksort(arr, 0, len(arr) - 1)
                quicktime = time.time() - st
                session['sorted'] = sorted
                session['unsorted'] = unsorted
                algorithms = [['Insert sort',round(inserttime,3)], ['Merge sort',round(mergetime,3)], ['Select sort',round(selecttime,3)], ['Bubble sort',round(bubbletime,3)], ['Quick sort',round(quicktime,3)]]

                session['algorithms'] = algorithms
                print(algorithms)
                flash("SORTED", "won")
                return redirect("/sorting")
        else:
            n = int(request.form["slider"])
            if not isinstance(n, int):
                flash("WRONG INPUT", "lost")
                return redirect("/sorting")
            session['val'] = n
            arr = random.randint(1, n, n)
            unsorted = arr.copy()
            st = time.time()
            sorted = sort.insertsort(arr.copy())
            inserttime = time.time() - st

            st = time.time()
            sorted = sort.mergesort(arr.copy())
            mergetime = time.time() - st

            st = time.time()
            sorted = sort.select(arr.copy())
            selecttime = time.time() - st

            st = time.time()
            sorted = sort.bubblesort(arr.copy())
            bubbletime = time.time() - st

            st = time.time()
            sort.quicksort(arr, 0, len(arr) - 1)
            quicktime = time.time() - st
            session['sorted'] = sorted
            session['unsorted'] = unsorted
            algorithms = [['Insert sort',round(inserttime,3)], ['Merge sort',round(mergetime,3)], ['Select sort',round(selecttime,3)], ['Bubble sort',round(bubbletime,3)], ['Quick sort',round(quicktime,3)]]

            session['algorithms'] = algorithms
            print(algorithms)
            flash("SORTED", "won")
            return redirect("/sorting")
        
    
    if session.get('algorithms'):
        return render_template("sorting.html", algorithms = session.get('algorithms'), val = session.get('val'), sorted = session.get('sorted'), unsorted = session.get('unsorted'))
    else:
        return render_template("sorting.html", val = 5000)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
