from GPIO_code.stepper_function import init_stepper
import RPi.GPIO as GPIO
from web.api import app_api
from web.webcam import app_webcam
from flask import Flask, render_template

app = Flask(__name__, template_folder='web/templates')


app.register_blueprint(app_api)
app.register_blueprint(app_webcam)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    init_stepper()
    app.run(debug=False, host='0.0.0.0')
    GPIO.cleanup()
    # app.run(host='0.0.0.0')
