import time
import schedule
import datetime
import requests,json
from post import get



schedule.every(1).minutes.do(get)# <- 関数とか

while True:
    schedule.run_pending()

