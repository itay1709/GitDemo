import time

import pytest

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    @pytest.fixture()
    def get_homepage(self):
        self.homePage = HomePage(self.driver)
        return self.homePage

    def test_validateTopBarElements(self,  get_homepage):
        assert self.homePage.protoCommerceE().text == "ProtoCommerce"
        assert self.homePage.homeBtnE().text == "Home"
        assert self.homePage.shopBtnE().text == "Shop"
        self.logScriptDemo().info("the text from shop button from the app was: "+self.homePage.shopBtnE().text)

    def test_validateFormElements(self, get_homepage):
        if self.homePage.nameE().text == "Name":
            self.logScriptDemo().info("text field name is correct")
        else:
            self.logScriptDemo().error("text name field is wrong. the value in app was:"+self.homePage.nameE().text)
        assert self.homePage.nameE().text == "Name"
        assert self.homePage.emailE().text == "Email"

    def test_submitForm(self, get_homepage):
        self.homePage.nameInputE().send_keys(self.getTestDataExcel("test1")["firstname"])
        self.homePage.emailInputE().send_keys(self.getTestDataExcel("test1")["email"])
        self.selectByText(self.homePage.genderSelectE(), "Female")
        self.homePage.dateOfBirthInputE().send_keys("03/17/2000")
        self.homePage.submitBtnE().click()






