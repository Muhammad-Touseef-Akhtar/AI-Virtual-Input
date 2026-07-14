import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui as auto
import Suporting_Functions as sf
    
#---------------------------------------------------------------------------------------------------------
  
class Mouse_Fingers_Detection():
    
    def __init__(self):
        
       self.Current_Time = 0
       self.prev_left = 0
       self.prev_right = 0
       self.prev_double = 0


    def cursor_movement(self, land_marks_list):

        if len(land_marks_list) != 0:
            
            index_tip,index_joint,middle_tip,middle_joint,ring_tip,ring_joint,small_tip,small_joint,thumb_tip_x,thumb_mcp_x = sf.getting_fingers_coordinates(land_marks_list, 1, 8,6,12,10,16,14,20,18,4,3)
           
            if (thumb_tip_x < thumb_mcp_x):
                    
                    if ((index_tip < index_joint) and 
                        (middle_tip < middle_joint) and
                        (ring_tip > ring_joint) and 
                        (small_tip > small_joint)):
                        
                        points = sf.screen_adjust(land_marks_list, 8)
                        
                        auto.moveTo(points)
                    
                        
                
    
    def left_click(self, land_marks_list):
          
           if len(land_marks_list) != 0:
            
            index_tip,index_joint,middle_tip,middle_joint,ring_tip,ring_joint,small_tip,small_joint,thumb_tip_x,thumb_mcp_x = sf.getting_fingers_coordinates(land_marks_list, 1, 8,7,12,10,16,14,20,18,4,2)
            self.Current_Time = time.time()
             
            if  self.Current_Time  - self.prev_left > 0.25:
                if (thumb_tip_x > thumb_mcp_x):
                    
                    if (index_tip > index_joint and
                        middle_tip < middle_joint):
              
                      if ((ring_tip > ring_joint) and
                          (small_tip > small_joint)):
                    
                          auto.leftClick()
                          self.prev_left = self.Current_Time
    
  
    def right_click(self, land_marks_list):
          
           if len(land_marks_list) != 0:
      
            middle_mcp = land_marks_list[9][1]
            
            index_tip,index_joint,middle_tip,middle_joint,ring_tip,ring_joint,small_tip,small_joint,thumb_tip_x,thumb_mcp_x = sf.getting_fingers_coordinates(land_marks_list, 1, 8,6,12,11,16,14,20,18,4,2)
            self.Current_Time = time.time()
            
            if  self.Current_Time  - self.prev_right > 0.25:
                
                if (thumb_tip_x > thumb_mcp_x):
                    
                 if (index_tip < index_joint and
                     middle_tip > middle_joint and
                     middle_tip < middle_mcp):
                    
                       if ((ring_tip > ring_joint) and
                           (small_tip > small_joint)):
                    
                           auto.rightClick()
                           self.prev_right = self.Current_Time  
                          
                          
    def double_click(self, land_marks_list):
        
        if len(land_marks_list) != 0:
            
            index_mcp = land_marks_list[5][1]
            middle_mcp = land_marks_list[9][1]
 
            index_tip,index_joint,middle_tip,middle_joint,ring_tip,ring_joint,small_tip,small_joint,thumb_tip_x,thumb_mcp_x = sf.getting_fingers_coordinates(land_marks_list, 1, 8,6,12,7,16,13,20,17,4,2)
            self.Current_Time = time.time()
            
            if  self.Current_Time  - self.prev_double > 0.35:
                
                if (thumb_tip_x > thumb_mcp_x):
                    
                     if (index_tip < index_mcp and
                         middle_tip <  middle_mcp and
                         index_tip > index_joint and
                         middle_tip >  middle_joint):
                    
                        if(ring_tip > ring_joint) and (small_tip > small_joint):
                 
                          auto.doubleClick()
                          self.prev_double = self.Current_Time
                                          