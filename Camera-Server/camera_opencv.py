import cv2
import time
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        for x in range(1,10):
            print("Trying " + str(x) + "/10... "),
            camera = cv2.VideoCapture(Camera.video_source)
            if camera.isOpened():
                print("Success!")
                break
            print("Failed.")
            time.sleep(2)
        if not camera.isOpened() :
            raise RuntimeError('Could not start camera.')
        camera.set(3,1280)
        camera.set(4,720)

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
