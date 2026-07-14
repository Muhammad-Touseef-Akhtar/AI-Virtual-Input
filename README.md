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

1. **Clone the repository:**
   git clone https://github.com

2. **Install core dependencies:**
   pip install opencv-python mediapipe

3. **Run the entry file:**
   python main.py
