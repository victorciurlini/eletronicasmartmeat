#Define Libraries
import RPi.GPIO as gpio
import time
 
#Configuring don’t show warnings 
gpio.setwarnings(False)
 
#Configuring GPIO
gpio.setmode(gpio.BOARD)
gpio.setup(33,gpio.OUT)
gpio.setup(35,gpio.OUT)
gpio.setup(38,gpio.OUT)
gpio.setup(40,gpio.OUT)
 
#Configure the pwm objects and initialize its value
pwmMot1 = gpio.PWM(38,100)
pwmMot1.start(0)
 
pwmMot2 = gpio.PWM(33,100)
pwmMot2.start(0)

pwmMot3 = gpio.PWM(35,100)
pwmMot3.start(0)

pwmMot4 = gpio.PWM(40,100)
pwmMot4.start(0)
 
#Create the dutycycle variables
dc1 = 0
dc2  = 0
dc3 = 0
dc4 = 0

#Loop infinite
while True:
   
    #increment gradually the luminosity
    pwmMot1.ChangeDutyCycle(dc1)
    time.sleep(0.05)
    dc1 = dc1 + 1
    if dc1 == 100:
        dc1 = 0

    #increme'nt gradually the luminosity
    pwmMot1.ChangeDutyCycle(dc1)
    time.sleep(0.05)
    dc1 = dc1 + 1
    if dc1 == 100:
        dc1 = 0

    #increment gradually the luminosity
    pwmMot2.ChangeDutyCycle(dc2)
    time.sleep(0.05)
    dc2 = dc2 + 1
    if dc2 == 100:
        dc2 = 0

    #increment gradually the luminosity
    pwmMot3.ChangeDutyCycle(dc3)
    time.sleep(0.05)
    dc3 = dc3 + 1
    if dc3 == 100:
        dc3 = 0

    pwmMot4.ChangeDutyCycle(dc3)
    time.sleep(0.05)
    dc3 = dc3 + 1
    if dc3 == 100:
        dc3 = 0
    
#End code
gpio.cleanup()
exit()
