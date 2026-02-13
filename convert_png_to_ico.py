from PIL import Image

img = Image.open(r"c:/path/to/input.png")
# Convert to RGBA if it isn't already
img = img.convert('RGBA')
# Create a new square image
size = (64, 64)
img_resized = img.resize(size, Image.Resampling.LANCZOS)
img_resized.save('outputs/favicon.ico')