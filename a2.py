import RPi.GPIO as GPIO
import time
import array
import matplotlib.pyplot as plt
import scipy
from time import sleep


hcnok_list = [10,9,11,5,6,13,19,26]
GPIO.setmode(GPIO.BCM)
GPIO.setup(hcnok_list,GPIO.OUT)

def decToBin(m):
    konch_list = [0,0,0,0,0,0,0,0]
    for i in range(7,-1,-1):
        if m % 2 == 1:
            konch_list[i] = 1
        m = m // 2
    return (konch_list)

def lightNumber(m):
    konch_list = decToBin(m)
    GPIO.output(hcnok_list,0)
    for l in range (7,-1,-1):
        if konch_list[l] == 1:
            GPIO.output(hcnok_list[7-l],1)
    


def num2dec(value):
    print("vvedi chislo")
    value = int(input())
    if value > -1:
        lightNumber(value)
        num2dec(1)
    elif value == -1:
        print("nya poka")
    else:
        print("fck u")
        num2dec(1)


try:
    print("vvedi kol-vo povtorenii")
    numb = int(input()) 
    while numb>0:
        for value in range (256,-256,-1):
            lightNumber(abs(value))
            time.sleep(0.01)
        numb = numb-1
except KeyboardInterrupt: 
    print("Prerivanie s klavi")
finally:
    for i in range (0,7,1):
        GPIO.output(hcnok_list[i], 0)
    GPIO.cleanup()
    print("ochistilos´")


    
