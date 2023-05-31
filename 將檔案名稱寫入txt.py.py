# from driver_web import WebControl
# from selenium import webdriver
# import os
# from selenium.webdriver.common.keys import Keys #鍵盤
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from driver_dynamic import DynamicControl
# from driver_filemanager import DownloadRename 
# from driver_whiteboard import FileConverter_Olf
# from driver_web import WebControl
# import pyautogui , pyperclip  ,re

# prefs = {'download.default_directory': os.path.abspath('download_file')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
# options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
# options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

# #上傳檔案的路徑
# # folder_path = 'C:\\Users\\HsiehHa\Desktop\\File Converter\\converted_file'
# # upload_file_folder = os.listdir(folder_path)[0]
# # file_path = os.path.join(folder_path, upload_file_folder)

# #建立一個Chrome瀏覽器的WebDriver物件driver，並傳入ChromeDriverManager().install()的值作為ChromeDriver的路徑，以及上面設定好的選項options。
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# #呼叫
# wc = WebControl(driver)
# # df = DynamicControl()
# new_name = DownloadRename()
# delete_file = DownloadRename()
# da = DynamicControl()
# move_to=FileConverter_Olf()






# #登入流程 
# wc.enter_target_page('https://worker.stage.myviewboard.cloud/')
# wc.maximize_window()
# wc.element_send_keys(wc.get_element('//input[@placeholder="帳號"]'),'DCC') #先抓到get elemet 而後send keys
# wc.element_send_keys(wc.get_element('//input[@placeholder="密碼"]'),'DCC')
# wc.element_send_keys(wc.get_element('//button[@type="button"]'),Keys.ENTER)
# time.sleep(3)
# currentPage = 1
# newfilesnamelist = []
# isNextPage = True
# while isNextPage:
#     task_total = len(wc.get_elements('//tbody/tr')) #當前頁面有幾個任務
#     print(task_total)
#     for i in range(task_total):
#         currentTaskCreateTime = wc.get_element(f'//tbody/tr[{i+1}]/td[{2}]').text #建立時間
#         currentFileName = wc.get_element(f'//tbody/tr[{i+1}]/td[{4}]').text #檔案名稱
#         newfilesname = currentTaskCreateTime + '' + currentFileName
#         newfilesnamelist.append(newfilesname)
#         fail_name = "fails.txt"




#     # 迴圈結束，程式執行完成
#     print("檔案已成功儲存。")

#     pageList = []
    
#     # WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, f'//a[@tabindex][text()]')))
#     pageElements = wc.get_elements( '//a[@tabindex][text()]')
#     for i in range(len(pageElements)):
#         pageList.append(pageElements[i].text)

#     if str(currentPage + 1) in pageList:
#         currentPage += 1
#         wc.element_click(wc.get_elements('//a//span')[2]) #下一頁的index    
#         time.sleep(2)
#         # isNextPage = True
#         print('點擊下一頁')
#     else:
#         isNextPage = False
#         print('沒有下一頁了')

# with open(fail_name, "a", encoding="utf-8") as file:

#     for newfile in newfilesnamelist:
#         file.write(newfile + "\n")