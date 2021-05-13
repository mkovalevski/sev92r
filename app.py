from flask import Flask, render_template, abort

from data import cars, title, aparts, flat1

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title=title, cars=cars)


@app.route('/about/')
def about():
    return render_template("about.html", title=title)


@app.route('/terms/')
def terms():
    return render_template("terms.html", title=title)


@app.route('/apartments/')
def apps():
    return render_template("apps.html", aparts=aparts, title=title)


@app.route('/flat1/')
def app1():
    return render_template("flat1.html", flat=flat1, title=title)


@app.route('/flat2/')
def app2():
    return render_template("flat2.html", title=title)


app.run('localhost', port=8000, debug=True)

# if __name__ == '__main__':
#     app.run()
