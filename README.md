# ML Projects

## Overview

This repository contains several machine learning and computer vision projects implemented using Python and OpenCV. Each project demonstrates different aspects of real-time image and video processing, including shape detection, color detection, object detection, and perspective transformation.

## Projects

### 1. Realtime Shape Detection using Contours

This project focuses on detecting various geometric shapes (like triangles, squares, circles, etc.) in real-time using contours. It leverages OpenCV's contour detection and approximation methods to identify shapes based on the number of vertices.

#### Key Features:
- Detects basic geometric shapes.
- Real-time video processing.
- Uses contour approximation to differentiate shapes.

#### Usage:
1. Run the script to start the real-time shape detection.
2. The shapes detected in the video feed will be highlighted with different colors.

### 2. Realtime Color Detection

This project captures a live video feed and isolates specific colors in real-time based on user-defined HSV (Hue, Saturation, Value) ranges. It allows users to fine-tune the color ranges using trackbars.

#### Key Features:
- Live video feed with HSV adjustments.
- Color masking and detection in real-time.
- Adjustable sliders for tuning the color detection range.

#### Usage:
1. Run the script to start the real-time color detection.
2. Use the trackbars to adjust the HSV range and observe the color detection in the video feed.

### 3. Object Detection

This project implements a real-time object detection system using OpenCV. It utilizes Haar cascades to detect and track objects in real-time via a webcam feed. The script displays bounding boxes around detected objects and provides adjustable parameters through trackbars.

#### Key Features:
- Real-time object detection using Haar cascades.
- Dynamic adjustment of detection parameters via trackbars.
- Displays bounding boxes around detected objects.
- Allows adjustment of camera brightness, detection scale, neighbors, and minimum area.

#### Usage:
1. Run the script to start the real-time object detection.
2. Use the trackbars to adjust detection parameters and view results in the video feed.

### 4. Warp Perspective / Bird's-Eye View

This project demonstrates how to perform perspective transformation on an image using OpenCV. The script allows users to select four points on an image, which are then used to warp the image into a rectangle.

#### Key Features:
- Allows interactive selection of four points on an image.
- Performs perspective transformation to warp the selected region into a rectangular form.
- Displays both the original and the warped images.

#### Usage:
1. Place the image you want to transform in the `Resources` directory.
2. Run the script to start the perspective transformation.
3. Click on four points on the image to define the region to be transformed.
4. The transformed image will be displayed in a new window.

## Requirements

To run these projects, ensure you have the following installed:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)

