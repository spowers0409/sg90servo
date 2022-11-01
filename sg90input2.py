#!/usr/bin/env python

import time
from time import sleep
from adafruit_servokit import ServoKit
from pynput.keyboard import Key, Listener

kit = ServoKit(channels=16)
angle = 0

def show(key):
    
    while angle <= 180:
        # move main arm forward/backward 30-160 degrees
        if key == Key.up: # up arrow key
            kit.servo[0].angle = 30
            time.sleep(0.01)
            break    
        if key == Key.down: # down arrow key
            kit.servo[0].angle = 160
            time.sleep(0.01)
            break
        
        # move base rotation 0-180 degreeas
        if key == Key.left: # left arrow key
            kit.servo[1].angle = 180
            time.sleep(0.01)
            break    
        if key == Key.right: # right arrow key
            kit.servo[1].angle = 0
            time.sleep(0.01)
            break
        
        # move arm tip up or own 0-180 degrees
        if key == Key.shift: # left shift key
            kit.servo[2].angle = 0
            time.sleep(0.01)
            break    
        if key == Key.alt: # right shift key
            kit.servo[2].angle = 180
            time.sleep(0.01)
            break
        
        # rotate arm tip 0-180 degrees
        if key == Key.ctrl_l: # left ctrl key
            kit.servo[3].angle = 0
            time.sleep(0.01)
            break    
        if key == Key.ctrl_r: # right ctrl key
            kit.servo[3].angle = 180
            time.sleep(0.01)
            break
        
        # extend upper arm 0-90 degrees
        if key == Key.tab: # tab key
            kit.servo[4].angle = 0
            time.sleep(0.01)
            break
        if key == Key.home: # shift key
            kit.servo[4].angle = 90
            time.sleep(0.01)
            break
        
        # move pca location 4 to 179 degrees
        if key == Key.page_up: # page up key
            kit.servo[5].angle = 180
            time.sleep(0.01)
            break    
        if key == Key.page_down: # page down key
            kit.servo[5].angle = 0
            time.sleep(0.01)
            break
            
        
        
        # exit the program    
        else:
            return False
    
with Listener(on_press = show) as listener:
    listener.join()
    
    