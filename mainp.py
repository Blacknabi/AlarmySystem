#coding : UTF-8


import os, sys, platform
import time, datetime
from turtle import color
import schedule, playsound

os.system('color e')
# os.system('title Alarmy System ')
def kite():
    time.sleep(1.2)
    sys.exit("BYE BYE !")


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
    while not antre.upper() in lisAntre:
        print('SVP FE YON BON CHWA. CHWAZI YON OPSYON ')
        antre = input("::>>> ")
    return antre
   

def redemare():
    print('|----------------------------------------------------|')
    print('|           ::: PWOGRAME YON REDEMARAJ :::           |')
    print('|----------------------------------------------------|')
    ss = input("Antre nan konbyen segonn poun redemare. Eg: <34> : ")
    while not ss.isdigit():
        ss = input("Antre nan konbyen segonn poun redemare. Eg: <34> : ") 
    try:
        if platform.system()=='Windows':
            print(f'Machin ou an pral femen nan {ss} segonn.')
            os.system(f"shutdown /r /t {ss}")
        elif  platform.system() == 'Linux':
            print(f'Machin ou an pral femen nan {ss} segonn.')
            try:
                os.system(f"sudo reboot {ss}")
            except:
                os.system("color c")
                os.system(f"sudo reboot")
    except:
        os.system("color c")
        print("Dezole. Pwosesis redemaraj la echwe.")
   
    
    
def femen():
    print('|----------------------------------------------------|')
    print('|         ::: PWOGRAME YON ARE OTAMATIK :::          |')
    print('|----------------------------------------------------|')
    ss = input("Antre nan konbyen segonn femen. Eg: <34> : ")
    while not ss.isdigit():
        ss = input("Antre nan konbyen segonn poun redemare. Eg: <34> : ") 
    try:
        if platform.system()=='Windows':
            print(f'Machin ou an pral femen nan {ss} segonn.')
            os.system(f"shutdown /s /t {ss}")
        elif  platform.system() == 'Linux':
            print(f'Machin ou an pral femen nan {ss} segonn.')
            try:
                os.system(f"sudo shutdown {ss}")
            except:
                os.system("color c")
                os.system(f"sudo shutdown now")
    except:
        os.system("color c")
        print("Dezole. Pwosesis are otomatik la echwe.")
     
                   
def alarm(ajiste_alam):
    while True:
        time.sleep(1.2)
        lh_kounyea = datetime.datetime.now()
        kounya = lh_kounyea.strftime("%H:%M")
        dat = lh_kounyea.strftime("%d/%m/%Y")
        print(f"{dat}")
        print(f"- - - - - {kounya} - - - - - ")
        if kounya == ajiste_alam:
            try:
                os.system('color a')
                print("Alam lanse...")
                # playsound.playsound(son)
                break
            except:
                os.system('color c')
                print("Alam nan pa rive lanse !")
                break



def done_alam():
    global h, mn, son
    print('|----------------------------------------------------|')
    print('|              ::: PWOGRAME YON ALAM :::             |')
    print('|----------------------------------------------------|')
    print("|                    Itilize foma  24H               |")
    print('|----------------------------------------------------|')
    lh = input("Tape lh a : ")
    while not lh.isdigit():
        lh = input("Retape lh a : ") 
    try:
        lh = int(lh)
        while lh<0 or lh>23:
            lh = input("Retape lh a : ")
            lh = int(lh)
    except:
        os.system("color c")
        print('Dezole. Foma lh a pa bon.')
    
    mn = input("Tape minit la : ")
    while not mn.isdigit():
        mn = input("Retape minit a : ")  
    try:
        mn = int(mn)
        while mn<0 or mn>59:
            mn = input("Retape minit a : ")
            mn = int(mn)
    except:
        os.system("color c")
        print('Dezole. Foma minit a pa bon.')
    time.sleep(0.9)
    print(f"Ou pwograme yon alam pou {lh} : {mn} ")
    
    son = input("Antre chemen son alam nan. Eg: <C:/Users/JRJC/Music/aaa.m4a>")
    
    ajiste_alam = f"{lh}:{mn}"
    alarm(ajiste_alam)





#---------------------------MAIN---------------------------


antre = aficheMeni()

if antre == 'R' or antre == 'r':
    redemare()
elif antre == 'F' or antre == 'f':
    femen()
elif antre == 'A' or antre == 'a':
    done_alam()
else:
    kite()
