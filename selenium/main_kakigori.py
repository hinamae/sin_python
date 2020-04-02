from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Kentei:
    def load(driver):
        url = 'http://kakigoori.or.jp/'
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
        # driver.find_element_by_xpath('//*[@id="myMenuBottom"]/dl/dd[1]/div/div/ul/li/div[1]/a').click()
        #xpathで指定
    def kentei_select():
        while True:
            print("どの検定を受けますか")
            print("1:初級")
            print("2:中級")
            print("3:上級")
            input_line1 = input()
        
            if input_line1 == "1":
                print("初級の検定を始めます")
                return 1
            elif input_line1 == "2":
                print("中級の検定を始めます")
                return 2
            elif input_line1 == "3":
                print("上級の検定を始めます")
                return 3
            else:
                print("1,2,3のどれかを入力してください")
    def kentei_start(driver,mode):
        
        if mode == 1:
            # 初級セレクタ
            mode_s="easy"
        elif mode == 2:
            # 中級セレクタ
            mode_s="normal"
        elif mode == 3:
            # 上級セレクタ
            mode_s="hard"
        driver.find_element_by_css_selector("#kenteiAnc > div > div.kentei-content > div.kentei.%s > div.button > a" %mode_s).click()
    
    def analisis(driver,mode):
        if  mode == 1:
            # 初級セレクタ
            mode_s="easy"
        elif mode == 2:
            # 中級セレクタ
            mode_s="normal"
        elif mode == 3:
            # 上級セレクタ
            mode_s="hard"

        for num_q in range(1,9):
            

            answer_num=2
            print(num_q)
            #1問目
            ##A1z
            text = "#kentei{0} > fieldset > div:nth-child({1}) > div > div > div > div > div > label:nth-child({2})"
            css_selector = text.format(mode_s, num_q, answer_num)
            driver.find_element_by_css_selector(css_selector).click()
            # driver.find_element_by_css_selector("#kenteieasy > fieldset > div:nth-child(%s) > div > div > div > div > div > label:nth-child(2)" %num_q).click()
            ##A2
            #kenteieasy > fieldset > div:nth-child(1) > div > div > div > div > div > label:nth-child(4)
            ##A3
            #kenteieasy > fieldset > div:nth-child(1) > div > div > div > div > div > label:nth-child(6)
        
            #2問目
            ##A1
            #kenteieasy > fieldset > div:nth-child(2) > div > div > div > div > div > label:nth-child(2)
    

    driver_path=webdriver.Chrome('./chromedriver')
    load(driver_path)
    mode = kentei_select()
    kentei_start(driver_path,mode)
    analisis(driver_path,mode)
    # driver_path.close()

