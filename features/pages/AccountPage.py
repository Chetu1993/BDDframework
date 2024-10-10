from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    accountinfo="//div[@id='content']//h2[text()='My Account']"
    accountverify="//div[@id='content']//h1[text()='Your Account Has Been Created!']"

    def account(self):
        # return self.get_element("accountinfo",self.accountinfo).text
        return self.driver.find_element(By.XPATH,self.accountinfo).text

    def accountcreated(self,text):
        # return self.element_text_should_equal_to("accountverify",self.accountverify,text)
        return self.driver.find_element(By.XPATH,self.accountverify).__eq__(text)

