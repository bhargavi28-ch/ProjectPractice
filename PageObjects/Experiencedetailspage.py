from selenium.webdriver.common.by import By


class Experiencedetailspage:
    def __init__(self,driver):
        self.driver = driver

    experience_details_button = (By.LINK_TEXT,"Experience Details")
    company = (By.XPATH,"//input[@id='exp_company']")
    joining_date = (By.XPATH,"//input[@id='exp_join_date']")
    designation = (By.XPATH,"//input[@id='exp_join_date']")
    left_date = (By.XPATH,"//input[@id='exp_left_date']")
    location = (By.XPATH,"//input[@id='exp_location']")

    def getexperience_details_button(self):
        return self.driver.find_element(*Experiencedetailspage.experience_details_button)

    def getcompany(self):
        return self.driver.find_element(*Experiencedetailspage.company)

    def getjoining_date(self):
        return self.driver.find_element(*Experiencedetailspage.joining_date)

    def getdesignation(self):
        return self.driver.find_element(*Experiencedetailspage.designation)

    def getleft_date(self):
        return self.driver.find_element(*Experiencedetailspage.left_date)

    def getlocation(self):
        return self.driver.find_element(*Experiencedetailspage.location)

