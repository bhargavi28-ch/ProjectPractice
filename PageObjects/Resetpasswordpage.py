from selenium.webdriver.common.by import By


class Resetpasswordpage:
    def __init__(self,driver):
        self.driver = driver

    resetpassword_button = (By.XPATH,"//a[normalize-space()='Reset Password']")
    enter_new_password = (By.XPATH,"//input[@id='floatingPassword1']")
    confirm_new_password = (By.XPATH,"//input[@id='floatingPassword2']")
    submit_button = (By.XPATH,"//button[normalize-space()='Submit']")

    def getresetpassword_button(self):
        return self.driver.find_element(*Resetpasswordpage.resetpassword_button)

    def getenter_new_password(self):
        return self.driver.find_element(*Resetpasswordpage.enter_new_password)

    def getconfirm_new_password(self):
        return self.driver.find_element(*Resetpasswordpage.confirm_new_password)

    def getsubmit_button(self):
        return self.driver.find_element(*Resetpasswordpage.submit_button)