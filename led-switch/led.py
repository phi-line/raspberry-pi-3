import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(16,GPIO.OUT)

    while True:
	time.sleep(0.2)
    	GPIO.output(16,GPIO.HIGH)
    	time.sleep(0.2)
        GPIO.output(16,GPIO.LOW)

if __name__=='__main__':
    main()
