import pytest

from PageObjects.Contactspage import Contactspage
from TeatData.contactsData import contactsData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class TestContacts(BaseClass):


    def test_Contactlist(self,setupbrowser,getData,getcontactData):


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        contactspage = Contactspage(driver)
        contactspage.getcontacts_button().click()
        contactspage.getcontacts_search().send_keys(getcontactData["contacts_search"])

    def test_Addcontactslist(self,getcontactData):

        addcontactspage = Contactspage(self.driver)
        addcontactspage.getcontacts_button().click()
        addcontactspage.getadd_contacts_button().click()
        addcontactspage.getcheck_box_activated().click()
        addcontactspage.getcheck_box_deactivated().click()
        addcontactspage.getsearch_employeeID_bar().send_keys(getcontactData["employeeID"])
        addcontactspage.getsearch_button().click()
        addcontactspage.getadvanced_search_dropdown().click()
        self.selectOptionByText(addcontactspage.getdepartment_dropdown(),getcontactData["department"])
        addcontactspage.getsearch_button().click()
        self.selectOptionByText(addcontactspage.getdesignation_dropdown(),getcontactData["designation"])
        addcontactspage.getsearch_button().click()
        self.selectOptionByText(addcontactspage.getactive_dropdown(),getcontactData["status_dropdown"])
        addcontactspage.getsearch_button().click()





    @pytest.fixture(params= contactsData.test_contacts_Data)
    def getcontactData(self,request):
        return request.param

