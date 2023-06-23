from flask import Flask, redirect, render_template, request, flash, session, send_file
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

# Creating Flask instance
app = Flask(__name__)
app.secret_key = 'aAbBcD'
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Main page
@app.route('/', methods=["GET", "POST"])
def index():
    session.clear()
    session['val'] = 5000
    return render_template("index.html")

# Rock-Paper-Scissors
@app.route('/rps', methods=["GET", "POST"])
def rps():
    if request.method == "POST":
        pchoice = request.form['button']
        # Clearing session when button <Clear> is chosen
        if pchoice == "clear":
            session.clear()
            session['val'] = 5000
            flash("Points cleared", 'clear')
            session['B'] = 0
            session['P'] = 0
            return redirect("/rps")
        # Error handling            
        if not pchoice in ['R', 'P', 'S']:
            flash("WRONG INPUT!", 'lost')
            return redirect("/rps")
        else:
            status, bchoice = RPS(pchoice)
            P = int(session.get('P'))
            B = int(session.get('B'))
            # Updating score by using dictionary
            P += {0:0, 1:1, 2:0}[status]
            B += {0:1, 1:0, 2:0}[status]
            # Saving score in session variables
            session['P'] = P
            session['B'] = B
            # Creating Result message
            bottxt = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}[bchoice]
            resulttxt = {0:'lost', 1:'won', 2:'tied'}[status]
            result = "Bot choice is {}, you {}!".format(bottxt, resulttxt)
            flash(result, resulttxt)
            return redirect("/rps")
    else:
        if not session.get('B') and not session.get('P'):
        # If method GET -> set session score variables to 0
            session['B'] = 0
            session['P'] = 0
        return render_template("rps.html", bot = session.get('B'), player = session.get('P'))

@app.route('/sorting', methods=["GET", "POST"])
def sorting():
    if request.method == "POST":
        print('request.form: {}'.format(request.form.keys()))
        print('request.files: {}'.format(request.files.keys()))
        # If .csv file uploaded, sort values from file
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(path)
                array = open(path)
                csvreader = csv.reader(array)
                arr = []
                # Create array from .csv file
                for row in csvreader:  # Read uploaded file
                    arr.append(int(row[0]))
                    if not row[0].isnumeric():
                        flash('Number has to be integer', 'lost')
                        return redirect('/sorting')
                array.close()
                # Sort values
                arr=list(arr)
                os.remove(path)
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
                # Update session values
                session['sorted'] = sorted
                session['unsorted'] = unsorted
                algorithms = [['Insert sort',round(inserttime,3)], ['Merge sort',round(mergetime,3)], ['Select sort',round(selecttime,3)], ['Bubble sort',round(bubbletime,3)], ['Quick sort',round(quicktime,3)]]
                sortalgorithms(algorithms)
                session['algorithms'] = algorithms
                print(algorithms)
                return redirect("/sorting")
        # If there is not .csv file uploaded, sort random generated values
        else:
            n = int(request.form["slider"])
            if not isinstance(n, int):
                flash("WRONG INPUT", "lost")
                return redirect("/sorting")
            session['val'] = n
            arr = random.randint(1, n+1, n)
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
            sortalgorithms(algorithms)
            session['algorithms'] = algorithms
            print(algorithms)
            return redirect("/sorting")
        
    
    if session.get('algorithms'):
        return render_template("sorting.html", algorithms = session.get('algorithms'), val = session.get('val'), sorted = session.get('sorted'), unsorted = session.get('unsorted'))
    else:
        # 5000 is Deafult value of slider
        return render_template("sorting.html", val = 5000)

# .csv file generator
@app.route('/csv', methods=["GET", "POST"])
def csvv():
    if request.method == "POST":
        n = int(request.form["slider"])
        if not isinstance(n, int):
            flash("WRONG INPUT", "lost")
            return redirect("/sorting")
        session['val'] = n
        arr = random.randint(1, n+1, n)

        with open('UPLOAD/output.csv', 'w', newline = '') as output:
            writer = csv.writer(output)
            for i in range(len(arr)):
                writer.writerow([arr[i]])
            output.close()

        return send_file('UPLOAD/output.csv', as_attachment=True)
    
    if session.get('val'):
        x = session.get('val')
        session.pop('val')
        return render_template("csv.html", val = x)
    # 5000 is Deafult value of slider
    return render_template("csv.html", val = 5000)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Sort algorithms by time 
def sortalgorithms(arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i][1] < arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
    
if __name__ == '__main__':
    app.run()