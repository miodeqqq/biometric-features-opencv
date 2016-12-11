#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2
import sys

from classifiers.classifiers import prepare_classifiers


class DetectEyes(object):
    def __init__(self):
        self.classifiers = prepare_classifiers()
        self.input_image = os.path.join(sys.argv[1])
        self.output_dir = 'eyes_found_directory'

    def create_output_directory(self):
        """
        General method to create output directory.
        """

        try:
            if not os.path.isdir(self.output_dir):
                return os.makedirs(self.output_dir)
        except OSError as e:
            pass

    def find_eyes(self):
        """
        General method to find eyes in image.
        """

        self.create_output_directory()

        eyes_classifier = self.classifiers.get('eyes', None)
        eyes_cascade = cv2.CascadeClassifier(eyes_classifier)

        image = cv2.imread(self.input_image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = eyes_cascade.detectMultiScale(gray, 1.2, 3)

        eyes = None

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]

            eyes = eyes_cascade.detectMultiScale(roi_gray)

            for (x_eye, y_eye, w_eye, h_eye) in eyes:
                center = (int(x_eye + 0.5 * w_eye), int(y_eye + 0.5 * h_eye))
                radius = int(0.3 * (w_eye + h_eye))
                color = (0, 255, 0)
                thickness = 3
                cv2.circle(roi_color, center, radius, color, thickness)

        print('Found {number_of_faces} eyes in \'{file_name}.\''.format(
            number_of_faces=len(eyes),
            file_name=os.path.basename(self.input_image)
        ))

        output_dir = '{dir}/{file_name}'.format(
            dir=self.output_dir,
            file_name=os.path.basename(self.input_image)
        )

        cv2.imwrite(os.path.expanduser(output_dir), image)


eyes = DetectEyes()
eyes.find_eyes()
