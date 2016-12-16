#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
from datetime import datetime

import cv2


class VideoCamera(object):
    def __init__(self):
        self.capturing = False
        self.video = cv2.VideoCapture(0)
        self.ds_factor = 0.5
        self.interpolation = cv2.INTER_CUBIC
        self.photo_counter = 0
        self.output_dir = u'camera_images/{current_date}'.format(current_date=str(datetime.now().replace(microsecond=0)))

    def create_output_directory(self):
        """
        General method to create output directory.
        """

        try:
            if not os.path.isdir(self.output_dir):
                return os.makedirs(self.output_dir)
        except OSError as e:
            pass

    def start_capture(self):
        self.create_output_directory()
        self.capturing = True

        camera = self.video

        counter = self.photo_counter

        while self.capturing:
            ret, frame = camera.read()

            frame = cv2.resize(
                frame, None,
                fx=self.ds_factor,
                fy=self.ds_factor,
                interpolation=cv2.INTER_AREA
            )

            cv2.imshow("Basic Video Capture", frame)

            # stop capturing if pressed S button
            if cv2.waitKey(10) == ord('s'):
                break

            # make a photo if pressed P button
            elif cv2.waitKey(1) == ord('p'):
                photo_name = u'photo_{counter_value}.png'.format(
                    counter_value=counter
                )

                output_dir = u'{dir}/{photo_name}'.format(
                    dir=self.output_dir,
                    photo_name=photo_name,
                )

                cv2.imwrite(os.path.expanduser(output_dir), frame)

                print(u'{photo_name} has been written!'.format(
                    photo_name=photo_name
                ))

                counter += 1

        camera.release()
        cv2.destroyAllWindows()

camera = VideoCamera()
camera.start_capture()
