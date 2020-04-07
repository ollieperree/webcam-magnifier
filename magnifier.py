import cv2
from pynput import keyboard
import numpy as np
import subprocess
import settings
import datetime
from time import sleep


# Set up webcam
if settings.WEBCAM_FOCUS == "auto":
    subprocess.run(["v4l2-ctl", "-d", settings.WEBCAM_DEVICE, "-c", "focus_auto=1"])
else:
    subprocess.run(["v4l2-ctl", "-d", settings.WEBCAM_DEVICE, "-c", "focus_auto=0"])
    subprocess.run(["v4l2-ctl", "-d", settings.WEBCAM_DEVICE, "-c", f"focus_absolute={settings.WEBCAM_FOCUS}"])
cam = cv2.VideoCapture(settings.WEBCAM_DEVICE)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, settings.WEBCAM_RESOLUTION_WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.WEBCAM_RESOLUTION_HEIGHT)

binary_mode = settings.BINARY_MODE_DEFAULT
binary_setting = settings.BINARY_SETTING_DEFAULT
zoom = settings.ZOOM_DEFAULT

# Set up keyboard shortcuts
def handle_key_press(key):
    global binary_mode, binary_setting, zoom
    if hasattr(key, "char"):
        key = key.char
    elif hasattr(key, "_name_"):
        key = key._name_
    else:
        return

    if key in settings.KEYMAP:
        action = settings.KEYMAP[key]
        if action == "zoom in":
            zoom += 20
        elif action == "zoom out":
            zoom = max(100, zoom - 20)
        elif action == "zoom default":
            zoom = settings.ZOOM_DEFAULT
        elif action == "enhance":
            pass
        elif action == "snapshot":
            d = datetime.datetime.now()
            img_name = "reader_image_{date:%Y-%m-%d_%H:%M:%S}.png".format(date=d)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
        elif action == "binary mode":
            if binary_mode == True:
                binary_setting = (binary_setting + 1) % len(settings.BINARY_COLOURS)
            else:
                binary_mode = True
        elif action == "colour mode":
            binary_mode = False

keyboard_controller = keyboard.Controller()
listener = keyboard.Listener(on_press=handle_key_press)
listener.start()

prev_frame = None

while True:
    ret, frame = cam.read()

    # rotation
    if settings.WEBCAM_ORIENTATION == "left":
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame, flipCode=0)
    elif settings.WEBCAM_ORIENTATION == "right":
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame, flipCode=1)
    elif settings.WEBCAM_ORIENTATION == "inverted":
        frame = cv2.flip(frame, flipCode=0)
        frame = cv2.flip(frame, flipCode=1)

    if binary_mode:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 33, 22)  # 33, 20
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        new_frame = frame.copy()
        new_frame[np.where((frame == [255,255,255]).all(axis=2))] = settings.BINARY_COLOURS[binary_setting][1]
        new_frame[np.where((frame == [0,0,0]).all(axis=2))] = settings.BINARY_COLOURS[binary_setting][0]
        frame = new_frame

    if zoom == 100:
        frame = cv2.resize(frame,
                       (settings.DISPLAY_RESOLUTION_WIDTH, settings.DISPLAY_RESOLUTION_HEIGHT),
                       cv2.INTER_AREA)
    else:
        crop_width = int(settings.WEBCAM_RESOLUTION_WIDTH / (zoom/100))
        crop_height = int(settings.WEBCAM_RESOLUTION_HEIGHT / (zoom/100))
        crop_offset_left = (settings.WEBCAM_RESOLUTION_WIDTH - crop_width) // 2
        crop_offset_top = (settings.WEBCAM_RESOLUTION_HEIGHT - crop_height) // 2
        frame = frame[crop_offset_top:crop_offset_top+crop_height, crop_offset_left:crop_offset_left+crop_width]
        frame = cv2.resize(frame,
                       (settings.DISPLAY_RESOLUTION_WIDTH, settings.DISPLAY_RESOLUTION_HEIGHT),
                       cv2.INTER_AREA)

    # Note: important to resize after binarisation so we get that sweet sweet antialiasing

    # If frame is very similar to previous frame, don't change it.
    if prev_frame is not None:
        frame_similarity = np.sum(frame == prev_frame) / np.product(frame.shape)
        if frame_similarity >= 1 - settings.FRAME_DIFFERENCE_THRESHOLD:
            frame = prev_frame
    prev_frame = frame.copy()

    cv2.imshow("Magnifier", np.array(frame))
    cv2.namedWindow("Magnifier", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Magnifier", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break


cam.release()

cv2.destroyAllWindows()
