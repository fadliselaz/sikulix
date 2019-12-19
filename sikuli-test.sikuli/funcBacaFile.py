import random
import time

def readFile():
    with open('msg.txt', 'r') as rd:
        baca = rd.read().splitlines()
    
    lg = len(baca)

    for i in range(lg):
        contact = baca[i].split(',')
        print(contact[0]+ " "+contact[1])
        time.sleep(2)
