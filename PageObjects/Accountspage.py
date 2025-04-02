from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Accountspage:
    def __init__(self, driver):
        self.driver = driver

    accounts = (By.XPATH, "//span[normalize-space()='Accounts']")
    pay_register = (By.XPATH, "//a[normalize-space()='Pay Register']")
    add_payregister = (By.XPATH, "//button[normalize-space()='Add Pay Register']")
    select_month_year = (By.XPATH, "//input[@id='pay_month']")
    # sample_download = (By.XPATH,"//a[normalize-space()='Download Sample']")
    upload_file = (By.XPATH, "//input[@type='file']")
    submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    pay_slips = (By.XPATH,"//a[normalize-space()='Pay Slips']")
    pay_slip_self = (By.XPATH,"//a[normalize-space()='Self']")
    pay_slip_employee = (By.XPATH,"//a[@role='tab'][normalize-space()='Employees']")
    employee_search_payslip = (By.XPATH,"//input[@id='empid']")
    search_button = (By.XPATH,"//button[normalize-space()='Search']")
    view_payslip_actions = (By.XPATH,"//i[@class='fa fa-eye fa-fw']")
    check_box_payslip_activation = (By.XPATH,"//label[normalize-space()='#']")
    search_employeeID = (By.XPATH,"(//input[@id='empid'])[1]")
    search_employeeID_search_button = (By.XPATH,"//button[normalize-space()='Search']")
    yes_button = (By.XPATH,"//button[normalize-space()='Yes']")
    no_button = (By.XPATH,"//button[normalize-space()='No']")
    self_view = (By.XPATH,"//div[@id='self_search-results']//a[@type='button']")
    employee_view = (By.XPATH,"//div[@class='team_search-results']//a[@type='button']")


    def getaccounts(self):
        return self.driver.find_element(*Accountspage.accounts)

    def getpay_register(self):
        return self.driver.find_element(*Accountspage.pay_register)

    def getadd_payregister(self):
        return self.driver.find_element(*Accountspage.add_payregister)

    def getselect_month_year(self):
        return self.driver.find_element(*Accountspage.select_month_year)

    def getupload_file(self,file_input):
        file_input2 = self.driver.find_element(*Accountspage.upload_file)
        file_input2.send_keys(file_input)

    def getsubmit_button(self):
        return self.driver.find_element(*Accountspage.submit_button)

    def getpay_slips(self):
        return self.driver.find_element(*Accountspage.pay_slips)

    def getpay_slip_self(self):
        return self.driver.find_element(*Accountspage.pay_slip_self)

    def getpay_slip_employee(self):
        return self.driver.find_element(*Accountspage.pay_slip_employee)

    def getemployee_search_payslip(self):
        return self.driver.find_element(*Accountspage.employee_search_payslip)

    def getsearch_button(self):
        return self.driver.find_element(*Accountspage.search_button)

    def getview_payslip_actions(self):
        return self.driver.find_element(*Accountspage.view_payslip_actions)

    def getcheck_box_payslip_activation(self):
        return self.driver.find_element(*Accountspage.check_box_payslip_activation)

    def getsearch_employeeID(self):
        return self.driver.find_element(*Accountspage.search_employeeID)

    def getsearch_employeeID_search_button(self):
        return self.driver.find_element(*Accountspage.search_employeeID_search_button)

    def getyes_button(self):
        return self.driver.find_element(*Accountspage.yes_button)

    def getno_button(self):
        return self.driver.find_element(*Accountspage.no_button)

    def getself_view(self):
        return self.driver.find_element(*Accountspage.self_view)

    def getemployee_view(self):
        return self.driver.find_element(*Accountspage.employee_view)






