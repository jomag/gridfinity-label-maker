import math
from PIL import Image, ImageFont, ImageDraw

# Use "1" for monochrome, "RGB" for color
image_mode = "1"
bg_color = "#fff"
fg_color = "#000"

mm_per_inch = 25.4
inches_per_mm = 1 / mm_per_inch

font_path = "fonts/static/OpenSans-Medium.ttf"
# font_path = "fonts/Exo2-VariableFont_wght.ttf"

# Brother PT-P710BT has a standard resolution of 180 dpi,
# and a high resolution of 180x360 dpi.
dpi = (180, 180)

# Tape width: 12 mm
tape_width = 12

# Label size
height = tape_width
width = 50

# Label size in pixels
height_px = math.ceil(height * dpi[0] * inches_per_mm)
width_px = math.ceil(width * dpi[1] * inches_per_mm)

# Base font size (pixels)
base_font_size = math.ceil(height_px / 2 * 0.95)

img = Image.new(image_mode, (width_px, height_px), color=bg_color)

rows = (
    {"font_size": base_font_size, "text": ["Resistors"]},
    {
        "font_size": math.ceil(base_font_size * 0.8),
        "text": ["1", "1k", "1M"],
    },
)

canvas = ImageDraw.Draw(img)

yf = height_px / len(rows)
for ri, row in enumerate(rows):
    xf = width_px / len(row["text"])
    fnt = ImageFont.truetype(font_path, row["font_size"])
    y = yf * (ri + 0.5)
    for ti, text in enumerate(row["text"]):
        x = xf * (ti + 0.5)
        canvas.text(
            xy=(x, y),
            anchor="mm",
            text=text,
            font=fnt,
            fill=fg_color,
        )

img.save("label.png")
