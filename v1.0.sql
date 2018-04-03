DROP TABLE IF EXISTS rentLog;
CREATE TABLE rentLog(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,-- 使用者姓名
phone TEXT,--   使用者的电话号码，方便管理者联系到使用者
rentPhoneType TEXT,----当前手机的型号，如荣耀V8等
deviceId TEXT,----当前手机的imei号
status int,--当前手机状态，0表示已结束流程，1表示借出状态

renttime DATA DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')),
returntime DAT,
battaryLevel int,---当前手机的电量信息
gameboxVersion TEXT, ---当前手机的游戏中心版本号信息
hiappVersion  TEXT, --当前手机应用市场的版本号信息
hmsVersion   TEXT  ---当前手机华为移动服务的版本号信息
);

