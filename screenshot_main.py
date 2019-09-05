import sys
from lib.take_screenshots import take_screenshots

type_of_items = input("Type of items ([c]harms, [s]kins, [u]niforms, [h]eadgears): ")
number_of_items = input("Number of items: ")
verbose = False

if len(sys.argv) > 1:
  if str(sys.argv[1]) == '-v':
    verbose = True

if (type_of_items == 'charms' or type_of_items == 'c'):
  take_screenshots(int(number_of_items), 4.0, verbose)
elif (type_of_items == 'skins' or type_of_items == 's'):
  take_screenshots(int(number_of_items), 1.5, verbose)
elif (type_of_items == 'uniforms' or type_of_items == 'headgears' or type_of_items == 'u' or type_of_items == 'h'):
  take_screenshots(int(number_of_items), 2.0, verbose)
else:
  print('Missing or wrong arguments')