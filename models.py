# coding=utf-8
from __init__ import *
# from app import login_manger
from flask_login import UserMixin


#用户表
class Users(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False,index=True)
    password=db.Column(db.String(255), nullable=False,index=True)
    phone=db.Column(db.String(32),nullable=False)

# 用户认证的回调函数
@login_manger.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
