from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_address="//input[@name='email']"
    password="//input[@name='password']"
    loginbutton="//input[@value='Login']"
    warning_message="//div[@class='alert alert-danger alert-dismissible']"
    productvis="//a[text()='HP LP3065']"


    def enter_email(self,username):
        # self.type_into_text("email_address",self.email_address,username)
        self.driver.find_element(By.XPATH,self.email_address).send_keys(username)

    def enter_password(self,password):
        # self.type_into_text("password",self.password,password)
        self.driver.find_element(By.XPATH,self.password).send_keys(password)

    def click_login(self):
        # self.click_on_element("loginbutton",self.loginbutton).click()
        self.driver.find_element(By.XPATH,self.loginbutton).click()
        return AccountPage(self.driver)

    def warning_msg(self):
        return self.driver.find_element(By.XPATH,self.warning_message).text

    def productvisible(self):
        return self.driver.find_element(By.XPATH,self.productvis).text



