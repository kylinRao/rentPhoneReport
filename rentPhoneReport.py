from flask import Flask, request
import sqlite3
from flask import g

app = Flask(__name__)

DATABASE = './phone.db'

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
    print(request.method)
    print(request.form.get("phone",'getNoPhone'),request.form.get("name",'getNoName'))


    return 'rtnCode:0'



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888,debug=True)
