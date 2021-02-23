from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    #contructor:
    def __init__(self, driver):
        self.driver = driver

    #locators:
    protoCommerce = (By.CLASS_NAME, "navbar-brand")
    homeBtn = (By.LINK_TEXT, "Home")
    shopBtn = (By.LINK_TEXT, "Shop")

    name = (By.XPATH, "//form/div[1]/label")
    nameInput = (By.XPATH, "//form/div[1]/input")
    email = (By.XPATH, "//form/div[2]/label")
    emailInput = (By.XPATH, "//form/div[2]/input")
    password = (By.XPATH, "//form/div[3]/label")
    passwordInput = (By.XPATH, "//form/div[3]/input")
    checkBox = (By.XPATH, "//form/div[4]/input")
    checkBoxText = (By.XPATH, "//form/div[4]/label")
    gender = (By.XPATH, "//form/div[5]/label")
    genderSelect = (By.ID, "exampleFormControlSelect1")
    employmentStatus = (By.XPATH, "//form/div[6]/label")
    studentCheckBox = (By.ID, "inlineRadio1")
    student = (By.XPATH, "//form/div[6]/div[1]/label")
    dateOfBirth = (By.XPATH, "//form/div[7]/label")
    dateOfBirthInput = (By.XPATH, "//form/div[7]/input")

    submitBtn = (By.XPATH, "//input[@value='Submit']")

    #elements
    def protoCommerceE(self):
        return self.driver.find_element(*HomePage.protoCommerce)

    def homeBtnE(self):
        return self.driver.find_element(*HomePage.homeBtn)

    def shopBtnE(self):
        return self.driver.find_element(*HomePage.shopBtn)

    def nameE(self):
        return self.driver.find_element(*HomePage.name)

    def nameInputE(self):
        return self.driver.find_element(*HomePage.nameInput)

    def emailE(self):
        return self.driver.find_element(*HomePage.email)

    def emailInputE(self):
        return self.driver.find_element(*HomePage.emailInput)

    def checkBoxE(self):
        return self.driver.find_element(*HomePage.checkBox)

    def genderSelectE(self):
        return self.driver.find_element(*HomePage.genderSelect)

    def studentCheckBoxE(self):
        return self.driver.find_element(*HomePage.studentCheckBox)

    def dateOfBirthInputE(self):
        return self.driver.find_element(*HomePage.dateOfBirthInput)

    def submitBtnE(self):
        return self.driver.find_element(*HomePage.submitBtn)

