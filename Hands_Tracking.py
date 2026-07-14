import cv2
import pyautogui as auto
import mediapipe as mp
import time
import Suporting_Functions as sf


# ----------------------------------------------------------------------------------------------------------

class Hand_Detection():

    def __init__(self, mode=False, maxHands=2, detection_con=0.7, track_con=0.7):
        self.mode = mode
        self.maxHands = maxHands
        self.detection_con = detection_con
        self.track_con = track_con
    

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detection_con,
                                        min_tracking_confidence=self.track_con)
        self.mpDraw = mp.solutions.drawing_utils
        

    def Find_Hands(self, img, results, draw=True):

        if results.multi_hand_landmarks:
            for hand_lm in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, hand_lm, self.mpHands.HAND_CONNECTIONS)

        return img

    def Find_Hand_Coordinates_For_Mouse(self, results,  draw=True):

        land_marks_list = []

        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]

            for land_mark in myHand.landmark:
                land_marks_list.append((land_mark.x, land_mark.y))

        return land_marks_list
    

    def Find_Hand_Coordinates_For_Keyboard(self, img, results,  draw=True):
         
        right_hand_list = []
        left_hand_list = []
            
        if results.multi_hand_landmarks:
           for hand_lm, my_hand in zip(results.multi_hand_landmarks, results.multi_handedness):

              hand_label = my_hand.classification[0].label
               
              current_hand_landmarks = []
            
              for land_mark in hand_lm.landmark:
                 
               current_hand_landmarks.append((land_mark.x, land_mark.y))
              
               if hand_label == "Right":
                 right_hand_list = current_hand_landmarks
               elif hand_label == "Left":
                 left_hand_list = current_hand_landmarks
        
        return right_hand_list, left_hand_list
              
                                         
