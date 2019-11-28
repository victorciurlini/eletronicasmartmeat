import RPi.GPIO as gpio
import time



def mainTermo():

    CLK1 = 33
    DBIT1 = 35 #S0
    CS1 = 37

    CLK2 = 36
    DBIT2 = 38 #S0
    CS2 = 40


    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    gpio.setup(CLK1, gpio.OUT)
    gpio.setup(DBIT1, gpio.IN)
    gpio.setup(CS1, gpio.OUT)
    gpio.setup(CLK2, gpio.OUT)
    gpio.setup(DBIT2, gpio.IN)
    gpio.setup(CS2, gpio.OUT)

##    def getTemp():
##        Temp = CtempMedia
##        return Temp


    def Thermal_Couple_Read(CLK, DBIT, CS):
        value = 0
        #iniciar sensor
        gpio.output(CS, False)
        time.sleep(0.002)
        gpio.output(CS, True)
        time.sleep(0.02)

        #Ler o chip e retornar a temperatura
        gpio.output(CS, False)
        gpio.output(CLK, True)
        gpio.output(CLK, False)

        i = 14
        while i>= 0:
            gpio.output(CLK, True)
            value += gpio.input(DBIT) << i
            gpio.output(CLK, False)
            i = i-1

        if((value & 0x04)==0x04):
            return -1

        return value >> 3
            
    SENSOR_VALUE1 = 0
    SENSOR_VALUE2 = 0
    x = 1

    gpio.output(CS1, True)
    gpio.output(CLK1, False)
    gpio.output(CS2, True)
    gpio.output(CLK2, False)

    SENSOR_VALUE1 = Thermal_Couple_Read(CLK1, DBIT1, CS1)
    if(SENSOR_VALUE1 == -1):
        println("Sensor 1 nao conectado")

    SENSOR_VALUE2 = Thermal_Couple_Read(CLK2, DBIT2, CS2)
    if(SENSOR_VALUE2 == -1):
        println("Sensor 2 nao conectado")

    else:
        while True:
            SENSOR_VALUE1 = Thermal_Couple_Read(CLK1, DBIT1, CS1)
            SENSOR_VALUE2 = Thermal_Couple_Read(CLK2, DBIT2, CS2)

            Ctemp1 = SENSOR_VALUE1*0.25
            Ctemp2 = SENSOR_VALUE2*0.25
            CtempMedia = (Ctemp1+Ctemp2)/2
            #print("\nTemperatura media = ", CtempMedia)
            return CtempMedia
            time.sleep(5)
        
        
##        print("\nS1: ", SENSOR_VALUE1)
##        
##        print("\nTemperatura C1 = ", Ctemp1)
##
##        print("\nS2: ", SENSOR_VALUE2)
##        Ctemp2 = SENSOR_VALUE2*0.25
##        print("\nTemperatura C2 = ", Ctemp2)
