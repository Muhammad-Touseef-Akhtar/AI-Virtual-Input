import pyautogui as auto
import numpy as np
import time

# ------------------------------------------------------------------------------------------------------

auto.FAILSAFE = False

def screen_adjust(land_marks_list, value):
   
    x1_raw = land_marks_list[value][0]
    y1_raw = land_marks_list[value][1]
    
    width, height = auto.size()
    
    LEFT_LIMIT, RIGHT_LIMIT = 0.25, 0.75
    TOP_LIMIT, BOTTOM_LIMIT = 0.25, 0.75
    

    x1 = int(np.interp(x1_raw, [LEFT_LIMIT, RIGHT_LIMIT], [0, width]))
    y1 = int(np.interp(y1_raw, [TOP_LIMIT, BOTTOM_LIMIT], [0, height]))
    
    x1 = max(0, min(width - 1, x1))
    y1 = max(0, min(height - 1, y1))
    
    return x1, y1
 

def getting_fingers_coordinates(land_marks_list, type, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
      
      if type == 1:
       index_tip = land_marks_list[v1][1]
       index_joint = land_marks_list[v2][1]
       middle_tip = land_marks_list[v3][1]
       middle_joint = land_marks_list[v4][1]
       ring_tip = land_marks_list[v5][1]
       ring_joint = land_marks_list[v6][1]
       small_tip = land_marks_list[v7][1]
       small_joint = land_marks_list[v8][1]
       thumb_tip = land_marks_list[v9][0]
       thumb_mcp = land_marks_list[v10][0]
      else:
       index_tip = land_marks_list[v1][0]
       index_joint = land_marks_list[v2][0]
       middle_tip = land_marks_list[v3][0]
       middle_joint = land_marks_list[v4][0]
       ring_tip = land_marks_list[v5][0]
       ring_joint = land_marks_list[v6][0]
       small_tip = land_marks_list[v7][0]
       small_joint = land_marks_list[v8][0]
       thumb_tip = land_marks_list[v9][1]
       thumb_mcp = land_marks_list[v10][1]
              
      return index_tip,index_joint,middle_tip,middle_joint,ring_tip,ring_joint,small_tip,small_joint,thumb_tip,thumb_mcp



def is_wrist_cross(left_hand_list, right_hand_list, prev_time, mouse_active):
        
    if len(left_hand_list) != 0 and len(right_hand_list) != 0:
        
        left_wrist_x = left_hand_list[0][0]
        right_wrist_x = right_hand_list[0][0]
        
        current_time = time.time()  
        
        if current_time - prev_time > 1:
                
            if left_wrist_x > right_wrist_x:
                    
                mouse_active = not mouse_active
                prev_time = current_time 
                
    return prev_time, mouse_active
