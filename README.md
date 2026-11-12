# Football Tracker

## Introduction
This project leverages YOLO, a state-of-the-art object detection model, to detect and track players, referees, and footballs in match footage, incorporating custom training to optimize accuracy. Using K-means clustering for pixel segmentation, the system classifies players into teams based on jersey colors to calculate team ball possession percentages. To ensure precise movement tracking, optical flow is applied to compensate for camera motion across frames, while perspective transformation maps the 2D video feed into real-world dimensions. This allows the pipeline to translate pixel displacement into meters, enabling the accurate calculation of player speed and total distance covered.

![Screenshot](img/screenshot.png)

## Modules Used
The following modules are used in this project:
- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player

## Requirements
To run this project, you need to have the following requirements installed:
- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
