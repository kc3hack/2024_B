from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import requests
import time
import os

def capture_screenshots(target_string):
    # Chromeドライバーのパス
    CHROMEDRIVER_PATH = "./chromedriver.exe"

    # スクリーンショットおよび画像の保存先ディレクトリ
    SAVE_DIR = "./media/"

    # ライブストリームURLの辞書
    URLS = {
        "嵐山": "https://www.youtube.com/watch?v=Op-lf2NRMzs&t=0s",
        "本願寺": "https://hongwanji-live.securesite.jp/camera/camera01.html",
        # 他の特定の文字列に対するURLを追加
    }

    # 対応するURLを取得
    url = URLS.get(target_string)

    # ブラウザを起動
    driver = webdriver.Chrome()
    try:
        
        if target_string == "本願寺":
            # 画像を取得するURL
            IMAGE_URL = "https://hongwanji-live.securesite.jp/camera/camera01.jpg"

            # 保存先ファイルパスを作成
            os.makedirs(SAVE_DIR, exist_ok=True)

            try:
                while True:
                    # 画像を取得
                    response = requests.get(IMAGE_URL)
                    if response.status_code == 200:
                        # 画像を保存
                        timestamp = time.strftime("%Y%m%d%H%M")
                        filename = f"image_{timestamp}.jpg"
                        image_path = os.path.join(SAVE_DIR, filename)
                        with open(image_path, 'wb') as f:
                            f.write(response.content)
                        print(f"Image saved: {image_path}")

                    # 10秒待機
                    time.sleep(10)
            except KeyboardInterrupt:
                print("Program terminated by user.")
        while True:
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

                location['y'] += 80  

                # スクリーンショットの保存先ディレクトリを作成
                os.makedirs(SAVE_DIR, exist_ok=True)

                count = 1
                while True:
                    try:
                        # スクリーンショットを取得して保存
                        screenshot = driver.get_screenshot_as_png()
                        screenshot = Image.open(BytesIO(screenshot))
                        screenshot = screenshot.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
                        screenshot_path = os.path.join(SAVE_DIR, f"screenshot_{count}.png")
                        screenshot.save(screenshot_path)
                        print(f"Screenshot {count} saved at {screenshot_path}")

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

# 他のプログラムから呼び出す際に文字列を引数として渡す
# 嵐山という文字列を引数として渡す
capture_screenshots("本願寺")
