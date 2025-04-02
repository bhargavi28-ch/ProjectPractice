from selenium.webdriver.common.by import By


class Holidayspage:
    def __init__(self, driver):
        self.driver = driver

    holidays = (By.XPATH, "//span[normalize-space()='Holidays']")
    add_holidays = (By.XPATH, "//a[normalize-space()='Add Holiday Calender']")
    status = (By.XPATH, "//select[@id='holid_type']")
    year = (By.XPATH, "//input[@id='year']")
    upload_document = (By.XPATH,"//input[@type='file']")
    save_button = (By.XPATH,"//button[@id='update3']")

    action_edit_draft = (By.XPATH,"//tbody/tr[2]/td[5]/button[1]/i[1]")
    action_edit_published =(By.XPATH,"//tbody/tr[1]/td[5]/button[1]")
    published_document = (By.XPATH,"//tbody/tr[2]/td[3]/a[1]/i[1]")

    status_published_dropdown = (By.XPATH,"//div[@class='modal-body']//select[@id='holid_type']")
    update_button = (By.XPATH,"//button[@class='btn btn-primary update_holid_form']")

    status_draft_dropdown = (By.XPATH,"(//select[@id='holid_type'])[1]")
    # update_button2 = (By.XPATH,"//button[@class='btn btn-primary update_holid_form']")




    def getholidays(self):
        return self.driver.find_element(*Holidayspage.holidays)

    def getadd_holidays(self):
        return self.driver.find_element(*Holidayspage.add_holidays)

    def getstatus(self):
        return self.driver.find_element(*Holidayspage.status)

    def getyear(self):
        return self.driver.find_element(*Holidayspage.year)

    def getupload_document(self):
        return self.driver.find_element(*Holidayspage.upload_document)


    def getsave_button(self):
        return self.driver.find_element(*Holidayspage.save_button)

    def getaction_edit_draft(self):
        return self.driver.find_element(*Holidayspage.action_edit_draft)

    def getaction_edit_published(self):
        return self.driver.find_element(*Holidayspage.action_edit_published)

    def getpublished_document(self):
        return self.driver.find_element(*Holidayspage.published_document)

    def getstatus_published_dropdown(self):
        return self.driver.find_element(*Holidayspage.status_published_dropdown)

    def getupdate_button(self):
        return self.driver.find_element(*Holidayspage.update_button)

    def getstatus_draft_dropdown(self):
        return self.driver.find_element(*Holidayspage.status_draft_dropdown)
