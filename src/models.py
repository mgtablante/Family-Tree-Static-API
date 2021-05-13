from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# crear cada modelo con una generacion serian 3 
# faltaria probar con postman 
# falta crear grand_parents
# falta comprobar las relaciones

class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), nullable=False)
    # grand = db.relationship('Parent', backref='Current', lazy=True)


    def __repr__(self):
        return '<Current %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age

            # do not serialize the password, its a security breach
        }

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('grand_parent.id'), nullable=False)
    children = db.relationship('Current', backref='Parent', lazy=True)
    # grand_parent = db.relationship('grand_parent', backref='parent', lazy=True)


    def __repr__(self):
        return '<Parent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age

            # do not serialize the password, its a security breach
        }

class Grand_parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.String(3), unique=False, nullable=False)
    children = db.relationship('Parent', backref='grand_parent', lazy=True)


    

    def __repr__(self):
        return '<Grand_parent %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age

            # do not serialize the password, its a security breach
        }

