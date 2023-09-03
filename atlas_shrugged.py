import cv2 
import mediapipe as mp
import numpy as np
import sounddevice as sd

mp_pose = mp.solutions.pose

def play_beep():
    frequency = 440
    duration = 0.3

    t = np.linspace(0, duration, int(duration * 44100), False)
    beep_waveform = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(beep_waveform, samplerate=44100)
    sd.wait()

def capture_landmarks(pose, image):
    image.flags.writeable = False
    result = pose.process(image)
    image.flags.writeable = True 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark
        return landmarks
    else:
        return None 

def deviation_detector(landmarks, landmarks_ideal):
    if landmarks[11].y > landmarks_ideal[11].y and landmarks[12].y > landmarks_ideal[12].y and landmarks[0].y > landmarks_ideal[0].y:
    	return True 
    else:
    	return False 


def main():

    ready = input("Are you ready ? - Yes or No: ").lower()
    
    if ready == "yes":

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            camera = cv2.VideoCapture(0)
            print("Capturing your ideal posture")

            while True:
                if not camera.isOpened():
                    raise Exception('Could not open camera')
                    continue

                ret, ideal_image = camera.read()
                if ret:
                    landmarks_ideal = capture_landmarks(pose, ideal_image)
                    
                    if not landmarks_ideal:
                        print("Trying again....")
                        continue
                    break

                if not ret:
                    raise Exception('Could not capture image')
                    continue


        camera.release()

        cap = cv2.VideoCapture(0)

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            print('Sit up straight, AtlasShrugged is watching you')

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                landmarks = capture_landmarks(pose, frame)

                if not landmarks:
                    pass

                elif deviation_detector(landmarks, landmarks_ideal):
                    play_beep()


        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
