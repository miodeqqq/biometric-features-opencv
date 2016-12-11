#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from classifiers.classifiers import prepare_classifiers

import cv2


class EyesDetect(object):
    def __init__(self):
        self.capturing = True
        self.video = cv2.VideoCapture(0)
        self.ds_factor = 0.5
        self.interpolation = cv2.INTER_AREA
        self.classifiers = prepare_classifiers()

    def start_capture(self):
        camera = self.video

        face_classifier = self.classifiers.get('frontal_face_default', None)
        eyes_classifier = self.classifiers.get('eyes', None)

        face_cascade = cv2.CascadeClassifier(face_classifier)
        eyes_cascade = cv2.CascadeClassifier(eyes_classifier)

        while self.capturing:
            ret, frame = camera.read()

            frame = cv2.resize(
                frame, None,
                fx=self.ds_factor,
                fy=self.ds_factor,
                interpolation=cv2.INTER_AREA
            )

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.2, 3)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                eyes = eyes_cascade.detectMultiScale(roi_gray)

                for (x_eye, y_eye, w_eye, h_eye) in eyes:
                    center = (int(x_eye + 0.5 * w_eye), int(y_eye + 0.5 * h_eye))
                    radius = int(0.3 * (w_eye + h_eye))
                    color = (0, 255, 0)
                    thickness = 3
                    cv2.circle(roi_color, center, radius, color, thickness)

            cv2.imshow('Eyes detector', frame)

            # stop capturing if pressed S button
            if cv2.waitKey(10) == ord('s'):
                break
        camera.release()
        cv2.destroyAllWindows()


eyes = EyesDetect()
eyes.start_capture()
