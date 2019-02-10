import picamera
import picamera.array

import numpy as np


with picamera.PiCamera as camera:
    with picamera.array.PiRGBArray(camera) as output:
        camera.capture(output, "rgb")
        print(output.array)
