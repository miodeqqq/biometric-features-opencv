Biometric Features with OpenCV
=========================================

Current stable version: v1.0

Release date: 11.12.2016

### About:

* Python scripts with usage of OpenCV found on different sites.

### Author:

* Maciej Januszewski (maciek@mjanuszewski.pl)


### Requirements:
* Python 2.7;
* OpenCV;

### Using:

* **Camera features (`camera_features package`):**

**Basic video capture:**
```
./video_capture.py
```

**Face detection:**
```
./face_detect.py
```

**Eyes detection:**
```
./eyes_detect.py
```

**Object tracker:**
```
./object_tracker.py
```

**Motion vectors:**
```
./motion_vectors.py
```

* **Images features (`images_features package`):**

**Face detection:**
```
./detect_faces.py input_image
```

**Eyes detection:**
```
./detect_eyes.py input_image
```

**Image threshold with PLT output:**
```
./image_threshold_plt.py input_image
```

### Resolving problems with missing libraries:

* **Install OpenCV:**
```
brew install opencv
```
* **You can find OpenCV at:**
```
/usr/local/Cellar/opencv/2.x.x/
```

* **Create symlinks:**
```
ln -s /usr/local/Cellar/opencv/2.x.x/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/2.x.x/lib/python2.7/site-packages/cv2.so cv2.so
```
* **If that will not work, copy these files to your env site-packages:**
```
cp /usr/local/Cellar/opencv/2.x.x/lib/python2.7/site-packages/cv2.so your_project_name/env/lib/python2.7/site-packages/
cp /usr/local/Cellar/opencv/2.x.x/lib/python2.7/site-packages/cv.py your_project_name/env/lib/python2.7/site-packages/
```