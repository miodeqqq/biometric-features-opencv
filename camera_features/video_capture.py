#!/usr/bin/env python

# -*- coding: utf-8 -*-

import cv2


class VideoCamera(object):
    def __init__(self):
        self.capturing = False
        self.video = cv2.VideoCapture(0)
        self.ds_factor = 0.5
        self.interpolation = cv2.INTER_CUBIC

    def start_capture(self):
        self.capturing = True

        camera = self.video

        while self.capturing:
            ret, frame = camera.read()

            frame = cv2.resize(
                frame, None,
                fx=self.ds_factor,
                fy=self.ds_factor,
                interpolation=cv2.INTER_AREA
            )

            cv2.imshow("Capture", frame)

            # stop capturing if pressed S button
            if cv2.waitKey(10) == ord('s'):
                break

        cv2.destroyAllWindows()


camera = VideoCamera()
camera.start_capture()
