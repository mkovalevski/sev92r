from flask import Flask, render_template
from data import departures, tours, title, subtitle, description, single_departures

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.route('/')
def index():
    return render_template("index.html", title=title, tours=tours, departures=departures)


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


#app.run('localhost', port=8000, debug=True)

if __name__ == '__main__':
    app.run()
