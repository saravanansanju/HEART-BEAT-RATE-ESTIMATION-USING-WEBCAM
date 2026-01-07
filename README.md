# Heart Beat Rate Estimation Using Webcam

This project estimates a human heart beat rate (BPM) in real time using a webcam by analyzing facial color changes caused by blood flow (remote photoplethysmography).

## Features
- Real-time heart beat rate estimation
- No external sensors required
- Uses webcam input
- Face detection using Haar Cascade
- Signal processing for BPM calculation

## Technologies Used
- Python
- OpenCV
- NumPy
- SciPy
- Haar Cascade Classifier

## Project Structure
 webcam-pulse-detector/
│── get_pulse.py
│── level.py
│── confgtest.py
│── haarcascade_frontalface_alt.xml
│── tests/
│── lib/
│── README.md
## How to Run the Project

1. Clone the repository:
   git clone https://github.com/saravanansanju/HEART-BEAT-RATE-ESTIMATION-USING-WEBCAM.git
2. Navigate to the project directory:
   cd HEART-BEAT-RATE-ESTIMATION-USING-WEBCAM
3. Install the required libraries:
   pip install opencv-python numpy scipy
4. Run the program:
   python get_pulse.py

## Working Principle
- The webcam captures facial video.
- Face is detected using Haar Cascade classifier.
- Small changes in skin color are analyzed.
- Heart beat rate (BPM) is calculated and displayed.

## Applications
- Health monitoring systems
- Academic and research projects
- Computer vision learning
- Non-contact heart rate measurement

## Disclaimer
This project is for educational purposes only and should not be used for medical diagnosis.

## Author
Saravanan Sanju
