from PIL import Image

input_path = r"C:/assets/quickerqr_logo_raw.png"
output_path = "outputs/quickerqr_logo_500.png"

img = Image.open(input_path)
img = img.resize((500, 500), Image.LANCZOS)
img.save(output_path)

print("Done.")