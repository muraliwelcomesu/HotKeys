from pynput import keyboard
import os
import send2trash
import numpy as np 
import cv2 
import pyautogui 
import Debug_Voice as dbg
import time,sys

KEY_START = keyboard.Key.f2
KEY_PROCESS = keyboard.Key.print_screen
KEY_END   = keyboard.Key.f3

    
def  execute_end():
    print('execute end')
    if  os.path.exists('D:\\HotKeys\\start.txt'):
        send2trash.send2trash('D:\\HotKeys\\start.txt')
    dbg.PlayResponse('HotKey Complete.Files are available at D:\HotKeys Folder. Thank you.')
    
def  execute_start():
    print('execute start')
    dbg.PlayResponse('HotKey Program Started')
    dbg.PlayResponse('Press print screen to take screen shots')
    dbg.PlayResponse('Press F3 to Quit Program')
    if not os.path.exists('D:\\HotKeys\\start.txt'):
        fp = open("D:\HotKeys\\start.txt",'w')
        fp.write('F2 to start Program')
        fp.write('print_screen to take screen shots')
        fp.write('F3 to End Program')
        fp.close()

def  execute_process():
    print('execute process')
    if  os.path.exists('D:\\HotKeys\\start.txt'):
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        l_no = len([x for x in os.listdir('D:\\HotKeys') if x.endswith('.png')]) + 1 
        file_name = 'D:\\HotKeys\\image_{}.png'.format(l_no) 
        cv2.imwrite(file_name, image)  
        dbg.beep() 
            
def on_press(key):
    print('inside key press {}'.format(key))
    if key == KEY_START:
        execute_start()
    elif key == KEY_END:
        execute_end()
        return False
    elif key == KEY_PROCESS:
        execute_process()

dbg.PlayResponse('Press F2 to Start')

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()
    
''' related articles 
https://stackoverflow.com/questions/55742069/how-to-click-hotkey-and-simultaneously-type-a-string
https://buildmedia.readthedocs.org/media/pdf/pynput/latest/pynput.pdf
https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
https://www.youtube.com/watch?v=Cuyu3VU0yD4 - socket shtdwn
https://www.youtube.com/watch?v=3QiPPX-KeSc - socket
'''