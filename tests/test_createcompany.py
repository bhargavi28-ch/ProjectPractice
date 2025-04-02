

import pytest

from PageObjects.CreatecompanyPage import Createcompanypage

from TeatData.cretaecompanyData import CreatecompanyData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class TestOrganization(BaseClass):


    def test_create_company(self,setupbrowser,getData,getcreateData):


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        createcompanypage = Createcompanypage(driver)

        createcompanypage.getcreate_company_dropdown().click()
        createcompanypage.getupload_Profile(CreatecompanyData.upload_file)
        createcompanypage.getcompany_name().send_keys(getcreateData["Company_Name"])
        createcompanypage.getshort_name().send_keys(getcreateData["Short_Name"])
        self.selectOptionByText(createcompanypage.getcompany_type(),getcreateData["Company_Type"])
        createcompanypage.getcompany_registration_number().send_keys(getcreateData["Company_Registration_No."])
        createcompanypage.getdate_of_registration().send_keys(getcreateData["Date_of_Registration"])

        createcompanypage.getregistration_type().send_keys(getcreateData["Registration_Type"])
        createcompanypage.getbusiness_nature().send_keys(getcreateData["Nature_of_Business"])
        createcompanypage.getallows_leaves_per_month().send_keys(getcreateData["Allowed_Leaves_Per_Month"])
        createcompanypage.getsave_button().click()

    @pytest.fixture(params= CreatecompanyData.test_create_company_Data)
    def getcreateData(self,request):
        return request.param



    