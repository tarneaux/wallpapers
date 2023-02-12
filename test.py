import os

images = os.listdir('.')

for n, image_1 in enumerate(images):
    print(int(n/len(images)*100))
    for image_2 in images:
        if image_1 == image_2:
            continue
        if open(image_1,"rb").read() == open(image_2,"rb").read():
            print("Found duplicate: %s and %s" % (image_1, image_2))
        

