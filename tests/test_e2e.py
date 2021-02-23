import time

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from PageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass

class TestDashboard(BaseClass):

    def test_orderE2e(self):

        homePage = HomePage(self.driver)  # home page object
        shopPage = ShopPage(self.driver)  # shop page object
        checkOutPage = CheckOutPage(self.driver)  # check out page object
        confirmPage = ConfirmPage(self.driver)  # confirm page object

        devicesChosen = []
        deviceNameCheckOut = []

        #  page 1 - home page
        homePage.shopBtnE().click()

        #  page 2 - shop page
        productCards = shopPage.productCardE()
        for productCard in productCards:
            devicesName = productCard.find_element_by_xpath("div/h4").text
            if devicesName == "Blackberry":
                devicesChosen.append(devicesName)
                buttons = productCard.find_element_by_xpath("div/button")
                buttons.click()
        self.driver.execute_script("window.scrollTo(0, 0);")
        shopPage.checkOutBtnE().click()

        #  page 3 - check out page
        deviceNameCheckOut.append(checkOutPage.deviceNameE().text)
        assert deviceNameCheckOut == devicesChosen
        checkOutPage.checkOutBtnE().click()

        #  page 4 - confirm page
        confirmPage.inputCountryE().send_keys("ind")
        self.waitUntilXpath("//div[@class='suggestions']")
        countries = confirmPage.countriesE()
        for country in countries:
            chooseCounty = country.find_element_by_xpath("ul")
            if chooseCounty.text == "India":
                chooseCounty.click()
        time.sleep(3)
        confirmPage.purchaseBtnE().click()
        successMsg = confirmPage.successMsgE().text
        print(successMsg)
        assert "Thank youuu!" in successMsg