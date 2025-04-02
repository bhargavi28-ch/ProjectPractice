from selenium.webdriver.common.by import By


class Qualificationdetailspage:
    def __init__(self,driver):
        self.driver = driver


    qualification_details_button = (By.XPATH,"//a[@id='tab4-tab']")
    qualification = (By.XPATH,"//input[@id='qualification']")
    yearofpassing = (By.XPATH,"//input[@id='year_passed']")
    collegedetails = (By.XPATH,"//input[@id='college']")
    percentage = (By.XPATH,"//input[@id='grade']")
    university = (By.XPATH,"//input[@id='university']")
    addqualification_button = (By.XPATH,"//button[@id='update4']")


    def getqualification_details_button(self):
        return self.driver.find_element(*Qualificationdetailspage.qualification_details_button)

    def getqualification(self):
        return self.driver.find_element(*Qualificationdetailspage.qualification)

    def getyearofpassing(self):
        return self.driver.find_element(*Qualificationdetailspage.yearofpassing)

    def getcollegedetails(self):
        return self.driver.find_element(*Qualificationdetailspage.collegedetails)

    def getpercentage(self):
        return self.driver.find_element(*Qualificationdetailspage.percentage)

    def getuniversity(self):
        return self.driver.find_element(*Qualificationdetailspage.university)

    def getaddqualification_button(self):
        return self.driver.find_element(*Qualificationdetailspage.qualification_details_button)
