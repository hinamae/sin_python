from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#引数でメールとパスワード指定できるようになりたいな

class Yoyaku:
    def login(e,p,driver):
        url = 'https://beauty.hotpepper.jp/slnH000313094/'
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
        #xpathで指定
        driver.find_element_by_xpath('//*[@id="myMenuBottom"]/dl/dd[1]/div/div/ul/li/div[1]/a').click()
        # ユーザIDとパスワードを入力
        userid_textbox = driver.find_element_by_id('mainEmail')
        userid_textbox.send_keys(e)
        password_textbox = driver.find_element_by_id('passwordText')
        password_textbox.send_keys(p)

        login_btn = driver.find_element_by_class_name('button_01')
        login_btn.click()

    def yoyaku(driver):
        #サロンのXパス
        driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div/ol/li/p[2]/a').click()
        #コースのXパス
        driver.find_element_by_xpath('//*[@id="contents"]/div[1]/div[2]/div/div/div/div/ul/li/div/div/div/div/div[2]/div[3]/div[2]/div/div/div/div[1]/p[3]/a').click()
        #日付のXパス
        driver.find_element_by_xpath('//*[@id="jsRsvCdTbl"]/table/tbody/tr[3]/th[7]/table/tbody/tr[12]/td/a').click()
        #チェックボックス
        driver.find_element_by_id('forRsvStoreConfirmAnswer').click()
        #
        driver.find_element_by_id('jsiMoreDetailRequestInput').click()
        driver.find_element_by_id('forEverydayStyling').click()
        driver.find_element_by_id('notCareService').click()
        message = "技術重視"
        driver.find_element_by_id('rsvDemandAskDetail').send_keys(message)

        driver.find_element_by_xpath('//*[@id="bt_reserveActionForm"]/div[6]/div/input').click()

    def kakutei(driver):
        driver.find_element_by_id('doComplete').click()

    driver_path=webdriver.Chrome('./chromedriver')    
    mail=""
    password=""

    login(mail,password,driver_path)
    yoyaku(driver_path)
    kakutei(driver_path)
#driver.close()