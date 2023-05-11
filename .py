from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.ui import WebDriverWait
import os, time, glob, shutil, pyperclip, pyautogui
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


prefs = {'download.default_directory': os.path.abspath('file_download')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址


driver.maximize_window() #視窗最大化
driver.minimize_window() #視窗最小化

account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)

WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@label]')))
WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//button[@label]')))

#下載檔案
create_time = all_elements[i+1].text #建立時間的element
files_name = all_elements[i+3].text #檔案名稱的element
test1 = create_time.replace(':', '-')  # 處理字串
new_file_name = test1 + ' '+ files_name
print(f'下載 {new_file_name}')

while os.path.isfile(f'./file_download/{files_name}') == False: #動態檢查下載是否完成
    time.sleep(1)

#修改檔名
filename = glob.glob(os.path.join(os.path.abspath('file_download'), '*'))[0]
os.rename(filename, os.path.join(os.path.abspath('file_download'), new_file_name))
while os.path.isfile(f'./file_download/{new_file_name}') == False: #動態檢查檔案是否改名完成
    time.sleep(1)


#上傳檔案
folder_path = 'C:\\Users\\HsiehHa\Desktop\\Selenium\\converted_file'
upload_file_folder = os.listdir(folder_path)[0]
file_path = os.path.join(folder_path, upload_file_folder)


WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="file"]')))
upload_file = driver.find_elements(By.XPATH, '//input[@type="file"]')[i//9] #按照順序往下上傳 跟著本來的迴圈
upload_file.send_keys(file_path)
while driver.find_elements(By.XPATH, '//button[@label]')[i//9].text != 'Review':
    time.sleep(1) #轉檔頁面上的檔案狀態




#刪除檔案
for deletefile_download in os.listdir('file_download'): 
    try:
        os.remove(os.path.join('file_download', deletefile_download))
    except PermissionError:
    # 如果刪除失敗，可能是因為檔案正在被其他程序使用中
    # 等待一段時間，讓其他程序釋放對檔案的使用權     
        time.sleep(2)
        os.remove(os.path.join('converted_file', deletefile_download))

for deleteconverted_file in os.listdir('converted_file'):
    try:
        os.remove(os.path.join('converted_file', deleteconverted_file))
    except PermissionError:
    # 如果刪除失敗，可能是因為檔案正在被其他程序使用中
    # 等待一段時間，讓其他程序釋放對檔案的使用權            
        time.sleep(2)
        os.remove(os.path.join('converted_file', deleteconverted_file))