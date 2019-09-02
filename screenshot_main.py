from lib.take_screenshots import take_screenshots

type_of_items = input("Type of items (charms [c], skins [s], uniforms [u], headgears [h]): ")
number_of_items = input("Number of items: ")

if (type_of_items == 'charms' or type_of_items == 'c'):
  take_screenshots(int(number_of_items), 4.0)
elif (type_of_items == 'skins' or type_of_items == 's'):
  take_screenshots(int(number_of_items), 1.25)
elif (type_of_items == 'uniforms' or type_of_items == 'headgears' or type_of_items == 'u' or type_of_items == 'h'):
  take_screenshots(int(number_of_items), 2.0)
else:
  print('Missing or wrong arguments')