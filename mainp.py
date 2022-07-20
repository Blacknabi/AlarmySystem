#coding : UTF-8

import os, sys, platform
import time, datetime
import schedule, winsound

def aficheMeni():
    print('')
    print('|         ' + time.strftime("%H:%M") + '          |')
    print('|----------------------------------------------------|')
    print('|                        ALARMY                      |') 
    print('|----------------------------------------------------|')
    print('|    Tape R pou pwograme redemaraj odinate w la      |')
    print('|    Tape F pou pwogram nan femen odinate w la       |')
    print('|            Tape A pou pwograme yon alam            |')
    print('|                  Tape K pou kite                   |')
    print('|____________________________________________________|')
    print('')
    
def rekipereAntre():
    lisAntre = ['R', 'F', 'A', 'K']
    print('CHWAZI YON OPSYON ')
    antre = input(":::>>> ")
    while antre.upper() not in lisAntre:
        print('SVP FE YON BON CHWA ')
        antre = input("::>>> ")
    return antre



def redemare():
    if platform.system()=='Windows':
        
        print(f'Machin ou an pral redemare nan kek segonn.')
        os.system(f"shutdown /r /t 1")
    else:
        print(f'Machin ou an pral redemare nan kek segonn.')
        os.system(f"shutdown /r now")
    
def femen():
    if platform.system()=='Windows':
        print(f'Machin ou an pral femen.')
        os.system(f"shutdown /s /t 1")
    else:
        print(f'Machin ou an pral femen.')
        os.system(f"shutdown /h now")
        
        
    
    

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    global h, mn 
    lh = input("Antre lh a nan foma HH:MM : ")
    h, mn = lh.split(":")
    set_alarm_timer = f"{h}:{mn}"
    alarm(set_alarm_timer)



def kite():
    time.sleep(1.2)
    sys.exit("BYE BYE !")


actual_time()