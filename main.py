from flask import Flask, request
import led
app = Flask(__name__)




@app.route('/test')
def hello_world():
    return 'Hello World'




@app.route('/connect')
def connect():
    return lamp.currentColor




@app.route('/changeColor')
def changeColor():
    color = request.args.get('color', type=str, default='0xffff0000')
    lamp.changeColor(color.replace('Color(0xff', '').replace(')', ''))
    return lamp.currentColor




@app.route('/stop')
def stop():
    lamp.stopLed()
    return '200'




if __name__ == '__main__':
    lamp = False
    try:
        lamp = led.Led(21, 20, 16)
        lamp.changeColor(lamp.currentColor)
        app.run(host='0.0.0.0', port=5000, debug=True)


    except KeyboardInterrupt:
        pass
    finally:
        lamp.cleanup()
