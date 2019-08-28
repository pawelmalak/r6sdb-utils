from lib.take_screenshots import take_screenshots

type_of_items = input("Type of items (charms, skins, uniforms, headgears): ")
number_of_items = input("Number of items: ")

if (type_of_items == 'charms'):
  take_screenshots(int(number_of_items), 4.0)
elif (type_of_items == 'skins'):
  take_screenshots(int(number_of_items), 1.25)
elif (type_of_items == 'uniforms' or type_of_items == 'headgears'):
  take_screenshots(int(number_of_items), 2.0)
else:
  print('Missing or wrong arguments')