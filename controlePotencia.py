import RPi.GPIO as GPIO
import time


def mainTriac():
    from valor import getValor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    valor2 =0
    tempo = 0
    entrada = 16 #pin 16
    saida = 18 #pin 18
    GPIO.setup(saida, GPIO.OUT)
    GPIO.output(saida, False)
    GPIO.setup(entrada, GPIO.IN)
            
    def acende(a):
        microseconds = 0.00001*float(tempo)
        time.sleep(microseconds)
        GPIO.output(saida, True)
        time.sleep(0.001)
        GPIO.output(saida, False)
        #print("xauzin")


    GPIO.add_event_detect(entrada, GPIO.RISING, callback=acende)

    while True:
        valor = getValor()
        if(valor == 0):
            valor2 = 800
        if(valor == 1):
            valor2 = 70
        if(valor == 2):
            valor2 = 20
        if(valor == 3):
            valor2 = 0
        tempo = (90*valor2)
        time.sleep(0.005)
        #print("Valor = ", valor2)
