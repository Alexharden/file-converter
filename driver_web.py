from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.ui import WebDriverWait
import os, time, glob, shutil, pyperclip, pyautogui
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


class WebControl:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
    def element_get(self, elementPath):
        WebDriverWait(self.driver, 10, 1.0).until(EC.element_to_be_clickable((By.XPATH, elementPath)))
        return self.driver.find_element(By.XPATH, elementPath)
    def elements_get(self, elementPath):
        WebDriverWait(self.driver, 10, 1.0).until(EC.presence_of_all_elements_located((By.XPATH, elementPath)))
        return self.driver.find_elements(By.XPATH, elementPath)
    def element_sendKey(self, element, content):
        element.send_keys(content)
    def element_click(self, element):
        element.click()
    def enter_webpage(self, url):
        self.driver.get(url)

class SignInFlow:
    def __init__(self):
        wc = WebControl()
        wc.element_sendKey(wc.element_get("//input[@placeholder='帳號']"), "DCC")
        wc.element_click(wc.element_get('//button[@type="button"]'))

if __name__ == "__main__":
    SignInFlow()