import os
import sys
import time
from lib.blur_image import blur_image
from lib.create_thumbnail import create_thumbnail

type_of_process = input("[B]lur images or create [T]humbnails: ").lower()

def scan_and_process(path, mode):
  instances = os.listdir(path)

  # Check if output directory exists. Create if not
  if (not os.path.isdir(path.replace('input', 'output'))):
    os.mkdir(path.replace('input', 'output'))

  for index, instance in enumerate(instances, start = 1):
    instance_path = os.path.join(path, instance)

    if (os.path.isfile(instance_path)):
      image_input = instance_path
      image_output = instance_path.replace('input', 'output')

      if mode == 'b':
        blur_image(image_input, image_output)
      elif mode == 't':
        create_thumbnail(image_input, image_output.replace(instance, 'tb' + instance))
      
      print(instance, 'done', '|||', len(instances) - index, 'left')
    
    elif (os.path.isdir(instance_path)):
      print(instance_path)
      scan_and_process(instance_path, mode)


if type_of_process == 'b' or type_of_process == 't':
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
      scan_and_process(images_input_path, type_of_process)

  # Execution time: End
  end = time.time()
  print('Done in:', end - start, 'seconds')
  
else:
  print('Missing or wrong arguments')