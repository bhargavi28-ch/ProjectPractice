from selenium.webdriver.common.by import By

from tests.conftest import driver


class Companyinformation:
    def __init__(self,driver):
        self.driver = driver


    company_information_button = (By.XPATH,"//a[@id='tab2-tab']")
    dateofjoin = (By.XPATH,"//input[@id='join_date']")
    department = (By.XPATH,"//select[@id='department']")
    designation = (By.XPATH,"//select[@id='designation']")
    employeement_type = (By.XPATH,"//select[@id='employment_type']")
    worklocation = (By.XPATH,"//select[@id='work_location']")
    shifttiming = (By.XPATH,"//select[@id='shift_type']")
    reporting_manager = (By.XPATH,"//select[@id='reporting_manager1']")
    reporting_manager2 = (By.XPATH,"//select[@id='reporting_manager2']")
    save_button = (By.XPATH,"//button[@id='update6']")

    def getcompany_information_button(self):
        return self.driver.find_element(*Companyinformation.company_information_button)


    def getdateofjoin(self):
        return self.driver.find_element(*Companyinformation.dateofjoin)

    def getdepartment(self):
        return self.driver.find_element(*Companyinformation.department)

    def getdesignation(self):
        return self.driver.find_element(*Companyinformation.designation)

    def getemployeement_type(self):
        return self.driver.find_element(*Companyinformation.employeement_type)

    def getworklocation(self):
        return self.driver.find_element(*Companyinformation.worklocation)

    def getshifttiming(self):
        return self.driver.find_element(*Companyinformation.shifttiming)

    def getreporting_manager(self):
        return self.driver.find_element(*Companyinformation.reporting_manager)

    def getreportingmanager2(self):
        return self.driver.find_element(*Companyinformation.reporting_manager2)

    def getsave_button(self):
        return self.driver.find_element(*Companyinformation.save_button)




