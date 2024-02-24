import time
import schedule
import datetime
import requests,json
from post import get



schedule.every(1).minutes.do(get)# <- 関数とか、なんなら上に関数追加してデータを送るのでも

while True:
    schedule.run_pending()

import sys
sys.path.append('live_sc')  # live_scディレクトリをモジュール検索パスに追加

import ファイル名  # ファイル名はlive_scディレクトリ内のPythonファイル名
