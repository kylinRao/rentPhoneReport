DROP TABLE IF EXISTS rentLog;
CREATE TABLE rentLog
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              phone TEXT,
              rentPhoneType TEXT,
              actionType int,
              renttime DATA DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')),
              returntime DAT)

