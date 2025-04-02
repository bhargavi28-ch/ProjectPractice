import pytest

from PageObjects.Bulkleavepage import Bulkleavepage
from TeatData.bulkleaveData import TestbulkleaveData
from TeatData.bulkupload import Testbulkdata
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class Testbulkleave(BaseClass):


    def test_bulkleave(self,setupbrowser,getData):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)


        bulkleavepage = Bulkleavepage(driver)
        bulkleavepage.getleavemanagemenet().click()
        bulkleavepage.getbulk_leave().click()
        bulkleavepage.getdrag_drop(TestbulkleaveData.file_input)
        bulkleavepage.getupload_button().click()