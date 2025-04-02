from selenium.webdriver.common.by import By


class Timesheetpage:
    def __init__(self,driver):
        self.driver = driver

    timesheet_button = (By.XPATH,"//span[normalize-space()='Timesheet']")
    addtimesheet_button = (By.XPATH,"//a[normalize-space()='Add Timesheet']")
    selectproject_button = (By.XPATH,"//img[@id='selectProjectImage']")
    selectproject_search = (By.ID,"findproject")
    #create_task = (By.XPATH,"//li[@id='project10']//img[@alt='Add new item required field']")
    create_task = (By.XPATH,"//li[@id='projectcreatetask10']//img[@alt='Add new item required field']")
    task_name = (By.XPATH,"//input[@placeholder='task name']")
    create_task_button = (By.XPATH,"(//button[normalize-space()='create'])[1]")

    task_assigned = (By.XPATH,"//li[@id='project10']//a[@class='has-arrow tasks']")
    login_page_button = (By.XPATH,"//li[@id='project10']//li[1]")
    task_timings1 = (By.XPATH,"//input[@name='2025-01-20']")
    task_timings2 = (By.XPATH,"//input[@name='2025-01-21']")
    save_as_draft_button = (By.XPATH,"//button[@id='savebutton']")
    submit_approval_button = (By.XPATH,"(//button[normalize-space()='Submit For Approval'])[1]")


    timesheet_reports = (By.XPATH,"//a[normalize-space()='Timesheet reports']")
    self_report = (By.XPATH,"//a[normalize-space()='Self']")
    team_report = (By.XPATH,"//a[normalize-space()='Team']")
    approvals_button = (By.XPATH,"//div[@class='main-view']//li[3]")
    employees_button = (By.XPATH,"//li[@class='emp']")
    project_button = (By.XPATH,"(//li[@class='project active'])[1]")


    def gettimesheet_button(self):
        return self.driver.find_element(*Timesheetpage.timesheet_button)

    def getaddtimesheet_button(self):
        return self.driver.find_element(*Timesheetpage.addtimesheet_button)

    def getselectproject_button(self):
        return self.driver.find_element(*Timesheetpage.selectproject_button)

    def getselectproject_search(self):
        return self.driver.find_element(*Timesheetpage.selectproject_search)

    def getcreate_task(self):
        return self.driver.find_element(*Timesheetpage.create_task)

    def gettask_name(self):
        return self.driver.find_element(*Timesheetpage.task_name)

    def getcreate_task_button(self):
        return self.driver.find_element(*Timesheetpage.create_task_button)



    def gettask_assigned(self):
        return self.driver.find_element(*Timesheetpage.task_assigned)

    def getlogin_page_button(self):
        return self.driver.find_element(*Timesheetpage.login_page_button)

    def gettask_timings1(self):
        return self.driver.find_element(*Timesheetpage.task_timings1)

    def gettask_timings2(self):
        return self.driver.find_element(*Timesheetpage.task_timings2)

    def getsave_as_draft_button(self):
        return self.driver.find_element(*Timesheetpage.save_as_draft_button)

    def getsubmit_approval_button(self):
        return self.driver.find_element(*Timesheetpage.submit_approval_button)

    def gettimesheet_reports(self):
        return self.driver.find_element(*Timesheetpage.timesheet_reports)

    def getself_report(self):
        return self.driver.find_element(*Timesheetpage.self_report)

    def getteam_report(self):
        return self.driver.find_element(*Timesheetpage.team_report)

    def getapprovals_button(self):
        return self.driver.find_element(*Timesheetpage.approvals_button)

    def getemployees_button(self):
        return self.driver.find_element(*Timesheetpage.employees_button)

    def getproject_button(self):
        return self.driver.find_element(*Timesheetpage.project_button)