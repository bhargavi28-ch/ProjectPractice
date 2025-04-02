from selenium.webdriver.common.by import By
from urllib3 import request


class AwardscertificatesPage:
    def __init__(self,driver):
        self.driver = driver

    awards_certificates = (By.XPATH,"//a[@id='tab9-tab']")
    doc_type = (By.ID,"doc_type")
    issue_date = (By.XPATH,"//input[@id='start_date']")
    title = (By.ID,"title")
    valid_till = (By.XPATH,"//input[@id='end_date']")
    certificate_no = (By.ID,"certificate_no")
    browse_document = (By.XPATH,"//input[@type='file']")
    save_button = (By.XPATH,"//button[@id='update9']")

    def getawards_certificates(self):
        return self.driver.find_element(*AwardscertificatesPage.awards_certificates)

    def getdoc_type(self):
        return self.driver.find_element(*AwardscertificatesPage.doc_type)

    def getissue_date(self):
        return self.driver.find_element(*AwardscertificatesPage.issue_date)

    def gettitle(self):
        return self.driver.find_element(*AwardscertificatesPage.title)

    def getvalid_till(self):
        return self.driver.find_element(*AwardscertificatesPage.valid_till)

    def getcertificate_no(self):
        return self.driver.find_element(*AwardscertificatesPage.certificate_no)

    def getbrowse_document(self):
        return self.driver.find_element(*AwardscertificatesPage.browse_document)

    def getsave_button(self):
        return self.driver.find_element(*AwardscertificatesPage.save_button)



