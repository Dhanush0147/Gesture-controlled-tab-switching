# Gesture-controlled-tab-switch

This project allows users to switch between windows on their computer using **hand gestures** captured via a webcam. It utilizes **OpenCV**, **MediaPipe**, and **PyAutoGUI** to detect hand movements and trigger `ALT+TAB` or `SHIFT+ALT+TAB` commands.

## Libraries Used

1. **OpenCV** (`cv2`): Used for capturing and displaying video from the webcam.
2. **MediaPipe** (`mediapipe`): Handles real-time hand landmark detection.
3. **PyAutoGUI** (`pyautogui`): Simulates keyboard shortcuts to switch between windows.
4. **Time** (`time`): Used to set time intervals for gesture recognition.

## How It Works

1. The webcam captures live video.
2. The **MediaPipe Hands** module detects hand landmarks.
3. The x-coordinate of the **wrist** is tracked over time.
4. If the **hand moves significantly left or right**, the program triggers:
   - `ALT + TAB` → **Switch to the next window** (Right movement)
   - `SHIFT + ALT + TAB` → **Switch to the previous window** (Left movement)
5. The script runs in a loop, continuously detecting hand movements until **'q'** is pressed.

## How to Run

1. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe pyautogui
Run the script:

