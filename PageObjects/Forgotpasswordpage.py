from selenium.webdriver.common.by import By


class Forgotpasswordpage:
    def __init__(self,driver):
        self.driver = driver

    forgotpassword_button = (By.XPATH,"//a[normalize-space()='Forgot Password?']")
    enter_employeeID = (By.XPATH,"//input[@id='employee_id']")
    send_reset_password_link = (By.XPATH,"//button[normalize-space()='Send Reset Password Link']")


    def getforgotpassword_button(self):
        return self.driver.find_element(*Forgotpasswordpage.forgotpassword_button)

    def getenter_employeeID(self):
        return self.driver.find_element(*Forgotpasswordpage.enter_employeeID)

    def getsend_reset_password_link(self):
        return self.driver.find_element(*Forgotpasswordpage.send_reset_password_link)