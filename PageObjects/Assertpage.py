from selenium.webdriver.common.by import By


class Assertdetailspage:
    def __init__(self,driver):
        self.driver = driver

    assert_button = (By.XPATH,"//a[@id='tab6-tab']")
    assert_type = (By.XPATH,"//select[@id='asset_type']")
    assert_alloted = (By.XPATH,"//select[@id='asset_code']")
    allotment_date = (By.XPATH,"//input[@id='allot_date']")

    def getassert_button(self):
        return self.driver.find_element(*Assertdetailspage.assert_button)

    def getassert_type(self):
        return self.driver.find_element(*Assertdetailspage.assert_type)

    def getassert_alloted(self):
        return self.driver.find_element(*Assertdetailspage.assert_alloted)

    def getallotment_date(self):
        return self.driver.find_element(*Assertdetailspage.allotment_date)