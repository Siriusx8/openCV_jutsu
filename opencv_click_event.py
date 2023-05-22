import time
import os
import pyautogui
import cv2
import numpy as np
#pyautogui.screenshot().save(r'C:\geeksforgeeks.png')
#screenshot = r'C:\geeksforgeeks.png'
# Using cv2.imshow() method 
# Displaying the image
ancor_hh = r'C:\Users\Black\Pictures\NEXT_BOTTOM.png'
ancor_hh_2 = r'C:\Users\Black\Pictures\NEXT_BOTTOM_2.png'
#cv2.imshow("screenshot", frame)
#cv2.imshow("screenshot", cv2.imread(ancor_hh))
#cv2.imshow("screenshot", cv2.imread(screenshot))
flag = 0
while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        time.sleep(4)
        
        if flag == 0:
                print(flag)
                img_rgb = frame 
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                template = cv2.imread(ancor_hh,0)
                w, h = template.shape[::-1]
                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where( res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                    #print("pt[0] {} + w {}, pt[1] {} + h {} " .format(pt[0],w, pt[1],h))
                    click_hh = (pt[0],pt[1])
                    pyautogui.click(click_hh[0]+10, click_hh[1]+10)
                    pyautogui.press('ctrl')
                    flag = 2
                    print('click ,пропустить заставку')
        elif flag == 2:
                print(flag, )
                img_rgb = frame 
                img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                template = cv2.imread(ancor_hh_2,0)
                w, h = template.shape[::-1]
                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where( res >= threshold)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                    #print("pt[0] {} + w {}, pt[1] {} + h {} " .format(pt[0],w, pt[1],h))
                    click_hh = (pt[0],pt[1])
                    pyautogui.click(click_hh[0]+10, click_hh[1]+10)
                    pyautogui.press('ctrl')
                    flag = 0
                    print('click Следующая серия')
                    #time.sleep(12)
                    time.sleep(4)
                    pyautogui.click(790, 900)
                    time.sleep(1)
                    pyautogui.click(clicks=2, interval=0.45)
        else:
            print('нет кнопки, ждем 5 сек')
            
cv2.waitKey(0) 
cv2.destroyAllWindows()

