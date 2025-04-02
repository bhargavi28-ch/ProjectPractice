from selenium.webdriver.common.by import By


class PMSpage:
    def __init__(self,driver):
        self.driver = driver


    pms_button = (By.XPATH,"//span[normalize-space()='PMS']")
    create_button = (By.XPATH,"//button[normalize-space()='Create Project']")
    project_name = (By.ID,"project_name")
    project_code = (By.ID,"project_code")
    employee_search = (By.XPATH,"//input[@placeholder='Search for an employee...']")
    submit_button = (By.XPATH,"//button[normalize-space()='Submit']")

    def getpms_button(self):
        return self.driver.find_element(*PMSpage.pms_button)

    def getcreate_button(self):
        return self.driver.find_element(*PMSpage.create_button)

    def getproject_name(self):
        return self.driver.find_element(*PMSpage.project_name)

    def getproject_code(self):
        return self.driver.find_element(*PMSpage.project_code)

    def getemployee_search(self):
        return self.driver.find_element(*PMSpage.employee_search)

    def getsubmit_button(self):
        return self.driver.find_element(*PMSpage.submit_button)