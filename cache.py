#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2021, 8,30)
today=date.today()
def hero():
    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    decision=1
    y=1
    newperiod=period
    banner='figlet RXCE'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @Prithvihackz")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        checkRED =current%10
        if(checkRED==0 or checkRED ==2 or checkRED ==4 or checkRED ==6 or checkRED==8):
            previouscolour=1
        else:
            previouscolour=0
        #previouscolour=input("If current colour is RED press 1, or press 0 ")
        if (previouscolour==1):
            Even=True
            Odd=False
        else:
            Even=False
            Odd=True
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        m=0
        def getSum(n):
            sum = 0
            for digit in str(n):
                sum += int(digit)
            return sum
        m=getSum(current)+1
        if(m%2==0):
            R=True
            G=False
        else:
            G=True
            R=False
        #print(m)
        newperiod=period+decision
        x=(newperiod,"GREEN","")
        y=(newperiod,"RED","")
        if(Even and R):
            if (current in numbers):
                print (y)
            else:
                print(x)
        elif(Odd and G):
            if (current in numbers):
                print (y)
            else:
                print (x)
        else:
            if (current in numbers):
                print (x)
            else:
                print (y)
        decision+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @Prithvihackz")
            print(numbers)

if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=14, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=15, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=16, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>First and now<Firstend):
            period=300
            hero()
    elif(now>Second and now<Secondend):
            period=320
            hero()
    elif(now>Third and now<Thirdend):
            period=340
            hero()
    elif(now>Final and now<Finalend):
            period=360
            hero()
    else:
        banner='figlet RXCE'
        print("Please play on the given time, and If you think it is an error contact admin on telegram @Prithvihackz ")



else:
    banner='figlet RXCE'
    print("Your hack has expired--- Please contact on telegram -----------@Prithvihackz")
