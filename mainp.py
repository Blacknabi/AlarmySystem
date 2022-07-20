#coding : UTF-8

import os, sys, platform
import time, datetime
import schedule, playsound

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
    lisAntre = ['R', 'F', 'A', 'K']
    print('CHWAZI YON OPSYON ')
    antre = input(":::>>> ")
    antre = antre.upper()
    while antre not in lisAntre:
        print('SVP FE YON BON CHWA. CHWAZI YON OPSYON ')
        antre = input("::>>> ")
    return antre
   

def redemare():
    print('|----------------------------------------------------|')
    print('|           ::: PWOGRAME YON REDEMARAJ :::           |')
    print('|----------------------------------------------------|')
    ss = input("Antre nan konbyen segonn poun redemare. Eg: <34> : ")
    if platform.system()=='Windows':
        print(f'Machin ou an pral redemare nan {ss} segonn.')
        os.system(f"shutdown /r /t {ss}")
    else:
        print(f'Machin ou an pral redemare nan {ss} segonn.')
        os.system(f"shutdown /r /t {ss}")
   
    
    
def femen():
    print('|----------------------------------------------------|')
    print('|         ::: PWOGRAME YON ARE OTAMATIK :::          |')
    print('|----------------------------------------------------|')
    ss = input("Antre nan konbyen segonn femen. Eg: <34> : ")
    if platform.system()=='Windows':
        print(f'Machin ou an pral femen nan {ss} segonn.')
        os.system(f"shutdown /s /t {ss}")
    else:
        print(f'Machin ou an pral femen nan {ss} segonn.')
        os.system(f"shutdown /h {ss}")
           
                   
def alarm(ajiste_alam):
    while True:
        time.sleep(1.2)
        lh_kounyea = datetime.datetime.now()
        now = lh_kounyea.strftime("%H:%M")
        date = lh_kounyea.strftime("%d/%m/%Y")
        print("Date jodi a se : ",date)
        print(now)
        if now == ajiste_alam:
            print("Alam lanse...")
            playsound.playsound(son)
            break



def done_alam():
    global h, mn, son, foma
    print('|----------------------------------------------------|')
    print('|              ::: PWOGRAME YON ALAM :::             |')
    print('|----------------------------------------------------|')
    print("|                    Itilize foma  24H               |")
    print('|----------------------------------------------------|')
    lh = input("Antre lh a nan foma HH:MM. Eg: <22:15> : ")
    son = input("Antre chemen mizik ou vle a. Eg: <C:/Users/JRJC/Music/aaa.m4a>")
    h, mn = lh.split(":")
    ajiste_alam = f"{h}:{mn}"
    alarm(ajiste_alam)



def kite():
    time.sleep(1.2)
    sys.exit("BYE BYE !")


#---------------------------MAIN---------------------------


antre = aficheMeni()

if antre == 'R':
    redemare()
elif antre == 'F':
    femen()
elif antre == 'A':
    done_alam()
else:
    kite()
