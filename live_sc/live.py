from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Chromeドライバーのパス（自分の環境に合わせて変更してください）
CHROMEDRIVER_PATH = "./chromedriver.exe"

# YouTubeのライブストリームURL
LIVESTREAM_URL = "https://www.youtube.com/watch?v=v9rQqa_VTEY"

# スクリーンショットの保存先ディレクトリ
SCREENSHOT_DIR = "./screenshots/"

# Chromeドライバーを起動
driver = webdriver.Chrome()
try:
    # YouTubeのライブストリームページを開く
    driver.get(LIVESTREAM_URL)

    # ウェブページの読み込みが完了するまで待機
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ytp-large-play-button")))

    # 動画再生ボタンがクリック可能になるまで待機
    play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-large-play-button")))
    play_button.click()

    # スクリーンショットの保存先ディレクトリを作成
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    count = 1
    while True:
        # スクリーンショットを取得して保存
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{count}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot {count} saved at {screenshot_path}")

        # 次のスクリーンショットまで待機
        time.sleep(10)  # 10秒ごとにスクリーンショットを取得

        count += 1
        

except Exception as e:
    print("An error occurred:", e)

finally:
    # ブラウザを閉じる
    driver.quit()
