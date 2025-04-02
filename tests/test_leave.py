import time

import pytest

from PageObjects.Leavepage import Leavepage
from TeatData.LeaveData import LeaveData
from Utilities.BaseClass import BaseClass

pytest.mark.usefixtures("setupbrowser")
class Testleavemanagement(BaseClass):


    def test_applyleaveself(self,setupbrowser,getData,getleaveData):



        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        leavepage = Leavepage(driver)
        leavepage.getleavemanagement().click()
        leavepage.getapply_leave().click()
        leavepage.getself_button().click()
        self.selectOptionByText(leavepage.getleave_type(),getleaveData["leavetype"])
        leavepage.getfullday_button().click()

        leavepage.getend_date().send_keys(getleaveData["to_date"])
        leavepage.getfrom_date().send_keys(getleaveData["from_date"])


        leavepage.getapply_leave_button().click()


    def test_applyleaveemployee(self,getleaveData):

        leaveemployeepage = Leavepage(self.driver)
        leaveemployeepage.getleavemanagement().click()
        leaveemployeepage.getapply_leave().click()
        leaveemployeepage.getemployee_button().click()
        self.selectOptionByText(leaveemployeepage.getselect_employee_dropdown(),getleaveData["employeename"])
        self.selectOptionByText(leaveemployeepage.getleave_type(),getleaveData["leave_type"])
        leaveemployeepage.getfullday_button().click()
        leaveemployeepage.getend_date().send_keys(getleaveData["end_date"])
        leaveemployeepage.getfrom_date().send_keys(getleaveData["start_date"])
        time.sleep(20)


        leaveemployeepage.getapply_leave_button().click()


    def test_selfreports(self,getleaveData):

        selfreportspage = Leavepage(self.driver)
        selfreportspage.getleavemanagement().click()
        selfreportspage.getleavereport().click()
        selfreportspage.getselfreport_button().click()
        self.selectOptionByText(selfreportspage.getself_leavetype_dropdown(),getleaveData["leavetype"])
        self.selectOptionByText(selfreportspage.getself_status_dropdown(),getleaveData["status_type"])
        selfreportspage.getself_search_button().click()

    def test_teamreports(self,getleaveData):

        teamreportpage = Leavepage(self.driver)
        teamreportpage.getleavemanagement().click()
        teamreportpage.getleavereport().click()
        teamreportpage.getteamreport_button().click()
        teamreportpage.getteam_monthly_button().click()
        teamreportpage.getteam_summary_button().click()

    def test_employeereports(self,getleaveData):

        employeereports = Leavepage(self.driver)
        employeereports.getleavemanagement().click()
        employeereports.getleavereport().click()
        employeereports.getemployeereport_button().click()
        employeereports.getemployee_monthly_button().click()
        employeereports.getemployee_summary_button().click()


    def test_approvals(self,getleaveData):

        approvalspage = Leavepage(self.driver)
        approvalspage.getleavemanagement().click()
        approvalspage.getleavereport().click()
        approvalspage.getapprovalsreport_button().click()
        approvalspage.getapprovals_search().send_keys(getleaveData["approvals_employeeID"])
        approvalspage.getapprovals_search_button().click()
        approvalspage.getapprovals_approve_button().click()
        approvalspage.getapprovals_accept_no_button().click()






    @pytest.fixture(params= LeaveData.test_leave_Data)
    def getleaveData(self,request):
        return request.param
