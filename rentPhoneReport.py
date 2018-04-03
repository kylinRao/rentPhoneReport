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
        phone,name,deviceId,rentPhoneType = request.form.get("phone",'getNoPhone'),request.form.get("name",'getNoName'),request.form.get("deviceId",'getNodeviceId'),request.form.get("phoneType",'getNophoneType');

        print(request.method)
        print(request.form.get("phone",'getNoPhone'),
              request.form.get("name",'getNoName'),
              request.form.get("deviceId",'getNodeviceId'),
              request.form.get("phoneType",'getNophoneType'),)
        rentSql = "INSERT INTO rentLog (name, phone,deviceId,rentPhoneType,status) VALUES (?,?,?,?,?)"
        g.db.execute(rentSql,(name, phone,deviceId,rentPhoneType,1))
        g.db.commit()
    if request.form.get("method",'getNoMethod') == "return":
        phone,name,deviceId,rentPhoneType = request.form.get("phone",'getNoPhone'),request.form.get("name",'getNoName'),request.form.get("deviceId",'getNodeviceId'),request.form.get("phoneType",'getNophoneType');

        print(request.method)
        print(request.form.get("phone",'getNoPhone'),
              request.form.get("name",'getNoName'),
              request.form.get("deviceId",'getNodeviceId'),
              request.form.get("phoneType",'getNophoneType'),)
        rentSql = "INSERT INTO rentLog (name, phone,deviceId,rentPhoneType,status) VALUES (?,?,?,?,?)"
        g.db.execute(rentSql,(name, phone,deviceId,rentPhoneType,1))
        g.db.commit()



    return 'rtnCode:0'



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888,debug=True)
