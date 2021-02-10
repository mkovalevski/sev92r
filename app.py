from random import randint

from flask import Flask, render_template, abort

from data import departures, tours, title, subtitle, description, single_departures

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
    for i in rand:
        new_tours[i] = tours[i]
    return render_template("index.html", title=title, tours=new_tours, departures=departures)


@app.route('/departures/<departure>/')
def departure(departure):
    departure_prices = []
    departure_nights = []
    tours_for_departure = {}
    for tour_id, tour in tours.items():
        if tour['departure'] == departure:
            departure_prices.append(tour['price'])
            departure_nights.append(tour['nights'])
            tours_for_departure[tour_id] = tour
    return render_template('departure.html', departure=departure, tours=tours_for_departure, departures=departures,
                           title=title, single_departures=single_departures,
                           subtitle=subtitle, description=description,
                           departure_prices=departure_prices, departure_nights=departure_nights)


@app.route('/tours/<int:id>/')
def tour(id):
    tour = tours.get(id)
    if tour is None:
        abort(404)
    return render_template('tour.html',
                           tour=tour,
                           single_departures=single_departures,
                           departures=departures,
                           stars=int(tour["stars"]),
                           title=title, )


app.run('localhost', port=8000, debug=True)

# if __name__ == '__main__':
#     app.run()
