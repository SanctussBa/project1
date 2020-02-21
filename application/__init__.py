
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


@app.route('/selected', methods=["GET", "POST"])
def selected():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT Country FROM database')# Select list of unique countries for select option
    list_of_all_countries = c.fetchall()
    x = []
    for country in list_of_all_countries:
        if country not in x:
            x.append(country)
    unique_countries = map(''.join,x)


    choice_country = str(request.form.get("country-choice", ""))
    selector = str(request.form['selector'])

    # Country and Selector are not chosen
    if choice_country == "all" and selector == "any":
        c.execute('SELECT * FROM database')# Select main list of all data
        lis = c.fetchall()

    # ANY COUNTRY but CHOSEN PROPERTY OF PLACE
    elif choice_country == "all" and selector == "beach":
        c.execute('SELECT * FROM database where Beach = ?', ['yes'])
        lis = c.fetchall()
    elif choice_country == "all" and selector == "mountains":
        c.execute('SELECT * FROM database where Mountains = ?', ['yes'])
        lis = c.fetchall()
    elif choice_country == "all" and selector == "desert":
        c.execute('SELECT * FROM database where Desert = ?', ['yes'])
        lis = c.fetchall()
    elif choice_country == "all" and selector == "forest":
        c.execute('SELECT * FROM database where Forest = ?', ['yes'])
        lis = c.fetchall()
    elif choice_country == "all" and selector == "hiking":
        c.execute('SELECT * FROM database where Hiking = ?', ['yes'])
        lis = c.fetchall()
    elif choice_country == "all" and selector == "city":
        c.execute('SELECT * FROM database where City = ?', ['yes'])
        lis = c.fetchall()
    elif choice_country == "all" and selector == "party":
        c.execute('SELECT * FROM database where Party = ?', ['yes'])
        lis = c.fetchall()

    # particular country and no Selector
    elif choice_country != "all" and selector == "any":
        c.execute('SELECT * FROM database WHERE Country = ?', [choice_country])
        lis = c.fetchall()

    # Particular country and particular Selector

    elif choice_country != "all" and selector == "beach":
        c.execute('SELECT * FROM database WHERE Country = ? AND Beach = ?', [choice_country, "yes"])

    elif choice_country != "all" and selector == "mountains":
        c.execute('SELECT * FROM database WHERE Country = ? AND Mountains = ?', [choice_country, "yes"])
        lis = c.fetchall()
    elif choice_country != "all" and selector == "desert":
        c.execute('SELECT * FROM database WHERE Country = ? AND Desert = ?', [choice_country, "yes"])
        lis = c.fetchall()
    elif choice_country != "all" and selector == "forest":
        c.execute('SELECT * FROM database WHERE Country = ? AND Forest = ?', [choice_country, "yes"])
        lis = c.fetchall()
    elif choice_country != "all" and selector == "hiking":
        c.execute('SELECT * FROM database WHERE Country = ? AND Hiking = ?', [choice_country, "yes"])
        lis = c.fetchall()
    elif choice_country != "all" and selector == "city":
        c.execute('SELECT * FROM database WHERE Country = ? AND City = ?', [choice_country, "yes"])
        lis = c.fetchall()
    elif choice_country != "all" and selector == "party":
        c.execute('SELECT * FROM database WHERE Country = ? AND Party = ?', [choice_country, "yes"])
        lis = c.fetchall()

    return render_template('list.html', lis=lis, unique_countries=unique_countries)
    conn.close()

@app.route('/list', methods=["GET", "POST"])
def list():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('SELECT Country FROM database')# Select list of unique countries for select option
    list_of_all_countries = c.fetchall()
    x = []
    for country in list_of_all_countries:
        if country not in x:
            x.append(country)
    unique_countries = map(''.join,x)

    c.execute('SELECT * FROM database')# Select main list of all data
    lis = c.fetchall()
    return render_template('list.html', lis=lis, unique_countries=unique_countries)

    conn.close()

@app.route('/save-place', methods=["GET", "POST"])
def save_place():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS database(Country TEXT, Place TEXT, Beach TEXT, Mountains TEXT, Desert TEXT, Forest TEXT, Hiking TEXT, City TEXT, Party TEXT)')

    x = "no"
    country = str(request.form.get("country", ""))
    place = str(request.form.get("place", ""))
    try:
        beach = str(request.form['beach'])
        if beach == "yes":
            b = "You can find there amazing beaches."
        else:
            b = "Unfortunately it is not a seaside, that's why do not search for beach there."
    except KeyError:
        beach = x
        b = "You will not find any beach there but there are other things to explore."

    try:
        mountains = str(request.form['mountains'])
        if mountains == "yes":
            m = "Definitely you can go there to explore mountains."
        else:
            m = "Do not try to go to mountains, because you will not find them there."
    except KeyError:
        mountains = x
        m = "There you do not have to claim mountains."


    try:
        desert = str(request.form['desert'])
        if desert == "yes":
            d = "It's quite hot there, sand all around."
        else:
            d = "Not too hot, so no desert there."
    except KeyError:
        desert = x
        d = "It's not a sandy desert place."


    try:
        forest = str(request.form['forest'])
        if forest == "yes":
            f = "You will see there trees all around. Trees everywhere."
        else:
            f = "Don't be afraid to get lost in the fores. No forest there for you."
    except KeyError:
        forest = x
        f = "No forest adventures for you there. Not many trees."


    try:
        hiking = str(request.form['hiking'])
        if hiking == "yes":
            h = "Prepare your good walking shoes. You will need them for hiking."
        else:
            h = "Leave your hiking shoes home. No need there."
    except KeyError:
        hiking = x
        h = "In this place you don't have to walk a lot. No specific hiking routes known."


    try:
        city = str(request.form['city'])
        if city == "yes":
            ci = "There is a big city. So, no worries, your wifi probably will work."
        else:
            ci = "No civilization there. Maybe a little bit but do not expect a big city environment."
    except KeyError:
        city = x
        ci = "Not a city type? Want to run away a bit from a busy city? Good, then place for you"
    try:
        party = str(request.form['party'])
        if party == "yes":
            p = "Yo! check out the hottest nightclubs there. It's plenty of them."
        else:
            p = "Not the best place to have nightlife fun. Little bit boring at night, hey but check out other stuff there and you can sleep tight at night."
    except KeyError:
        party = x
        p = "Do not stress to find clubs there. Not a place for party."


    c.execute("INSERT INTO database (Country, Place, Beach, Mountains, Desert, Forest, Hiking, City, Party) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (country, place, beach, mountains, desert, forest, hiking, city, party))
    conn.commit()

    return render_template('saved.html', country=country, place=place, beach=beach,
    mountains=mountains, desert=desert, forest=forest, hiking=hiking, city=city, party=party, b=b, m=m, d=d, f=f, h=h, ci=ci, p=p)


    conn.close()
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/delete')
def delete_all():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM database')
    conn.commit()
    return render_template('delete.html')
    conn.close()
