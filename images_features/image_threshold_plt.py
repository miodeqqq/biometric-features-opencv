#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys

import cv2
from matplotlib import pyplot as plt


class ImageThreshold(object):
    def __init__(self):
        self.sample_image = os.path.join(sys.argv[1])
        self.titles = []
        self.images = []

    def threshold_image(self):

        img = cv2.imread(self.sample_image, 0)
        ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
        ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

        titles = [
            'Original Image',
            'BINARY',
            'BINARY_INV',
            'TRUNC',
            'TOZERO',
            'TOZERO_INV'
        ]

        images = [
            img,
            thresh1,
            thresh2,
            thresh3,
            thresh4,
            thresh5
        ]

        for i in xrange(6):
            plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()

thresh = ImageThreshold()
thresh.threshold_image()