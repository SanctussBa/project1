
from flask import Flask, render_template, request
import sqlite3


# Creation of FLASK APP. It is connected with app.py folder before
app = Flask(__name__)

app.config['Secret_KEY'] = 'mysecret'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=["GET"])
def add():
    return render_template('add.html')

@app.route('/list', methods=["GET", "POST"])
def list():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    countries = c.execute('SELECT Country FROM database')
    items = countries.fetchall()
    return render_template('list.html', items=items)

@app.route('/save-place', methods=["GET", "POST"])
def save_place():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS database(Country TEXT, Place TEXT, Beach TEXT, Mountains TEXT, Desert TEXT, Forest TEXT, Hiking TEXT, City TEXT, Party TEXT)')

    country = str(request.form.get("country", ""))
    place = str(request.form.get("place", ""))
    beach = str(request.form['beach'])
    mountains = str(request.form['mountains'])
    desert = str(request.form['desert'])
    forest = str(request.form['forest'])
    hiking = str(request.form['hiking'])
    city = str(request.form['city'])
    party = str(request.form['party'])

    c.execute("INSERT INTO database (Country, Place, Beach, Mountains, Desert, Forest, Hiking, City, Party) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (country, place, beach, mountains, desert, forest, hiking, city, party))
    conn.commit()

    return render_template('saved.html', country=country, place=place, beach=beach,
    mountains=mountains, desert=desert, forest=forest, hiking=hiking, city=city, party=party)


    conn.close()
