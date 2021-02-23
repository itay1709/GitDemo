from selenium.webdriver.common.by import By


class CheckOutPage:

    #constructor:
    def __init__(self, driver):
        self.driver = driver

    #locators:
    deviceName = (By.XPATH, "//h4[@class='media-heading']/a")
    checkOutBtn = (By.XPATH, "//button[@class='btn btn-success']")

    #elements:
    def deviceNameE(self):
        return self.driver.find_element(*CheckOutPage.deviceName)

    def checkOutBtnE(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)

