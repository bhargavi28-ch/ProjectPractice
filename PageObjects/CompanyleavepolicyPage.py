from selenium.webdriver.common.by import By


class CompanyleavepolicyPage:
    def __init__(self,driver):
        self.driver = driver

    select_company = (By.XPATH,"//select[@id='mySelect']")
    company_profile = (By.XPATH,"//a[normalize-space()='Company Profile']")
    company_leave_policy = (By.XPATH,"//a[@id='tab8-tab']")
    leave_type = (By.ID,"leave_type")
    leaves_month = (By.ID,"month")
    leave_3_month = (By.ID,"three_months")
    leave_6_month = (By.ID,"six_months")
    leave_1_year = (By.ID,"one_year")
    yes_button = (By.XPATH,"//label[normalize-space()='Yes']")
    no_button = (By.XPATH,"//label[normalize-space()='No']")
    save_button = (By.XPATH,"//button[@id='update8']")

    def getselect_company(self):
        return self.driver.find_element(*CompanyleavepolicyPage.select_company)

    def getcompany_profile(self):
        return self.driver.find_element(*CompanyleavepolicyPage.company_profile)

    def getcompany_leave_policy(self):
        return self.driver.find_element(*CompanyleavepolicyPage.company_leave_policy)

    def getleave_type(self):
        return self.driver.find_element(*CompanyleavepolicyPage.leave_type)

    def getleaves_month(self):
        return self.driver.find_element(*CompanyleavepolicyPage.leaves_month)

    def getleave_3_month(self):
        return self.driver.find_element(*CompanyleavepolicyPage.leave_3_month)

    def getleave_6_month(self):
        return self.driver.find_element(*CompanyleavepolicyPage.leave_6_month)

    def getleave_1_year(self):
        return self.driver.find_element(*CompanyleavepolicyPage.leave_1_year)

    def getyes_button(self):
        return self.driver.find_element(*CompanyleavepolicyPage.yes_button)

    def getno_button(self):
        return self.driver.find_element(*CompanyleavepolicyPage.no_button)

    def getsave_button(self):
        return self.driver.find_element(*CompanyleavepolicyPage.save_button)
