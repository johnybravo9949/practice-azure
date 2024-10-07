from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Create an image with 'HELLO WORLD :)' text
    img = Image.new('RGB', (500, 250), color=(73, 109, 137))
    d = ImageDraw.Draw(img)

    # If you have a specific font you want to use, you can specify the path to the .ttf file
    # font = ImageFont.truetype("path_to_font.ttf", 40)
    d.text((100, 100), "HELLO WORLD :)", fill=(255, 255, 0))

    # Save the image to a BytesIO object
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
