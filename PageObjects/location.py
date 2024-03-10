from selenium.webdriver.common.by import By


class Location:

    location_XPATH_link = "//span[contains(text(),'Select location')]"
    pincode_XPATH_link = "(//sapn[@class='R14_link'])[1]"
    pincode_XPATH_txtbox = "//input[@id='nonlpincode']"
    Apply_XPATH_btn = "(//span[@class='M16_white'][normalize-space()='APPLY'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def select_location(self):
        self.driver.find_element(By.XPATH, self.location_XPATH_link).click()

    def pincode_link(self):
        self.driver.find_element(By.XPATH, self.pincode_XPATH_link).click()

    def enter_pincode(self, pincode):
        self.driver.find_element(By.XPATH, self.pincode_XPATH_txtbox).send_keys(pincode)

    def click_apply(self):
        self.driver.find_element(By.XPATH, self.Apply_XPATH_btn).click()

