from selenium.webdriver.common.by import By


class Contactspage:
    def __init__(self,driver):
        self.driver = driver

    contacts_button =(By.XPATH,"//span[normalize-space()='Contacts']")
    contacts_search = (By.XPATH,"//input[@id='table_search']")
    add_contacts_button = (By.XPATH,"//a[normalize-space()='Add Contacts']")
    search_employeeID_bar = (By.ID,"search_key")
    search_button = (By.XPATH,"//button[normalize-space()='Search']")
    department_dropdown = (By.XPATH,"//select[@id='search_dept_key']")
    advanced_search_dropdown = (By.XPATH,"//a[normalize-space()='Advanced Search']")
    designation_dropdown = (By.XPATH,"//select[@id='search_desg_key']")
    active_dropdown = (By.XPATH,"//select[@id='search_status_key']")
    check_box_activated = (By.XPATH,"//tr[@id='rowid_17']//div[@class='control__indicator control__indicator--sm']")
    check_box_deactivated = (By.XPATH,"//tr[@id='rowid_12']//div[@class='control__indicator control__indicator--sm']")

    def getcontacts_button(self):
        return self.driver.find_element(*Contactspage.contacts_button)

    def getcontacts_search(self):
        return self.driver.find_element(*Contactspage.contacts_search)

    def getadd_contacts_button(self):
        return self.driver.find_element(*Contactspage.add_contacts_button)

    def getsearch_employeeID_bar(self):
        return self.driver.find_element(*Contactspage.search_employeeID_bar)

    def getsearch_button(self):
        return self.driver.find_element(*Contactspage.search_button)

    def getdepartment_dropdown(self):
        return self.driver.find_element(*Contactspage.department_dropdown)

    def getadvanced_search_dropdown(self):
        return self.driver.find_element(*Contactspage.advanced_search_dropdown)

    def getdesignation_dropdown(self):
        return self.driver.find_element(*Contactspage.designation_dropdown)

    def getactive_dropdown(self):
        return self.driver.find_element(*Contactspage.active_dropdown)

    def getcheck_box_activated(self):
        return self.driver.find_element(*Contactspage.check_box_activated)

    def getcheck_box_deactivated(self):
        return self.driver.find_element(*Contactspage.check_box_deactivated)





