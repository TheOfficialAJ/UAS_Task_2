import cv2 as cv
import random
import numpy as np
import sys


def stitchImages(imgs):
    sticher = cv.Stitcher.create()

    random.shuffle(imgs)
    numcode, output = sticher.stitch(imgs)
    return numcode, output


def inputImages():
    files = input("Enter img names separated by commas: ")
    files = files.split(",")
    files = [f.strip() for f in files]
    img_paths = []

    for filename in files:
        img_paths.append("imgs/" + filename)

    # Inititalizing imgs from img paths
    imgs = []
    for (i, path) in enumerate(img_paths):
        imgs.append(cv.imread(path))
    return img_paths, imgs


img_paths, imgs = inputImages()
for (i, path) in enumerate(img_paths):
    cv.imshow(path, imgs[i])

# Stitches the image together
numcode, output = stitchImages(imgs)
print(numcode)
if numcode != 0:
    print("ERROR: Cannot stitch images (Insufficient overlap)")
    sys.exit()
cv.imshow("Stitched image", output)
#
# grayscale = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(grayscale, 5, 255, cv.THRESH_BINARY)
#
# # apply close and open morphology to fill tiny black and white holes
# kernel = np.ones((5, 5), np.uint8)
# thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
# thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
# cv.imshow("Mask", thresh)
#
# # get contours (presumably just one around the nonzero pixels)
# # then crop it to bounding rectangle
# contours = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# contours = contours[0] if len(contours) == 2 else contours[1]
# for cntr in contours:
#     x, y, w, h = cv.boundingRect(cntr)
#     print(x,y,w,h)
#     crop = output[y:y + h, x:x + w]
#     # show cropped image
#     cv.imshow("CROP", crop)

cv.waitKey(0)

print("test")
