from selenium.webdriver.common.by import By


class Bulkleavepage:
    def __init__(self,driver):
        self.driver = driver

    leavemanagement = (By.XPATH,"//span[normalize-space()='Leave Management']")
    bulk_leave = (By.XPATH,"//a[normalize-space()='Bulk import leaves']")
    #sample_download = (By.XPATH,"//a[normalize-space()='Download Sample']")
    drag_drop = (By.XPATH,"//input[@id='file-input']")
    upload_button = (By.XPATH,"//button[@id='bulk_upload']")


    def getleavemanagemenet(self):
        return self.driver.find_element(*Bulkleavepage.leavemanagement)

    def getbulk_leave(self):
        return self.driver.find_element(*Bulkleavepage.bulk_leave)

    def getdrag_drop(self,file_input):
        file_input2 = self.driver.find_element(*Bulkleavepage.drag_drop)
        file_input2.send_keys(file_input)

    def getupload_button(self):
        return self.driver.find_element(*Bulkleavepage.upload_button)





