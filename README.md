# face_classification
Real-time face detection and emotion/gender classification using fer2013/imdb
datasets with a keras CNN model and openCV.

[Original source](https://github.com/oarriaga/face_classification)

The difference between the original code and this is, the web application
accepts images in different ways (Multipart, Base64 in JSON, Base64 in raw HTTP
body) and returns an array of object instead of image binary data.
