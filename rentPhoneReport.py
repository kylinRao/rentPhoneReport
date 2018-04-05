from flask import Flask, request
import sqlite3
from flask import g

app = Flask(__name__)

DATABASE = r'D:\projects\github\rentPhoneReport\phone.db'

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




@app.route('/rentPhoneReport',methods=['POST','GET'])
def hello_world():
    if request.form.get("method",'getNoMethod') == "rent":
        phone,name,deviceId,rentPhoneType,battaryLevel,gameboxVersion,hiappVersion,hmsVersion = request.form.get("phone",'getNoPhone'),                                                                                            request.form.get("name",'getNoName'),\
                                                                                                request.form.get("deviceId",'getNodeviceId'),\
                                                                                                request.form.get("phoneType",'getNophoneType'),\
                                                                                                request.form.get("battaryLevel",'getNobattaryLevel'),\
                                                                                                request.form.get("gameboxVersion",'getNogameboxVersion'),\
                                                                                                request.form.get("hiappVersion",'getNohiappVersion'),\
                                                                                                request.form.get("hmsVersion",'getNohmsVersion');
        print(request.method)
        print(request.form.get("phone",'getNoPhone'),
              request.form.get("name",'getNoName'),
              request.form.get("deviceId",'getNodeviceId'),
              request.form.get("phoneType",'getNophoneType'),)
        rentSql = u"INSERT INTO rentLog (name, phone,deviceId,rentPhoneType,status,battaryLevel,gameboxVersion,hiappVersion,hmsVersion) " \
                  u"VALUES ('{name}','{phone}','{deviceId}','{rentPhoneType}','{status}','{battaryLevel}','{gameboxVersion}','{hiappVersion}','{hmsVersion}')".format(
            name=name,phone=phone,deviceId=deviceId,rentPhoneType=rentPhoneType,status=1,battaryLevel=battaryLevel,gameboxVersion=gameboxVersion,hiappVersion=hiappVersion,hmsVersion=hmsVersion
        )
        g.db.execute(rentSql)
        g.db.commit()
    if request.form.get("method",'getNoMethod') == "return":
        phone,name,deviceId,rentPhoneType,battaryLevel,gameboxVersion,hiappVersion,hmsVersion = request.form.get("phone",'getNoPhone'),                                                                                            request.form.get("name",'getNoName'),\
                                                                                                request.form.get("deviceId",'getNodeviceId'),\
                                                                                                request.form.get("phoneType",'getNophoneType'),\
                                                                                                request.form.get("battaryLevel",'getNobattaryLevel'),\
                                                                                                request.form.get("gameboxVersion",'getNogameboxVersion'),\
                                                                                                request.form.get("hiappVersion",'getNohiappVersion'),\
                                                                                                request.form.get("hmsVersion",'getNohmsVersion');

        print(request.method)
        print(request.form.get("phone",'getNoPhone'),
              request.form.get("name",'getNoName'),
              request.form.get("deviceId",'getNodeviceId'),
              request.form.get("phoneType",'getNophoneType'),)
        returnSql = u"UPDATE rentLog set returnName='{returnName}',returnPhone='{returnPhone}',status={status},returnTime=(datetime(CURRENT_TIMESTAMP,'localtime')),battaryLevel='{battaryLevel}',gameboxVersion='{gameboxVersion}',hiappVersion='{hiappVersion}',hmsVersion='{hmsVersion}' " \
                    u"where status=1 and deviceId = '{deviceId}'".format(returnName=name,status=0,returnPhone=phone,deviceId=deviceId,battaryLevel=battaryLevel,gameboxVersion=gameboxVersion,hiappVersion=hiappVersion,hmsVersion=hmsVersion);
        print returnSql
        g.db.execute(returnSql)
        g.db.commit()



    return 'rtnCode:0'



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9999,debug=True)
