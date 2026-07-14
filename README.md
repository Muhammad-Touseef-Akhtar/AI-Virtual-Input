# AI Virtual Mouse & Keyboard (Hybrid Python/C++)

A gesture-controlled computer vision application built as a 2nd Semester Object-Oriented Programming (OOP) project. This software serves as a hardware-free backup utility, allowing users to control system navigation and input commands through a laptop webcam.

### Project Purpose

Engineered as a software-driven backup solution to reduce reliance on physical input hardware, allowing users to maintain complete system control even if physical input devices fail.

### Key Features

* **Computer Vision Tracking:** Processes real-time webcam frames to track hand gestures for seamless mouse cursor movement and click events.
* **Hybrid System Logic:** Bridges Python vision pipelines with C++ to inject system-wide numeric commands (0-9) across any active text editor software.
* **OOP Architecture:** Designed with highly modular Python classes to encapsulate gesture tracking data using strict inheritance patterns.

### Future Scope

* **Multimodal Overrides:** Incorporating voice command overrides to ensure reliable operation in low-light environments.
* **Native Integration:** Expanding the extensible architecture to propose native, camera-based gesture backup utilities that standard consumer laptops lack.
  


### How to Run Locally

Because this project uses a hybrid architecture, you must run the Python tracking module and the C++ system command listener in **two separate terminal windows simultaneously**.

#### Terminal 1: Start the Python Tracking Module
1. Navigate into the project folder.
2. Install core dependencies:
 
   pip install opencv-python mediapipe
   
4. Execute the core computer vision tracking script:
  
   python PYTHON_Main_Body.py
  

#### Terminal 2: Create and Run the C++ Key Listener
1. Open a brand-new terminal tab or window.
2. Navigate into the same project folder.
3. **Step 1: Create the Executable File**
   Run the compilation command below to generate your own executable application from the C++ source files. You can change    YourCustomName.exe` to any name you prefer for your program file:

   g++ CPP_Main_Body.cpp Keyboard_KeyReceiver.cpp -o YourCustomName.exe -lws2_32
 
5. **Step 2: Verify File Creation**  
   Check your local project folder directory. You will see that a brand-new, compiled binary file matching your chosen name (e.g., `YourCustomName.exe`) has been successfully created.
6. **Step 3: Run the Created Executable**  
   Execute the generated program file to start the system-wide key listener:
  
   .\YourCustomName.exe

  

### Important: First-Time Run & Windows Security Alert

When you execute your newly created C++ executable application for the first time, Windows Defender Firewall will pop up a window asking for network access permissions. This happens because the application sets up a local network socket bridge on Port 5005 to transmit tracking data from Python to C++.

To ensure the virtual input commands transfer successfully:
1. When the Windows Security Alert window appears, check the box for **Private networks** (such as your home or work network).
2. Click **Allow access**.
3. If this permission is denied, the Python computer vision application will fail to send hand gesture inputs to the system text editor.
