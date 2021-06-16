# -*- coding: utf-8 -*-
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\jaski\\PycharmProjects\\pythonProject\\test\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # self.base_url = "https://www.google.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do")
        driver.find_element_by_id("select2-stfNameId-container").click()
        driver.find_element_by_xpath("//body/span[1]/span[1]/span[1]/input[1]").send_keys("punjab")
        driver.find_element_by_class_name("select2-results__options").click()
        time.sleep(2)
        # driver.find_element_by_link_text("Slot Booking DL Test").click()
        # driver.find_element_by_class_name("icon-list").click()
        driver.find_element_by_xpath("//body/div[1]/div[1]/div[3]/section[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]").click()
        # driver.find_element_by_link_text("DL Slots Enquiry").click()
        driver.find_element_by_xpath("//a[contains(text(),'Enquiry DL Test Slot')]").click()
        driver.find_element_by_id("stCodeId").click()
        Select(driver.find_element_by_id("stCodeId")).select_by_visible_text("PB")
        driver.find_element_by_id("stCodeId").click()
        driver.find_element_by_id("rtoCodes1Id").click()
        Select(driver.find_element_by_id("rtoCodes1Id")).select_by_visible_text("PB02")
        time.sleep(1)
        driver.find_element_by_id("rtoCodes1Id").click()
        time.sleep(1)
        Select(driver.find_element_by_id("trackName")).select_by_visible_text("AMRITSAR_TRACK")

        Select(driver.find_element_by_id("trackRTO")).select_by_visible_text("PB02")

        # driver.find_element_by_id("trackRTO").click()
        driver.find_element_by_id("COVorTRANS").click()
        driver.find_element_by_id("slotTypesdl").click()
        Select(driver.find_element_by_id("slotTypesdl")).select_by_visible_text("NormalQuota")
        driver.find_element_by_id("slotTypesdl").click()
        driver.find_element_by_id("proceedBtn").click()
        #driver.find_element_by_id("refresh").click()
        time.sleep(3)
        # driver.find_element_by_xpath("//tbody/tr[30]").click()
        driver.find_element_by_xpath("//tbody/tr[30]/td[2]").click()
        time.sleep(10)
        driver.save_screenshot("C:\Screenshot\slot.png")

        # driver.close()

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)


# if __name__ == "__main__":
#     unittest.main()
