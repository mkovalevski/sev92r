from flask import Flask, render_template, abort

from data import cars, title

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title=title, cars=cars)


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/terms/')
def terms():
    return render_template("terms.html")


@app.route('/apartments/')
def apps():
    return render_template("apps.html")


# app.run('localhost', port=8000, debug=True)

if __name__ == '__main__':
    app.run()
