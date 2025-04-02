from selenium.webdriver.common.by import By

from PageObjects.Addemployeepage import Addemployeepage


class Loginpage:
    def __init__(self,driver):
        self.driver = driver



    employeeID = (By.NAME,"employee_id")
    password = (By.ID,"floatingPassword1")
    loginbutton = (By.XPATH,"//button[@type='submit']")


    def getemployeeID(self):
        return self.driver.find_element(*Loginpage.employeeID)

    def getpassword(self):
        return self.driver.find_element(*Loginpage.password)

    def getloginbutton(self):
        self.driver.find_element(*Loginpage.loginbutton).click()
        addemployeepage = Addemployeepage(self.driver)
        return addemployeepage