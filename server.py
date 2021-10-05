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

@app.route('/')
def show_dashboard():
    """Show dashboard."""

    return render_template("index.html")

if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug=True)