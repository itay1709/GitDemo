from selenium.webdriver.common.by import By


class ShopPage:

    #constructor:
    def __init__(self, driver):
        self.driver = driver

    #locators:
    productCard = (By.XPATH, "//div[@class='card h-100']")
    deviceName = (By.XPATH, "div/h4")
    checkOutBtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    #elements:
    def productCardE(self):
        return self.driver.find_elements(*ShopPage.productCard)

    def deviceNameE(self):
        return self.driver.find_elements(*ShopPage.deviceName)

    def checkOutBtnE(self):
        return self.driver.find_element(*ShopPage.checkOutBtn)

