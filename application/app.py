from flask import Flask, render_template, request,redirect,url_for,jsonify
import sqlite3
import datetime
import db

# .venv\Scripts\activate.bat 有効化


#####################################################################################################################################################################
##################################################################   これはFlaskのメインファイルです   ################################################################
#####################################################################################################################################################################


app = Flask(__name__)

DBTABLE = ("sample1","sample2","sample3")# <---------   ここに場所追加
TXT_LOG = 'history.log'
DATABASE = 'DB.db'


for NAME in DBTABLE:
    db.create_db(NAME)


@app.route("/", methods=["GET"])#トップページ表示
def top():
    PLACE="sample1"#欲しいデータのテーブル名 ((DBNAMEで設定した中から))

    con = sqlite3.connect(DATABASE)
    db_data = con.execute("SELECT * FROM %s where time = '2024/02/20 19:51:10'" % PLACE).fetchall()
    con.close()

    data = []
    for row in db_data:
        data.append({"time": row[1], "condition": row[2]})
    WriteLog("GET","---","connect web site.")
    return render_template("home.html" , get_data=data)
#dataの構成は   [{ "time" : '' , "condition" : '' },{ "time" : '' , "condition" : '' }........]


#####################################################################################################################################################################
##################################################################   以下にルーティングする場所を追加   ###############################################################
#####################################################################################################################################################################


@app.route("/sample1",methods=['GET','POST'])
def sample1():
    PLACE="sample1"#欲しいデータのテーブル名 ((DBNAMEで設定した中から))
    data = []
    if request.method=='POST':


#####################################################################################################
######################## この間の文を複製することで任意の数の時刻のデータを取得 ########################


        TIME='2024/02/20 21:23:56'#欲しい時間を指定

        con = sqlite3.connect(DATABASE)
        db_data = con.execute("SELECT * FROM %s where time = ? " % PLACE, (TIME,)).fetchall()
        con.close()

        data.append({"time": db_data[0][1], "condition": db_data[0][2]})

######################## この間の文を複製することで任意の数の時刻のデータを取得 ########################
####################################################################################################



        WriteLog("POST","sample1","connect web site.")
        return render_template("sample1.html" , get_data=data)#アクセスするhtmlファイルを設定
    else:

######################## ""GET""メソッドでアクセスされたら最新のものを取得 ########################


        con = sqlite3.connect(DATABASE)
        latest = con.execute("SELECT max(ID) from %s" % PLACE).fetchall()
        con.close()
        con = sqlite3.connect(DATABASE)
        db_data = con.execute("SELECT * FROM %s where ID = ? " % PLACE , (latest[0][0],)).fetchall()
        con.close()



        data.append({"time": db_data[0][1], "condition": db_data[0][2]})
        print(data)
        WriteLog("GET","sample1","connect web site.")
        return render_template("sample1.html" , get_data=data)#アクセスするhtmlファイルを設定






#####################################################################################################################################################################
##################################################################   以上にルーティングする場所を追加   ###############################################################
#####################################################################################################################################################################

@app.route("/write_date/ここはデータベース書き込み用のURLです", methods=["POST"])#DB書き込み
def write_date():
    try:
        #ここはデータの受け取り方によって """PLACE""" , """condition""" を書き換える


        #maybe 画像検出用の.pyファイルがあるならimport文でヨシ
        #      リクエスト受けて書き込むなら
        data = request.get_json()
        PLACE = data.get("place", "default_PLACE")
        condition = data.get("condition", "default_condition")


###################################################################################
################################   ただしjson形式   ################################
####################################################################################

        #PLACE = "place"
        #condition ="condition"
        time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        WriteData(PLACE,time,condition)
        WriteLog("POST",PLACE,"add DATA success!")
        return jsonify({"result": True})
    except:
        WriteLog("POST",PLACE,"add DATA error.")
        return jsonify({"result": False})



def WriteLog(place,type,Message):#LOG書き込み関数
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    f = open(TXT_LOG, 'a')
    f.write(f'{now} || {type.ljust(20)}| {place.ljust(15)}| {Message}\n')
    f.close()

def WriteData(place,time,condition):#DB書き込み関数
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO %s (time ,condition) VALUES (?, ?)" % place, (time,condition))
    con.commit()
    con.close()


if __name__ == "__main__":  #Flask起動
    app.run(port=int("5000"), debug=True, host="localhost")

    # 開発時 ->port=int("5000"), debug=True, host="localhost"
    # 実装時 ->port=int("5000"), debug=False, host="0.0.0.0"
