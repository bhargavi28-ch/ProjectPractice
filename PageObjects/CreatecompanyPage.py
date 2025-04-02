from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Createcompanypage:
    def __init__(self,driver):
        self.driver = driver


    organization_dropdown = (By.PARTIAL_LINK_TEXT,"Organization")
    company_dropdown = (By.XPATH,"//span[normalize-space()='Company']")
    create_company_dropdown = (By.LINK_TEXT,"Create Company")
    company_profile = (By.XPATH,"//a[normalize-space()='Company Profile']")

    #companyinformation
    upload_profile = (By.ID,"company_logo")
    company_name = (By.ID,"company_name")
    short_name = (By.ID,"legal_name")
    company_type = (By.XPATH,"//select[@id='company_type']")
    company_registration_number = (By.XPATH,"//input[@id='reg_no']")
    date_of_registration= (By.ID,"reg_date")
    registration_type = (By.XPATH,"//input[@id='reg_type']")
    business_nature = (By.ID,"business_nature")
    allows_leaves_per_month = (By.XPATH,"//input[@id='month_leaves_limit']")
    save_button = (By.XPATH,"//button[@id='save1']")
    select_company_dropdown = (By.XPATH,"//select[@id='mySelect']")

    def getorganization_dropdown(self):
        return self.driver.find_element(*Createcompanypage.organization_dropdown)

    def getcompany_dropdown(self):
        return self.driver.find_element(*Createcompanypage.company_dropdown)

    def getcreate_company_dropdown(self):
        return self.driver.find_element(*Createcompanypage.create_company_dropdown)

    def getupload_Profile(self,upload_file):
        upload_file2 = self.driver.find_element(*Createcompanypage.upload_profile)
        upload_file2.send_keys(upload_file)

    def getcompany_name(self):
        return self.driver.find_element(*Createcompanypage.company_name)

    def getshort_name(self):
        return self.driver.find_element(*Createcompanypage.short_name)

    def getcompany_type(self):
        return self.driver.find_element(*Createcompanypage.company_type)

    def getcompany_registration_number(self):
        return self.driver.find_element(*Createcompanypage.company_registration_number)

    def getdate_of_registration(self):
        return self.driver.find_element(*Createcompanypage.date_of_registration)

    def getregistration_type(self):
        return self.driver.find_element(*Createcompanypage.registration_type)

    def getbusiness_nature(self):
        return self.driver.find_element(*Createcompanypage.business_nature)

    def getallows_leaves_per_month(self):
        return self.driver.find_element(*Createcompanypage.allows_leaves_per_month)

    def getsave_button(self):
        return self.driver.find_element(*Createcompanypage.save_button)

    def getselect_company_dropdown(self):
        return self.driver.find_element(*Createcompanypage.select_company_dropdown)

    def getcompany_profile(self):
        return self.driver.find_element(*Createcompanypage.company_profile)
