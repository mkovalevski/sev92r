from flask import Flask, render_template
from data import departures, tours, title, subtitle, description, single_departures
from random import randint

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/')
def index():
    rand = []
    new_tours = {}
    b = 7
    i = 0
    while i <= b:
        if len(rand) == 6:
            break
        random_id = randint(1, 16)
        if random_id not in rand:
            rand.append(random_id)
        else:
            b += 1
        i += 1
    print(rand)
    for i in rand:
        new_tours[i] = tours[i]
    return render_template("index.html", title=title, tours=new_tours, departures=departures)


@app.route('/departures/<departure>/')
def departure(departure):
    departure_prices = []
    departure_nights = []
    for tour in tours:
        if tours[tour]['departure'] == departure:
            departure_prices.append(tours[tour]["price"])
            departure_nights.append(tours[tour]["nights"])
    return render_template('departure.html', departure=departure, tours=tours, departures=departures,
                           title=title, single_departures=single_departures,
                           subtitle=subtitle, description=description,
                           departure_prices=departure_prices, departure_nights=departure_nights)


@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html', tours=tours, single_departures=single_departures, id=int(id),
                           departures=departures, stars=int(tours[int(id)]["stars"]), title=title)


# app.run('localhost', port=8000, debug=True)

if __name__ == '__main__':
    app.run()
