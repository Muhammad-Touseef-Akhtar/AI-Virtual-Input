import cv2
import time
import socket
import Hands_Tracking as ht
import Mouse_Events as me
import Keyboard_Events as ke
import Suporting_Functions as sf

# ----------------------------------------------------------------------------------------------------

def main():

    Previous_Time = 0
    Current_Time = 0
    is_mouse_active = True
    Mouse_Active_Previous_Time = 0

    cap = cv2.VideoCapture(0)
    
    H_detector = ht.Hand_Detection() 
    MF_detector = me.Mouse_Fingers_Detection()
    KF_detector = ke.Keyboard_Fingers_Detection()

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to grab camera frame. Exiting.....")
            break

        img = cv2.flip(img, 1)

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = H_detector.hands.process(imgRGB)

        img = H_detector.Find_Hands(img, results)
        land_marks_list = H_detector.Find_Hand_Coordinates_For_Mouse(results)
        right_hand_list, left_hand_list = H_detector.Find_Hand_Coordinates_For_Keyboard(img, results)
       
        if len(right_hand_list) > 0 and len(left_hand_list) > 0:
          Mouse_Active_Previous_Time, is_mouse_active = sf.is_wrist_cross(left_hand_list, right_hand_list, Mouse_Active_Previous_Time, is_mouse_active)

       
        if not (is_mouse_active):
          
          cv2.putText(img, "MOUSE CLOSE", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 1)
          if len(right_hand_list) > 0 and len(left_hand_list) > 0:
             KF_detector.typing_four(right_hand_list, left_hand_list)
           
          elif len(right_hand_list) > 0 and len(left_hand_list) == 0:
    
            KF_detector.typing_one(right_hand_list)
            KF_detector.typing_two(right_hand_list)
            KF_detector.typing_five(right_hand_list)
            KF_detector.typing_six(right_hand_list)
            KF_detector.typing_seven(right_hand_list)
            KF_detector.typing_eight(right_hand_list)
            KF_detector.typing_nine(right_hand_list)
           
          elif len(left_hand_list) > 0 and len(right_hand_list) == 0:
            KF_detector.typing_zero(left_hand_list)
            KF_detector.typing_three(left_hand_list)
            KF_detector.typing_backspace(left_hand_list)
        
        else:   
    
            cv2.putText(img, "MOUSE ON", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 1)
            MF_detector.cursor_movement(land_marks_list)
            MF_detector.double_click(land_marks_list)
            MF_detector.left_click(land_marks_list)
            MF_detector.right_click(land_marks_list)

        Current_Time = time.time()
        Frame_per_sec = 1/(Current_Time-Previous_Time)
        Previous_Time = Current_Time
        
        cv2.imshow("Image", img) 

        if cv2.waitKey(1) & 0xFF in [ord('e'), ord('E')]:
           break
       
       
    exit_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sending shutdown command to C++ on Port 5005...")
    exit_socket.sendto(b"EXIT", ("127.0.0.1", 5005))
    exit_socket.close()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


# python PYTHON_Main_Body.py       
# g++ CPP_Main_Body.cpp Keyboard_KeyReceiver.cpp -o Virtual_Project_V2.exe -lws2_32 ; .\Virtual_Project_V2.exe