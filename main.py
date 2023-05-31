from driver_web import WebControl
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys #鍵盤
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



# 圖片下載路徑
m_login = r'./image/m_login.jpg' #判斷w是否開啟的圖
magic_box = r'./image/magicbox.jpg' #百寶箱的圖
m_steel_channel = r'./image/m_steelchannel.jpg' #c槽
m_fileconverter_folder = r'./image/m_fileconvented.jpg'  #轉檔資料夾
m_download_file_folder = r'./image/m_downloadfile.jpg' #下載資料夾
m_olf_image = r'./image/m_olfimage.jpg' #olf 檔案的圖
select_allpage = r'./image/selectallpage.jpg' #選取所有頁面
checkmark = r'./image/m_checkmark.jpg' #點所選取所有頁面 會打勾 來判斷是否點到了選取頁面    
import_landscape = r'./image/importlandscape.jpg' #水平匯入檔案
magic_tool = r'./image/m_magic_tool.jpg' #百寶箱的工具欄 來判斷是否匯入完成
page_menagement_menu = r'./image/pagemanagementmenu.jpg' #頁面管理
delete_page= r'./image/deletepage.jpg' #刪除頁面
confirm_delete = r'./image/confirmyes.jpg' #確認刪除 是
page1 = r'./image/page1.jpg' #判斷是否刪除掉空白第一頁

#存檔路徑
file_manager = r'./image/file_manager.jpg' #文件管理
save_as_image = r'./image/saveas.jpg' #另存新檔
f_steel_channel = r'./image/f_steelchannel.jpg' #c槽

f_fileconverter_folder = r'./image/f_fileconverter.jpg' 
f_converted_file_folder = r'./image/f_convertedfile.jpg' #轉檔資料夾
rename_olf_file = r'./image/rename_olffile.jpg' #重新命名
f_confirm_save = r'./image/f_confirm_save.jpg' #輸入檔案名稱後的 能不能點擊確認存檔的勾
save_success = r'./image/save_success.jpg' #判斷 檔案是否存檔完成

#開啟失敗過的txt檔案
fail_fileslist = [] #用一個空列表存失敗的的檔案
with open('fail_files/failed_files.txt', 'r', encoding='utf-8') as file: #開啟後將資料丟入空的list中
    for i in file:
        fail_fileslist.append(i.replace("\n", ""))
print(fail_fileslist)
#登入流程 
wc.enter_target_page('https://worker.stage.myviewboard.cloud/')
wc.maximize_window()
wc.element_send_keys(wc.get_element('//input[@placeholder="帳號"]'),'DCC') #先抓到get elemet 而後send keys
wc.element_send_keys(wc.get_element('//input[@placeholder="密碼"]'),'DCC')
wc.element_send_keys(wc.get_element('//button[@type="button"]'),Keys.ENTER)
time.sleep(3)
currentPage = 1
#下載
# wc.element_click(wc.get_elements('//a[text()="原檔"]')[0])
isNextPage = True
while isNextPage:
    task_total = len(wc.get_elements('//tbody/tr')) #當前頁面有幾個任務
    print(task_total)
    for i in range(task_total):
        typeicon = wc.get_elements('//button[@label]//span')[i].text #狀態
        if typeicon != 'Review' and typeicon != 'Reject': #判斷狀態是不是Review
            currentTaskCreateTime = wc.get_element(f'//tbody/tr[{i+1}]/td[{2}]').text #建立時間
            currentFileName = wc.get_element(f'//tbody/tr[{i+1}]/td[{4}]').text #檔案名稱
            new_files_name = currentTaskCreateTime + currentFileName  #組成新的檔案
            if new_files_name in fail_fileslist:
                print('此檔案有出現在失敗的list中')
                continue
                
            wc.element_click(wc.get_elements('//a[text()="原檔"]')[i]) #下載的動作

            # cut_currentFileName = currentFileName.split('.')   #分開檔名跟副檔名
            # cut_currentFileName[1] = '.' + cut_currentFileName[1]     #用來判斷資料夾內是否有該副檔名

            da.dynamic_fileWait(f'./download_file/') 
            # print(currentTaskCreateTime.replace(":", "-"))
            # da.dynamic_fileWait(f'./download_file/{currentFileName}') #確定檔案是否下載完成 用名稱判斷
            new_name.rename_file(currentTaskCreateTime, currentFileName, './download_file/' ) #更改名稱
            newfilename = os.listdir('./download_file')[0]  #
            wc.minimize_window()    
            
            os.popen('C:\\Program Files\\ViewSonic\\vBoard\\vBoard.exe') #開啟白板
            da.dynamic_appearWait(m_login) #比對白板是否開啟

            #將檔案載入 whileboard
            move_to.appear_mouse_contorl(magic_box, m_login, 1) #百寶箱
        
            move_to.appear_mouse_contorl(m_steel_channel,magic_tool , 2)  #c槽 currentFileName

            move_to.appear_mouse_contorl(imagePath= m_fileconverter_folder, clicks= 2) #轉檔資料夾
            move_to.appear_mouse_contorl(imagePath = m_download_file_folder, clicks = 2) #下載檔案的資料夾
            move_to.appear_mouse_contorl(imagePath = m_olf_image, clicks = 2) #olf 圖檔
            move_to.appear_mouse_contorl(imagePath = select_allpage, clicks =1) #選取所有頁面
            move_to.appear_mouse_contorl(import_landscape,checkmark,1) # 當判斷選取所有頁面的勾出現後 水平匯入 
            move_to.disappear_mouse_contorl(page_menagement_menu,magic_tool,1) #當判斷水平匯入完成後 點擊頁面管理 他會顯示第二頁  
            move_to.appear_mouse_contorl(imagePath = delete_page,clicks = 1) #刪除第一頁
            move_to.appear_mouse_contorl(imagePath = confirm_delete, clicks= 1) #確認刪除

            #將檔案存成 olf

            # move_to.appear_mouse_contorl(imagePath = page1, clicks = 1)
            
            move_to.appear_mouse_contorl(imagePath = file_manager, clicks = 1) #點擊文件管理

            move_to.appear_mouse_contorl(save_as_image,save_success,1) #點擊另存新檔

            move_to.appear_mouse_contorl(imagePath = f_steel_channel, clicks = 2) #點擊c槽
            move_to.appear_mouse_contorl(imagePath = f_fileconverter_folder, clicks = 2) #點擊轉檔資料夾
            move_to.appear_mouse_contorl(imagePath = f_converted_file_folder, clicks = 2) #點擊存放olf轉檔的資料夾
            move_to.appear_mouse_contorl(imagePath = rename_olf_file, clicks = 1) #點擊重新命名框
            new_name.rename_olf(currentTaskCreateTime, currentFileName)#重新命名 貼上
            move_to.appear_mouse_contorl(imagePath = f_confirm_save, clicks = 1)    #確認存檔
            print('這邊是完成了點擊確認')
        #檢查存檔是否完成
            print(newfilename)
            da.dynamic_fileWait(f'./converted_file/') #存檔位置
            print("檔案已經存檔好了")
            os.system('TASKKILL /F /IM vBoard.exe /T') #關閉白板
            time.sleep(3)

            wc.maximize_window() #放大網頁
            wc.element_send_keys(wc.get_elements('//input[@type="file"]')[i], os.path.abspath('./converted_file/'+os.listdir('./converted_file/')[0])) #找到檔案資料夾內的檔案上傳
            da.dynamic_webWait(driver, '//button//span', i) #等待狀態改變

            #上傳檔案
            # wc.element_send_keys(wc.get_elements('//input[@placeholder="密碼"]'),'DCC')
            # print(wc.get_element(f'//tbody/tr[{i+1}]/td[{2}]').text)
            delete_file.delete_allfile('download_file') #刪除檔案 輸入資料夾名稱
            delete_file.delete_allfile('converted_file')

        elif typeicon == 'Review':
            print('狀態是Review')
            continue

    pageList = []
    
    # WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, f'//a[@tabindex][text()]')))
    pageElements = wc.get_elements( '//a[@tabindex][text()]') #頁數
    for i in range(len(pageElements)):
        pageList.append(pageElements[i].text) #把目前頁數丟到空列表

    if str(currentPage + 1) in pageList: #如果再pagelist內有該數字+1 做以下動作
        currentPage += 1 #此處頁數+1是因為頁數增加了
        wc.element_click(wc.get_elements('//a//span')[2]) #下一頁的index    
        time.sleep(2)
        # isNextPage = True
        print('點擊下一頁')
    else:
        isNextPage = False
        print('沒有下一頁了')
    
totalPage = currentPage #DCC帳號一共點擊幾頁
wc.close_webpage()

              # WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, f'//a[@tabindex][text()="{str(currentPage)}"]')))
            # wc.get_elements(f'//a[@tabindex][text()="{str(currentPage)}"]')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wc = WebControl(driver)
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#執行批准的流程
wc.enter_target_page('https://worker.stage.myviewboard.cloud/')
wc.maximize_window()
wc.element_send_keys(wc.get_element('//input[@placeholder="帳號"]'),'admin') #先抓到get elemet 而後send keys
wc.element_send_keys(wc.get_element('//input[@placeholder="密碼"]'),'12345')
wc.element_send_keys(wc.get_element('//button[@type="button"]'),Keys.ENTER)
time.sleep(3)

currentPage = 1
isNextPage = True
# review_total = len(wc.get_elements('//div/span[@class="ui-radiobutton-icon ui-clickable"]')) #當前頁面有幾個任務
# review_total = len(wc.get_elements('//p-radiobutton[@value="1"]')) 


# all_total = len(wc.get_elements('//tr/td')) #總共有幾格
task_total = len(wc.get_elements('//tbody/tr')) #當前頁面有幾個任務

while isNextPage:    
    if currentPage > totalPage:     #這邊是在DCC點擊多少頁 就會在admin 多點擊一頁
        break

   
    # review_total = len(wc.get_elements('//p-radiobutton[@value="1"]')) #當前頁面有幾個任務
    # print(review_total)
    
    for i in range(task_total):
        currentTaskCreateTime = wc.get_elements('//tbody/tr/td')[i*11+1].text #建立時間
        currentFileName = wc.get_elements('//tbody/tr/td')[i*11+3].text #檔案名稱
        new_files_name = currentTaskCreateTime + currentFileName
        print(new_files_name)
        if new_files_name not in fail_fileslist:  #如果檔案組成的新名稱不再fail內 下方用父子元素做才找的到
            print(i)
            # wc.element_click(wc.get_elements('//tr/td"]')[6*i])
            state = wc.get_elements('//tbody/tr/td')[i*11+4] #父元素 把網頁上的元素拆成一塊 共有110個項目 狀態的元素 判斷他是new review、progress
            print(wc.get_subElement(state, './button/span').text) #子元素
            if wc.get_subElement(state, './/button/span').text == "Review":
                print('進了')
                acceptBtn = wc.get_elements("//tbody/tr/td")[i*11+9] #父元素
                wc.element_click(wc.get_subElement(acceptBtn, './/div/span[@class="ui-radiobutton-icon ui-clickable"]')) #點擊批准 子元素
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