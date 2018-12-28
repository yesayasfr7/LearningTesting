from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class TestKumparan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.base_url = "https://www.kumparan.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
    def testUserSeeNews(self):
        driver = self.driver
        #-- Getting into facebook website --#
        driver.get("https://www.kumparan.com")
        time.sleep(5)
        #-- Turn Off Notifications --##
        driver.find_element_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click()
        time.sleep(3)
        #-- Login Google Plus --##
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/nav/div/div[2]/div[3]/div/button/span/div/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/button/span/span').click()
        time.sleep(5)
        parent_window_handle = driver.current_window_handle
        masuk_window_handles = driver.window_handles
        driver.switch_to.window(masuk_window_handles[1])
        time.sleep(5)
        ##-- ini kalau sudah ada akun yang terdaftar di browser --##
        #driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div/div/form/content/section/div/content/div/div/ul/li[7]/div').click()
        #time.sleep(5)
        ##-- Batasnya sampai sini --##
        driver.find_element_by_xpath('//*[@id="identifierId"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("yesayas.napitu@gmail.com")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Y3$4y4s78")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
        time.sleep(5)
        ##-- Kode dibawah digunakan untuk user yang baru pertama kali akses kumparan --##
        ##driver.find_element_by_xpath('//*[@id="submit_approve_access"]/content/span').click()
        ##-- Batasnya disini --##
        driver.switch_to.window(parent_window_handle)
        time.sleep(5)
        #-- Search News --#
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/nav/div/div[1]/div[3]/div/div/div/div/div[1]/input').click()
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/nav/div/div[1]/div[3]/div/div/div/div/div[1]/input').clear()
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/nav/div/div[1]/div[3]/div/div/div/div/div[1]/input').send_keys("Eureka")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/nav/div/div[1]/div[3]/div/div/div/div/div[2]/div/button/span/div/span').click() 
        time.sleep(5)
        #--Mengklik salah satu berita dengan menggunakan fitur search--#
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div/div/div[1]/div/a/div[1]/div').click()
        time.sleep(5)
        #-- Melakukan Like pada Berita --##
        driver.execute_script('window.scrollTo(0,1800);')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[6]/div/div[1]/div/button/span/span').click()
        time.sleep(5) 
        #-- Melakukan Comment pada Berita karena tidak ada fitur share pada google --##
        driver.find_element_by_class_name("public-DraftStyleDefault-block").click()
        time.sleep(5)
        driver.execute_script("document.getElementsByClassName('public-DraftStyleDefault-block')[0].value='Komeng Dulu Gan'")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/a/span/div/div/img').click()
        time.sleep(10)






def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()