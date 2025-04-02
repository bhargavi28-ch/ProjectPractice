from selenium.webdriver.common.by import By


class Statutoryregistrationpage:
    def __init__(self,driver):
        self.driver = driver

    statutoryregistration_button = (By.XPATH,"//a[@id='tab4-tab']")
    sta_reg_type = (By.ID,"sta_type")
    sta_reg_no = (By.ID,"stax_no")
    browse_document = (By.XPATH,"(//input[@type='file'])")
    save_button = (By.XPATH,"//button[@id='update4']")

    def getstatutoryregistration_button(self):
        return self.driver.find_element(*Statutoryregistrationpage.statutoryregistration_button)

    def getsta_reg_type(self):
        return self.driver.find_element(*Statutoryregistrationpage.sta_reg_type)

    def getsta_reg_no(self):
        return self.driver.find_element(*Statutoryregistrationpage.sta_reg_no)

    def getbrowse_button(self):
        return self.driver.find_element(*Statutoryregistrationpage.browse_document)

    def getsave_button(self):
        return self.driver.find_element(*Statutoryregistrationpage.save_button)