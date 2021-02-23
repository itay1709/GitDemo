from selenium.webdriver.common.by import By


class ConfirmPage:

    #constructor:
    def __init__(self, driver):
        self.driver = driver

    #locators:
    inputCountry = (By.ID, "country")
    countries = (By.XPATH, "//div[@class='suggestions']")
    purchaseBtn = (By.XPATH, "//input[@value='Purchase']")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    #elements:
    def inputCountryE(self):
        return self.driver.find_element(*ConfirmPage.inputCountry)

    def countriesE(self):
        return self.driver.find_elements(*ConfirmPage.countries)

    def purchaseBtnE(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def successMsgE(self):
        return self.driver.find_element(*ConfirmPage.successMsg)