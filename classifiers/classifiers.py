#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os


def prepare_classifiers():
    """
    General method to prepare classifiers.
    """

    classifiers_dict = {
        'eyes': os.path.join('../classifiers/haarcascades/haarcascade_eye.xml'),
        'eyes_glasses': os.path.join('../classifiers/haarcascades/haarcascade_eye_tree_eyeglasses.xml'),
        'cat_face': os.path.join('../classifiers/haarcascades/haarcascade_frontalcatface.xml'),
        'cat_face_extended': os.path.join('../classifiers/haarcascades/haarcascade_frontalcatface_extended.xml'),
        'frontal_face_alt': os.path.join('../classifiers/haarcascades/haarcascade_frontalface_alt.xml'),
        'frontal_face_alt2': os.path.join('../classifiers/haarcascades/haarcascade_frontalface_alt2.xml'),
        'frontal_face_alt_tree': os.path.join('../classifiers/haarcascades/haarcascade_frontalface_alt_tree.xml'),
        'frontal_face_default': os.path.join('../classifiers/haarcascades/haarcascade_frontalface_default.xml'),
        'fullbody': os.path.join('../classifiers/haarcascades/haarcascade_fullbody.xml'),
        'left_eye_2splits': os.path.join('../classifiers/haarcascades/haarcascade_lefteye_2splits.xml'),
        'licence_plate_rus_16stages': os.path.join('../classifiers/haarcascades/haarcascade_licence_plate_rus_16stages.xml'),
        'lowerbody': os.path.join('../classifiers/haarcascades/haarcascade_lowerbody.xml'),
        'mcs_leftear': os.path.join('../classifiers/haarcascades/haarcascade_mcs_leftear.xml'),
        'mcs_mouth': os.path.join('../classifiers/haarcascades/haarcascade_mcs_mouth.xml'),
        'mcs_rightear': os.path.join('../classifiers/haarcascades/haarcascade_mcs_rightear.xml'),
        'profileface': os.path.join('../classifiers/haarcascades/haarcascade_profileface.xml'),
        'righteye_2splits': os.path.join('../classifiers/haarcascades/haarcascade_righteye_2splits.xml'),
        'russian_plate_number': os.path.join('../classifiers/haarcascades/haarcascade_russian_plate_number.xml'),
        'smile': os.path.join('../classifiers/haarcascades/haarcascade_smile.xml'),
        'upperbody': os.path.join('../classifiers/haarcascades/haarcascade_upperbody.xml'),

    }

    return classifiers_dict
