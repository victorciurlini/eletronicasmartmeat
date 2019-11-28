import RPi.GPIO as gpio
import time
import _thread
from termopar import mainTermo as termopar
from controlePotencia import mainTriac as triac
import valor as value
#from buttons import mainBTN


_thread.start_new_thread(termopar, ())
_thread.start_new_thread(triac, ())
_thread.start_new_thread(value.getValor, ())
#_thread.start_new_thread(mainBTN, ())

while True:
    termperatura = termopar()
    #print("Temp Media= ", termperatura)
    pass
