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
        ##--Bug pada tombol like facebook Klik Like untuk salah satu berita ketika user belum login --##
        driver.execute_script('window.scrollTo(0,1800);')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[6]/div/div[1]/div/button/span/span').click()
        time.sleep(5) 
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/button/span/span').click()
        time.sleep(5)
        ##-- Windows Handle --##
        parent_window_handle = driver.current_window_handle
        like_window_handles = driver.window_handles
        driver.switch_to.window(like_window_handles[1])
        time.sleep(5)
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").send_keys("cancer_goodboy@yahoo.com")
        time.sleep(5)
        driver.find_element_by_id("pass").click()
        driver.find_element_by_id("pass").send_keys("ulungn4p1tu")
        time.sleep(5)
        driver.find_element_by_name("login").click()
        time.sleep(5)
        driver.switch_to.window(parent_window_handle)
        time.sleep(5)
        ##-- Kode dibawah ini dipakai ketika baru login dari facebook pertama kali--##
        #driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button').click()
        #time.sleep(10)
        ##--End of Code Autentikasi Pertama Kali--##
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[7]/div/div[1]/div/button/span/span').click()
        time.sleep(5)
        ##-- Bug pada tombol bagikan facebook  Kode untuk Bagikan berita ke facebook --##
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[6]/div/div[3]/div/button/span/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[7]/div[2]/div/div[1]/div/div/div/button[1]/span/span').click()
        time.sleep(20)
        bagi_window_handles = driver.window_handles
        driver.switch_to.window(bagi_window_handles[1])
        driver.find_element_by_xpath('//*[@id="u_0_24"]').click()
        time.sleep(5)
        driver.switch_to.window(parent_window_handle)
        ##-- Bug  yang ada di kumparan.com ialah setelah share tombolnya ga langsung menghilang --##
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[7]/div[2]/div/div[2]/button/span/span').click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        driver.execute_script('window.scrollTo(0,1800);')
        time.sleep(5)
        ##-- Comment with Javascript executor karena tidak comment javascript --##
        driver.find_element_by_class_name("public-DraftStyleDefault-block").click()
        time.sleep(5)
        driver.execute_script("document.getElementsByClassName('public-DraftStyleDefault-block')[0].value='Komeng Dulu Gan'")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/a/span/div/div/img').click()
        time.sleep(5)

def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()