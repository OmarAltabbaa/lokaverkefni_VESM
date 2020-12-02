#Libraries
import RPi.GPIO as GPIO
import time
import digitalio
import serial
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
 
ADAFRUIT_IO_USERNAME = "OmarAltabbaa"
ADAFRUIT_IO_KEY = "aio_hZec22spHUK9fN4ndWXIwd2hx1Hj"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
 
try: # if we have a 'digital' feed
    digital = aio.feeds('digital')
except RequestError: # create a digital feed
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)
try: # if we have a 'digital' feed
    analog=aio.feeds('distance')
except RequestError: # create a digital feed
    feed = Feed(name="distance")
    analog = aio.create_feed(feed)
#GPIO Mode (BOARD / BCM)

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            aio.send(analog.key, dist)
            read_ser=str( ser.readline().decode('utf-8').rstrip())
            print(read_ser)
            if dist <=200:
                aio.send(digital.key, read_ser)
            

            time.sleep(5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        

    read_ser=ser.readline()
    print(read_ser)
    aio.send(digital.key, read_ser)

