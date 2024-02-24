from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import requests
import time
import os
from bs4 import BeautifulSoup
import hito

global TIME
global place

def capture_screenshots(target_string, time):
    global TIME
    global place
    TIME = time
    place = target_string
    # Chromeドライバーのパス
    #CHROMEDRIVER_PATH = "./chromedriver.exe"
    # ライブストリームURLの辞書
    URLS = {
        "嵐山": "https://www.youtube.com/watch?v=Op-lf2NRMzs&t=0s",
        "本願寺": "https://hongwanji-live.securesite.jp/camera/camera01.jpg",
        "智積院": "https://www.youtube.com/watch?v=n8uPgSSZCEc",
        "伏見稲荷": "https://www.youtube.com/watch?v=pgqwfZj9HPY",
        "花見小路": "https://www.youtube.com/watch?v=PXg3ZXgMkGk",
        "天橋立": "https://www.youtube.com/watch?v=ZCWMo8yzWT0",
        "ねねの道": "https://www.youtube.com/watch?v=Gxt3YCa2Phc",
        "北野天満宮": "https://www.youtube.com/watch?v=KHglGodzQ9g",
        "銀閣寺":"https://www.shokoku-ji.jp/read_live_camera_image/?src=/img/webcam/ginkaku/full/ginkaku01.jpg",
        # 他の特定の文字列に対するURLを追加
    }

    # 対応するURLを取得
    url = URLS.get(target_string)
    #print("今は"+url)
    # もしURLが存在しない場合は終了
    if url is None:
        print(f"URL for {target_string} is not found.")
        return None

    # ブラウザを起動
    # ブラウザを起動
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # ブラウザをバックグラウンドで実行
    driver = webdriver.Chrome(options=options)

    screenshots = []  # ここにスクリーンショットを追加していく
    try:
        if target_string == "本願寺" :
           
            try:
                if target_string == "本願寺":
                    # 画像を取得
                    response = requests.get(url)
                    if response.status_code == 200:
                        # 取得した画像を直接返す
                        img = Image.open(BytesIO(response.content))
                        return img
            except KeyboardInterrupt:
                print("Program terminated by user.")
                
        if target_string == "銀閣寺":
            try:
                # 画像のURL
                #image_url = "https://www.shokoku-ji.jp/read_live_camera_image/?src=/img/webcam/ginkaku/full/ginkaku01.jpg"
                # 画像を取得
                response = requests.get(url)
                # 取得した画像を開く
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    return img
                else:
                     print("Failed to fetch image")
            except KeyboardInterrupt:
                print("Program terminated by user.")
        
        else:
            
            count = 1
            while count < 2:
                try:
                    # YouTubeのライブストリームページを開く
                    driver.get(url)

                    # ウェブページの読み込みが完了するまで待機
                    wait = WebDriverWait(driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ytp-large-play-button")))

                    # 動画再生ボタンがクリック可能になるまで待機
                    play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-large-play-button")))
                    play_button.click()

                    # 再生部分の要素を特定して位置とサイズを取得
                    video_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "html5-main-video")))
                    location = video_element.location
                    size = video_element.size

                    location['y'] += 2
                    location['x'] += 25
                    time.sleep(10)
                    count = 1
                    while count < 2:
                        try:
                            # スクリーンショットを取得して保存
                            screenshot = driver.get_screenshot_as_png()
                            screenshot = Image.open(BytesIO(screenshot))
                            screenshot = screenshot.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
                            screenshots.append(screenshot)  # リストに追加
                            print(f"Screenshot {count} taken")

                            # 次のスクリーンショットまで待機
                            time.sleep(10)  # 10秒ごとにスクリーンショットを取得

                            count += 1
                        except Exception as e:
                            print("An error occurred while taking screenshot:", e)
                            # エラーが発生した場合はページを再読み込みして続行
                            driver.refresh()
                except Exception as e:
                    print("An error occurred:", e)
                    # エラーが発生した場合はプログラムを継続
                    continue
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        # ブラウザを閉じる
        driver.quit()
    
    img = screenshots[0] if screenshots else None

    return img  

####################################################################
# # 実行例
IMG = capture_screenshots("伏見稲荷")
# print(IMG)
# print("人物検出")
hito.process(IMG)

hito.analyze(place,TIME,IMG)

