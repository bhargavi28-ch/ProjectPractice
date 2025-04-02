import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Searchemployeepage:
    def __init__(self,driver):
        self.driver = driver

    employee = (By.XPATH, "//span[text()='Employee']")
    employees_button = (By.XPATH, "//a[normalize-space()='Employees']")
    search_bar = (By.XPATH, "//input[@id='search_key']")
    search_button = (By.XPATH, "//button[normalize-space()='Search']")

    def getemployee(self):
        return self.driver.find_element(*Searchemployeepage.employee)

    def getemployees_button(self):
        return self.driver.find_element(*Searchemployeepage.employees_button)

    def getsearch_bar(self):
        return self.driver.find_element(*Searchemployeepage.search_bar)



    def getsearch_button(self):
        return self.driver.find_element(*Searchemployeepage.search_button)

