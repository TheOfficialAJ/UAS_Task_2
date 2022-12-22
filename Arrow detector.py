import cv2 as cv
import numpy as np
import math

feed = cv.VideoCapture(0)


def minDistElem(coords):
    minDist = None
    mina = None
    minb = None
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i != j:
                x1, y1 = [x for x in coords[i]]
                x2, y2 = [x for x in coords[j]]
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if minDist is None:
                    minDist = dist
                    mina = i
                    minb = j
                    continue
                if dist < minDist:
                    minDist = dist
                    mina = i
                    minb = j
    return (mina, minb)


while True:
    ret, frame = feed.read()
    grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # grayscale = 255 - grayscale

    canny = cv.Canny(grayscale, 255 / 3, 255)
    # ret, thresh = cv.threshold(grayscale, 200, 255, cv.THRESH_BINARY)
    # adap_thresh = cv.adaptiveThreshold(grayscale, 255, cv.ADAPTIVE_THRESH_MEAN_C,
    #                                    cv.THRESH_BINARY, 11, 2)
    # blur = cv.GaussianBlur(grayscale, (5, 5), 0)
    # otsu_ret, otsu_thresh = cv.threshold(grayscale, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # cv.imshow("Threshold", thresh)
    # cv.imshow("Adaptive Threshold (Gaussian)", adap_thresh)
    # cv.imshow("OTSU Thresholding", otsu_thresh)
    contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cv.imshow("Canny", canny)

    grayscale = cv.cvtColor(grayscale, cv.COLOR_GRAY2BGR)
    # cv.drawContours(grayscale, contours, -1, (0, 255, 0), 1)
    if contours is not None:
        # Only considers innermost contours
        ChildContour = hierarchy[0, :, 2]
        WithoutChildContour = (ChildContour == -1).nonzero()[0]
        childlessCnts = [contours[i] for i in WithoutChildContour]
        arrow = None
        for cnt in childlessCnts:
            if cv.contourArea(cnt) > 1000:
                rect = cv.minAreaRect(cnt)

                M = cv.moments(cnt)
                # Calculates centroid
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                ratio = rect[1][0] / rect[1][1]
                print(rect[2])
                box = cv.boxPoints(rect)
                box = np.int0(box)
                print()
                grayscale = cv.circle(grayscale, (cx, cy), 5, (200, 200, 150), -1)

                # TODO Get mid point of the bottom edge of the arrow and get angle of line joining it to the centroid
                epsilon = 0.01 * cv.arcLength(cnt, True)
                approximations = cv.approxPolyDP(cnt, epsilon, True)

                # if len(approximations) == 7:
                #     # cv.drawContours(grayscale, [approximations], 0, (0, 255, 0), 2)
                #     arrow = approximations
                #     break
                cv.drawContours(grayscale, [box], 0, (0, 0, 255), 2)
    if arrow is not None:
        coords = [x for x in arrow]
        print(coords[0])

        i, j = minDistElem(coords)
        grayscale = cv.circle(grayscale, (coords[i][0], coords[i][1]), 5, (255, 0, 0), -1)
        grayscale = cv.circle(grayscale, (coords[j][0], coords[j][1]), 5, (255, 0, 0), -1)

        cv.drawContours(grayscale, [arrow], 0, 0, 3)

    cv.imshow("Grayscale", grayscale)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

feed.release()
cv.destroyAllWindows()
