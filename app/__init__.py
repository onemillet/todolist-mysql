#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from os import path
from flask_bootstrap import Bootstrap

app = Flask('__name__')

#下面的代码是使用sqlite数据库时的配置
# basedir = path.abspath(path.dirname(__file__))
# app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI']=\
# 'sqlite:///'+path.join(basedir,'todolist.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

#下面的代码是使用mysql数据库时的配置
app.config['SECRET_KEY'] ='hard to guess'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3306/todolist' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名todolist
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动

# db = SQLAlchemy()
# db.init_app(app)
db=SQLAlchemy(app)
Bootstrap(app)

from app import views,models