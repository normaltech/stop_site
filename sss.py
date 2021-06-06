from selenium import webdriver
import chromedriver_autoinstaller
import time
from run_sel import run_selenium

import sys
stop_screen = "https://yt3.ggpht.com/ytc/AAUvwniNREN3_CmwuOG9cm18p57QPow_wgyq_7JO65On=s900-c-k-c0x00ffffff-no-rj"

def start_selenium1(list_1):
    print("변수확인",run_selenium)
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
    driver.get("https://blackboard.sejong.ac.kr/?new_loc=%2Fultra%2Fcourse")
    driver.implicitly_wait(10)
    num = 0
    while run_selenium:
        num = stop_function(driver,list_1,num)
    
def stop_function(driver,list_1,num):
    
    try:
        if len(driver.window_handles) != num:
            driver.switch_to.window(driver.window_handles[-1])
            target = driver.current_url +"\n"
            if target in list_1:
                driver.get("https://yt3.ggpht.com/ytc/AAUvwniNREN3_CmwuOG9cm18p57QPow_wgyq_7JO65On=s900-c-k-c0x00ffffff-no-rj")
                time.sleep(5)
                driver.quit()
        elif len(driver.window_handles) == 1:
            target = driver.current_url +"\n"
            if target in list_1:
                driver.get("https://yt3.ggpht.com/ytc/AAUvwniNREN3_CmwuOG9cm18p57QPow_wgyq_7JO65On=s900-c-k-c0x00ffffff-no-rj")
                time.sleep(5)
                driver.quit()

    except:
        pass
    return num