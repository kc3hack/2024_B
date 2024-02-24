import requests
from PIL import Image
import time
import os

# 画像を取得するURL
IMAGE_URL = "https://hongwanji-live.securesite.jp/camera/camera01.jpg"

# 保存先ディレクトリ
SAVE_DIR = "./images/"

def save_image(image_data, filename):
    # 画像を保存する
    image_path = os.path.join(SAVE_DIR, filename)
    with open(image_path, 'wb') as f:
        f.write(image_data)
    print(f"Image saved: {image_path}")

def main():
    # 保存先ディレクトリを作成
    os.makedirs(SAVE_DIR, exist_ok=True)

    try:
        while True:
            # 画像を取得
            response = requests.get(IMAGE_URL)
            if response.status_code == 200:
                # 画像を保存
                timestamp = time.strftime("%Y%m%d%H%M")
                filename = f"image_{timestamp}.jpg"
                save_image(response.content, filename)

            # 10秒待機
            time.sleep(10)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
