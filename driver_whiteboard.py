import os
import pyautogui
import time
from driver_dynamic import DynamicControl

class FileConverter_Olf:
    def __init__(self):
        self.da = DynamicControl()
    def appear_mouse_contorl(self, imagePath, recogImagePath = '', clicks = 1):
        try:
            pyautogui.moveTo(10, 10) #滑鼠移動位置
            time.sleep(1)
            if recogImagePath == "":   #配對目標和實際目標相同時 設為空字串
                recogImagePath = imagePath  #配對目標 =實際目標
            self.da.dynamic_appearWait(recogImagePath) #配對目標 出現 使用等待方法
            self.da.dynamic_appearWait(imagePath) #實際目標 #使用等待方法

            x, y= pyautogui.locateCenterOnScreen(imagePath, confidence=0.9)  #圖片識別取得中心位置
            pyautogui.moveTo(x, y, duration=0.1) #移動到中心位置座標 花費0.1秒  
            time.sleep(1)
            if clicks == 1: #看參數數入幾點擊1次或2次
                pyautogui.click()
            elif clicks == 2:
                pyautogui.doubleClick()
            time.sleep(1)
        except Exception as e: #error code
         print("An error occurred:", str(e))


    def disappear_mouse_contorl(self, imagePath, recogImagePath = '', clicks= 1):
        try:
            pyautogui.moveTo(10, 10)
            if recogImagePath == '':
                recogImagePath = imagePath
            self.da.dynamic_disappearWait(recogImagePath) #配對目標 消失

            self.da.dynamic_appearWait(imagePath) #實際目標

            x, y= pyautogui.locateCenterOnScreen(imagePath, confidence=0.9)
            pyautogui.moveTo(x, y, duration=0.1)
            time.sleep(1)
            if clicks == 1:
                pyautogui.click()
            elif clicks == 2:
                pyautogui.doubleClick()
            time.sleep(1)
        except Exception as e:
            print("An error occurred:", str(e))
        