import os
import time
import pyautogui
import pyperclip
import re
class DownloadRename:
    def rename_file(self, create_time,file_name, folderName): #改名
        try:
            new_file_name = create_time.replace(':', '-')+' '+file_name #刪除會影響判斷的符號改成:        
            os.rename(folderName + os.listdir(folderName)[0], f'./download_file/{new_file_name}')
            # create_time + file_name
            # new_file_name = test1 + ' '+ files_name 
        except:
            raise
    def delete_allfile(self, deletelocation):  #刪除檔案
        for delete_file in os.listdir(deletelocation):
            try:
                os.remove(os.path.join(deletelocation, delete_file)) #移除兩個資料夾內的檔案
            except PermissionError: #如果跳錯誤 等待三秒後再刪除一次檔案
                time.sleep(3)
                os.remove(os.path.join(deletelocation, delete_file)) 
                
    def rename_olf(slef, create_time, file_name): #複製檔名
        try:
            new_file_name = create_time.replace(':', '-')+' '+file_name
            pyperclip.copy(new_file_name)
            time.sleep(1)
            pyautogui.hotkey('ctrl','v')
            time.sleep(2)
        except:
            raise