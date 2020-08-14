from app import db

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))
    items=db.relationship('Item', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {} >'.format(self.username)