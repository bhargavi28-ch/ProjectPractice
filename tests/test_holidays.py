import pytest

from PageObjects.Holidayspage import Holidayspage
from TeatData.holidaysData import HolidaysData
from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setupbrowser")
class Testholidays(BaseClass):


    def test_holidayspublished(self,setupbrowser,getData,getholidayData):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        holidayspage = Holidayspage(driver)
        holidayspage.getholidays().click()
        holidayspage.getadd_holidays().click()
        self.selectOptionByText(holidayspage.getstatus(),getholidayData["status"])
        holidayspage.getyear().send_keys(getholidayData["year"])
        holidayspage.getupload_document().send_keys(HolidaysData.file_path)
        holidayspage.getsave_button().click()

    def test_holidaysedit(self,getholidayData):

        holidayeditpage = Holidayspage(self.driver)
        holidayeditpage.getholidays().click()
        holidayeditpage.getadd_holidays().click()
        holidayeditpage.getaction_edit_draft().click()
        self.selectOptionByText(holidayeditpage.getstatus_published_dropdown(),getholidayData["status1"])
        holidayeditpage.getupdate_button().click()
        holidayeditpage.getaction_edit_published().click()
        self.selectOptionByText(holidayeditpage.getstatus_draft_dropdown(),getholidayData["status2"])
        holidayeditpage.getupdate_button().click()
        holidayeditpage.getpublished_document().click()




    @pytest.fixture(params= HolidaysData.test_holidays_Data)
    def getholidayData(self,request):
        return request.param



