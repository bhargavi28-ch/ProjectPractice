from selenium.webdriver.common.by import By


class Leavepage:
    def __init__(self,driver):
        self.driver = driver

    leavemanagement = (By.XPATH,"//span[normalize-space()='Leave Management']")
    apply_leave = (By.XPATH,"//a[normalize-space()='Apply Leave']")
    self_button = (By.XPATH,"//label[normalize-space()='Self']")
    employee_button = (By.XPATH,"//label[normalize-space()='Employee']")
    select_employee_dropdown = (By.XPATH,"//select[@id='leave_emp_id']")
    leave_type = (By.XPATH,"//select[@id='leave_type']")
    fullday_button = (By.XPATH,"//label[normalize-space()='Full Day']")
    halfday_btton = (By.XPATH,"//label[normalize-space()='Half Day']")
    from_date = (By.XPATH,"//input[@id='start_date']")
    end_date = (By.XPATH,"//input[@id='end_date']")
    noof_days = (By.XPATH,"(//div[@class='form-field'])[9]")
    apply_leave_button = (By.XPATH,"//button[@id='apply']")


    leavereport = (By.XPATH,"//a[normalize-space()='Leave Report']")

    
    selfreport_button = (By.XPATH,"//a[normalize-space()='Self']")
    self_leavetype_dropdown = (By.XPATH, "//select[@id='lv_type']")
    self_status_dropdown = (By.XPATH, "//select[@id='lv_sts']")
    self_search_button = (By.XPATH, "//button[@onclick='self_leave_search()']")

    teamreport_button =(By.XPATH,"//a[normalize-space()='Team']")
    team_summary_button = (By.XPATH, "//a[@href='#team_summary']")
    team_monthly_button = (By.XPATH, "//a[@href='#team_monthly']")

    employeereport_button = (By.XPATH,"//a[@role='tab'][normalize-space()='Employees']")
    employee_monthly_button = (By.XPATH, "//a[@href='#emp_monthly']")
    employee_summary_button = (By.XPATH, "//a[@href='#emp_summary']")

    approvalsreport_button = (By.XPATH,"//a[@href='/leaves/pending ']")
    approvals_search = (By.XPATH,"//input[@id='pending_emp']")
    approvals_search_button = (By.XPATH,"//button[normalize-space()='Search']")
    approvals_approve_button = (By.XPATH,"//tbody/tr[1]/td[13]/a[1]/i[1]")
    approvals_reject_button = (By.XPATH,"//tbody/tr[1]/td[13]/a[2]")
    approvals_accept_yes_button = (By.XPATH,"//button[@id='status_submit']")
    approvals_no_button = (By.XPATH,"//button[normalize-space()='No']")








    def getleavemanagement(self):
        return self.driver.find_element(*Leavepage.leavemanagement)

    def getapply_leave(self):
        return self.driver.find_element(*Leavepage.apply_leave)

    def getself_button(self):
        return self.driver.find_element(*Leavepage.self_button)

    def getemployee_button(self):
        return self.driver.find_element(*Leavepage.employee_button)

    def getselect_employee_dropdown(self):
        return self.driver.find_element(*Leavepage.select_employee_dropdown)

    def getleave_type(self):
        return self.driver.find_element(*Leavepage.leave_type)

    def getfullday_button(self):
        return self.driver.find_element(*Leavepage.fullday_button)

    def gethalfday_button(self):
        return self.driver.find_element(*Leavepage.halfday_btton)

    def getfrom_date(self):
        return self.driver.find_element(*Leavepage.from_date)

    def getend_date(self):
        return self.driver.find_element(*Leavepage.end_date)

    def getnoof_days(self):
        return self.driver.find_element(*Leavepage.noof_days)

    def getapply_leave_button(self):
        return self.driver.find_element(*Leavepage.apply_leave_button)


    def getleavereport(self):
        return self.driver.find_element(*Leavepage.leavereport)

    def getselfreport_button(self):
        return self.driver.find_element(*Leavepage.selfreport_button)

    def getteamreport_button(self):
        return self.driver.find_element(*Leavepage.teamreport_button)

    def getemployeereport_button(self):
        return self.driver.find_element(*Leavepage.employeereport_button)

    def getapprovalsreport_button(self):
        return self.driver.find_element(*Leavepage.approvalsreport_button)

    def getapprovals_search(self):
        return self.driver.find_element(*Leavepage.approvals_search)

    def getapprovals_search_button(self):
        return self.driver.find_element(*Leavepage.approvals_search_button)

    def getself_leavetype_dropdown(self):
        return self.driver.find_element(*Leavepage.self_leavetype_dropdown)

    def getself_status_dropdown(self):
        return self.driver.find_element(*Leavepage.self_status_dropdown)

    def getself_search_button(self):
        return self.driver.find_element(*Leavepage.self_search_button)

    def getteam_monthly_button(self):
        return self.driver.find_element(*Leavepage.team_monthly_button)


    def getteam_summary_button(self):
        return self.driver.find_element(*Leavepage.team_summary_button)

    def getapprovals_approve_button(self):
        return self.driver.find_element(*Leavepage.approvals_approve_button)

    def getapprovals_reject_button(self):
        return self.driver.find_element(*Leavepage.approvals_reject_button)

    def getapprovals_accept_yes_button(self):
        return self.driver.find_element(*Leavepage.approvals_accept_yes_button)

    def getapprovals_accept_no_button(self):
        return self.driver.find_element(*Leavepage.approvals_no_button)

    def getemployee_monthly_button(self):
        return self.driver.find_element(*Leavepage.employee_monthly_button)

    def getemployee_summary_button(self):
        return self.driver.find_element(*Leavepage.employee_monthly_button)







