import os

images_input_path = os.path.join(os.getcwd(), '..', 'input')

def scan_and_blur(path):
  instances = os.listdir(path)

  for instance in instances:
    instance_path = os.path.join(path, instance)

    if (os.path.isfile(instance_path)):
      print('plik')
    
    elif (os.path.isdir(instance_path)):
      print('folder')
      scan_and_blur(instance_path)

scan_and_blur(images_input_path)