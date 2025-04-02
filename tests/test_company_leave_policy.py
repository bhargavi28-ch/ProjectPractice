import pytest

from PageObjects.AwardsandcertificatesPage import AwardscertificatesPage
from PageObjects.CompanyBankDetailsPage import CompanyBankdetailspage
from PageObjects.CompanyleavepolicyPage import CompanyleavepolicyPage
from TeatData.AwardsandcertificateData import AwardsandcertificatesData
from TeatData.CompanyBankDetailsData import BankdetailsData
from Utilities.BaseClass import BaseClass
from TeatData.CompanyleavepolicyData import CompanyleavepolicyData


@pytest.mark.usefixtures("setupbrowser")
class TestOrganization(BaseClass):


    def test_company_leave_policy(self,setupbrowser,getData,getleaveData):


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)


        companyleavepolicypage = CompanyleavepolicyPage(driver)

        companyleavepolicypage.getcompany_profile().click()


        companyleavepolicypage.getcompany_leave_policy().click()
        self.selectOptionByText(companyleavepolicypage.getleave_type(),getleaveData["leave_type"])
        companyleavepolicypage.getleaves_month().send_keys(getleaveData["leaves_month"])
        companyleavepolicypage.getleave_3_month().send_keys(getleaveData["leave_3_month"])
        companyleavepolicypage.getleave_6_month().send_keys(getleaveData["leave_6_month"])
        companyleavepolicypage.getleave_1_year().send_keys(getleaveData["leave_1_year"])
        companyleavepolicypage.getyes_button().click()
        companyleavepolicypage.getsave_button().click()

    @pytest.fixture(params= CompanyleavepolicyData.test_leave_Data)
    def getleaveData(self,request):
        return request.param

    def test_awards_certificates(self,getawardsData):

        companyawardcertificatespage = AwardscertificatesPage(self.driver)
        companyawardcertificatespage.getawards_certificates().click()
        self.selectOptionByText(companyawardcertificatespage.getdoc_type(),getawardsData["doc_type"])
        companyawardcertificatespage.getissue_date().send_keys(getawardsData["issue_date"])
        companyawardcertificatespage.gettitle().send_keys(getawardsData["title"])
        companyawardcertificatespage.getvalid_till().send_keys(getawardsData["valid_till"])
        companyawardcertificatespage.getcertificate_no().send_keys(getawardsData["certificate_no"])
        companyawardcertificatespage.getbrowse_document().send_keys(AwardsandcertificatesData.document_browse)
        companyawardcertificatespage.getsave_button().click()

    @pytest.fixture(params= AwardsandcertificatesData.test_awards_certificates)
    def getawardsData(self,request):
        return request.param


    def test_bank_details(self,getbankData):

        companybankdetailspage = CompanyBankdetailspage(self.driver)
        companybankdetailspage.getbank_details().click()
        self.selectOptionByText(companybankdetailspage.getbank_name(),getbankData["bank_name"])
        companybankdetailspage.getbranch_name().send_keys(getbankData["branch_name"])
        companybankdetailspage.getaccount_no().send_keys(getbankData["account_no"])
        companybankdetailspage.getifsc_code().send_keys(getbankData["ifsc_code"])
        companybankdetailspage.getbrowse_document().send_keys(BankdetailsData.document_file)
        companybankdetailspage.getsave_document().click()
        
    @pytest.fixture(params= BankdetailsData.test_bank_Data)
    def getbankData(self,request):
        return request.param