from PIL import ImageGrab, Image
import keyboard
import pyautogui
import time
import random
from pynput import mouse

cor = ["",""]
i = 0
hmir = 0

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
        global cor
        cor = pyautogui.position()
        return False # Returning False if you need to stop the program when Left clicked.

def rangen(x,r):
    f = x - r
    l = x + r
    ran = random.uniform(f,l)
    return (ran)

#click checking
while (True):
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    check = listener.join()
    if (check != True):
        break


while (True):
    time.sleep(rangen(10.2,1))

    xc = rangen(cor[0], 10)
    yc = rangen(cor[1], 10)
    pyautogui.moveTo(xc, yc, rangen(0.4,0.1), pyautogui.easeInOutQuad)
    pyautogui.click()
    
    time.sleep(rangen(1,0.3))
    keyboard.press_and_release("e")
    time.sleep(rangen(1,0.3))
    while (True) :
        hmir += 1
        for y in range(486, 492, 1):
            for x in range(958, 962, 1):
                px = ImageGrab.grab().load()
                color = px[x, y]
                strcolor = str(color)
                RGB = strcolor.split (", ")
                R = RGB[0].replace("(","")
                G = RGB[1]
                B = RGB[2].replace(")","")
                white = int(R) + int(G) + int(B)
                test = int(R) - 234
                if white <= 690:
                    if hmir >=25:
                        print(white)
                        break
                    if test >= 10:
                        print("/n-------------",R ,"-------", test,"---------------/n")
                        keyboard.press_and_release("e")
                        break
                print(x , " - " , y , " - " , color)
            if white <= 690:
                if hmir >=25:
                    print(white)
                    break
                if test >= 10:
                    print("/n-------------",R ,"-------", test,"---------------/n")
                    keyboard.press_and_release("e")
                    break
        if test >= 10 or hmir >= 25:
            if hmir >= 25:
                print("faild!!!!!!")
                hmir = 0
                break
            else:
                if white < 690:
                    hmir = 0
                    i += 1
                    print("amount of success : ", i)
                    break

