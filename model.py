"""Model for plant watering app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    user_name = db.Column(db.String(20),
                          nullable = False)
    email = db.Column(String(30),
                      unique = True)
    password = db.Column(String(15),
                         nullable = False)
    
    def get_id(self):
        """Get user id."""

        return str(self.user_id)

    def __repr__(self):
        
        return f"<User user_id = {self.user_id}, email = {self.email}>"

class Plant(db.Model):
    """A plant."""

    __tablename__ = "plants"

    plant_id = db.Column(db.Integer, 
                         autoincrement = True,
                         primary_key = True)
    plant_name = db.Column(db.String)
    plant_img = db.Column(db.String)
    water_schedule = db.Column(db.Integer)
    fertalize_schedule = db.Column(db.Integer)



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