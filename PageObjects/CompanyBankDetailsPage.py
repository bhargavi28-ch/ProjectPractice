from selenium.webdriver.common.by import By


class CompanyBankdetailspage:
    def __init__(self,driver):
        self.driver = driver

    bank_details = (By.XPATH,"//a[@id='tab6-tab']")
    bank_name = (By.ID,"bank_id")
    branch_name = (By.ID,"branch_name")
    account_no = (By.ID,"acc_no")
    ifsc_code = (By.ID,"ifsc_code")
    browse_document = (By.XPATH,"//input[@type='file']")
    save_document = (By.XPATH,"//button[@id='update6']")

    def getbank_details(self):
        return self.driver.find_element(*CompanyBankdetailspage.bank_details)

    def getbank_name(self):
        return self.driver.find_element(*CompanyBankdetailspage.bank_name)

    def getbranch_name(self):
        return self.driver.find_element(*CompanyBankdetailspage.branch_name)

    def getaccount_no(self):
        return self.driver.find_element(*CompanyBankdetailspage.account_no)

    def getifsc_code(self):
        return self.driver.find_element(*CompanyBankdetailspage.ifsc_code)

    def getbrowse_document(self):
        return self.driver.find_element(*CompanyBankdetailspage.browse_document)

    def getsave_document(self):
        return self.driver.find_element(*CompanyBankdetailspage.save_document)
