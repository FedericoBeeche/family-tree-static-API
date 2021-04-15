from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age
        }

    def getAllPeople():
        all_users = Person.query.order_by(Person.age.desc()).all()
        return list(map(lambda x: x.serialize(), all_users))

class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.String(120), unique=True, nullable=False) #falta foreign key
    father_id = db.Column(db.String(80), unique=False, nullable=False) #falta foreign key
    mother_id = db.Column(db.String(80), unique=False, nullable=False) #falta foreign key

    def __repr__(self):
        return '<User %r>' % self.child_id

    def serialize(self):
        return {
            "child_id": self.child_id,
            "father_id": self.father_id,
            "mother_id": self.mother_id
        }