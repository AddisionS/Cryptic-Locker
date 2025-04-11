from PIL import Image, ImageDraw, ImageFont

def generate_header():
    img = Image.new("RGB", (600, 100), color="#337b87")

    font = ImageFont.truetype("../assets/fonts/BungeeShade-Regular.ttf", size=52)

    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "CRYPTIC LOCKER", font=font, fill="#f1f5f4")

    return img
