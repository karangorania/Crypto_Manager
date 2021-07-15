from manage import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader  
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    entrys = db.relationship('Entry', backref='user')
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Entry(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(50), nullable=False)
    asset_qty = db.Column(db.Float(100), nullable=False)
    asset_price = db.Column(db.Float(100), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Entry('{self.asset_name}', '{self.asset_qty}', '{self.asset_price}', '{self.date_added}')"
