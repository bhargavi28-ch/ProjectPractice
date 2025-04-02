import time
import unittest
from logging import getLogger

import pytest
from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver import Keys

from PageObjects.PMSpage import PMSpage
from TeatData.PMSdata import PMSdata
from Utilities.BaseClass import BaseClass



@pytest.mark.usefixtures("setupbrowser")
class TestPMS(BaseClass):


    def test_PMS(self,setupbrowser,getData,getpmsdata):
        log = self.getlogger()

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        pmspage = PMSpage(driver)

        pmspage.getpms_button().click()
        pmspage.getcreate_button().click()
        pmspage.getproject_name().send_keys(getpmsdata["project_name"])
        pmspage.getproject_code().send_keys(getpmsdata["project_code"])
        log.info("Searching for employee ID: %s", getpmsdata["employeeID"])
        pmspage.getemployee_search().send_keys(getpmsdata["employeeID"])
        time.sleep(5)
        pmspage.getemployee_search().send_keys(Keys.ARROW_DOWN)
        pmspage.getemployee_search().send_keys(Keys.ENTER)

        pmspage.getsubmit_button().click()

    @pytest.fixture(params= PMSdata.test_pms_Data)
    def getpmsdata(self,request):
        return request.param







