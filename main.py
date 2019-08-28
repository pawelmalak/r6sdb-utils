import os
import time
from lib.blur_image import blur_image
from lib.take_screenshots import take_screenshots

# Execution time: Start
start = time.time()

# Directories paths
images_input_path = os.path.join(os.getcwd(), 'input')
images_output_path = os.path.join(os.getcwd(), 'output')

# Check if /input directory exists. Create if not
if (not os.path.isdir(images_input_path)):
  os.mkdir(images_input_path)
  print('No images found. Please put them into /input directory and run script again')

else:
  # Check if /output directory exists. Create if not
  if (not os.path.isdir(images_output_path)):
    os.mkdir(images_output_path)

  # Get all list of all images in /input directory
  images = os.listdir(images_input_path)

  if (len(images) == 0):
    print('No images found. Please put them into /input directory and run script again')

  # Blur every image
  for index, image in enumerate(images, start = 1):
    image_input = os.path.join(images_input_path, image)
    image_output = os.path.join(images_output_path, image)
    blur_image(image_input, image_output)
    print(image, 'done', '|||', len(images) - index, 'left')

# Execution time: End
end = time.time()
print('Done in:', end - start, 'seconds')