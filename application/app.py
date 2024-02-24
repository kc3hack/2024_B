from flask import Flask, render_template, request,redirect,url_for,jsonify,Blueprint,session
import sqlite3
import datetime
import func





# .venv\Scripts\activate.bat 有効化


#####################################################################################################################################################################
##################################################################   これはFlaskのメインファイルです   ################################################################
#####################################################################################################################################################################



"""  dataの構成は   [{ "time" : '' , "condition" : '' },{ "time" : '' , "condition" : '' }........]  """

app=Flask(__name__)
app.secret_key = b"efb94fcefa1ef7f281d69a979cdf251b2b9bdd8b770d7a0fbfb9427287fec9f6"
#app1= Blueprint('app',__name__,template_folder='templates')

def pad_filter(s, width):
    return str(s).ljust(width)

DBTABLE = ("test","嵐山","銀閣寺","本願寺","智積院","伏見稲荷","花見小路","北野天満宮","天橋立")# <---------   ここに場所追加
TXT_LOG = 'history.log'
DATABASE = 'DB.db'


for NAME in DBTABLE:
    func.create_db(NAME)

def login_required(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("passkey") is None:
            return redirect("/")
        else:
            return func(*args, **kwargs)
    return wrapper


@app.route("/", methods=["GET","POST"])#トップページ表示
def top():
    if request.method == "GET":
        func.WriteLog("GET","/","connect web site.")
        return render_template("home.html",msg="1")
    else:
        passkey = request.form["password"]
        if func.check_passkey(passkey):
            session["passkey"] = passkey
            return redirect(url_for("administrator"))
        else:
            return render_template("home.html",msg="2")


@app.route("/administrator")
@login_required
def administrator():
    data=[]
    for NAME in DBTABLE:
        func.receiveRichData_latest(NAME,data)
    print(data)
    return render_template("administrator.html",get_data=data)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


#####################################################################################################################################################################
##################################################################   以下にルーティングする場所を追加   ###############################################################
#####################################################################################################################################################################


@app.route("/test",methods=['GET','POST'])
def test():
    PLACE="test"#欲しいデータのテーブル名 ((DBNAMEで設定した中から))
    data = []
    if request.method=='POST':

#####################################################################################################
######################## この間の文を複製することで任意の数の時刻のデータを取得 ########################

        TIME='2024/02/21 13:03:03'#欲しい時間を指定
        data = func.receiveData(PLACE,TIME,data)

######################## この間の文を複製することで任意の数の時刻のデータを取得 ########################
####################################################################################################

        func.WriteLog("POST","/test","connect web site.")
        return render_template("test.html" , get_data=data)#アクセスするhtmlファイルを設定
    else:

        """"""""""""""""""""""""" '''GET'''メソッドでアクセスされたら最新のものを取得 """""""""""""""""""""""""

        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/test","connect web site.")
        return render_template("test.html" , get_data=data)#アクセスするhtmlファイルを設定


@app.route("/嵐山",methods=['GET','POST'])
def 嵐山():
    PLACE="嵐山"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/arashiyama","connect web site.")
        return render_template("嵐山.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/arashiyama","connect web site.")
        return render_template("嵐山.html" , get_data=data)


@app.route("/銀閣寺",methods=['GET','POST'])
def 銀閣寺():
    PLACE="銀閣寺"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/ginkakuji","connect web site.")
        return render_template("銀閣寺.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/ginkakuji","connect web site.")
        return render_template("銀閣寺.html" , get_data=data)


@app.route("/本願寺",methods=['GET','POST'])
def 本願寺():
    PLACE="本願寺"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/honganji","connect web site.")
        return render_template("本願寺.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/honganji","connect web site.")
        return render_template("本願寺.html" , get_data=data)


@app.route("/智積院",methods=['GET','POST'])
def 智積院():
    PLACE="智積院"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/tisyakuin","connect web site.")
        return render_template("智積院.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/tisyakuin","connect web site.")
        return render_template("智積院.html" , get_data=data)


@app.route("/伏見稲荷",methods=['GET','POST'])
def 伏見稲荷():
    PLACE="伏見稲荷"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/伏見稲荷","connect web site.")
        return render_template("伏見稲荷.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/伏見稲荷","connect web site.")
        return render_template("伏見稲荷.html" , get_data=data)


@app.route("/花見小路",methods=['GET','POST'])
def 花見小路():
    PLACE="花見小路"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/花見小路","connect web site.")
        return render_template("花見小路.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/花見小路","connect web site.")
        return render_template("花見小路.html" , get_data=data)


@app.route("/北野天満宮",methods=['GET','POST'])
def 北野天満宮():
    PLACE="北野天満宮"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/北野天満宮","connect web site.")
        return render_template("北野天満宮.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/北野天満宮","connect web site.")
        return render_template("北野天満宮.html" , get_data=data)


@app.route("/天橋立",methods=['GET','POST'])
def 天橋立():
    PLACE="天橋立"
    data = []
    if request.method=='POST':
        TIME='2024/02/21 13:03:03'
        data = func.receiveData(PLACE,TIME,data)
        func.WriteLog("POST","/天橋立","connect web site.")
        return render_template("天橋立.html" , get_data=data)

    else:
        func.receiveData_latest(PLACE,data)
        func.WriteLog("GET","/天橋立","connect web site.")
        return render_template("天橋立.html" , get_data=data)




#####################################################################################################################################################################
##################################################################   以上にルーティングする場所を追加   ###############################################################
#####################################################################################################################################################################

@app.route("/write_date/ここはデータベース書き込み用のURLです", methods=["POST"])#DB書き込み
def ここはデータベース書き込み用のURLです():
    try:
        data = request.get_json()
        PLACE = data.get("place", "XXX")
        condition = data.get("condition", "XXX")
        time = data.get("time","XXXX/XX/XX XX:XX:XX")
        rich=data.get("rich","XXX")
        func.WriteData(PLACE,time,condition,rich)
        func.WriteLog("POST","/"+PLACE,"add DATA success!")
        return jsonify({"result": True})
    except:
        func.WriteLog("POST","/"+PLACE,"add DATA error.")
        return jsonify({"result": False})


if __name__ == "__main__":  #Flask起動
    app.run(port=int("5000"), debug=True, host="localhost")



    # 開発時 ->port=int("5000"), debug=True, host="localhost"
    # 実装時 ->port=int("5000"), debug=False, host="0.0.0.0"


    #http://localhost:5000/
    #http://127.0.0.1:5000/
    #http://192.168.0.10:5000/
