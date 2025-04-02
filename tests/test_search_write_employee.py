import time

import pytest

from PageObjects.Addemployeepage import Addemployeepage
from PageObjects.Searchemployeepage import Searchemployeepage
from TeatData.writesData import ExcelWriter, SearchemployeeData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class TestHRMSwriteemployee(BaseClass):


    def test_writeemployee(self,setupbrowser,getData,getsearchData):
        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        employeedirectorypage = Searchemployeepage(self.driver)
        employeedirectorypage.getemployee().click()
        employeedirectorypage.getemployees_button().click()
        time.sleep(20)


        employeedirectorypage.getsearch_bar().send_keys(getsearchData["empname"])
        employeedirectorypage.getsearch_button().click()

        ExcelWriter.write_employee_data("reademployee.xlsx","employee_data")



    @pytest.fixture(params= SearchemployeeData.test_search_Data)
    def getsearchData(self,request):
        return request.param



