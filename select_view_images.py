from PIL import Image
import os

from shared.files.util import get_data_dir

img_dir  = get_data_dir("quality", "reference_auto")
view = "AP4CH"
new_img_dir = f"/code_projects/labelme-with-segment-anything/{view}"
os.makedirs(new_img_dir, exist_ok=True)
j = 0
for i, filename in enumerate(sorted(os.listdir(img_dir))):
    if (filename.endswith(".png") or filename.endswith(".jpg")) and view in filename:

        png_image = Image.open(os.path.join(img_dir, filename))
        rgb_image = png_image.convert("L")
        j += 1
        new_filename = f"{j:05d}.jpg"

        # Save the image in JPG format
        rgb_image.save(os.path.join(new_img_dir, new_filename), "JPEG")
