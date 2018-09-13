#encoding:UTF-8

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import ocrorot

rot = ocrorot.RotationEstimator("rot-000003456-020897.pt")


#path = "data/en/down/"
#imgs = [i for i in os.listdir(path)]

#ret = []
#for i in os.listdir(path):
    #if '.jpg' not in i:
        #continue
    #image = cv2.imread(path+i)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = image / 255.0
    #middle = (np.max(image) + np.min(image)) / 2.0
    #image[image > middle] = 1
    #image[image <= middle] = 0
    #if np.sum(image[0]) + np.sum(image[-1]) >= image.shape[1]:
        #image = 1 - image
    #print(i)
    #result = rot.rotation(image)
    #print(result)
    #ret.append(result)

#cnt = 0
#for i in ret:
    #if i < 90 or i > 270:
        #cnt += 1

#print('down precision is %.2f'%(float(cnt)/len(ret)))

path = "data/en/up/"
imgs = [i for i in os.listdir(path)]

ret = []
for i in os.listdir(path):
    if '.jpg' not in i:
        continue
    image = cv2.imread(path+i)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image / 255.0
    middle = (np.max(image) + np.min(image)) / 2.0
    image[image > middle] = 1
    image[image <= middle] = 0
    if np.sum(image[0]) + np.sum(image[-1]) >= image.shape[1]:
        image = 1 - image
    print(i)
    result = rot.rotation(image)
    print(result)
    if result != 180:
        plt.imshow(image)
        plt.show()
    ret.append(result)

cnt = 0
for i in ret:
    if i > 90 and i < 270:
        cnt += 1

print('down precision is %.2f'%(float(cnt)/len(ret)))