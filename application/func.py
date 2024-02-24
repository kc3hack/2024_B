import sqlite3
import datetime
import requests
import json


#############################################################################################################################################################################
################################################################# ここはapp.pyで使用する関数があるファイルです #################################################################
#############################################################################################################################################################################



TXT_LOG = 'history.log'
DATABASE = 'DB.db'
PASSKEY = "1111"


def create_db(DBNAME):#任意のテーブルを作成する関数
    con=sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS %s (ID INTEGER PRIMARY KEY AUTOINCREMENT,time ,condition,rich)" % DBNAME)
    con.close()


def WriteLog(type,place,Message):#LOG書き込み関数
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    f = open(TXT_LOG, 'a')
    f.write(f'{now} || {type.ljust(10)}| {Message.ljust(40)}| {place}\n')
    f.close()


def WriteData(place,time,condition,rich):#DB書き込み関数
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO %s (time ,condition ,rich) VALUES (?, ?, ?)" % place, (time,condition,rich))
    con.commit()
    con.close()


def receiveData(PLACE,TIME,data):#DBから任意のテーブル、時刻のデータを変数dataに追加する関数
    con = sqlite3.connect(DATABASE)
    db_data = con.execute("SELECT * FROM %s where time = ? " % PLACE, (TIME,)).fetchall()
    con.close()
    data.append({"time": db_data[0][1], "condition": db_data[0][2]})
    return data


def receiveData_latest(PLACE,data):#DBから任意のテーブルの最新のデータを変数dataに追加する関数
    con = sqlite3.connect(DATABASE)
    latest = con.execute("SELECT max(ID) from %s" % PLACE).fetchall()
    con.close()
    con = sqlite3.connect(DATABASE)
    db_data = con.execute("SELECT * FROM %s where ID = ? " % PLACE , (latest[0][0],)).fetchall()
    con.close()
    data.append({"time": db_data[0][1], "condition": db_data[0][2]})
    return data

def receiveRichData_latest(PLACE,data):#DBから任意のテーブルの最新のデータを変数dataに追加する関数
    con = sqlite3.connect(DATABASE)
    latest = con.execute("SELECT max(ID) from %s" % PLACE).fetchall()
    con.close()
    con = sqlite3.connect(DATABASE)
    db_data = con.execute("SELECT * FROM %s where ID = ? " % PLACE , (latest[0][0],)).fetchall()
    con.close()
    data.append({"place":PLACE,"time": db_data[0][1], "rich": db_data[0][3]})
    return data

def check_passkey(passkey):
    return passkey==PASSKEY
