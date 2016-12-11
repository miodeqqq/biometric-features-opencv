#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2
import sys

from classifiers.classifiers import prepare_classifiers


class DetectFaces(object):
    def __init__(self):
        self.classifiers = prepare_classifiers()
        self.input_image = os.path.join(sys.argv[1])
        self.output_dir = 'faces_found_directory'

    def create_output_directory(self):
        """
        General method to create output directory.
        """

        try:
            if not os.path.isdir(self.output_dir):
                return os.makedirs(self.output_dir)
        except OSError as e:
            pass

    def find_faces(self):
        """
        General method to find faces in image.
        """

        self.create_output_directory()

        face_classifier = self.classifiers.get('frontal_face_default', None)
        face_cascade = cv2.CascadeClassifier(face_classifier)

        image = cv2.imread(self.input_image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        print('Found {number_of_faces} faces in \'{file_name}.\''.format(
            number_of_faces=len(faces),
            file_name=os.path.basename(self.input_image)
        ))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            output_dir = '{dir}/{file_name}'.format(
                dir=self.output_dir,
                file_name=os.path.basename(self.input_image)
            )

            cv2.imwrite(os.path.expanduser(output_dir), image)


face = DetectFaces()
face.find_faces()
