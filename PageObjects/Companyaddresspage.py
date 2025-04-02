from selenium.webdriver.common.by import By


class Companyaddresspage:
    def __init__(self,driver):
        self.driver = driver


    company_postal_address = (By.XPATH,"//a[@id='tab5-tab']")
    add_line1 = (By.ID,"addr1")
    add_line2 = (By.ID,"addr2")
    country_dropdown = (By.ID,"country")
    state_dropdown = (By.ID,"state")
    city_dropdown = (By.ID,"city")
    pincode = (By.ID,"pincode")
    update_button = (By.XPATH,"//button[@id='update5']")
    edit_button = (By.XPATH,"//button[@id='edit5']")

    def getcompany_postal_address(self):
        return self.driver.find_element(*Companyaddresspage.company_postal_address)

    def getadd_line1(self):
        return self.driver.find_element(*Companyaddresspage.add_line1)

    def getadd_line2(self):
        return self.driver.find_element(*Companyaddresspage.add_line2)

    def getcountry_dropdown(self):
        return self.driver.find_element(*Companyaddresspage.country_dropdown)

    def getstate_dropdown(self):
        return self.driver.find_element(*Companyaddresspage.state_dropdown)

    def getcity_dropdown(self):
        return self.driver.find_element(*Companyaddresspage.city_dropdown)

    def getpincode(self):
        return self.driver.find_element(*Companyaddresspage.pincode)

    def getupdate_button(self):
        return self.driver.find_element(*Companyaddresspage.update_button)

    def getedit_button(self):
        return self.driver.find_element(*Companyaddresspage.edit_button)