from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class Logoutpage:
    def __init__(self, driver):
        self.driver = driver



    profile_info = (By.CLASS_NAME,"profile-info")
    logout_icon = (By.XPATH,"//i[@class='infoTimestyles-icon infoTimestyles-icon--logout']")

    def getprofile_info(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*Logoutpage.profile_info)
        action.move_to_element(element).perform()

    def getlogout_icon(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*Logoutpage.logout_icon)
        action.move_to_element(element).click().perform()