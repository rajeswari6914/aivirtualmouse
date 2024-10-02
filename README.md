# AI Virtual Mouse Project

This project implements an AI-based virtual mouse using computer vision techniques. It allows users to control their computer mouse using hand gestures captured through a webcam. The project leverages machine learning for real-time hand tracking and gesture recognition to simulate mouse movements and actions.

## Project Overview

The AI Virtual Mouse uses computer vision and hand tracking to move the cursor, click, and perform other mouse functions without the need for a physical mouse. This project is an implementation of human-computer interaction using Python, OpenCV, and Mediapipe.

## Features

- **Hand Tracking**: Tracks hand movements in real-time using a webcam.
- **Cursor Control**: Moves the computer cursor based on hand movement.
- **Mouse Click Actions**: Performs left-click actions with specific hand gestures.

## Dependencies

To run this project, you will need the following Python libraries:

- OpenCV
- Mediapipe
- Autopy
- NumPy

## File Structure
- `AiVirtualMouseProject.py`: Main Python script that runs the AI Virtual Mouse program.
- `hand_tracking_module.py`: A custom module used for hand tracking and gesture recognition.
- `README.md`: This README file describing the project.
## How to Run the Project
### 1.Clone the repository:
First, clone the repository to your local machine using the following command:
```sh
git clone <https://github.com/rajeswari6914/aivirtualmouse.git>
cd AI-Virtual-Mouse
```
### 2. Install dependencies:
To install all the required Python libraries, run:
```sh
pip install opencv-python mediapipe autopy numpy
```
### 3. Run the AI Virtual Mouse:
To run the virtual mouse, execute the following command:
```sh
python AiVirtualMouseProject.py
```
### 4. Use the application:
- Hand Positioning: Hold your hand up in front of the webcam.
- Cursor Control: Move your hand to move the cursor on the screen.
- Click Action: Use specific hand gestures (e.g., bringing the thumb and index finger together) to perform a mouse click.
## Hand Tracking Module
The `hand_tracking_module.py` is a utility module that uses Mediapipe to track hands in real-time. It provides methods to detect and track landmarks and recognize gestures for controlling the mouse.
