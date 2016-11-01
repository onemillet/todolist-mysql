#encoding:utf-8
from . import db
from datetime import datetime

class TodoList(db.Model):
    __tablename__="todolists"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(30),nullable=False,)
    status=db.Column(db.Integer,default=0)
    create_time=db.Column(db.DateTime,default=datetime.utcnow)


