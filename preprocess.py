import glob
import os

path = "processed_data/"
images = glob.glob("*/*/*")
print(len(images))
counter = 1
for image in images:
  try:
    im = Image.open(image).convert("RGB")
    image_array = os.path.split(image)
    imResize = im.resize((300, 300), Image.ANTIALIAS)
    imResize.save(path + image_array[1], "JPEG", quality = 100)
    print("{}/{} resizing completed".format(counter, len(images)))
    counter = counter + 1
  except:
    print("error saving {} file".format(image))
