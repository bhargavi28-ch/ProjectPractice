from selenium.webdriver.common.by import By


class Contactdetailspage:
    def __init__(self,driver):
        self.driver = driver

    contact_information_button = (By.LINK_TEXT,"Contact Information")
    per_add1 = (By.XPATH,"//input[@id='paddr1']")
    per_add2 = (By.XPATH,"//input[@id='paddr2']")
    per_city = (By.XPATH,"//input[@id='pcity']")
    per_country = (By.XPATH,"//select[@id='pcountry']")
    per_state = (By.XPATH,"//select[@id='pstate']")
    per_district = (By.XPATH,"//select[@id='pdistrict']")
    per_pincode = (By.XPATH,"//input[@id='ppincode']")
    check_box = (By.XPATH,"//label[normalize-space()='same as permanent address']")
    # pre_add1 = (By.XPATH,"//input[@id='caddr1']")
    # pre_add2 = (By.XPATH,"//input[@id='caddr2']")
    # pre_city = (By.XPATH,"//input[@id='ccity']")
    # pre_country = (By.XPATH,"//select[@id='ccountry']")
    # pre_state = (By.XPATH,"//select[@id='cstate']")
    # pre_district = (By.XPATH,"//select[@id='cdistrict']")
    # pre_pincode = (By.XPATH,"//input[@id='cpincode']")
    contact_person = (By.XPATH,"//input[@id='contact_person']")
    relation_type = (By.XPATH,"//select[@id='relation']")
    mobile_number = (By.XPATH,"//input[@id='emrg_mobile']")
    address = (By.XPATH,"//textarea[@id='emerg_addr']")

    def getcontact_information_button(self):
        return self.driver.find_element(*Contactdetailspage.contact_information_button)

    def getper_add1(self):
        return self.driver.find_element(*Contactdetailspage.per_add1)

    def getper_add2(self):
        return self.driver.find_element(*Contactdetailspage.per_add2)

    def getper_city(self):
        return self.driver.find_element(*Contactdetailspage.per_city)

    def getper_country(self):
        return self.driver.find_element(*Contactdetailspage.per_country)

    def getper_state(self):
        return self.driver.find_element(*Contactdetailspage.per_state)

    def getper_district(self):
        return self.driver.find_element(*Contactdetailspage.per_district)

    def getper_pincode(self):
        return self.driver.find_element(*Contactdetailspage.per_pincode)

    def getcheck_box(self):
        return self.driver.find_element(*Contactdetailspage.check_box)

    # def getpre_add1(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_add1)
    #
    # def getpre_add2(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_add2)
    #
    # def getpre_city(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_city)
    #
    # def getpre_country(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_country)
    #
    # def getpre_state(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_state)
    #
    # def getpre_district(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_district)
    #
    # def getpre_pincode(self):
    #     return self.driver.find_element(*Contactdetailspage.pre_pincode)

    def getcontact_person(self):
        return self.driver.find_element(*Contactdetailspage.contact_person)

    def getrelation_type(self):
        return self.driver.find_element(*Contactdetailspage.relation_type)

    def getmobile_number(self):
        return self.driver.find_element(*Contactdetailspage.mobile_number)

    def getaddress(self):
        return self.driver.find_element(*Contactdetailspage.address)