import logging
import inspect

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait



from TeatData.LoginpageData import LoginpageData



@pytest.mark.usefixtures("setupbrowser")
class BaseClass:
    def navigate_to_url(self, url):
        self.driver.get(url)

    employeeID = (By.NAME, "employee_id")
    password = (By.ID, "floatingPassword1")
    loginbutton = (By.XPATH, "//button[@type='submit']")


    def login(self,getData):
        self.driver.find_element(*self.employeeID).send_keys(getData["employeeID"])
        self.driver.find_element(*self.password).send_keys(getData["password"])
        self.driver.find_element(*self.loginbutton).click()

    @pytest.fixture(params= LoginpageData.test_Login_Data)
    def getData(self,request):
        return request.param

    profile_info = (By.CLASS_NAME, "profile-info")
    logout_icon = (By.XPATH, "//i[@class='infoTimestyles-icon infoTimestyles-icon--logout']")

    def logout(self):
        wait = WebDriverWait(self.driver,20)
        profile_info = wait.until(expected_conditions.presence_of_element_located(self.profile_info))
        logout_icon = wait.until(expected_conditions.presence_of_element_located(self.logout_icon))

        action = ActionChains(self.driver)
        action.move_to_element(profile_info).perform()
        logout_icon.click()

        # action.move_to_element(self.driver.find_element(*self.profile_info)).perform()
        # action.move_to_element(self.driver.find_element(*self.logout_icon)).perform().click()



    def Verifylinkpresence(self, text):


        wait = WebDriverWait(self.driver, 20)
        wait.until((expected_conditions.presence_of_element_located(By.LINK_TEXT,text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getlogger(self):

        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.file')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger













