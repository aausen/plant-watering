"""CRUD operations"""

from model import User, Plants, User_plants, db, connect_to_db

def create_user(user_name, email, password):
    """Create and return a new user."""

    user = User(user_name = user_name,
                email = email,
                password = password)

    db.session.add(user)
    db.session.commit()

    return user

def create_plant(plant_name, plant_img, water_schedule, fertalizer_scheudle):
    """Create and return a new plant."""

    plant = Plants(plant_name = plant_name,
                   plant_img = plant_img,
                   water_schedule = water_schedule,
                   fertalizer_scheudle = fertalizer_scheudle)

    db.session.add(plant)
    db.session.commit()

    return plant

def create_user_plant(user_id, plant_id, plant_img, last_watered, water_schedule, last_fertalized, fertalize_schedule):
    """Create and return a new user-plant."""

    user_plant = User_plants(user_id = user_id,
                             plant_id = plant_id,
                             plant_img = plant_img,
                             last_watered = last_watered,
                             water_schedule = water_schedule,
                             last_fertalized = last_fertalized,
                             fertalize_schedule = fertalize_schedule)
    db.session.add(user_plant)
    db.session.commit()

    return user_plant