from ultralytics import YOLO
import collections
from decimal import *

global model
model = YOLO("./models/yolov8x.pt")
global results
global person_count
global backpack_count
global suitcase_count
global umbrella_count
global traveler_rate

import requests
import json

global place
global time
global url
url = "http://localhost:5000/"+"write_date/ここはデータベース書き込み用のURLです"

'''
initialize(_place, _time): この関数は、場所と時間を引数として受け取り、
グローバル変数 place と time にそれぞれ格納します。これらの変数は後で他の関数で使用されます。
'''
def initialize(_place, _time):
    global place
    global time
    place = _place
    time = _time

'''
process(_img): この関数は、画像 _img を引数として受け取り、
YOLO モデルを使用して物体検出を行います。
検出された物体の数や種類を取得し、それらの情報をグローバル変数に格納します。
また、検出された人の数が 0 の場合は 1 として扱います。
最後に、旅行者の割合を計算し、適切な精度で丸めます。
'''
def process(_img):
    global model
    global results
    global person_count
    global backpack_count
    global suitcase_count
    global umbrella_count
    global traveler_rate
    results = model(_img,show=False,conf=0.05,classes=[0,24,28,25])
    #person,backpack,suitcase,umbrella
    detected_class = results[0].boxes.cls
    detected_class = detected_class.tolist()
    counter = collections.Counter(detected_class)
    person_count = counter[0]
    backpack_count = counter[24]
    suitcase_count = counter[28]
    umbrella_count = counter[25]
    if person_count == 0:
        person_count = 1
    traveler_rate = (backpack_count+suitcase_count)/person_count
    traveler_rate = Decimal(str(traveler_rate))
    traveler_rate = traveler_rate.quantize(Decimal(".0001"),rounding=ROUND_HALF_UP)
'''
update(): この関数は、データベースを更新するために必要な情報を含む HTTP POST リクエストを送信します。
グローバル変数 place と time、および物体検出の結果から得られた情報を使用して、
データを構築し、JSON 形式に変換してリクエストの本文とします。
その後、リクエストを送信し、サーバーからの応答を受け取ります。
'''
def update():
    global place
    global time
    global url
    data = {"place": place, "time": time, "condition": person_count}
    headers = {"Content-type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    #print(response.json())

'''
analyze(_place, _time, _img): この関数は、場所、時間、および画像を引数として受け取り、
initialize を呼び出してグローバル変数 place と time を設定し、
process を呼び出して物体検出を実行します。最後に、update を呼び出してデータベースを更新します。
'''
def analyze(_place, _time, _img):
    initialize(_place, _time)
    process(_img)
    update()
    
from PIL import Image

# 画像を読み込む
img = Image.open("screenshot_39.png")

# 分析対象の場所と時間を設定する
place = "嵐山"
time = "2024"

# analyze 関数を呼び出して物体検出を実行し、データベースを更新する
analyze(place, time, img)
