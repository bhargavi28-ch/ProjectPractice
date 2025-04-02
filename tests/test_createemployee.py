
from datetime import datetime, date

import pytest

from PageObjects.Addemployeepage import Addemployeepage
from Utilities.BaseClass import BaseClass
from selenium.common import NoSuchElementException

from Utilities.Excelutils import Excelutils

file_path = "C:\\Users\\Dell\\OneDrive - paccore\\Desktop\\twoemployees.xlsx"
sheetName = "Data1"

@pytest.mark.usefixtures("setupbrowser")
class Testcreateemployee(BaseClass,Excelutils):

    def test_addemployee(self,setupbrowser,getData):

        driver = setupbrowser
        self.driver = setupbrowser
        self.navigate_to_url("https://infotimeqa.azurewebsites.net/")
        self.login(getData)

        addemployeepage = Addemployeepage(driver)
        addemployeepage.getemployee().click()
        addemployeepage.getaddemployee().click()

        row_count = Excelutils.getRowcount(file_path,sheetName)


        for row in range(2,row_count+1):
            firstname = str(Excelutils.readData(file_path,sheetName,row,2))
            lastname =  str(Excelutils.readData(file_path,sheetName,row,3))
            fathername =  str(Excelutils.readData(file_path,sheetName,row,4))
            relationtype_dp = str(Excelutils.readData(file_path,sheetName,row,5))
            gender_dp = str(Excelutils.readData(file_path,sheetName,row,6))
            marrital_status = str(Excelutils.readData(file_path,sheetName,row,7))
            emprole_dp = str(Excelutils.readData(file_path,sheetName,row,8))
            isreportingmanager_dp = str(Excelutils.readData(file_path,sheetName,row,9))
            mobile_number = str(Excelutils.readData(file_path,sheetName,row,10))
            company_email = str(Excelutils.readData(file_path,sheetName,row,11))
            personal_email = str(Excelutils.readData(file_path,sheetName,row,12))
            dob = Excelutils.readData(file_path,sheetName,row,13)
            nationality_dp = str(Excelutils.readData(file_path,sheetName,row,14))



            personalinformation = Addemployeepage(self.driver)
            personalinformation.getfirstname().clear()
            personalinformation.getfirstname().send_keys(firstname)

            personalinformation.getlastname().clear()
            personalinformation.getlastname().send_keys(lastname)

            personalinformation.getfathername().clear()
            personalinformation.getfathername().send_keys(fathername)

            self.selectOptionByText(personalinformation.getrelationtype_dp(),relationtype_dp)
            self.selectOptionByText(personalinformation.getgender_dp(),gender_dp)
            self.selectOptionByText(personalinformation.getmarrital_status(),marrital_status)
            self.selectOptionByText(personalinformation.getemprole_dp(),emprole_dp)
            self.selectOptionByText(personalinformation.getisreportingmanager_dp(),isreportingmanager_dp)

            personalinformation.getmobile_number().clear()
            personalinformation.getmobile_number().send_keys(mobile_number)

            personalinformation.getcompany_email().clear()
            personalinformation.getcompany_email().send_keys(company_email)

            personalinformation.getpersonal_email().clear()
            personalinformation.getpersonal_email().send_keys(personal_email)



            if isinstance(dob, (datetime, date)):
                dob_str = dob.strftime("%d-%m-%Y")
                personalinformation.getdob().clear()
                personalinformation.getdob().send_keys(dob_str)

            else:
                personalinformation.getdob().clear()
                personalinformation.getdob().send_keys(dob)
            # if isinstance(dob, (datetime, date)):
            #     dob = dob.strftime("%d-%m-%Y")

            # personalinformation.getdob().send_keys(dob)



            self.selectOptionByText(personalinformation.getnationality_dp(),nationality_dp)
            personalinformation.getsave_button()
            # if save_button and save_button.is_enabled():
            #     save_button.click()
            #     print("Clicked Save button successfully.")
            # else:
            #     print("Save button is either not found or disabled.")




            personal_information = Addemployeepage(self.driver)
            try:
                sucess_alert = personal_information.getsucess_alert()
                if sucess_alert:

                    Excelutils.writeData(file_path,sheetName,2,15,"Created")
                    # if "successfully saved" in sucess_alert:
                    print(f"Success: {sucess_alert}")
                else:
                    print("No success alert found.")


            except NoSuchElementException:
                try:
                    error_alert = personal_information.geterror_alert()
                    if error_alert:
                        Excelutils.writeData(file_path,sheetName,2,15,"already exists")
                        # if "already exists" in error_alert:
                        print(f"Error: {error_alert}")
                    else:
                        print(f"already exists: {error_alert}")
                except NoSuchElementException:
                    print("No success or error message found.")












