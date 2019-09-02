import os
import time
from lib.blur_image import blur_image

def scan_and_blur(path):
  instances = os.listdir(path)

  # Check if output directory exists. Create if not
  if (not os.path.isdir(path.replace('input', 'output'))):
    os.mkdir(path.replace('input', 'output'))

  for index, instance in enumerate(instances, start = 1):
    instance_path = os.path.join(path, instance)

    if (os.path.isfile(instance_path)):
      image_input = instance_path
      image_output = instance_path.replace('input', 'output')
      blur_image(image_input, image_output)
      print(instance, 'done', '|||', len(instances) - index, 'left')
    
    elif (os.path.isdir(instance_path)):
      print(instance_path)
      scan_and_blur(instance_path)

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
  # Get all list of all images in /input directory
  dir_instances = os.listdir(images_input_path)

  if (len(dir_instances) == 0):
    print('No images found. Please put them into /input directory and run script again')

  else:
    scan_and_blur(images_input_path)

# Execution time: End
end = time.time()
print('Done in:', end - start, 'seconds')