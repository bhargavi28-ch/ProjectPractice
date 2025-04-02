from selenium.webdriver.common.by import By


class TaxinformationPage:
    def __init__(self, driver):
        self.driver = driver

    tax_information = (By.XPATH, "//a[@id='tab3-tab']")
    tax_type = (By.ID, "tax_type")
    registration_no = (By.XPATH, "//input[@id='tax_no']")
    browse_button = (By.XPATH, "//input[@id='tax_doc']")
    save_button = (By.XPATH, "//button[@id='update3']")

    def gettax_information(self):
        return self.driver.find_element(*TaxinformationPage.tax_information)

    def gettax_type(self):
        return self.driver.find_element(*TaxinformationPage.tax_type)

    def getregistration_no(self):
        return self.driver.find_element(*TaxinformationPage.registration_no)

    def getbrowse_button(self):
        return self.driver.find_element(*TaxinformationPage.browse_button)

    def getsave_button(self):
        return self.driver.find_element(*TaxinformationPage.save_button)
