# coding=utf-8
import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)
DATABASE = './phone.db'
conn = sqlite3.connect(DATABASE)
# 创建表格、插入数据
@app.before_first_request
def create_db():
  # 连接
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  # 创建表
#   c.execute('''DROP TABLE IF EXISTS rentLog''')
#   c.execute('''
# CREATE TABLE rentLog
#               (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               name TEXT,
#               phone TEXT,
#               rentPhoneType TEXT,
#               actionType int,
#               renttime DATA DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')),
#               returntime DATA )
#               ''')
  with open('v1.0.sql','r') as f:
    c.executescript(f.read());


  # 数据
  # 格式：用户名,邮箱
  purchases = [('admin', 'admin@example.com','XIAOMI',1),
        ('admin0', 'admin@example.com','XIAOLAJIAO',0),
         ('admin2', 'admin@example.com','DAMI',1)]
  # 插入数据
  c.executemany('INSERT INTO rentLog (name, phone,rentPhoneType,status) VALUES (?,?,?,?)', purchases)
  # 提交！！！
  conn.commit()
  # 关闭
  conn.close()
def get_db():
  db = sqlite3.connect(DATABASE)
  db.row_factory = sqlite3.Row
  return db
def query_db(query, args=(), one=False):
  db = get_db()
  cur = db.execute(query, args)
  db.commit()
  rv = cur.fetchall()
  db.close()
  return (rv[0] if rv else None) if one else rv
@app.route("/user")
def users():
  res = query_db("SELECT * FROM user WHERE id <= ?", args=(6,))
  return "<br>".join(["{0}: {1}".format(user[1], user[2]) for user in res])
@app.route("/user/<int:id>")
def user(name):
  res = query_db("SELECT * FROM user WHERE id=?", args=(id,)) #不妨设定：第一次只返回6个数据
  return jsonify(id = res[1],
          name = res[2],
          email = res[3]) # 返回json格式
if __name__ == '__main__':
    create_db()