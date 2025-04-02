from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Documentspage:
    def __init__(self,driver):
        self.driver = driver

    documents_button = (By.ID,"tab8-tab")
    document_type = (By.XPATH,"//select[@id='doc_type']")
    document_ID = (By.XPATH,"//input[@id='doc_name']")
    upload_document = (By.XPATH,"//input[@id='document']")
    upload_button = (By.XPATH,"//button[@id='update8']")

    def getdocuments_button(self):

        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(self.documents_button)
            )
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
            return element
        except Exception as e:
            print(f"Error finding or interacting with the button: {e}")
            return None

        # return self.driver.find_element(*Documentspage.documents_button)

    def getdocument_type(self):
        return self.driver.find_element(*Documentspage.document_type)

    def getdocument_ID(self):
        return self.driver.find_element(*Documentspage.document_ID)

    def getupload_document(self):
        return self.driver.find_element(*Documentspage.upload_document)

    def getupload_button(self):
        return self.driver.find_element(*Documentspage.upload_button)