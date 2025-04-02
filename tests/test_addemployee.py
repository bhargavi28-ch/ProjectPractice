from datetime import datetime, date
import pytest
from selenium.common import NoSuchElementException
from PageObjects.Addemployeepage import Addemployeepage
from TeatData.AddemployeepageData import AddemployepageData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class Testaddemployee(BaseClass):

    def test_addemployee(self,setupbrowser,getData,getdata):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        addemployeepage = Addemployeepage(driver)
        addemployeepage.getemployee().click()
        addemployeepage.getaddemployee().click()

        personalinformation = Addemployeepage(self.driver)
        personalinformation.getfirstname().send_keys(getdata["firstname"])
        personalinformation.getlastname().send_keys(getdata["lastname"])
        personalinformation.getfathername().send_keys(getdata["fathername"])

        self.selectOptionByText(personalinformation.getrelationtype_dp(),getdata["relationtype_dp"])
        self.selectOptionByText(personalinformation.getgender_dp(),getdata["gender_dp"])
        self.selectOptionByText(personalinformation.getmarrital_status(),getdata["marrital_status"])
        self.selectOptionByText(personalinformation.getemprole_dp(),"Employee")
        self.selectOptionByText(personalinformation.getisreportingmanager_dp(),"False")

        personalinformation.getmobile_number().send_keys(getdata["mobile_number"])
        personalinformation.getcompany_email().send_keys(getdata["company_email"])
        personalinformation.getpersonal_email().send_keys(getdata["personal_email"])

        dob = getdata["dob"]
        if isinstance(dob, (datetime, date)):
            dob_str = dob.strftime("%d-%m-%Y")
            personalinformation.getdob().send_keys(dob_str)

        else:
            personalinformation.getdob().send_keys(dob)

            # personalinformation.getdob().send_keys(getdata["dob"])

        self.selectOptionByText(personalinformation.getnationality_dp(),"Indian")
        personalinformation.getsave_button()

        personal_information = Addemployeepage(self.driver)

        try:
            sucess_alert = personal_information.getsucess_alert()
            if "successfully saved" in sucess_alert:
                print(f"Success: {sucess_alert}")
            else:
                print(f"Successfully saved: {sucess_alert}")


        except NoSuchElementException:
            try:
                error_alert = personal_information.geterror_alert()
                if "already exists" in error_alert:
                    print(f"Error: {error_alert}")
                else:
                    print(f"already exists: {error_alert}")
            except NoSuchElementException:
                print("No success or error message found.")

    @pytest.fixture(params=AddemployepageData.getTestData())
    def getdata(self,request):
        return request.param

