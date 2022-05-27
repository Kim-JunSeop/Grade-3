from pybo import db


class Health_Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    body_fat = db.Column(db.Integer, nullable=False)
    body_muscle = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Exercise_Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_type = db.Column(db.String(200), nullable=False)
    exercise_time = db.Column(db.Integer, nullable=False)
    exercise_note = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Signup_Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.String(200), unique=True,nullable=False)
    user_password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(150), nullable=False)

