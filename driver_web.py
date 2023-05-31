from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.ui import WebDriverWait
import os, time, glob, shutil, pyperclip, pyautogui
from selenium.webdriver.support import expected_conditions as EC
# from PIL import Image


class WebControl(): #python v3.11.x selenium 4.8.x
    
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver 
 


    """呼叫此函式需可最大化當前控制的瀏覽器"""
    def maximize_window(self):
        self.driver.maximize_window()
        
    """呼叫此函式需可最小化當前控制的瀏覽器"""
    def minimize_window(self):
        self.driver.minimize_window()

    """呼叫此函式可以將視窗移到所需的位置"""
    def move_window(self, x, y):
        self.driver.set_window_position(x, y)

    """呼叫此函式並於參數位置放入URL，連結至目標網頁"""
    def enter_target_page(self, url):
        self.driver.get(url)
        self.all_page_wait()
    
    """呼叫此函式可以關閉當前控制的瀏覽器"""
    def close_webpage(self):
        self.driver.close()
    
    """呼叫此函式需可重整當前控制的瀏覽器"""
    def reload_webpage(self):
        self.driver.refresh()
        self.all_page_wait()
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件"""
    def get_element(self, element):
        try:
            self.element_wait(element, 5)
            return self.driver.find_element(By.XPATH, element)
        except:
            raise
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件列表，並給定另一參數指定要從
    列表中取第幾個index的元件"""
    def get_elements(self, elements):
        try:
            self.elements_wait(elements, 5)
            return self.driver.find_elements(By.XPATH, elements)
        except :
            return False

    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件
    做點擊的動作"""
    def element_click(self, getElement: get_element or get_elements):
        try:
            getElement.click()
        except:
            raise
    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件
    做輸入的動作，並給定另一參數指定可以輸入什麼"""
    def element_send_keys(self, getElement: get_element or get_elements, content=''):
        try:
            getElement.send_keys(content)
        except:
            raise
    
    """呼叫此函式並從參數代入欲定位的元件要等待多久時間載入"""
    def element_wait(self, element, time: int):
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, element))) #等待直到until內的元素可以被點擊為止

            # logging.error(msg= "Time Out! Cannot locate the eleement. 時間到！無法定位到該元件。\n", exc_info= True)


    """呼叫此函式並從參數代入欲定位的元件列表要等待多久時間載入"""
    def elements_wait(self,  elements, time: int):

            WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH, elements)))#等待直到until內的條件元素都被定位到且可見時停止

    """等待整個頁面載入完畢"""
    def all_page_wait(self):
            self.driver.implicitly_wait(30)


    def get_subElement(self, subdriver:webdriver.Chrome, element):
        try:
            return subdriver.find_element(By.XPATH, element)
        except:
            raise