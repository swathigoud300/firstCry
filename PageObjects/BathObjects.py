from selenium.webdriver.common.by import By


class Bath:

    Bath_XPATH_link = "//a[normalize-space()='Bath']"
    ubtan_XPATH_link = "(//a[text()='Ubtan for Babies '])[2]"
    BabyOrgano_XPATH_link = "//a[normalize-space()='BabyOrgano Natural Ubtan - 100 g']"
    ADDCART_XPATH_button = "//div[@class='btn btn-add-cart add-cart']//span[@class='M16_white'][normalize-space()='ADD TO CART']"

    def __init__(self, driver):
        self.driver = driver

    def Bathlink(self):
        self.driver.find_element(By.XPATH, self.Bath_XPATH_link).click()

    def Ubtanlink(self):
        self.driver.find_element(By.XPATH, self.ubtan_XPATH_link).click()

    def BabyOrganoPowder(self):
        self.driver.find_element(By.XPATH, self.BabyOrgano_XPATH_link).click()

    def Add2Cart(self):
        self.driver.find_element(By.XPATH, self.ADDCART_XPATH_button).click()


