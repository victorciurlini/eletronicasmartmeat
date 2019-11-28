import RPi.GPIO as GPIO
import time


def mainBTN ():
        #Nao esquecer de alterar para os pinos da rasp
        slot1 = 7
        slot2 = 11 
        slot3 = 12
        slot4 = 13

        #GPIO.setmode(GPIO.BCM)
        # BCM significa que estamos utilizando pelo numero GPIO
        # Caso queira usar pelo numero da porta basta comentar a linha de cima e descomentar a de baixo
        GPIO.setmode(GPIO.BOARD) 

        #Estao definidos resistores de pull ups externos. Ou seja, sempre 5 e fecha quando o botao for pressionado
        GPIO.setup(slot1, GPIO.IN)
        GPIO.setup(slot2, GPIO.IN)
        GPIO.setup(slot3, GPIO.IN)
        GPIO.setup(slot4, GPIO.IN)
        GPIO.setwarnings(False)

        while True:
                if (slot1 == True):
                        print("oi")
                        return True
                elif (slot1 == False):
                        return False
                
                if (slot2 == True):
                        return True
                elif (slot2 == False):
                        return False
                
                if (slot3 == True):
                        return True
                elif (slot3 == False):
                        return False
                
                if (slot4 == True):
                        return True
                elif (slot4 == False):
                        return False

                



	
        
