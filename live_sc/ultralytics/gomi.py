import hito
from PIL import Image

# 画像を読み込む
img = Image.open("screenshot_39.png")

# 分析対象の場所と時間を設定する
place = "嵐山"
time = "2024"

# analyze 関数を呼び出して物体検出を実行し、データベースを更新する
hito.process(img)
from PIL import ImageDraw, ImageFont

# 物体検出の結果を含む画像のコピーを作成
draw_img = img.copy()
draw = ImageDraw.Draw(draw_img)

# 物体のラベルと枠の描画
font = ImageFont.truetype("arial.ttf", 20)
for box in results.xyxy[0]:
    label = model.names[int(box[5])]
    draw.rectangle(box[:4], outline="red", width=3)
    draw.text((box[0], box[1]), label, fill="red", font=font)

# 画像を保存
draw_img.save("detected_image.png")

# 保存された画像を表示
draw_img.show()
