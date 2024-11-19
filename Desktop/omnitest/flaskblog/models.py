from datetime import datetime
from flaskblog import db, loginmanager
from flask import current_app, session
from flask_login import UserMixin
from itsdangerous import URLSafeSerializer

@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False, unique=True)
    email=db.Column(db.String(120), nullable=False, unique=True)
    image_file=db.Column(db.String(225), nullable=False, default='default.jpg')
    password=db.Column(db.String(100), nullable=False)
    author=db.relationship('Post', backref='author', lazy=True)


    def get_reset_token(self):
        s = URLSafeSerializer(current_app.config['SECRET_KEY'], 'saltvalue')
        return s.dumps({'user_id': self.id, 'name':'itsdangerous'})

    @staticmethod 
    def verify_reset_token(token):
        s = URLSafeSerializer(current_app.config['SECRET_KEY'], 'saltvalue')
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)




    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    content=db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(225), nullable=False, default='default_post.jpg')
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}', '{self.image_file}')"

