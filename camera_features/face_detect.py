#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2

from classifiers.classifiers import prepare_classifiers


class FaceDetect(object):
    def __init__(self):
        self.capturing = True
        self.video = cv2.VideoCapture(0)
        self.ds_factor = 0.5
        self.interpolation = cv2.INTER_AREA
        self.classifiers = prepare_classifiers()

    def start_capture(self):
        camera = self.video

        face_classifier = self.classifiers.get('frontal_face_default', None)

        face_cascade = cv2.CascadeClassifier(face_classifier)

        while self.capturing:
            ret, frame = camera.read()

            frame = cv2.resize(
                frame,
                None,
                fx=self.ds_factor,
                fy=self.ds_factor,
                interpolation=self.interpolation
            )

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('Face detector', frame)

            # stop capturing if pressed S button
            if cv2.waitKey(10) == ord('s'):
                break
        camera.release()
        cv2.destroyAllWindows()


face = FaceDetect()
face.start_capture()
