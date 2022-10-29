#!/usr/bin/env python

import time
from time import sleep
from adafruit_servokit import ServoKit
from pynput.keyboard import Key, Listener

kit = ServoKit(channels=16)
angle = 0

def show(key):
    
    while angle <= 180:
        if key == Key.left:
            kit.servo[4].angle = 179
            time.sleep(0.01)
            break
            #print("To 179")            
            
        if key == Key.right:
            kit.servo[4].angle = 0
            time.sleep(0.01)
            break
            #print("To 0")
        
        if key == Key.up:
            kit.servo[5].angle = 179
            time.sleep(0.01)
            break
        
        if key == Key.down:
            kit.servo[5].angle = 0
            time.sleep(0.01)
            break
            
        else:
            return False
    
with Listener(on_press = show) as listener:
    listener.join()