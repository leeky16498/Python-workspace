# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
import math
import fastdtw as dtw
from scipy.spatial.distance import euclidean

def video_to_images(file_in, folder_out):
    cap = cv2.VideoCapture(file_in)
    while not cap.isOpened():
        cap = cv2.VideoCapture("./out.mp4")
        cv2.waitKey(1000)
        print("Wait for the header")

    pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    while True:
        flag, frame = cap.read()
        if flag:
            # The frame is ready and already captured
            cv2.imshow('video', frame)
            cv2.imwrite(folder_out + '{:04d}.png'.format(int(pos_frame)), frame)
            pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            print(str(pos_frame)+" frames")
        else:
            # The next frame is not ready, so we try to read it again
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
            print("frame is not ready")
            # It is better to wait for a while for the next frame to be ready
            cv2.waitKey(1000)

        if cv2.waitKey(10) == 27:
            break
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            break
            
def find_contour_center(contour):
    kpCnt = len(contour)

    x = 0
    y = 0

    for kp in contour:
        x = x+kp[0][0]
        y = y+kp[0][1]
        
    x2 = x/kpCnt
    y2 = y/kpCnt
    x = math.ceil(x/kpCnt)
    y = math.ceil(y/kpCnt)
    return (x, y), (x2,y2)
    
def find_fan_center(image, color_image, offset=(0,0)):
    ret, thresh = cv2.threshold(image, 40, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea)  
    cnt = cnts[-1]

    
    image_with_contour=np.zeros_like(image)
    dist=np.zeros((image.shape[0],image.shape[1]))
    cv2.drawContours(image_with_contour,[cnt],0,255,-1)
    for ind_y in range(int(image.shape[0]/2-50),int(image.shape[0]/2+50)):
        for ind_x in range(int(image.shape[1]/2-50),int(image.shape[1]/2+50)):
            dist[ind_y,ind_x] = cv2.pointPolygonTest(cnt,(ind_x,ind_y),True)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
    # cv2.circle(color_image,maxLoc,int(maxVal),(0, 255, 0),1)

    # cv2.imshow('original', color_image)
    # cv2.imshow('thresh',image_with_contour)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return maxLoc
    
    

def find_black_spot(image, offset=(0,0)):
    #im = cv2.imread('test.jpg')
    #imgray = cv2.cvtColor(im, cv.COLOR_BGR2GRAY)
    #image[190:320,190:320]=255
    masked = np.zeros_like(image)
    cv2.circle(masked, (250,250),210, 255, -1)
    cv2.circle(image,(255,255), 110, 255, -1)
    image = 255-image
    a = cv2.bitwise_and(masked, image)
    ret, thresh = cv2.threshold(a, 80, 255, 0)
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key=cv2.contourArea)
    masked2 = np.zeros_like(image)
    cnt = cnts[-7]
    cv2.drawContours(masked2, [cnt], -1, 255, -1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image, mask=masked2)
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, offset=offset)
    cnts = sorted(contours, key=cv2.contourArea)
    
    max_loc, max_loc_acc = find_contour_center(cnts[-7])
    
    #max_loc = np.reshape(np.array(max_loc),(-1,1,2))
    #max_loc = (max_loc[0]+offset[0],max_loc[1]+offset[1])
    return cnts[-7], max_loc, max_loc_acc

def hypnotic_fan(image):
    image = image[0:1080,0:1080,:]
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    center_pos = find_fan_center(imgray,image)
    cnt, max_loc, max_loc_acc = find_black_spot(imgray[320:820,320:820], offset=(320,320))
#    ret, thresh = cv.threshold(imgray, 127, 255, 0)
#    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return cnt, max_loc, center_pos, max_loc_acc

def hypnotic_fan_all():
    folder = 'hypnoticfan/'
    
    with open('hypnoticfan_acc.txt', 'wt') as f:
        for filename in sorted(os.listdir(folder)):
            if '.png' in filename:
                img = cv2.imread(folder + '/' + filename)
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
                lower_red = np.array([110,50,50]) 
                upper_red = np.array([130,255,255]) 
                lower_red = np.array([60,10,0]) 
                upper_red = np.array([160,255,255]) 
                mask = cv2.inRange(hsv, lower_red, upper_red) 
                res = cv2.bitwise_and(img,img, mask= mask) 
#                cv2.imshow('blue',res)
#                cv2.waitKey()
                cnt, max_loc, center_pos, max_loc_acc = hypnotic_fan(img)
                cv2.drawContours(img, [cnt], 0, (0,255,0), 1)
                cv2.drawContours(img, [max_loc], 0, (0,255,255), 1)
                cv2.circle(img, max_loc,1, (0,0,255), -1)
                cv2.circle(img, center_pos,1, (255,0,0), -1)
                show_scale = 0.5
                cv2.imshow('fan',cv2.resize(img, (0,0), fx=show_scale, fy=show_scale))
                cv2.waitKey()
                #f.write('{} {} {} {} {}\n'.format(filename, max_loc_acc[0], max_loc_acc[1], center_pos[0], center_pos[1]))
            
            
def find_white_spot(imgray):
    imgray = imgray[1048:1060,718:730]
    ret, thresh = cv2.threshold(imgray, 200, 255, 0)
    offset = (1048,718)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, offset=offset)
    cnts = sorted(contours, key=cv2.contourArea)
    M = cv2.moments(cnts[-1])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    max_loc, max_loc_acc = find_contour_center(cnts[-1])
    #cv2.imshow('crop',thresh)
    #cv2.waitKey()
    max_coord = 0
    return (cX, cY), max_loc_acc
            
            
def find_two_lines(image):
    #ret, thresh = cv2.threshold(255-image, 80, 255, 0)
    #ret,thresh = cv2.threshold(255-image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thresh = cv2.adaptiveThreshold(255-image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    #cv2.imshow('thr',thresh)
    #cv2.waitKey()
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    cnts = sorted(contours, key=cv2.contourArea)
    cnt1 = cnts[-4]
    cnt2 = cnts[-3]
    if cnt1[0,0,0] < cnt2[0,0,0]:
        return cnt1, cnt2
    else:
        return cnt2, cnt1
    
            
def shake_the_snake(image):
    image_or = image
    image_or = cv2.cvtColor(image_or, cv2.COLOR_BGR2GRAY)
    image = image[90:890,640:1190]
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #imgray = imgray[90:890,640:1190]
    left, right = find_two_lines(imgray)
    coord, max_coord = find_white_spot(image_or)
    #cv2.drawContours(image, [left], 0, (0,255,0), 1)
    #cv2.drawContours(image, [right], 0, (0,0,255), 1)
    #cv2.imshow('test', image)
    #cv2.waitKey()
    #return None, None, coord, max_coord
    subpxcurve_left = estimateSubpixelCurve(255-imgray, left, debug=False)
    subpxcurve_right = estimateSubpixelCurve(255-imgray, right, debug=False)
    return subpxcurve_left, subpxcurve_right, coord, max_coord
            
def shake_the_snake_all():
    folder = 'shakethesnake/'
    out_folder = 'shakethesnake_out/'
    ind = 0
    
    #with open('shake_the_snake.txt', 'wt') as f:
    for filename in sorted(os.listdir(folder)):
        if '.png' in filename:
            if ind >=  1053:
                print(filename)
                img = cv2.imread(folder + '/' + filename)
                left, right, coord, max_coord = shake_the_snake(img)
                #f.write('{} {} {}\n'.format(filename, coord[0], coord[1]))
                #f.write('{} {} {} {} {}\n'.format(filename, coord[0], coord[1], max_coord[0], max_coord[1]))
                #continue
                np.savetxt(out_folder + filename[:-4]+'_left.txt',left,fmt='%f',delimiter=' ')
                np.savetxt(out_folder + filename[:-4]+'_right.txt',right,fmt='%f',delimiter=' ')
            ind = ind+1
    




def createLineIterator(P1, P2, img):
    """
    taken from :https://stackoverflow.com/questions/32328179/opencv-3-0-python-lineiterator

    Produces and array that consists of the coordinates and intensities of each pixel in a line between two points

    Parameters:
        -P1: a numpy array that consists of the coordinate of the first point (x,y)
        -P2: a numpy array that consists of the coordinate of the second point (x,y)
        -img: the image being processed

    Returns:
        -it: a numpy array that consists of the coordinates and intensities of each pixel in the radii (shape: [numPixels, 3], row = [x,y,intensity])
    """
    # define local variables for readability
    imageH = img.shape[0]
    imageW = img.shape[1]
    P1X = P1[0]
    P1Y = P1[1]
    P2X = P2[0]
    P2Y = P2[1]

    # difference and absolute difference between points
    # used to calculate slope and relative location between points
    dX = P2X - P1X
    dY = P2Y - P1Y
    dXa = np.abs(dX)
    dYa = np.abs(dY)

    # predefine numpy array for output based on distance between points
    itbuffer = np.empty(shape=(np.maximum(dYa, dXa), 3), dtype=np.float32)
    itbuffer.fill(np.nan)

    # Obtain coordinates along the line using a form of Bresenham's algorithm
    negY = P1Y > P2Y
    negX = P1X > P2X
    if P1X == P2X:  # vertical line segment
        itbuffer[:, 0] = P1X
        if negY:
            itbuffer[:, 1] = np.arange(P1Y - 1, P1Y - dYa - 1, -1)
        else:
            itbuffer[:, 1] = np.arange(P1Y + 1, P1Y + dYa + 1)
    elif P1Y == P2Y:  # horizontal line segment
        itbuffer[:, 1] = P1Y
        if negX:
            itbuffer[:, 0] = np.arange(P1X - 1, P1X - dXa - 1, -1)
        else:
            itbuffer[:, 0] = np.arange(P1X + 1, P1X + dXa + 1)
    else:  # diagonal line segment
        steepSlope = dYa > dXa
        if steepSlope:
            slope = dX.astype(np.float32) / dY.astype(np.float32)
            if negY:
                itbuffer[:, 1] = np.arange(P1Y - 1, P1Y - dYa - 1, -1)
            else:
                itbuffer[:, 1] = np.arange(P1Y + 1, P1Y + dYa + 1)
            itbuffer[:, 0] = (slope * (itbuffer[:, 1] - P1Y)).astype(np.int) + P1X
        else:
            slope = dY.astype(np.float32) / dX.astype(np.float32)
            if negX:
                itbuffer[:, 0] = np.arange(P1X - 1, P1X - dXa - 1, -1)
            else:
                itbuffer[:, 0] = np.arange(P1X + 1, P1X + dXa + 1)
            itbuffer[:, 1] = (slope * (itbuffer[:, 0] - P1X)).astype(np.int) + P1Y

    # Remove points outside of image
    colX = itbuffer[:, 0]
    colY = itbuffer[:, 1]
    itbuffer = itbuffer[(colX >= 0) & (colY >= 0) & (colX < imageW) & (colY < imageH)]

    # Get intensities from img ndarray
    itbuffer[:, 2] = img[itbuffer[:, 1].astype(np.uint), itbuffer[:, 0].astype(np.uint)]

    return itbuffer


def interpolate2Dpoints(data, point):
    xsubpx = np.interp(point, list(range(len(data))), data[:, 0])
    ysubpx = np.interp(point, list(range(len(data))), data[:, 1])
    return xsubpx, ysubpx


def extremePoints(contour):
    extLeft = tuple(contour[contour[:, :, 0].argmin()][0])
    extRight = tuple(contour[contour[:, :, 0].argmax()][0])
    extTop = tuple(contour[contour[:, :, 1].argmin()][0])
    extBot = tuple(contour[contour[:, :, 1].argmax()][0])
    return extLeft, extRight, extTop, extBot


def endPoints(image, contour, points=2):
    feats = cv2.goodFeaturesToTrack(image, points, 0.1, len(contour) / 4)
    feats = tuple(feats[0].ravel().astype('uint16')), tuple(feats[1].ravel().astype('uint16'))
    return [closestPointToContour(f, contour) for f in feats]


def splitContour(contour, points):
    c = contour.reshape((contour.shape[0], contour.shape[-1]))
    firstidx = [idx for idx, t in enumerate(c) if t[0] == points[0][0] and t[1] == points[0][1]]
    endidx = [idx for idx, t in enumerate(c) if t[0] == points[1][0] and t[1] == points[1][1]]
    upperside = c[firstidx[0]:endidx[-1]]
    lowerside = np.flipud(np.vstack((c[endidx[-1]:], c[:firstidx[0]])))

    return upperside, lowerside


def showCorners(img, corners):
    for c in corners:
        x, y = c.ravel()
        cv2.circle(img, (x, y), 4, 255, -1)


def closestPointToContour(point, contour):
    dists = [euclidean(point, c) for c in contour]
    return contour[np.argmin(dists)].ravel()


def estimateSubpixelCurve(image, contours, debug=False):
    a = np.zeros_like(image)
    a = cv2.drawContours(a, [contours], 0, 255, -1)
    image = cv2.bitwise_and(a,image)
    b = np.zeros((image.shape[0]+10,image.shape[1]),dtype=np.uint8)
    b[:-10,:] = image
    image = b
    a = np.zeros_like(image)
    a = cv2.drawContours(a, [contours], 0, 255, 1)
    np.savetxt('tmp.txt',np.reshape(contours,(-1,2)),fmt='%f',delimiter=' ')

    # punten op contour die het meest hoekachtig zijn
    #startpoint, endpoint = endPoints(image, contours, 2)
    # startpoint, endpoint = endPoints(a, contours, 2)
    mx = np.argmax(contours, axis=0)
    mn = np.argmin(contours, axis=0)
    endpoint = contours[-1][0]
    startpoint = contours[mx[0,1]][0]
    # upper and lowerside of contour between both points
    oneside, otherside = splitContour(contours, (startpoint, endpoint))

    # couple points from both sides of the contour
    distance, couples = dtw.dtw(oneside, otherside, dist=euclidean)

    if debug:
        imagecol = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    subpxcurve = []
    for i, cp in enumerate(couples):
        # itrator to go from one point to the next; returns array of [x,y, intensities]
        lprof = createLineIterator(oneside[cp[0]], otherside[cp[1]], image)
        index = list(range(len(lprof[:, 2])))
        # zwaartepunt
        gmean = np.sum(lprof[:, 2] * index) / np.sum(lprof[:, 2])
        # find exact coordinate of geometric center (piecewise linear interpolation)
        if len(lprof)==0:
            beamcen = (float(oneside[cp[0]][0]),float(oneside[cp[0]][1]))
        else:
            beamcen = interpolate2Dpoints(lprof, gmean)
        subpxcurve.append(beamcen)
        if debug:
    #        print(gmean, beamcen)
            cv2.circle(imagecol, tuple(oneside[cp[0]]), 4, (150, 50, 150), -1)
            cv2.circle(imagecol, tuple(otherside[cp[1]]), 4, (50, 255, 50), -1)
            cv2.circle(imagecol, tuple(np.round(beamcen).astype('int')), 1, (255, 255, 255), -1)
            # show the output image
            cv2.imshow("Image", imagecol)
            cv2.waitKey(50)
    cv2.destroyAllWindows()
    return subpxcurve





        
    
#video_to_images('hypnoticfan.mp4','hypnoticfan/')
#video_to_images('shakethesnake.mp4', 'shakethesnake/')
hypnotic_fan_all()
#shake_the_snake_all()

        
