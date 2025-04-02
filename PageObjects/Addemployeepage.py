from selenium.webdriver.common.by import By


class Addemployeepage:
    def __init__(self,driver):
        self.driver = driver


    employee = (By.XPATH,"//span[text()='Employee']")
    addemployee = (By.XPATH,"//a[normalize-space()='Add Employee']")
    firstname = (By.NAME,"first_name")
    lastname = (By.NAME,"last_name")
    fathername = (By.NAME,"father_name")
    relationtype_dp = (By.ID,"relation_type")
    gender_dp = (By.XPATH,"//select[@name='gender']")
    marrital_status = (By.XPATH,"//select[@name='marital_status']")
    emprole_dp = (By.XPATH,"//select[@name='role']")
    isreportingmanager_dp = (By.XPATH,"//select[@id='is_reporting_manager']")
    mobile_number = (By.XPATH,"//input[@id='mobile']")
    company_email = (By.XPATH,"//input[@id='company_email']")
    personal_email = (By.XPATH,"//input[@id='personal_email']")
    dob = (By.XPATH,"//input[@id='dob']")
    nationality_dp = (By.XPATH,"//select[@id='nationality']")
    save_button = (By.XPATH,"//button[@id='save']")
    sucess_alert = (By.XPATH,"//div[@class='alert alert-success']")
    error_alert = (By.XPATH,"//div[@class='alert alert-danger']")





    def getemployee(self):
        return self.driver.find_element(*Addemployeepage.employee)

    def getaddemployee(self):
        return self.driver.find_element(*Addemployeepage.addemployee)


    def getfirstname(self):
        return self.driver.find_element(*Addemployeepage.firstname)

    def getlastname(self):
        return self.driver.find_element(*Addemployeepage.lastname)

    def getfathername(self):
        return self.driver.find_element(*Addemployeepage.fathername)

    def getrelationtype_dp(self):
        return self.driver.find_element(*Addemployeepage.relationtype_dp)

    def getgender_dp(self):
        return self.driver.find_element(*Addemployeepage.gender_dp)

    def getmarrital_status(self):
        return self.driver.find_element(*Addemployeepage.marrital_status)

    def getemprole_dp(self):
        return self.driver.find_element(*Addemployeepage.emprole_dp)

    def getisreportingmanager_dp(self):
        return self.driver.find_element(*Addemployeepage.isreportingmanager_dp)

    def getmobile_number(self):
        return self.driver.find_element(*Addemployeepage.mobile_number)

    def getcompany_email(self):
        return self.driver.find_element(*Addemployeepage.company_email)

    def getpersonal_email(self):
        return self.driver.find_element(*Addemployeepage.personal_email)

    def getdob(self):
        return self.driver.find_element(*Addemployeepage.dob)

    def getnationality_dp(self):
        return self.driver.find_element(*Addemployeepage.nationality_dp)

    def getsave_button(self):
        return self.driver.find_element(*Addemployeepage.save_button).click()

    def getsucess_alert(self):
        return self.driver.find_element(*Addemployeepage.sucess_alert).text

    def geterror_alert(self):
        return self.driver.find_element(*Addemployeepage.error_alert).text
































