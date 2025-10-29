import random
import keyboard
import os
import time
global f1
f1=True
global f2
f2=True
global f3
f3=True
global f4
f4=True
global f5
f5=True
global f6
f6=True
global f7
f7=True
global f8
f8=True
global f9
f9=True
def randomlevelgen():
    for i in range(9):
        if i==0:
            global f1
            f1=random.choice([True,False])
        if i==1:
            global f2
            f2=random.choice([True,False])
        if i==2:
            global f3
            f3=random.choice([True,False])
        if i==3:
            global f4
            f4=random.choice([True,False])
        if i==4:
            global f5
            f5=random.choice([True,False])
        if i==5:
            global f6
            f6=random.choice([True,False])
        if i==6:
            global f7
            f7=random.choice([True,False])
        if i==7:
            global f8
            f8=random.choice([True,False])
        if i==8:
            global f9
            f9=random.choice([True,False])
def printlevel(f1,f2,f3,f4,f5,f6,f7,f8,f9):
    line1=str()
    line2=str()
    line3=str()
    if f1:
        line1+="X "
    else:
        line1+="O "
    if f2:
        line1+="X "
    else:
        line1+="O "
    if f3:
        line1+="X "
    else:
        line1+="O "
    if f4:
        line2+="X "
    else:
        line2+="O "
    if f5:
        line2+="X "
    else:
        line2+="O "
    if f6:
        line2+="X "
    else:
        line2+="O "
    if f7:
        line3+="X "
    else:
        line3+="O "
    if f8:
        line3+="X "
    else:
        line3+="O "
    if f9:
        line3+="X "
    else:
        line3+="O "  
    print(line1)
    print(line2)
    print(line3)
def checkwin(f1,f2,f3,f4,f5,f6,f7,f8,f9):
    if f1 and f2 and f3 and f4 and f5 and f6 and f7 and f8 and f9:
        return True
    elif not f1 and not f2 and not f3 and not f4 and not f5 and not f6 and not f7 and not f8 and not f9:
        return True
    else:
        return False
def switchfield(field):
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global f7
    global f8
    global f9
    if field==1:
        f1=not f1
        f2=not f2
        f4=not f4
    if field==2:
        f2=not f2
        f1=not f1
        f3=not f3
        f5=not f5
    if field==3:
        f3=not f3
        f2=not f2
        f6=not f6
    if field==4:
        f4=not f4
        f1=not f1
        f5=not f5
        f7=not f7
    if field==5:
        f5=not f5
        f2=not f2
        f4=not f4
        f6=not f6
        f8=not f8
    if field==6:
        f6=not f6
        f3=not f3
        f5=not f5
        f9=not f9
    if field==7:
        f7=not f7
        f4=not f4
        f8=not f8
    if field==8:
        f8=not f8
        f5=not f5
        f7=not f7
        f9=not f9
    if field==9:
        f9=not f9
        f6=not f6
        f8=not f8    
def playgame():
    randomlevelgen()
    while True:
        os.system("cls")
        printlevel(f1,f2,f3,f4,f5,f6,f7,f8,f9)
        if checkwin(f1,f2,f3,f4,f5,f6,f7,f8,f9):
            time.sleep(0.5)
            print("Gewonnen!")
            os.system("pause")
            break
        print("1-9")
        while True:
            if keyboard.is_pressed("1"):
                switchfield(1)
                break
            if keyboard.is_pressed("2"):
                switchfield(2)
                break
            if keyboard.is_pressed("3"):
                switchfield(3)
                break
            if keyboard.is_pressed("4"):
                switchfield(4)
                break
            if keyboard.is_pressed("5"):
                switchfield(5)
                break
            if keyboard.is_pressed("6"):
                switchfield(6)
                break
            if keyboard.is_pressed("7"):
                switchfield(7)
                break
            if keyboard.is_pressed("8"):
                switchfield(8)
                break
            if keyboard.is_pressed("9"):
                switchfield(9)
                break
        time.sleep(0.2)
    main()
def main():
    os.system("cls")
    print("Willkommen!\nS - Start Game\nQ - Quit")
    while True:
        if keyboard.is_pressed("s"):
            playgame()
            
        if keyboard.is_pressed("q"):
            exit()
main()