from selenium.webdriver.common.by import By

from tests.conftest import driver


class Familydetailspage:
    def __init__(self,driver):
        self.driver = driver

    familydetails_button = (By.XPATH,"//a[@id='tab3-tab']")
    name = (By.XPATH,"//input[@id='f_name']")
    contactnumber = (By.XPATH,"//input[@id='f_phone']")
    relation_type = (By.XPATH,"//select[@id='f_relationship']")
    insurance_covered = (By.XPATH,"//select[@id='f_ins']")
    dateofbirth = (By.XPATH,"//input[@id='f_dob']")

    def getfamilydetails_button(self):
        return self.driver.find_element(*Familydetailspage.familydetails_button)

    def getname(self):
        return self.driver.find_element(*Familydetailspage.name)

    def getcontactnumber(self):
        return self.driver.find_element(*Familydetailspage.contactnumber)

    def getrelation_type(self):
        return self.driver.find_element(*Familydetailspage.relation_type)

    def getinsurance_covered(self):
        return self.driver.find_element(*Familydetailspage.insurance_covered)

    def getdateofbirth(self):
        return self.driver.find_element(*Familydetailspage.dateofbirth)



