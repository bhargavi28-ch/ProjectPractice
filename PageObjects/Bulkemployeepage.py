from selenium.webdriver.common.by import By


class Bulkemployeepage:
    def __init__(self,driver):
        self.driver = driver

    employee = (By.XPATH, "//span[text()='Employee']")
    bulk_import = (By.LINK_TEXT,"Bulk Import")
    #sample_download = (By.XPATH,"//a[normalize-space()='Download Sample']")
    file_input = (By.XPATH,"//input[@type='file']")
    download_button = (By.XPATH,"//button[@id='bulk_upload']")
    success_message = (By.XPATH,"//div[@class='alert alert-success']")
    existing_message = (By.CSS_SELECTOR,"div[role='alert'] ul")




    def getemployee(self):
        return self.driver.find_element(*Bulkemployeepage.employee).click()

    def getbulk_import(self):
        return self.driver.find_element(*Bulkemployeepage.bulk_import).click()

    # def getsample_download(self):
    #     return self.driver.find_element(*Bulkemployeepage.sample_download)

    def getfile_input(self,file_path):
        file_input2 = self.driver.find_element(*Bulkemployeepage.file_input)
        file_input2.send_keys(file_path)

    def getdownload_button(self):
        return self.driver.find_element(*Bulkemployeepage.download_button).click()

    def getsuccess_message(self):
        return self.driver.find_element(*Bulkemployeepage.success_message)

    def getexisting_message(self):
        return self.driver.find_element(*Bulkemployeepage.existing_message)








