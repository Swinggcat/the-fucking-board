from flask import session
from ..model.User import User
from .. import db

def getname()->str:
    return session.setdefault('name','(Unknown Philosopher)')


def getid()->int:
    return session.setdefault('id',0)


def reg(username,password)->bool:
    try:
        db.session.add(User(username, password))
        db.session.commit()

    except:
        return False

    login(username, password)
    return True


def login(username,password):
    user = User.query.filter_by(name=username,password=password).first()
    if user:
        session['name'] = user.name
        session['id'] = user.id
        return True
    else:
        return False
