# AtlasShrugged
AtlasShrugged is a real time posture detection application that helps users to maintain an optimal posture during prolonged desktop or laptop use. It allows users to define their ideal posture, creating a personalized reference point to detect incorrect posture in the real time input using mediapipe's pose estimation model. The user is alerted via a beep sound that persists until the posture is corrected.  

## Features
- Real-time posture analysis using webcam
- Ideal posture capture for reference
- Audible feedback (beep sound) on posture deviations
- Configurable to allow or disallow leaning

## Installation
1. Prerequisties: [Python](https://www.python.org/downloads/)
2. Clone the repo
   
   ```git clone https://github.com/japjotsaggu/AtlasShrugged.git```
   
3. 'cd' into directory
   
   ```cd AtlasShrugged```
   
4. Install the required dependencies
   
   ```pip install -r requirements.txt```
   
5. Run application
   
   ```python posture_detection.py```

   - You will be prompted to allow or disallow leaning.
   - Capture your ideal posture when prompted by the program
   - The program will analyze your real-time posture and provide feedback with beep sounds for any detected deviations.

## Contributing 
Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request
