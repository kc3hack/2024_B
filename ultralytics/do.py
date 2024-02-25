import time
import schedule
import datetime
import requests,json
import time
from test import capture_screenshots

time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
DBTABLE = ("嵐山","銀閣寺","本願寺","智積院","伏見稲荷","花見小路","北野天満宮","天橋立")# <---------   ここに場所追加


schedule.every(10).minutes.do(capture_screenshots,DBTABLE[0],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[1],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[2],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[3],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[4],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[5],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[6],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも
schedule.every(10).minutes.do(capture_screenshots,DBTABLE[7],time)# <- 関数とか、なんなら上に関数追加してデータを送るのでも

while True:
    schedule.run_pending()
