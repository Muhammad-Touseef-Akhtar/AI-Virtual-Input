import cv2
import mediapipe as mp
import socket
import time
import numpy as np
import pyautogui as auto
import Suporting_Functions as sf
    
#---------------------------------------------------------------------------------------------------------
  
class Keyboard_Fingers_Detection():
    
    def __init__(self):
        
       self.Current_Time = 0
       self.prev_time = 0
        
       self.net_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       self.c_plus_address = ('127.0.0.1', 5005)
       
     
    def typing_zero(self, left_hand_list):
   
      if len(left_hand_list) != 0:

        left_small_mcp_x = left_hand_list[17][0]
        left_index_tip_y, left_index_joint_y, left_middle_tip_y, left_middle_joint_y, left_ring_tip_y, left_ring_joint_y, left_small_tip_y_coord, left_small_joint_y, left_thumb_tip_x, left_thumb_joint_x = sf.getting_fingers_coordinates(left_hand_list, 1, 8,6,12,10,16,14,20,18,4,2)
 
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
          
            if (left_thumb_tip_x < left_thumb_joint_x and
                left_thumb_tip_x > left_small_mcp_x):
           
               if ((left_index_tip_y > left_index_joint_y) and
                   (left_middle_tip_y > left_middle_joint_y) and 
                   (left_ring_tip_y > left_ring_joint_y) and
                   (left_small_tip_y_coord > left_small_joint_y)):
                 
                   self.net_socket.sendto(b"NUM_0", self.c_plus_address)
                   self.prev_time = self.Current_Time


    
    def typing_one(self, right_hand_list):
        
      if len(right_hand_list) != 0:
          
        right_index_tip_y = right_hand_list[8][1]
        right_small_joint_y = right_hand_list[18][1]
        right_index_joint_y = right_hand_list[6][1]
        right_thumb_tip_x = right_hand_list[4][0]
        right_thumb_joint_x = right_hand_list[3][0] 
        
        right_index_tip_x, right_index_joint_x, right_middle_tip_x, right_middle_joint_x, right_ring_tip_x, right_ring_joint_x, right_small_tip_x, right_small_joint_x, right_thumb_tip_y, right_thumb_joint_y = sf.getting_fingers_coordinates(right_hand_list, 0, 8,7,12,11,16,15,20,19,4,2)
 
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
            
          if (right_thumb_tip_x < right_thumb_joint_x):
              
            if ((right_index_tip_y < right_index_joint_y) and
               (right_index_tip_y < right_thumb_tip_y ) and
               (right_thumb_tip_y > right_small_joint_y)):
                
               if (right_middle_tip_x > right_middle_joint_x and
                    right_ring_tip_x > right_ring_joint_x and
                    right_small_tip_x > right_small_joint_x):
                        
                        self.net_socket.sendto(b"NUM_1", self.c_plus_address)
                        self.prev_time = self.Current_Time
 
     
       
    def typing_two(self, right_hand_list):
       
        if len(right_hand_list) != 0:
         
            right_index_tip,right_index_joint,right_middle_tip,right_middle_joint,right_ring_tip,right_ring_joint,right_small_tip,right_small_joint,right_thumb_tip_x,right_thumb_mcp_x = sf.getting_fingers_coordinates(right_hand_list, 1, 8,6,12,10,16,14,20,19,4,2)
            right_index_mcp = right_hand_list[5][1]
            self.Current_Time = time.time()
            
            if self.Current_Time - self.prev_time > 0.70:
             
                if (right_thumb_tip_x > right_thumb_mcp_x):
                 
                    if ((right_index_tip < right_index_joint) and
                        (right_middle_tip < right_middle_joint)): 
                      
                        if ((right_ring_tip > right_ring_joint) and
                            (right_small_tip > right_small_joint)):
                           
                            self.net_socket.sendto(b"NUM_2", self.c_plus_address)
                            self.prev_time = self.Current_Time
                            
     
     
    def typing_three(self, left_hand_list):
    
      if len(left_hand_list) != 0:
          
        left_index_tip_x = left_hand_list[8][0]
        left_index_mcp_x = left_hand_list[5][0]
        left_thumb_tip_y = left_hand_list[4][1]
        left_thumb_joint_y = left_hand_list[2][1]
       
        left_index_tip_y, left_index_mcp_y, left_middle_tip_y, left_middle_joint_y, left_ring_tip_y, left_ring_joint_y, left_small_tip_y, left_small_joint_y, left_thumb_tip_x, left_thumb_joint_x = sf.getting_fingers_coordinates(left_hand_list, 1, 8,7,12,10,16,14,20,18,4,3)
 
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
          
            if (left_index_tip_y > left_thumb_tip_y and
                left_thumb_tip_y < left_thumb_joint_y):
              
                if (left_index_tip_x > left_index_mcp_x):
                 
                    if ((left_middle_tip_y < left_middle_joint_y) and 
                        (left_ring_tip_y < left_ring_joint_y) and 
                        (left_ring_tip_y < left_index_mcp_y) and
                        (left_small_tip_y < left_small_joint_y)):
                      
                        self.net_socket.sendto(b"NUM_3", self.c_plus_address)
                        self.prev_time = self.Current_Time

                       
                            

    def typing_four(self, right_hand_list, left_hand_list):

        if len(right_hand_list) != 0 and len(left_hand_list) != 0:
            
            right_index_tip,right_index_joint,right_middle_tip,right_middle_joint,right_ring_tip,right_ring_joint,right_small_tip,right_small_joint,right_thumb_tip_x,right_thumb_mcp_x = sf.getting_fingers_coordinates(right_hand_list, 1, 8,6,12,10,16,14,20,19,4,2)
            left_index_tip,left_index_joint,left_middle_tip,left_middle_joint,left_ring_tip,left_ring_joint,left_small_tip,left_small_joint,left_thumb_tip_x,left_thumb_mcp_x = sf.getting_fingers_coordinates(left_hand_list, 1, 8,6,12,10,16,14,20,19,4,2)
            self.Current_Time = time.time()
           
            if self.Current_Time - self.prev_time > 0.70:
               
                if (right_thumb_tip_x > right_thumb_mcp_x and 
                    left_thumb_tip_x < left_thumb_mcp_x):
                    
                    if ((right_index_tip < right_index_joint and
                         left_index_tip < left_index_joint) and 
                        (right_middle_tip < right_middle_joint and
                         left_middle_tip < left_middle_joint)): 
                        
                        if ((right_ring_tip > right_ring_joint and left_ring_tip > left_ring_joint) and
                            (right_small_tip > right_small_joint and left_small_tip > left_small_joint)):
                       
                            self.net_socket.sendto(b"NUM_4", self.c_plus_address)
                            self.prev_time = self.Current_Time
                            
                            
                            
    def typing_five(self, right_hand_list):
      
      if len(right_hand_list) != 0:
      
        right_index_tip_y,right_index_joint_y,right_middle_tip_y,right_middle_joint_y,right_ring_tip_y,right_ring_joint_y,right_small_tip_y,right_small_joint_y,right_thumb_tip_x,right_thumb_joint_x = sf.getting_fingers_coordinates(right_hand_list, 1, 8,6,12,10,16,14,20,18,4,3)
        right_thumb_tip_y, right_wrist_y, right_index_tip_x = right_hand_list[4][1], right_hand_list[0][1], right_hand_list[8][0]
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
           
            if (right_thumb_tip_x < right_thumb_joint_x and
                right_index_tip_x > right_thumb_joint_x):
                
                if (right_index_tip_y > right_index_joint_y and
                    right_middle_tip_y > right_middle_joint_y and
                    right_ring_tip_y > right_ring_joint_y and
                    right_small_tip_y > right_small_joint_y and
                    right_small_tip_y > right_ring_joint_y 
                    and right_thumb_tip_y < right_wrist_y and
                    right_thumb_tip_y > right_middle_joint_y and
                    right_thumb_tip_y > right_small_joint_y):
                        
                        self.net_socket.sendto(b"NUM_5", self.c_plus_address)
                        self.prev_time = self.Current_Time
                        
                            
                            
    def typing_six(self, right_hand_list):
      
      if len(right_hand_list) != 0:
        print("send to func")
        right_index_joint_y = right_hand_list[6][1]
        right_index_tip_x,right_index_joint_x,right_middle_tip_x,right_middle_joint_x,right_ring_tip_x,right_ring_joint_x,right_small_tip_x,right_small_joint_x,right_thumb_tip_y,rigth_thumb_joint_y = sf.getting_fingers_coordinates(right_hand_list, 0, 8,6,12,10,16,14,20,18,4,3)
        right_thumb_tip_x, right_thumb_joint_x =  right_hand_list[4][0],  right_hand_list[3][0]
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
           
            if (right_thumb_tip_y < rigth_thumb_joint_y and
                rigth_thumb_joint_y < right_index_joint_y):
               
                if (right_index_tip_x > right_index_joint_x and
                    right_middle_tip_x > right_middle_joint_x and
                    right_ring_tip_x > right_ring_joint_x and
                    right_small_tip_x > right_small_joint_x):
                  
                    if ((right_thumb_joint_x > right_ring_joint_x)
                        and (right_thumb_joint_x > right_middle_joint_x)
                        and (right_thumb_joint_x > right_small_joint_x)):
                    
                        self.net_socket.sendto(b"NUM_6", self.c_plus_address)
                        self.prev_time = self.Current_Time

                
                        
    def typing_seven(self, right_hand_list):
        
      if len(right_hand_list) != 0:
       
        right_index_tip_y = right_hand_list[8][1] 
        right_index_tip_x, right_index_joint_x, right_middle_tip_x, right_middle_joint_x, right_ring_tip_x, right_ring_joint_x, right_small_tip_x, right_small_joint_x, right_thumb_tip_y, rigth_thumb_joint_y = sf.getting_fingers_coordinates(right_hand_list, 0, 8,7,12,10,16,14,20,18,4,3)
     
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
            
            if (right_thumb_tip_y < right_index_tip_y and
                right_thumb_tip_y < rigth_thumb_joint_y):
                
                if (right_index_tip_x < right_index_joint_x and
                    right_middle_tip_x > right_middle_joint_x and
                    right_ring_tip_x > right_ring_joint_x and
                    right_small_tip_x > right_small_joint_x):
                    
                        self.net_socket.sendto(b"NUM_7", self.c_plus_address)
                        self.prev_time = self.Current_Time
                        
                        
    def typing_eight(self, right_hand_list):
        
      if len(right_hand_list) != 0:
       
        right_index_tip_y = right_hand_list[8][1]
        right_small_joint_y = right_hand_list[18][1] 
        right_index_tip_x, right_index_joint_x, right_middle_tip_x, right_middle_joint_x, right_ring_tip_x, right_ring_joint_x, right_small_tip_x, right_small_joint_x, right_thumb_tip_y, rigth_thumb_joint_y = sf.getting_fingers_coordinates(right_hand_list, 0, 8,7,12,11,16,14,20,18,4,3)
     
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
            
            if (right_thumb_tip_y < right_index_tip_y and
                right_thumb_tip_y < right_small_joint_y and
                right_thumb_tip_y < rigth_thumb_joint_y):
                
                if (right_index_tip_x < right_index_joint_x and
                    right_index_tip_y <  right_small_joint_y 
                    and right_middle_tip_x < right_middle_joint_x 
                    and right_ring_tip_x > right_ring_joint_x 
                    and right_small_tip_x > right_small_joint_x):
                    
                        self.net_socket.sendto(b"NUM_8", self.c_plus_address)
                        self.prev_time = self.Current_Time
                        
                        
    def typing_nine(self, right_hand_list):
   
      if len(right_hand_list) != 0:

      
        right_index_tip_y, right_index_joint_y, right_middle_tip_y, right_middle_joint_y, right_ring_tip_y, right_ring_joint_y, right_small_tip_y, right_small_joint_y, right_thumb_tip_x, right_thumb_joint_x = sf.getting_fingers_coordinates(right_hand_list, 1, 8,7,12,11,16,15,20,19,4,2)
 
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
          
            if (right_thumb_tip_x > right_thumb_joint_x):
          
               if (right_small_tip_y < right_small_joint_y and
                   right_index_tip_y > right_index_joint_y and
                   right_middle_tip_y > right_middle_joint_y and 
                   right_ring_tip_y > right_ring_joint_y):
               
                   self.net_socket.sendto(b"NUM_9", self.c_plus_address)
                   self.prev_time = self.Current_Time
                   
                   
                   
    def typing_backspace(self, left_hand_list):
        
      if len(left_hand_list) != 0:
          
        left_index_tip_x, left_index_joint_x, left_middle_tip_x, left_middle_joint_x, left_ring_tip_x, left_ring_joint_x, left_small_tip_x, left_small_joint_x, left_thumb_tip_y, left_thumb_joint_y = sf.getting_fingers_coordinates(left_hand_list, 0, 8,6,12,10,16,14,20,18,4,3)
 
        self.Current_Time = time.time()
        
        if self.Current_Time - self.prev_time > 0.70:
            
            if (left_thumb_tip_y > left_thumb_joint_y):
                
                if ((left_index_tip_x > left_index_joint_x) and 
                    (left_middle_tip_x > left_middle_joint_x)):
                    
                    if ((left_ring_tip_x < left_ring_joint_x) and 
                        (left_small_tip_x < left_small_joint_x)):
                        
                        self.net_socket.sendto(b"BACKSPACE", self.c_plus_address)
                        self.prev_time = self.Current_Time
