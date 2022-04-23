from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
from colorthief import ColorThief

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_name = request.files['image']
        color_thief = ColorThief(file_name)
        color_palette = color_thief.get_palette(color_count=10, quality=1)
        hex_color = []
        for color in color_palette:
            hex_color.append('#%02x%02x%02x' % color)
        # hex_value = '#%02x%02x%02x' % (r, g, b)
        print(hex_color)
        return render_template('index.html', hex_color=hex_color)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
