#!/usr/bin/env python

import time
from time import sleep
from adafruit_servokit import ServoKit
from pynput.keyboard import Key, Listener

kit = ServoKit(channels=16)
angle = 0

def show(key):
    
    while angle <= 180:
        # move pca location 4 to 179 degrees
        if key == Key.left: # left arrow key
            kit.servo[4].angle = 179
            time.sleep(0.01)
            break
               
        # move pca location 4 to 0 degrees    
        if key == Key.right: # right arrow key
            kit.servo[4].angle = 0
            time.sleep(0.01)
            break
            
        # move pca location 5 to 179 degrees
        if key == Key.up: # up arrow key
            kit.servo[5].angle = 179
            time.sleep(0.01)
            break
        
        # move pca location 5 to 0 degrees
        if key == Key.down: # down arrow key
            kit.servo[5].angle = 0
            time.sleep(0.01)
            break
        
        # exit the program    
        else:
            return False
    
with Listener(on_press = show) as listener:
    listener.join()