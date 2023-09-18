import time
import pigpio




class Led:


    def __init__(self, redPin=25, greenPin=2, bluePin=3):
        self.redPin = redPin
        self.greenPin = greenPin
        self.bluePin = bluePin
        self.gpio = pigpio.pi()
        print(redPin, greenPin, bluePin)
        self.gpio.set_mode(redPin, pigpio.OUTPUT)
        self.gpio.set_PWM_frequency(redPin, 1000)
        self.gpio.set_PWM_dutycycle(redPin, 0)


        self.gpio.set_mode(greenPin, pigpio.OUTPUT)
        self.gpio.set_PWM_frequency(greenPin, 1000)
        self.gpio.set_PWM_dutycycle(greenPin, 0)


        self.gpio.set_mode(bluePin, pigpio.OUTPUT)
        self.gpio.set_PWM_frequency(bluePin, 1000)
        self.gpio.set_PWM_dutycycle(bluePin, 0)
        self.currentColor = "000000"


    def cleanup(self):
        self.gpio.stop()


    def hexToRgb(self, h):
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


    def changeColor(self, color):
        self.currentColor = color
        r, g, b = self.hexToRgb(color)
        print(r, g, b)
        self.gpio.set_PWM_dutycycle(self.redPin, r)
        self.gpio.set_PWM_dutycycle(self.greenPin, g)
        self.gpio.set_PWM_dutycycle(self.bluePin, b)


    def stopLed(self):
        self.changeColor('000000')
