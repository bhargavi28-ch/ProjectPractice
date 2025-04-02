import pytest

from Utilities.BaseClass import BaseClass



@pytest.mark.usefixtures("setupbrowser")
class TestHRMSLogin(BaseClass):
    def test_login(self,setupbrowser, getData):
           driver = setupbrowser
           self.driver = setupbrowser

           self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
           self.login(getData)



           # loginpage.getemployeeID().send_keys(getData["employeeID"])
           # loginpage.getpassword().send_keys(getData["password"])
           # loginpage.getloginbutton()


    # @pytest.fixture(params= LoginpageData.test_loginpage_Data)
    # def getData(self,request):
    #     return request.param