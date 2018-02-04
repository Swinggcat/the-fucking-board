from .. import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)

    post = db.relationship('Post',backref='user')

    def __init__(self, username, password):
        self.name = username
        self.password = password
