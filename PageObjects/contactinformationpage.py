from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CreatecompanyPage import Createcompanypage


class Contactinformationpage:
    def __init__(self,driver):
        self.driver = driver

    company_profile = (By.LINK_TEXT,"Company Profile")
    contact_information = (By.LINK_TEXT,"Contact Information")
    head_of_the_company = (By.XPATH,"//input[@id='company_head']")
    profile_pic = (By.ID,"profile_pic")
    head_designation = (By.XPATH,"//input[@id='head_desc']")
    head_contact_no = (By.XPATH,"//input[@id='head_phone']")
    company_website = (By.XPATH,"//input[@id='website']")
    company_email = (By.XPATH,"//input[@id='company_email']")
    notification_mails = (By.XPATH,"//input[@id='cc_emails']")
    save_button = (By.XPATH,"//button[@id='update2']")
    edit_button = (By.XPATH,"//button[@id='edit2']")
    update_button = (By.XPATH,"//form[@id='update_form2']")


    def getcontact_information(self):
        return self.driver.find_element(*Contactinformationpage.contact_information)

    def gethead_of_the_company(self):
        return self.driver.find_element(*Contactinformationpage.head_of_the_company)

    def getprofile_pic(self,profile_pic):
        upload2 = self.driver.find_element(*Contactinformationpage.profile_pic)
        upload2.send_keys(profile_pic)

    def gethead_designation(self):
        return self.driver.find_element(*Contactinformationpage.head_designation)

    def gethead_contact_no(self):
        return self.driver.find_element(*Contactinformationpage.head_contact_no)

    def getcompany_website(self):
        return self.driver.find_element(*Contactinformationpage.company_website)

    def getcompany_email(self):
        return self.driver.find_element(*Contactinformationpage.company_email)

    def getnotification_email(self):
        return self.driver.find_element(*Contactinformationpage.notification_mails)

    def getsave_button(self):
        return self.driver.find_element(*Contactinformationpage.save_button)

    def getcompany_profile(self):
        return self.driver.find_element(*Contactinformationpage.company_profile)

    def getedit_button(self):
        return self.driver.find_element(*Contactinformationpage.edit_button)

    def getupdate_button(self):
        return self.driver.find_element(*Contactinformationpage.update_button)





