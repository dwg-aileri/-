import RPi.GPIO as GPIO
import time

GPIO.cleanup()
chan_list = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list,GPIO.OUT)



def lightUp(led_number, period):
    GPIO.output(chan_list[led_number], 1)
    time.sleep(period)
    GPIO.output(chan_list[led_number], 0)

def Blink(led_number, blinkCount, blinkPeriod):
    for i in range(0,blinkCount,1):
        GPIO.output(chan_list[led_number], 1)
        time.sleep(blinkPeriod)
        GPIO.output(chan_list[led_number], 0)
        time.sleep(blinkPeriod)

def runningLight(count,per):
    for j in range(0, count, 1):
        for i in range(0,8,1):
            lightUp(i, per)

def darkUp(led_number, period):
    GPIO.output(chan_list[led_number], 0)
    time.sleep(period)
    GPIO.output(chan_list[led_number], 1)

def runningDark(count,pir):
    for k in range(0,8,1):
        GPIO.output(chan_list[k],1 )
        time.sleep(pir)
    for j in range(0, count, 1):
        for i in range(0,8,1):
            darkUp(i, pir)
    for m in range(0,8,1):
        GPIO.output(chan_list[m], 0)
        time.sleep(pir)

def decToBin(m):
    nahc_list = [0,0,0,0,0,0,0,0]
    for i in range(7,-1,-1):
        if m % 2 == 1:
            nahc_list[i] = 1
        m = m // 2
    return (nahc_list)

def lightNumber(m):
    nahc_list = decToBin(m)
    GPIO.output(chan_list,0)
    for l in range (7,-1,-1):
        if nahc_list[l] == 1:
            print(7-l)
            GPIO.output(chan_list[7-l],1)
    time.sleep(5)

lightNumber(243)



GPIO.cleanup()

