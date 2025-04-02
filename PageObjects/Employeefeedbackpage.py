from selenium.webdriver.common.by import By


class Employeefeedbackpage:
    def __init__(self,driver):
        self.driver = driver

    employee_feedback = (By.XPATH,"//span[normalize-space()='Employee Feedback']")
    team_radio_button = (By.XPATH,"//label[normalize-space()='Team']")
    select_team_member = (By.XPATH,"//span[@class='filter-option pull-left']")
    select_search_bar = (By.XPATH,"//input[@class='input-block-level form-control']")
    employee_radio_button = (By.XPATH,"//label[normalize-space()='Employees']")
    search_employeeID = (By.XPATH,"//input[@id='employee']")
    work_radio_button = (By.XPATH,"(//div[@class='control__indicator'])[2]")
    communication_radio_button = (By.XPATH,"(//div[@class='control__indicator'])[9]")
    teaminteraction_radio_button = (By.XPATH,"(//div[@class='control__indicator'])[16]")
    punctuality_radio_button = (By.XPATH,"(//div[@class='control__indicator'])[23]")
    submit_button = (By.XPATH,"//button[@id='save_fb']")
    view_report = (By.XPATH,"//a[normalize-space()='View Report']")
    search_viewreport_employeeID = (By.XPATH,"//input[@id='search_key']")
    department_dropdown = (By.XPATH,"//select[@id='empm_dept']")
    select_employee_dropdown = (By.XPATH,"//select[@id='user_type']")
    search_button = (By.XPATH,"//button[normalize-space()='Search']")

    def getemployee_feedback(self):
        return self.driver.find_element(*Employeefeedbackpage.employee_feedback)

    def getteam_radio_button(self):
        return self.driver.find_element(*Employeefeedbackpage.team_radio_button)

    def getselect_team_member(self):
        return self.driver.find_element(*Employeefeedbackpage.select_team_member)

    def getselect_search_bar(self):
        return self.driver.find_element(*Employeefeedbackpage.select_search_bar)

    def getemployee_radio_button(self):
        return self.driver.find_element(*Employeefeedbackpage.employee_radio_button)

    def getsearch_employeeID(self):
        return self.driver.find_element(*Employeefeedbackpage.search_employeeID)

    def getwork_radio_button(self):
        return self.driver.find_element(*Employeefeedbackpage.work_radio_button)

    def getcommunication_radio_button(self):
        return self.driver.find_element(*Employeefeedbackpage.communication_radio_button)

    def getteaminteraction_radio_button(self):
        return self.driver.find_element(*Employeefeedbackpage.teaminteraction_radio_button)

    def getpunctuality_radio_button(self):
        return self.driver.find_element(*Employeefeedbackpage.punctuality_radio_button)

    def getsubmit_button(self):
        return self.driver.find_element(*Employeefeedbackpage.submit_button)

    def getview_report(self):
        return self.driver.find_element(*Employeefeedbackpage.view_report)

    def getsearch_viewreport_employeeID(self):
        return self.driver.find_element(*Employeefeedbackpage.search_viewreport_employeeID)

    def getdepartment_dropdown(self):
        return self.driver.find_element(*Employeefeedbackpage.department_dropdown)

    def getselect_employee_dropdown(self):
        return self.driver.find_element(*Employeefeedbackpage.select_employee_dropdown)

    def getsearch_button(self):
        return self.driver.find_element(*Employeefeedbackpage.search_button)






