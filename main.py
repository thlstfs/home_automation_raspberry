import RPi.GPIO as GPIO
from flask import Flask, request
app = Flask(__name__)
global led, green

@app.route('/test')
def hello_world():
   led.start(100)
   return 'Hello World'


@app.route('/start')
def start():
   color = request.args.get('color', type=str, default='0xffff0000')
   led.start(100)
   led.ChangeDutyCycle(int(color))
   green.start(100)
   return '200'

@app.route('/stop')
def stop():
   led.stop()
   green.stop()
   return '200'


if __name__ == '__main__':
   ledPin = 21
   greenPin = 20
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(ledPin, GPIO.OUT)
   GPIO.setup(greenPin,GPIO.OUT)
   led = GPIO.PWM(ledPin, 100)
   green = GPIO.PWM(greenPin, 100)
   app.run(host='0.0.0.0', port=5000, debug=True)
