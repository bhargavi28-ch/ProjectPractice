
from Utilities.BaseClass import BaseClass
import pytest





@pytest.mark.usefixtures("setupbrowser")
class TestHRMSLoginLogout(BaseClass):
    def test_hrmsloginlogout(self,setupbrowser,getData):
        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)
        self.logout()


