import pytest
from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType

from PageObjects.Addemployeepage import Addemployeepage
from PageObjects.Assertpage import Assertdetailspage
from PageObjects.Companyinfopage import Companyinformation
from PageObjects.Contactdetailspage import Contactdetailspage
from PageObjects.Documentspage import Documentspage
from PageObjects.Exitdetailspage import Exitdetailspage
from PageObjects.Experiencedetailspage import Experiencedetailspage
from PageObjects.Familydetailspage import Familydetailspage
from PageObjects.quaificationdetailspage import  Qualificationdetailspage
from TeatData.Assertdata import AssertdetailsData
from TeatData.companyinfodata import CompanyinfoData
from TeatData.contactdetailsdata import ContactdetailsData
from TeatData.documentsdata import DocumentsData
from TeatData.exceladdemployeedata import getTestData
from TeatData.exitdetailsdata import ExitdetailsData
from TeatData.experiencedetailsData import ExperiencedetailsData
from TeatData.familydetailsdata import FamilydetailsData
from TeatData.qualificatindetailsdata import QualificationData
from Utilities.BaseClass import BaseClass
from tests.conftest import driver
import allure


@pytest.mark.usefixtures("setupbrowser")
@allure.severity(allure.severity_level.NORMAL)
class Testcompanyinformation(BaseClass):

    @allure.severity(allure.severity_level.MINOR)
    def test_companyinformation(self,setupbrowser,getData,getcompanydata):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        addemployeepage = Addemployeepage(driver)
        addemployeepage.getemployee().click()
        addemployeepage.getaddemployee().click()

        companyinformationpage = Companyinformation(self.driver)
        companyinformationpage.getcompany_information_button().click()
        companyinformationpage.getdateofjoin().send_keys(getcompanydata["dateofjoin"])

        self.selectOptionByText(companyinformationpage.getdepartment(),getcompanydata["department"])
        self.selectOptionByText(companyinformationpage.getdesignation(),getcompanydata["designation"])
        self.selectOptionByText(companyinformationpage.getemployeement_type(),getcompanydata["employeementtype"])
        self.selectOptionByText(companyinformationpage.getworklocation(),getcompanydata["worklocation"])
        self.selectOptionByText(companyinformationpage.getshifttiming(),getcompanydata["shifttiming"])
        self.selectOptionByText(companyinformationpage.getreporting_manager(),getcompanydata["reporting_manager"])
        self.selectOptionByText(companyinformationpage.getreportingmanager2(),getcompanydata["reporting_manager2"])

        companyinformationpage.getsave_button().click()

    @pytest.fixture(params= CompanyinfoData.test_companyinfo_Data)
    def getcompanydata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_familydetails(self,getfamilydata):

        familydetailspage = Familydetailspage(self.driver)
        familydetailspage.getfamilydetails_button().click()
        familydetailspage.getname().send_keys(getfamilydata["name"])
        familydetailspage.getcontactnumber().send_keys(getfamilydata["contactnumber"])

        self.selectOptionByText(familydetailspage.getrelation_type(),getfamilydata["relationtype"])
        self.selectOptionByText(familydetailspage.getinsurance_covered(),getfamilydata["insurance_covered"])

        familydetailspage.getdateofbirth().send_keys(getfamilydata["dateofbirth"])

    @pytest.fixture(params= FamilydetailsData.test_familydetais)
    def getfamilydata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_qualificationdetails(self,getqualificationdata):

        qualificationpage = Qualificationdetailspage(self.driver)
        qualificationpage.getaddqualification_button().click()
        qualificationpage.getqualification().send_keys(getqualificationdata["qualification"])
        qualificationpage.getyearofpassing().send_keys(getqualificationdata["yearofpassing"])
        qualificationpage.getcollegedetails().send_keys(getqualificationdata["college"])
        qualificationpage.getpercentage().send_keys(getqualificationdata["percentage"])
        qualificationpage.getuniversity().send_keys(getqualificationdata["university"])

    @pytest.fixture(params= QualificationData.test_qualification_Data)
    def getqualificationdata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_experiencedetails(self,getexperiencedata):

        expeiencedetailspage = Experiencedetailspage(self.driver)
        expeiencedetailspage.getexperience_details_button().click()
        expeiencedetailspage.getcompany().send_keys(getexperiencedata["company"])
        expeiencedetailspage.getjoining_date().send_keys(getexperiencedata["join_date"])
        expeiencedetailspage.getdesignation().send_keys(getexperiencedata["designation"])
        expeiencedetailspage.getleft_date().send_keys(getexperiencedata["left_date"])
        expeiencedetailspage.getlocation().send_keys(getexperiencedata["location"])

    @pytest.fixture(params= ExperiencedetailsData.test_experiencedetails_Data)
    def getexperiencedata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_assertdetails(self,getassertdata):

        assertdeatilspage = Assertdetailspage(self.driver)
        assertdeatilspage.getassert_button().click()
        self.selectOptionByText(assertdeatilspage.getassert_type(),getassertdata["asserttype"])
        self.selectOptionByText(assertdeatilspage.getassert_alloted(),getassertdata["assertalloted"])
        assertdeatilspage.getallotment_date().send_keys(getassertdata["alloted_date"])

    @pytest.fixture(params= AssertdetailsData.test_assert_Data)
    def getassertdata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_contactdetails(self,getcontactdata):

        contactdetailspage = Contactdetailspage(self.driver)
        contactdetailspage.getcontact_information_button().click()
        contactdetailspage.getper_add1().send_keys(getcontactdata["per_add1"])
        contactdetailspage.getper_add2().send_keys(getcontactdata["per_add2"])
        contactdetailspage.getper_city().send_keys(getcontactdata["per_city"])
        self.selectOptionByText(contactdetailspage.getper_country(),getcontactdata["per_country"])
        self.selectOptionByText(contactdetailspage.getper_state(),getcontactdata["per_state"])
        self.selectOptionByText(contactdetailspage.getper_district(),getcontactdata["per_district"])
        contactdetailspage.getper_pincode().send_keys(getcontactdata["per_pincode"])

        contactdetailspage.getcheck_box().click()
        contactdetailspage.getcontact_person().send_keys(getcontactdata["contact_person"])
        self.selectOptionByText(contactdetailspage.getrelation_type(),getcontactdata["relation_type"])
        contactdetailspage.getmobile_number().send_keys(getcontactdata["mobile"])
        contactdetailspage.getaddress().send_keys(getcontactdata["address"])

    @pytest.fixture(params= ContactdetailsData.test_contactdetails_Data)
    def getcontactdata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_documentsdetails(self,getdocumentsdata):

        documentspage = Documentspage(self.driver)



        documentspage.getdocuments_button().click()
        # button = documentspage.getdocuments_button()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        # button.click()

        self.selectOptionByText(documentspage.getdocument_type(),getdocumentsdata["document_type"])
        documentspage.getdocument_ID().send_keys(getdocumentsdata["document_ID"])

        documentspage.getupload_document().send_keys(DocumentsData.file_path)
        documentspage.getupload_button().click()
        allure.attach(self.driver.get_full_page_screenshot_as_png(),name="testcompanydetails",
                      attachment_type=AttachmentType.PNG)

    @pytest.fixture(params= DocumentsData.test_documents_Data)
    def getdocumentsdata(self,request):
        return request.param

    @allure.severity(allure.severity_level.NORMAL)
    def test_exitdetails(self,getexitdata):

        exitdetailspage = Exitdetailspage(self.driver)
        exitdetailspage.getexit_button().click()
        #button = exitdetailspage.getexit_button()
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        # button.click()
        exitdetailspage.getresignation_date().send_keys(getexitdata["resignationdate"])
        self.selectOptionByText(exitdetailspage.getnotice_period(),getexitdata["notice_period"])
        self.selectOptionByText(exitdetailspage.getexit_type(),getexitdata["exit_type"])
        exitdetailspage.getsave_button().click()


    @pytest.fixture(params= ExitdetailsData.test_exit_Data)
    def getexitdata(self,request):
        return request.param