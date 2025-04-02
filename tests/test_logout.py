import pytest

from PageObjects.Logoutpage import Logoutpage
from Utilities.BaseClass import BaseClass



@pytest.mark.usefixtures("setupbrowser")
class TestHRMSLogout(BaseClass):


    def test_Logout(self,setupbrowser,getData):
        driver = setupbrowser
        self.driver = setupbrowser

        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)




        logoutpage = Logoutpage(driver)
        logoutpage.getprofile_info()
        logoutpage.getlogout_icon()

        # logoutpage.getlogout_icon()


