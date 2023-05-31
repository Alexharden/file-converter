import pyautogui, time, os
from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別

"網頁動態等待"
class DynamicControl:
    def dynamic_webWait(self, driver: webdriver.Chrome, path, index): #
        try:
            while driver.find_elements(By.XPATH, path)[index].text != 'Review': #上傳檔案 直到檔案完成上傳 狀態跳成Review 會重複執行此等待的圈
                time.sleep(1)
        except:
            raise
    def dynamic_lenfilewait(self,folderPath):
        try:
            while len(os.listdir(folderPath)) == 0:  # 檢查資料夾內的檔案列表長度是否為0
                time.sleep(1)
        except:
            raise
    # def dynamic_fileWait(self, filePath): #下載檔案 直到該資料夾內出現檔案
        
    #     try:
    #         while os.path.isfile(filePath) == False:
    #             time.sleep(1)
    #     except:
    #         raise
    def dynamic_fileWait(self, folderName): #比對附檔名
        while True:
            try:
                if '.notebook' in os.listdir(folderName)[0] or '.flipchart' in os.listdir(folderName)[0] or '.enb' in os.listdir(folderName)[0] or '.olf' in os.listdir(folderName)[0]:
                    break 
            except:
                continue
    def dynamic_appearWait(self, imagePath): #比對圖片是否出現
        try:
            while pyautogui.locateCenterOnScreen(imagePath, confidence= 0.9) == None:
                time.sleep(1)
        except:
            raise            
    
    def dynamic_disappearWait(self, imagePath): #比對圖片是否消失
        try:
            while pyautogui.locateCenterOnScreen(imagePath, confidence= 0.9) != None:
                time.sleep(1)
        except:
            raise
# DC = DynamicControl()
# DC.Dynamic_AppearWait("")