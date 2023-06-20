<h1 align=center> Project Hub </h1>
<h3 align=center> Webapp that contains small python/html+css projects, created with Flask framework </h3>

<p align="center">
<img src=https://img.shields.io/github/last-commit/MaciejKarasek/Project-hub>
</p>

-This is webapp that contains small project's created with Flask framework.

## How to run

#### Install Python 3.11:
Linux:
```bash
$ sudo apt-get install python3.11
```

Windows:
Download Python from [official Python site](https://www.python.org/downloads/windows/).

#### Clone the repository:
```bash
$ git clone https://github.com/MaciejKarasek/Project-hub.git
```

#### Install Python libaries:
Go to .../Project-hub directory and run this command:
```bash
.../Project-hub$ pip install -r requirements.txt
```
#### Run the project:
Use this command and then open this site http://localhost:5000/
```bash
.../Project-hub$ flask run
```
## Files:
* static/ - Contains files that are used for page style (images, mp3 files, styles.css)
* templates/ - Contains flask .html templates
* UPLOAD/ - Directory that .csv files are uploaded to
* app.py - Main webapp file
* game.py - Python function for Rock-Paper-Scissors game
* sort.py - Sorting algorithms coded in python 
