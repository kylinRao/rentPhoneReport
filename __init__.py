# coding=utf-8
from flask_login import LoginManager
import sqlite3
from flask import g
from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.sqlalchemy import SQLAlchemy

#用户认证
login_manger=LoginManager()
app = Flask(__name__)
#配置用户认证信息
login_manger.init_app(app)
#认证加密程度
login_manger.session_protection='strong'
#登陆认证的处理视图
login_manger.login_view='.Hello'
#登陆提示信息
login_manger.login_message=u'对不起，您还没有登录'
login_manger.login_message_category='info'
DATABASE = r'D:\projects\github\rentPhoneReport\phone.db'
# window下的路径有三个/，lixus下的路径配置有4个/并且，不需要用raw字符串
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///d:\projects\github\rentPhoneReport\phone.db'
app.config['SECRET_KEY'] = '123456'
db = SQLAlchemy(app)