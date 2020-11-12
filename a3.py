import RPi.GPIO as GPIO
import time
import array
from time import sleep

hcnok_list = [10,9,11,5,6,13,19,26]
chan_list = [24, 25, 8, 7, 12, 16, 20, 21]


GPIO.setmode(GPIO.BCM)

GPIO.setup(hcnok_list,GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setup(chan_list,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)

def num2dec(value):
    
    #print("V=", value*3.3/255)
    while True:
        lightNumber(value)
        time.sleep(0.01)
        if GPIO.input(4) == 0:
            print("i=",value," V=", value*3.3/255)
            break

    
        
        
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
    
def dec(Value,pins):
    value = int(Value)
    for a in pins:
        GPIO.output(a, 0)
    for i in range(7, -1, -1):
        x = 1 << i
        GPIO.output(pins[i],(x&value)>>i)


def findvalue():
    l=0
    r=255
    dec(r,hcnok_list)
    while r-l >0:
        c = (r+l)//2
        dec(c, hcnok_list)
        time.sleep(0.001)
        if GPIO.input(4) == 1:
            l=c+1
        else: 
            r=c
    return (r+l)//2


try:
    value = 0
    start = time.time()
    while value<243:
        GPIO.output(17,1)
        value = adc()
        Voltage = float(value)*3.3/255
        print("Digital value:", value, "Analog value:%.2f V" % (Voltage))
        s.append(value)
        t.append(time.time()-start)
        time.sleep(0.001)
    GPIO.output(17,0)
    while value>5:
        value = adc()
        Voltage = float(value)*0.01289
        print("Digital value:", value, "Analog value:%.2f V" % (Voltage))
        s.append(value)
        t.append(time.time()-start)
        time.sleep(0.001)
    stop = time.time()
    tim = stop - start
    c = len(s)
    plt.plot(t, s)
    plt.show()
except KeyboardInterrupt:
    print("erorr kKeyboardInterupt")
finally:
    GPIO.cleanup()
    print("nya poka")