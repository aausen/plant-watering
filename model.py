"""Model for plant watering app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# classes

def connect_to_db(flask_app, db_uri="postgresql://plant-water", echo = True):
    flask_app.config['SQLALCHEMY_DATABAS_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == '__main__':
    from server import app

    connect_to_db(app)