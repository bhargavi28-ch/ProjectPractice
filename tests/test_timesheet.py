import time

import pytest
from selenium.webdriver import Keys

from PageObjects.Timesheetpage import Timesheetpage
from TeatData.TimesheetData import TimesheetData
from Utilities.BaseClass import BaseClass
from tests.conftest import driver

pytest.mark.usefixtures("setupbrowser")
class Testtimesheet(BaseClass):


    def test_timesheet(self,setupbrowser,getData,gettimesheetdata):
        log = self.getlogger()


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        timesheetpage = Timesheetpage(driver)
        timesheetpage.gettimesheet_button().click()

        log.info("Clicked on the timesheet button")
        timesheetpage.getaddtimesheet_button().click()


        timesheetpage.getselectproject_button().click()

        # timesheetpage.getselectproject_search().send_keys(gettimesheetdata["project_search"])
        # time.sleep(5)
        # timesheetpage.getselectproject_search().send_keys(Keys.ARROW_DOWN)
        # timesheetpage.getselectproject_search().send_keys(Keys.ENTER)
        # log.info(f"Searched for project: {gettimesheetdata['project_search']}")
        timesheetpage.gettask_assigned().click()


        timesheetpage.getcreate_task().click()

        timesheetpage.gettask_name().send_keys(gettimesheetdata["task_name"])
        log.info(f"Entered task name: {gettimesheetdata['task_name']}")

        timesheetpage.getcreate_task_button().click()
        log.info("Clicked on 'Create Task' button to save the task")



    def test_taskassigned(self,gettimesheetdata):

        taskassignedpage = Timesheetpage(self.driver)
        taskassignedpage.gettimesheet_button().click()
        taskassignedpage.getaddtimesheet_button().click()

        taskassignedpage.getselectproject_button().click()

        taskassignedpage.gettask_assigned().click()
        taskassignedpage.getlogin_page_button().click()
        taskassignedpage.gettask_timings1().send_keys(gettimesheetdata["task_timings1"])
        taskassignedpage.gettask_timings2().send_keys(gettimesheetdata["task_timings2"])
        #taskassignedpage.getsave_as_draft_button().click()
        taskassignedpage.getsubmit_approval_button().click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def test_timesheetreports(self,gettimesheetdata):

        timesheetreportspage = Timesheetpage(self.driver)
        timesheetreportspage.gettimesheet_button().click()
        timesheetreportspage.getaddtimesheet_button().click()
        timesheetreportspage.gettimesheet_reports().click()
        timesheetreportspage.getself_report().click()
        timesheetreportspage.getteam_report().click()
        timesheetreportspage.getapprovals_button().click()
        timesheetreportspage.getemployees_button().click()
        timesheetreportspage.getproject_button().click()











    @pytest.fixture(params= TimesheetData.test_timesheet_Data)
    def gettimesheetdata(self,request):
        return request.param
