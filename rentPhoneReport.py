# coding=utf-8

from __init__ import *
from models import *
from rentLogView import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, login_user, login_required, logout_user
from devicesView import *


###登陆相关
# @login_manager.user_loaded_from_request  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
# def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
#     from models import Users
#     user = Users.query.filter_by(id=id).first()
#     return user


# 添加登录视图，如果是GET方法，返回一个简单的表单

@app.route('/login/', methods=['GET', 'POST'])
def login():
    from models import Users
    if request.method == 'POST':
        name = request.form.get('name')
        user = Users.query.filter_by(name=name).first()
        if not user:
            flash('该用户不存在')
        elif request.form.get('pwd') != user.pwd:
            flash('密码错误')
        else:
            login_user(user, remember=True)
            next_url = request.args.get('next')
            return redirect(next_url or url_for('login_success'))
    return render_template('login.html')  # 如果密码是 123 就会跳转到视图函数 index 上


@app.route('/')
@login_required
def index():
    return 'Hello Tank'


@app.route('/succees/')
@login_required
def login_success():
    return render_template('base.html')


@app.route('/logout/')
@login_required
def logout():
    logout_user()  # 登出用户
    return '已经退出登录'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()
    print("====before request====")


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
        print("====after request====")


@app.route('/rentPhoneReport', methods=['POST', 'GET'])
def rentPhoneReport():
    if request.form.get("method", 'getNoMethod') == "rent":
        phone, name, deviceId, rentPhoneType, battaryLevel, gameboxVersion, hiappVersion, hmsVersion, isRoot = request.form.get(
            "phone", 'getNoPhone'), \
                                                                                                               request.form.get(
                                                                                                                   "name",
                                                                                                                   'getNoName'), \
                                                                                                               request.form.get(
                                                                                                                   "deviceId",
                                                                                                                   'getNodeviceId'), \
                                                                                                               request.form.get(
                                                                                                                   "phoneType",
                                                                                                                   'getNophoneType'), \
                                                                                                               request.form.get(
                                                                                                                   "battaryLevel",
                                                                                                                   'getNobattaryLevel'), \
                                                                                                               request.form.get(
                                                                                                                   "gameboxVersion",
                                                                                                                   'getNogameboxVersion'), \
                                                                                                               request.form.get(
                                                                                                                   "hiappVersion",
                                                                                                                   'getNohiappVersion'), \
                                                                                                               request.form.get(
                                                                                                                   "hmsVersion",
                                                                                                                   'getNohmsVersion'), \
                                                                                                               request.form.get(
                                                                                                                   "isRoot",
                                                                                                                   'false');
        if 'true' in isRoot:
            isRoot = 1
        else:
            isRoot = 0
        print(request.method)
        print(request.form.get("phone", 'getNoPhone'),
              request.form.get("name", 'getNoName'),
              request.form.get("deviceId", 'getNodeviceId'),
              request.form.get("phoneType", 'getNophoneType'),)
        rentLogUpdateSql = u"INSERT INTO rentLog (name, phone,deviceId,rentPhoneType,status,battaryLevel,gameboxVersion,hiappVersion,hmsVersion) " \
                           u"VALUES ('{name}','{phone}','{deviceId}','{rentPhoneType}','{status}','{battaryLevel}','{gameboxVersion}','{hiappVersion}','{hmsVersion}')".format(
                name=name, phone=phone, deviceId=deviceId, rentPhoneType=rentPhoneType, status=1,
                battaryLevel=battaryLevel, gameboxVersion=gameboxVersion, hiappVersion=hiappVersion,
                hmsVersion=hmsVersion
        )
        g.db.execute(rentLogUpdateSql)
        deviceUpdateSql = u"replace into devices ( renterName, deviceId ,rentPhoneType,status,gameboxVersion,hiappVersion,hmsVersion,isRoot) " \
                          u" VALUES ('{renterName}','{deviceId}','{rentPhoneType}','{status}','{gameboxVersion}','{hiappVersion}','{hmsVersion}',{isRoot})".format(
                renterName=name, deviceId=deviceId, rentPhoneType=rentPhoneType, status=1,
                gameboxVersion=gameboxVersion, hiappVersion=hiappVersion, hmsVersion=hmsVersion, isRoot=isRoot
        )
        print deviceUpdateSql

        g.db.execute(deviceUpdateSql)

        g.db.commit()
    if request.form.get("method", 'getNoMethod') == "return":
        phone, name, deviceId, rentPhoneType, battaryLevel, gameboxVersion, hiappVersion, hmsVersion = request.form.get(
            "phone", 'getNoPhone'), request.form.get("name", 'getNoName'), \
                                                                                                       request.form.get(
                                                                                                           "deviceId",
                                                                                                           'getNodeviceId'), \
                                                                                                       request.form.get(
                                                                                                           "phoneType",
                                                                                                           'getNophoneType'), \
                                                                                                       request.form.get(
                                                                                                           "battaryLevel",
                                                                                                           'getNobattaryLevel'), \
                                                                                                       request.form.get(
                                                                                                           "gameboxVersion",
                                                                                                           'getNogameboxVersion'), \
                                                                                                       request.form.get(
                                                                                                           "hiappVersion",
                                                                                                           'getNohiappVersion'), \
                                                                                                       request.form.get(
                                                                                                           "hmsVersion",
                                                                                                           'getNohmsVersion');

        print(request.method)
        print(request.form.get("phone", 'getNoPhone'),
              request.form.get("name", 'getNoName'),
              request.form.get("deviceId", 'getNodeviceId'),
              request.form.get("phoneType", 'getNophoneType'),)
        returnSql = u"UPDATE rentLog set returnName='{returnName}',returnPhone='{returnPhone}',status={status},returnTime=(datetime(CURRENT_TIMESTAMP,'localtime')),battaryLevel='{battaryLevel}',gameboxVersion='{gameboxVersion}',hiappVersion='{hiappVersion}',hmsVersion='{hmsVersion}' " \
                    u"where status=1 and deviceId = '{deviceId}'".format(returnName=name, status=0, returnPhone=phone,
                                                                         deviceId=deviceId, battaryLevel=battaryLevel,
                                                                         gameboxVersion=gameboxVersion,
                                                                         hiappVersion=hiappVersion,
                                                                         hmsVersion=hmsVersion);
        print returnSql
        g.db.execute(returnSql)

        deviceUpdateSql = u"update devices set renterName='{returnName}',status={status},gameboxVersion='{gameboxVersion}',hiappVersion='{hiappVersion}',hmsVersion='{hmsVersion}' " \
                          u"where status=1 and deviceId = '{deviceId}'".format(returnName='', status=0,
                                                                               deviceId=deviceId,
                                                                               gameboxVersion=gameboxVersion,
                                                                               hiappVersion=hiappVersion,
                                                                               hmsVersion=hmsVersion);

        g.db.execute(deviceUpdateSql)
        g.db.commit()
    return 'rtnCode:0'


if __name__ == '__main__':
    # admin = Admin(app,base_template='login.html')
    admin = Admin(app)

    admin.add_view(RentLogView(db.session, name=u'手机借还记录', endpoint='RentLogView', category=u'数据查看'))
    admin.add_view(DevicesView(db.session, name=u'手机状态查看', endpoint='DevicesView', category=u'数据查看'))
    admin.add_view(ModelView(rentlog, db.session, name=u'手机借还记录', endpoint='RentLogFix', category=u'数据维护'))
    admin.add_view(ModelView(devices, db.session, name=u'手机状态维护', endpoint='DevicesFix', category=u'数据维护'))
    app.run(host="0.0.0.0", port=9999, debug=True)
