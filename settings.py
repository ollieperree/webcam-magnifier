WEBCAM_DEVICE = "/dev/video2"
WEBCAM_RESOLUTION_WIDTH = 1920
WEBCAM_RESOLUTION_HEIGHT = 1080
WEBCAM_ORIENTATION = "inverted"  # "normal", "right", "inverted", "left"
WEBCAM_FOCUS = 14 # "auto"

DISPLAY_RESOLUTION_WIDTH = 1366
DISPLAY_RESOLUTION_HEIGHT = 768

BINARY_COLOURS = [
    [[0,0,0], [0,255,255]],  # black on yellow (BGR)
    [[0,255,255], [0,0,0]],  # yellow on black
    [[255,0,0], [0,255,255]],  # blue on yellow
    [[0,255,255], [255,0,0]],  # yellow on blue

]
BINARY_MODE_DEFAULT = True
BINARY_SETTING_DEFAULT =  0

ZOOM_DEFAULT = 100  # Default percent zoom
                    # This works by cropping to the center of the image and upsampling if necessary
                    # In future upsampling will be done using deep neural networks
                    # (probably at the expense of severly reduced frame rate)
                    

FRAME_DIFFERENCE_THRESHOLD = 0.02  # Frame must be more than ___ different to last frame to be updated
                                    # This value should be set just high enough that the binarised image doesn't flicker


KEYMAP = {
        "+": "zoom in",
        "-": "zoom out",
        "enter": "zoom default",
        "0": "enhance",
        "insert": "enhance",
        "/": "snapshot",
        "1": "binary mode",
        "end": "binary mode",
        "7": "colour mode",
        "home": "colour mode",
        "esc": "exit"
    }


