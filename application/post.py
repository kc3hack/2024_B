import requests
import json
import datetime

def get():
    url = "http://127.0.0.1:5000/write_date/ここはデータベース書き込み用のURLです"

    time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    data = {"place": "sample3", "condition": "テスト","time":time}


    headers = {"Content-type": "application/json"}

    response = requests.post(url, data=json.dumps(data), headers=headers)

    print(response.json())# <- ((true or false))
