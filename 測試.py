from driver_web import WebControl
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from driver_dynamic import DynamicControl
from driver_filemanager import DownloadRename 
from driver_whiteboard import FileConverter_Olf
from driver_web import WebControl
import pyautogui , pyperclip  ,re

prefs = {'download.default_directory': os.path.abspath('download_file')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

#上傳檔案的路徑
# folder_path = 'C:\\Users\\HsiehHa\Desktop\\File Converter\\converted_file'
# upload_file_folder = os.listdir(folder_path)[0]
# file_path = os.path.join(folder_path, upload_file_folder)

#建立一個Chrome瀏覽器的WebDriver物件driver，並傳入ChromeDriverManager().install()的值作為ChromeDriver的路徑，以及上面設定好的選項options。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#呼叫
wc = WebControl(driver)
# df = DynamicControl()
new_name = DownloadRename()
delete_file = DownloadRename()
da = DynamicControl()
move_to=FileConverter_Olf()

#開啟失敗過的txt檔案
fail_fileslist = [] #用一個空列表存失敗的的檔案
with open('fail_files/failed_files.txt', 'r', encoding='utf-8') as file: #開啟後將資料丟入空的list中
    for i in file:
        fail_fileslist.append(i.replace("\n", ""))
# print(fail_fileslist)
#登入流程 
wc.enter_target_page('https://worker.stage.myviewboard.cloud/')
wc.maximize_window()
wc.element_send_keys(wc.get_element('//input[@placeholder="帳號"]'),'admin') #先抓到get elemet 而後send keys
wc.element_send_keys(wc.get_element('//input[@placeholder="密碼"]'),'12345')
wc.element_send_keys(wc.get_element('//button[@type="button"]'),Keys.ENTER)
time.sleep(3)
currentPage = 1


# all_total = len(wc.get_elements('//tr/td')) #總共有幾格
# task_total = len(wc.get_elements('//tbody/tr')) #當前頁面有幾個任務
# print(all_total)
# print(task_total)

# wc.element_click


# for i in range(0,task_total):
#     currentTaskCreateTime = wc.get_element(f'//tbody/tr[{i+1}]/td[{2}]').text #建立時間
#     currentFileName = wc.get_element(f'//tbody/tr[{i+1}]/td[{4}]').text #檔案名稱
#     new_files_name = currentTaskCreateTime + currentFileName 
#     button = wc.element_click(wc.get_element(f'//tbody/tr[{i+1}]/td[{10}]').text)
#     # all_total = len(wc.get_elements('//tr/td')) #總共有幾格
   
#     print(f'這是數量{button}')
    # if new_files_name not in fail_fileslist:
    #     button = wc.element_click(wc.get_elements('//tr/td"]')[6+i*9].text)
    #     print(button)
    #     # wc.element_click(wc.get_elements('//div/span[@class="ui-radiobutton-icon ui-clickable"]')[i]) #點擊批准
    #     time.sleep(1.5)
    # else:
    #     i +1
    #     print('此檔案有出現在失敗的list中')
currentPage = 1
isNextPage = True
# review_total = len(wc.get_elements('//div/span[@class="ui-radiobutton-icon ui-clickable"]')) #當前頁面有幾個任務
# review_total = len(wc.get_elements('//p-radiobutton[@value="1"]')) 
# all_total = len(wc.get_elements('//tr/td')) #總共有幾格
task_total = len(wc.get_elements('//tbody/tr')) #當前頁面有幾個任務
while isNextPage:    

    # review_total = len(wc.get_elements('//p-radiobutton[@value="1"]')) #當前頁面有幾個任務
    # print(review_total)
    
    for i in range(task_total):
        currentTaskCreateTime = wc.get_elements('//tbody/tr/td')[i*11+1].text #建立時間
        currentFileName = wc.get_elements('//tbody/tr/td')[i*11+3].text #檔案名稱
        new_files_name = currentTaskCreateTime + currentFileName
        print(new_files_name)
        if new_files_name not in fail_fileslist:
            print(i)
            # wc.element_click(wc.get_elements('//tr/td"]')[6*i])
            state = wc.get_elements('//tbody/tr/td')[i*11+4]
            print(wc.get_subElement(state, './button/span').text)
            if wc.get_subElement(state, './/button/span').text == "Review":
                print('進了')
                acceptBtn = wc.get_elements("//tbody/tr/td")[i*11+9]
                wc.element_click(wc.get_subElement(acceptBtn, './/div/span[@class="ui-radiobutton-icon ui-clickable"]')) #點擊批准
                time.sleep(5)
        else:
            continue

    pageList = []
    
    # WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, f'//a[@tabindex][text()]')))
    pageElements = wc.get_elements( '//a[@tabindex][text()]')
    for i in range(len(pageElements)):
        pageList.append(pageElements[i].text)

    if str(currentPage + 1) in pageList:
        currentPage += 1
        wc.element_click(wc.get_elements('//a//span')[2]) #下一頁的index    
        time.sleep(2)
        # isNextPage = True
        print('點擊下一頁')

    else: #
        isNextPage = False
        print('沒有下一頁了')


wc.close_webpage()