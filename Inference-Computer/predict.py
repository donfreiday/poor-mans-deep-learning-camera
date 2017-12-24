from darkflow.net.build import TFNet
import cv2
from datetime import datetime

from io import BytesIO
import time
import requests
from PIL import Image
import numpy as np

options = {"model": "cfg/yolo-voc.cfg", "load": "bin/yolo-voc.weights", "threshold": 0.1}

tfnet = TFNet(options)

def handleBird():
    pass

while True:
    r = requests.get('http://192.168.1.71:5000/image.jpg') # replace with your ip address
    curr_img = Image.open(BytesIO(r.content))
    curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    # uncomment below to try your own image
    #imgcv = cv2.imread('./sample/bird.png')
    result = tfnet.return_predict(curr_img_cv2)
    for detection in result:
        print(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " + detection['label'] + " detected")
        if detection['label'] == 'bird' or detection['label'] == 'cat' or detection['label'] == 'person':
            curr_img.save('{0}/{1}.jpg'.format(detection['label'], datetime.now().strftime('%Y-%m-%d %H.%M.%S')))

    time.sleep(3)
