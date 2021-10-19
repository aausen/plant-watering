from flask import (Flask, 
                   render_template, 
                   request, session, 
                   redirect)
from jinja2 import StrictUndefined
import requests
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def show_dashboard():
    """Show dashboard."""

    return render_template("index.html")

@app.route("/login")
def login_user():
    """User login page."""

    return render_template("login.html")

@app.route("/search")
def search():
    """Plant search results."""

    return render_template("search.html")

@app.route("/add")
def add_plant():
    """Add a new plant to db."""

    return render_template("add-plant.html")

@app.route("/watering")
def watering_schedule():
    """Create watering schedule for plant."""

    return render_template("watering-schedule.html")

@app.route("/fertalizing")
def fertalizing_schedule():
    """"Create fertalizing scheudle for plant."""

    return render_template("fertalizing-schedule.html")

@app.route("/myplants")
def my_plants():
    """"Plant information page."""

    return render_template("my-plants.html")

@app.route("/profile")
def user_profile():
    """"Display user information."""

    return render_template("user-profile.html")

if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug=True)