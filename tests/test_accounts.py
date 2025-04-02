import pytest
from selenium.webdriver import Keys

from PageObjects.Accountspage import Accountspage

from TeatData.accountsData import AccountsData
from Utilities.BaseClass import BaseClass






@pytest.mark.usefixtures("setupbrowser")
class TestAccounts(BaseClass):


    def test_accountsaddpayregister(self,setupbrowser,getData,getaccountData):


        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        accountspage = Accountspage(driver)
        accountspage.getaccounts().click()
        accountspage.getpay_register().click()
        accountspage.getadd_payregister().click()



        accountspage.getselect_month_year().send_keys(getaccountData["month"])
        accountspage.getselect_month_year().send_keys(Keys.TAB)
        accountspage.getselect_month_year().send_keys(getaccountData["year"])




        accountspage.getupload_file(AccountsData.file_input)
        accountspage.getsubmit_button().click()

    def test_viewpayslips(self,getaccountData):

        viewpayslippage = Accountspage(self.driver)
        viewpayslippage.getaccounts().click()
        viewpayslippage.getpay_register().click()
        viewpayslippage.getview_payslip_actions().click()
        viewpayslippage.getcheck_box_payslip_activation().click()
        viewpayslippage.getyes_button().click()
        #viewpayslippage.getno_button().click()
        # viewpayslippage.getsearch_employeeID().send_keys(getaccountData["search_employeeID"])
        # viewpayslippage.getsearch_employeeID_search_button().click()



    def test_payslips(self,getaccountData):

        payslipspage = Accountspage(self.driver)
        payslipspage.getaccounts().click()
        payslipspage.getpay_slips().click()
        payslipspage.getpay_slip_self().click()

        payslipspage.getpay_slip_employee().click()
        payslipspage.getemployee_search_payslip().send_keys(getaccountData["enter_employeeID"])
        payslipspage.getsearch_button().click()


    def test_employeesearchinpayregister(self,getaccountData):

        employeesearchpage = Accountspage(self.driver)
        employeesearchpage.getaccounts().click()
        employeesearchpage.getpay_register().click()
        employeesearchpage.getview_payslip_actions().click()
        employeesearchpage.getsearch_employeeID().send_keys(getaccountData["search_employeeID"])
        employeesearchpage.getsearch_employeeID_search_button().click()

    def test_viewselfdownload(self,getaccountData):

        selfviewpage = Accountspage(self.driver)
        selfviewpage.getaccounts().click()
        selfviewpage.getpay_slips().click()
        selfviewpage.getpay_slip_self().click()
        selfviewpage.getself_view().click()

    def test_viewemployeedownload(self,getaccountData):

        employeeviewpage = Accountspage(self.driver)
        employeeviewpage.getaccounts().click()
        employeeviewpage.getpay_slips().click()
        employeeviewpage.getpay_slip_employee().click()
        employeeviewpage.getemployee_search_payslip().send_keys(getaccountData["enter_employeeID"])
        employeeviewpage.getsearch_button().click()
        employeeviewpage.getemployee_view().click()





    @pytest.fixture(params= AccountsData.test_accounts_Data)
    def getaccountData(self,request):
        return request.param

