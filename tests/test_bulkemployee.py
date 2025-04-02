import pytest

from PageObjects.Bulkemployeepage import Bulkemployeepage
from TeatData.bulkupload import Testbulkdata
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class Testbulkemployee(BaseClass):


    def test_bulkemployee(self,setupbrowser,getData):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        bulkemployeepage = Bulkemployeepage(driver)
        bulkemployeepage.getemployee()
        bulkemployeepage.getbulk_import()
        #bulkemployeepage.getdownload_sample()
        bulkemployeepage.getfile_input(Testbulkdata.FILE_PATH)
        bulkemployeepage.getdownload_button()

        try:
            bulkemployeepage.getsuccess_message()
            print("Upload Successful")
        except:
            try:
                bulkemployeepage.getexisting_message()
                print("Data already exists")
            except:
                print("Upload failed")








