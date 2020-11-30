import mediapipe as mp
import cv2
from scipy.spatial.distance import euclidean as dist



def gestureImg(img_path):
    mp_hands = mp.solutions.hands 
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    mp_hands = mp.solutions.hands 
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
       # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
   
       # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            fingers = [0,0,0,0,0]
            marks = hand_landmarks.landmark
            key = dict()
            for i in range(21):
                key[i] = [marks[i].x, marks[i].y]
            

            if dist(key[17], key[3]) < dist(key[17], key[4]):
                fingers[0] = 1
            if dist(key[0], key[6]) < dist(key[0], key[8]):
                fingers[1] = 1
            if dist(key[0], key[10]) < dist(key[0], key[12]):
                fingers[2] = 1
            if dist(key[0], key[14]) < dist(key[0], key[16]):
                fingers[3] = 1
            if dist(key[0], key[18]) < dist(key[0], key[20]):
                fingers[4] = 1
            
            if fingers == [0, 1, 0, 0, 1]:
                result = "peace"
            elif fingers[2:] == [1, 1, 1] and dist(key[4], key[8]) < dist(key[4], key[3]):
                result = "OK"
            elif fingers == [1, 1, 0, 0, 0]:
                result = "V"
            else:
                result = sum(fingers)            
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.namedWindow("preview")
            cv2.imshow("preview", image)
    hands.close()
    return result




def gestureVid(vid_path):
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(vid_path)
        
    while True:
        success, image = cap.read()
        if not success:
            print('here')
            break
       
           # Flip the image horizontally for a later selfie-view display, and convert
           # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
           # To improve performance, optionally mark the image as not writeable to
          # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)
       
           # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                fingers = [0 for _ in range(5)]
                marks = hand_landmarks.landmark
                key = dict()
                for i in range(21):
                    key[i] = [marks[i].x, marks[i].y]
                
    
                if dist(key[17], key[3]) < dist(key[17], key[4]):
                    fingers[0] = 1
                if dist(key[0], key[6]) < dist(key[0], key[8]):
                    fingers[1] = 1
                if dist(key[0], key[10]) < dist(key[0], key[12]):
                    fingers[2] = 1
                if dist(key[0], key[14]) < dist(key[0], key[16]):
                    fingers[3] = 1
                if dist(key[0], key[18]) < dist(key[0], key[20]):
                    fingers[4] = 1
                
                if fingers == [1, 1, 0, 0, 1]:
                    result = "peace"
                elif fingers[2:] == [1, 1, 1] and dist(key[4], key[8]) < dist(key[4], key[3]):
                    result = "OK"
                elif fingers == [0, 1, 1, 0, 0]:
                    result = "V"
                else:
                    result = sum(fingers)
                
            
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                print(result)

            cv2.imshow("preview", image)
            cv2.waitKey(0)
            if cv2.waitKey(25)  & 0xFF == ord('q'):
                break
    

    cv2.destroyAllWindows()
    return fingers
                

    hands.close()
    cap.release()
if __name__ == "__main__":
    vid_path = './handGesture3.mp4'
    gestureVid(vid_path)