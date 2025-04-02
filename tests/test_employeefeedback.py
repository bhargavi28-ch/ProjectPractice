import time

import pytest
from selenium.webdriver import Keys

from PageObjects.Employeefeedbackpage import Employeefeedbackpage
from TeatData.employeefeedbackData import EmployeefeedbackData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class Testemployeefeedback(BaseClass):


    def test_employeefeedbackteam(self,setupbrowser,getData,getfeedbackData):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        feedbackpage = Employeefeedbackpage(driver)
        feedbackpage.getemployee_feedback().click()
        feedbackpage.getteam_radio_button().click()
        feedbackpage.getselect_team_member().click()



        feedbackpage.getselect_search_bar().send_keys(getfeedbackData["selectteammember"])
        # time.sleep(10)
        # feedbackpage.getselect_search_bar().send_keys(Keys.ARROW_DOWN)
        # feedbackpage.getselect_search_bar().send_keys(Keys.ENTER)
        feedbackpage.getwork_radio_button().click()
        feedbackpage.getcommunication_radio_button().click()
        feedbackpage.getteaminteraction_radio_button().click()
        feedbackpage.getpunctuality_radio_button().click()
        feedbackpage.getsubmit_button().click()


    def test_employeefeedbackemployees(self,getfeedbackData):

        employeefeedbackpage = Employeefeedbackpage(self.driver)
        employeefeedbackpage.getemployee_feedback().click()
        employeefeedbackpage.getemployee_radio_button().click()
        employeefeedbackpage.getsearch_employeeID().send_keys(getfeedbackData["select_employee"])
        employeefeedbackpage.getwork_radio_button().click()
        employeefeedbackpage.getcommunication_radio_button().click()
        employeefeedbackpage.getteaminteraction_radio_button().click()
        employeefeedbackpage.getpunctuality_radio_button().click()
        employeefeedbackpage.getsubmit_button().click()


    def test_viewreport(self,getfeedbackData):

        viewreportpage = Employeefeedbackpage(self.driver)
        viewreportpage.getemployee_feedback().click()
        viewreportpage.getview_report().click()
        viewreportpage.getsearch_viewreport_employeeID().send_keys(getfeedbackData["search_employeeID"])
        self.selectOptionByText(viewreportpage.getdepartment_dropdown(),getfeedbackData["departmentdropdown"])
        self.selectOptionByText(viewreportpage.getselect_employee_dropdown(),getfeedbackData["select_employee_dropdown"])
        viewreportpage.getsearch_button().click()








    @pytest.fixture(params= EmployeefeedbackData.test_employeefeedback_Data)
    def getfeedbackData(self,request):
        return request.param
