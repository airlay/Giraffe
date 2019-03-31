from os import listdir
from PIL import Image

source = 'C:\\Users\\airlay\\Pictures\\ShermyOldHardrive\\Shermy Cell Samsumg\\up to 8-27-16'
i: int = 0
for filename in listdir(source):
    if filename.endswith('.jpg'):
        try:
            img = Image.open('./'+filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)
        # print out the names of corrupt files
    i += 1

print("total file: " + str(i))
