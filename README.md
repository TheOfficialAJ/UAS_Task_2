# UAS_Task_2
This is the project repository for the UAS Task 2 project, it contains two python files: `Image Mosaicing.py` which contains the main task and `Arrow Detector.py` which contains the secondary task.

## Image Mosaicing
The Image Mosaicing task takes as input multiple overlapping images and then stitches them together into a large image similar to how a phone takes panorama images. It works using the stitcher class of OpenCV.

### Using the Image Mosaicing Program
1. Download the source code and add the images you want to stitch together in the imgs folder.
2. Run the `Image Mosaicing.py` script and enter the names of the images with their extensions (E.g: pic1.jpg) separated by commas.
3. After a few seconds the program will open a new window containing the stiched image named Output or will throw an error if unable to stitch the images together.


## Arrow Detector
The arrow detector program takes the input feed from a laptop's webcam and detects if there are any arrows present in the feed, if there are arrows, it draws a bounding box around them and also highlights them in green. It uses Canny edge detection to find the edges of the arrow and only consider seven-sided contours to filter out other shapes.

### Using the Arrow Detector Program
1. Run `Arrow Detector.py`
2. Bring any photo or hand-drawn arrow in front of the webcam and hold it there.
