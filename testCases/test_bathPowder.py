import time
from hashlib import new
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.BathObjects import Bath
from PageObjects.location import Location
from utilities.readProperties import ReadConfig

class Test_BathPowder:
    baseURL = ReadConfig.getApplicationURL()
    pincode = ReadConfig.getLPincode()

    def test_001_Bath_powder(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.loc = Location(self.driver)
        self.loc.select_location()
        self.loc.pincode_link()
        self.driver.find_element(By.XPATH, self.loc.pincode_XPATH_txtbox).clear()
        self.loc.enter_pincode(self.pincode)
        self.loc.click_apply()

        self.bpowd = Bath(self.driver)
        self.ele = self.driver.find_element(By.XPATH, self.bpowd.Bath_XPATH_link)

        actions = ActionChains(self.driver)
        actions.move_to_element(self.ele).perform()
        time.sleep(3)
        self.bpowd.Ubtanlink()
        self.ele2 = self.driver.find_element(By.XPATH, self.bpowd.BabyOrgano_XPATH_link)
        actions.move_to_element(self.ele2).perform()
        time.sleep(3)
        self.bpowd.BabyOrganoPowder()
        self.cart = self.driver.find_element(By.XPATH, self.bpowd.ADDCART_XPATH_button)
        actions.move_to_element(self.cart).click()
        time.sleep(4)





