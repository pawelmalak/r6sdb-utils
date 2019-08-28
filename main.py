import os
from lib.blur_image import blur_image
from lib.take_screenshots import take_screenshots

images_source_path = os.path.join(os.getcwd(), 'input')
images_output_path = os.path.join(os.getcwd(), 'output')

# Check if /images directory exists. Create if not
if (not os.path.isdir(images_source_path)):
  os.mkdir(images_source_path)
  print('No images found. Please put them into /input directory and run script again')
else:
  if (not os.path.isdir(images_output_path)):
    os.mkdir(images_output_path)
  images = os.listdir(images_source_path)
  for image in images:
    blur_image(images_source_path, image)