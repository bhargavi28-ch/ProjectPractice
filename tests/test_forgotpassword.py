import time

import pytest

from PageObjects.Forgotpasswordpage import Forgotpasswordpage
from PageObjects.Resetpasswordpage import Resetpasswordpage
from TeatData.forgotpasswordData import ForgotpasswordData
from Utilities.BaseClass import BaseClass
from Utilities.Email_utils import Emailutils


@pytest.mark.usefixtures("setupbrowser")
class TestForgotpassword(BaseClass,Emailutils):


    def test_forgot_password(self,setupbrowser,getforgotData):


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")

        forgotpasswordpage = Forgotpasswordpage(driver)
        forgotpasswordpage.getforgotpassword_button().click()
        forgotpasswordpage.getenter_employeeID().send_keys(getforgotData["employeeID"])
        forgotpasswordpage.getsend_reset_password_link().click()
        time.sleep(5)

        reset_link = self.getreset_password_link(getforgotData["email_host"],getforgotData["email_user"],getforgotData["email_pass"])

        assert reset_link is not None
        self.driver.get(reset_link)
        time.sleep(2)


        resetpasswordpage = Resetpasswordpage(self.driver)
        resetpasswordpage.getenter_new_password().send_keys(getforgotData["new_password"])
        resetpasswordpage.getconfirm_new_password().send_keys(getforgotData["new_password"])
        resetpasswordpage.getsubmit_button().click()
        time.sleep(5)

        print("Password Reset Sucessfully")

    @pytest.fixture(params= ForgotpasswordData.test_forgot_password_Data)
    def getforgotData(self,request):
        return request.param





