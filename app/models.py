from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #numb=db.Column(db.Integer)
    typename=db.Column(db.String)
    itemname=db.Column(db.String)
    size_i=db.Column(db.Integer)
    price=db.Column(db.Integer)
    day=db.Column(db.Date)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    #isold=db.Column(db.Boolean)

    def __repr__(self):
        return '<Item {} {} size= {} price= {}>'.format(self.typename,self.itemname,self.size_i,self.price)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))
    items=db.relationship('Item', backref='author', lazy='dynamic')

    def set_password(self,pasword):
        self.password_hash= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {} >'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))