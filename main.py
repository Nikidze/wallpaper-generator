from PIL import Image, ImageDraw, ImageFont
import json
from random import choice
import subprocess

backgeound_color = "#2e2e2e"
primary_color = "#fb9f1b"
secondary_color = "#fafafa"

W, H = 1920, 1080

font1 = ImageFont.truetype("font.ttf", 80)
font2 = ImageFont.truetype("font2.ttf", 30)

title = "bspwm"

path = "/tmp/wallpaper.png"
quotes = "qoutes.json"

with open(quotes, 'r') as quotes:
    quotes = json.load(quotes)

quote = choice(quotes)

author = quote["author"]
quote = '«' + quote["quote"] + '»'


def get_w_and_h(text, font):
    _, _, w, h = draw.textbbox((0, 0), text, font)
    return w, h

img = Image.new('RGB', (W, H), color = backgeound_color)
draw = ImageDraw.Draw(img)

w, h = get_w_and_h(title, font1)
draw.text(((W-w)/2, (H/1.25-h)/2), title, font=font1, fill=secondary_color)

draw.line(((W-w)/2, (H-h)/2, (W+w)/2, (H-h)/2), fill=primary_color, width=3)

w, h = get_w_and_h(quote, font2)
draw.text(((W-w)/2, (H-h)/2), quote, font=font2, fill=secondary_color)

w2, _ = get_w_and_h(author, font=font2)
draw.text((W-(W-w)/2-w2, (H-h)/2+1.5*h), author, font=font2, fill=secondary_color)

img.save(path)
subprocess.run(["feh", "--bg-max", "/tmp/wallpaper.png"])