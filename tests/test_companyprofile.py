import pytest

from PageObjects.Companyaddresspage import Companyaddresspage
from PageObjects.CreatecompanyPage import Createcompanypage
from PageObjects.StatutoryregistrationPage import Statutoryregistrationpage
from PageObjects.TaxinformationPage import TaxinformationPage
from PageObjects.contactinformationpage import Contactinformationpage
from TeatData.CompanyaddressData import CompanyaddressData
from TeatData.TaxinformationData import TaxinformationData
from TeatData.contactinformationData import ContactinformationData
from TeatData.cretaecompanyData import CreatecompanyData
from TeatData.statutoryregistrationData import StatutoryregistrationData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class TestOrganization(BaseClass):


    def test_create_company(self,setupbrowser,getData,getcreateData):


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        createcompanypage = Createcompanypage(driver)
        self.selectOptionByText(createcompanypage.getselect_company_dropdown(),getcreateData["select_company"])
        createcompanypage.getcompany_profile().click()

    @pytest.fixture(params= CreatecompanyData.test_create_company_Data)
    def getcreateData(self,request):
        return request.param

    def test_contact_information(self ,getcontactData):


        contactinformationpage = Contactinformationpage(self.driver)



        contactinformationpage.getcompany_profile().click()
        contactinformationpage.getcontact_information().click()
        contactinformationpage.getedit_button().click()
        contactinformationpage.gethead_of_the_company().send_keys(getcontactData["head_of_the_company"])
        contactinformationpage.getprofile_pic(ContactinformationData.profile_pic)
        contactinformationpage.gethead_designation().send_keys(getcontactData["head_designation"])
        contactinformationpage.gethead_contact_no().send_keys(getcontactData["head_contact_no"])
        contactinformationpage.getcompany_website().send_keys(getcontactData["Company_Website"])
        contactinformationpage.getcompany_email().send_keys(getcontactData["Company_Email_Address"])
        contactinformationpage.getnotification_email().send_keys(getcontactData["Notification Emails"])
        #contactinformationpage.getsave_button().click()
        contactinformationpage.getupdate_button().click()

    @pytest.fixture(params= ContactinformationData.test_contactinformation_Data)
    def getcontactData(self,request):
        return request.param

    def test_tax_information(self,gettaxData):


        taxinformationpage = TaxinformationPage(self.driver)
        taxinformationpage.gettax_information().click()
        self.selectOptionByText(taxinformationpage.gettax_type(),gettaxData["tax_type"])
        taxinformationpage.getregistration_no().send_keys(gettaxData["registration_no"])
        taxinformationpage.getbrowse_button().send_keys(TaxinformationData.file_path)
        taxinformationpage.getsave_button().click()

    @pytest.fixture(params= TaxinformationData.test_tax_information_Data)
    def gettaxData(self,request):
        return request.param

    def test_statutory_registration(self,getstatuData):

        statutorypage = Statutoryregistrationpage(self.driver)
        statutorypage.getstatutoryregistration_button().click()
        self.selectOptionByText(statutorypage.getsta_reg_type(),getstatuData["reg_type"])
        statutorypage.getsta_reg_no().send_keys(getstatuData["reg_no"])
        statutorypage.getbrowse_button().send_keys(StatutoryregistrationData.browse_document)
        statutorypage.getsave_button().click()

    @pytest.fixture(params= StatutoryregistrationData.test_reg_Data)
    def getstatuData(self,request):
        return request.param

    def test_company_address(self,getcompaddData):

        companyaddpage = Companyaddresspage(self.driver)
        companyaddpage.getcompany_postal_address().click()
        #companyaddpage.getedit_button().click()
        companyaddpage.getadd_line1().send_keys(getcompaddData["add_line1"])
        companyaddpage.getadd_line2().send_keys(getcompaddData["add_line2"])
        self.selectOptionByText(companyaddpage.getcountry_dropdown(),getcompaddData["country"])
        self.selectOptionByText(companyaddpage.getstate_dropdown(),getcompaddData["state"])
        self.selectOptionByText(companyaddpage.getcity_dropdown(),getcompaddData["city"])
        companyaddpage.getpincode().send_keys(getcompaddData["pincode"])
        companyaddpage.getupdate_button().click()

    @pytest.fixture(params= CompanyaddressData.test_address_Data)
    def getcompaddData(self,request):
        return request.param












