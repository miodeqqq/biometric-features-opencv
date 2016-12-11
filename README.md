Biometric Features with OpenCV
=========================================

Current stable version: v1.0
Release date: 11.12.2016

### Author:

* Maciej Januszewski (maciek@mjanuszewski.pl)


### Requirements:
* Python 2.7;
* OpenCV;

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