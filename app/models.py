from . import db

class User(db.Model) :
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.String(32), primary_key=True)
    password = db.Column(db.String(50))

    def __init__(self,id,password) :
        self.id = id
        self.password = password

class Food(db.Model) :
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_name = db.Column(db.String(64), nullable=False)
    food_category = db.Column(db.String(32), nullable=False)
    food_detail_category = db.Column(db.String(32), nullable=False)
    serving_size = db.Column(db.Float, nullable=False)
    calorie = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    fat =  db.Column(db.Float, nullable=False)
    carbohydrate = db.Column(db.Float, nullable=False)
    sugar = db.Column(db.Float, nullable=False)
    calcium = db.Column(db.Float, nullable=False)
    phosphorus = db.Column(db.Float, nullable=False)
    iron = db.Column(db.Float, nullable=False)
    salt= db.Column(db.Float, nullable=False)
    potassium = db.Column(db.Float, nullable=False)
    vitaminA = db.Column(db.Float, nullable=False)
    vitaminB1 = db.Column(db.Float, nullable=False)
    vitaminB2 = db.Column(db.Float, nullable=False)
    niacin = db.Column(db.Float, nullable=False)
    vitaminC = db.Column(db.Float, nullable=False)
    folic_acid = db.Column(db.Float, nullable=False)