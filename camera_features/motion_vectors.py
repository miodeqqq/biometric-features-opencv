#!/usr/bin/env python

# -*- coding: utf-8 -*-

import cv2
import numpy as np


class MotionVectors(object):
    def __init__(self):
        self.capturing = True
        self.video = cv2.VideoCapture(0)
        self.scalling_factor = 0.5
        self.num_frames_to_track = 5
        self.num_frames_jump = 2
        self.tracking_paths = []
        self.frame_index = 0
        self.interpolation = cv2.INTER_AREA

        self.tracking_params = dict(
            winSize=(11, 11),
            maxLevel=2,
            criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
        )

    def star_motion_vectors(self):
        camera = self.video

        while self.capturing:
            ret, frame = camera.read()

            frame = cv2.resize(
                frame,
                None,
                fx=self.scalling_factor,
                fy=self.scalling_factor,
                interpolation=self.interpolation
            )

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            output_img = frame.copy()

            if len(self.tracking_paths) > 0:
                prev_img, current_img = prev_gray, frame_gray
                feature_points_0 = np.float32([tp[-1] for tp in self.tracking_paths]).reshape(-1, 1, 2)

                feature_points_1, _, _ = cv2.calcOpticalFlowPyrLK(
                    prev_img, current_img,
                    feature_points_0,
                    None,
                    **self.tracking_params
                )

                feature_points_0_rev, _, _ = cv2.calcOpticalFlowPyrLK(
                    current_img, prev_img,
                    feature_points_1, None,
                    **self.tracking_params
                )

                diff_feature_points = abs(feature_points_0 - feature_points_0_rev).reshape(-1, 2).max(-1)

                good_points = diff_feature_points < 1

                new_tracking_paths = []

                for tp, (x, y), good_points_flag in zip(
                        self.tracking_paths,
                        feature_points_1.reshape(-1, 2),
                        good_points
                ):
                    if not good_points_flag:
                        continue
                    tp.append((x, y))

                    if len(tp) > self.num_frames_to_track:
                        del tp[0]

                    new_tracking_paths.append(tp)

                    cv2.circle(output_img, (x, y), 3, (0, 255, 0), -1)

                tracking_paths = new_tracking_paths

                cv2.polylines(output_img, [np.int32(tp) for tp in tracking_paths], False, (0, 150, 0))

            if not self.frame_index % self.num_frames_jump:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255

                for x, y in [np.int32(tp[-1]) for tp in self.tracking_paths]:
                    cv2.circle(mask, (x, y), 6, 0, -1)

                feature_points = cv2.goodFeaturesToTrack(
                    frame_gray,
                    mask=mask,
                    maxCorners=500,
                    qualityLevel=0.3,
                    minDistance=7,
                    blockSize=7
                )

                if feature_points is not None:
                    for x, y in np.float32(feature_points).reshape(-1, 2):
                        self.tracking_paths.append([(x, y)])
            self.frame_index += 1

            prev_gray = frame_gray

            cv2.imshow('Motion vectors', output_img)

            # stop capturing if pressed S button
            if cv2.waitKey(10) == ord('s'):
                break

        camera.release()
        cv2.destroyAllWindows()


motion_vectors = MotionVectors()
motion_vectors.star_motion_vectors()
