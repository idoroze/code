from flask import Flask, Response, Blueprint
import cv2

from imutils.video.pivideostream import PiVideoStream
import imutils

import time

vs = PiVideoStream().start()
time.sleep(2)



app_webcam=Blueprint('webcam',__name__)

def gen_frames():  # generate frame by frame from camera
 while True:
     frame = vs.read()
    
     ret, buffer = cv2.imencode('.jpg', frame)
     frame = buffer.tobytes()
     yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result



@app_webcam.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
