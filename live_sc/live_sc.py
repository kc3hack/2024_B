from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import time
import os

# Chromeドライバーのパス
CHROMEDRIVER_PATH = "./chromedriver.exe"

# YouTubeのライブストリームURL
LIVESTREAM_URL = "https://www.youtube.com/watch?v=Op-lf2NRMzs&t=0s"

# スクリーンショットの保存先ディレクトリ
SCREENSHOT_DIR = "./screenshots/"

# Chromeドライバーを起動
driver = webdriver.Chrome()
try:
    while True:
        try:
            # YouTubeのライブストリームページを開く
            driver.get(LIVESTREAM_URL)

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
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)

            count = 1
            while True:
                try:
                    # スクリーンショットを取得して保存
                    screenshot = driver.get_screenshot_as_png()
                    screenshot = Image.open(BytesIO(screenshot))
                    screenshot = screenshot.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
                    screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{count}.png")
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
