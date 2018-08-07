# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:29:13 2018

@author: MathanP
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import cv2

img=mpimg.imread("3.jpg")
A=img/255
ish=A.shape
X=np.reshape(A,(ish[0]*ish[1],ish[2]))

centroids=np.array([0,1,0])
errlist=np.zeros((X.shape[0],1),np.float64)

for p in range(0,X.shape[0],1):
    mat=X[p,:]
    mat3=mat-centroids
    err=np.sum(np.multiply(mat3,mat3))
    errlist[p]=err

threshold=0.7
errlist=np.greater(errlist,threshold)
X=np.multiply(X,errlist)
X_out=np.reshape(X,(ish[0],ish[1],ish[2]))

'''
plt.subplot(1,2,1),plt.imshow(X_out)
plt.subplot(1,2,2),plt.imshow(mpimg.imread('2.jpg'))
'''

X_out=np.uint8(X_out*255)

img2=cv2.cvtColor(X_out,cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(img2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# You need to choose 4 or 8 for connectivity type
connectivity = 4  
# Perform the operation
output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)
# Get the results
# The first cell is the number of labels
num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The fourth cell is the centroid matrix
centroids = output[3]

list_new=[]
for i in range(0,num_labels,1):
    list1=np.equal(labels,i)
    if (np.sum(np.sum(list1))>800):
        list_new.append(i)

'''
plt.subplot(1,2,1),plt.imshow(X_out)
plt.subplot(1,2,2),plt.imshow(mpimg.imread('2.jpg'))
'''
n=len(list_new)
shape=np.shape(img2)
for j in range(1,n,1):
    filter1=np.zeros((shape[0],shape[1],3),np.float64)
    filter1[:,:,0]=np.equal(labels,list_new[j])
    filter1[:,:,1]=np.equal(labels,list_new[j])
    filter1[:,:,2]=np.equal(labels,list_new[j])
    plt.figure(j)
    plt.imshow(np.multiply(X_out/255,filter1))
