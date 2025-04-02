from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Exitdetailspage:
    def __init__(self,driver):
        self.driver = driver

    exit_button = (By.ID,"tab9-tab")
    resignation_date = (By.XPATH,"//input[@id='resignation_date']")
    notice_period = (By.XPATH,"//select[@id='notice_period']")
    exit_type = (By.XPATH,"//select[@id='exit_type']")
    save_button = (By.XPATH,"//button[@id='save1']")

    def getexit_button(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(self.exit_button)
            )
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
            return element
        except Exception as e:
            print(f"Error finding or interacting with the button: {e}")
            return None
        #return self.driver.find_element(*Exitdetailspage.exit_button)

    def getresignation_date(self):
        return self.driver.find_element(*Exitdetailspage.resignation_date)

    def getnotice_period(self):
        return self.driver.find_element(*Exitdetailspage.notice_period)

    def getexit_type(self):
        return self.driver.find_element(*Exitdetailspage.exit_type)

    def getsave_button(self):
        return self.driver.find_element(*Exitdetailspage.save_button)