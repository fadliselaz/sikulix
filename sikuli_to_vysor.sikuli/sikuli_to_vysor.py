
import os
import time
import random

msg = ["test","udah","lagi","dah","coba"]


l = Region(987,59,444,742)
w = "w.png"
m = "m.png"

sd = "sd.png"

for i in range(10):
    msr = random.choice(msg)
    l.click(m)
    type(msr)
    wait(2)
    l.click(sd)
    wait(2)
