from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    firstname="//input[@id='input-firstname']"
    lastname="//input[@id='input-lastname']"
    email="//input[@id='input-email']"
    telephone="//input[@name='telephone']"
    password="//input[@name='password']"
    confirmpassword="//input[@name='confirm']"
    checkboxclick="//input[@type='checkbox']"
    continuebutton="//input[@type='submit']"
    newsletter="//input[@name='newsletter'][@value='1']"
    warningmsg="//div[@class='alert alert-danger alert-dismissible']"

    privacy_warning="//div[@class='alert alert-danger alert-dismissible']"
    firstname_warning="//div[@class='text-danger'][text()='First Name must be between 1 and 32 characters!']"
    lastname_warning="//div[@class='text-danger'][text()='Last Name must be between 1 and 32 characters!']"
    email_warning="//div[@class='text-danger'][text()='E-Mail Address does not appear to be valid!']"
    telephone_warning="//div[@class='text-danger'][text()='Telephone must be between 3 and 32 characters!']"
    password_warning="//div[@class='text-danger'][text()='Password must be between 4 and 20 characters!']"




    def privacy_warn(self,message):

        # return self.element_text_should_contain("privacy_warning",self.privacy_warning,message)


        return self.driver.find_element(By.XPATH,self.privacy_warning).text.__contains__(message)



    def first_namewarn(self,message):
        # return self.element_text_should_contain("firstname_warning", self.firstname_warning, message)
        return self.driver.find_element(By.XPATH,self.firstname_warning).text.__contains__(message)


    def lastname_warn(self,message):
        # return self.element_text_should_contain("lastname_warning",self.lastname_warning,message)
        return self.driver.find_element(By.XPATH,self.lastname_warning).text.__contains__(message)

    def email_warn(self,message):
        # return self.element_text_should_contain("email_warning",self.email_warning,message)
        return self.driver.find_element(By.XPATH,self.email_warning).text.__contains__(message)

    def telephone_warn(self,message):
        # return self.element_text_should_contain("telephone_warning",self.telephone_warning,message)
        return self.driver.find_element(By.XPATH,self.telephone_warning).text.__contains__(message)

    def password_warn(self,message):
        # return self.element_text_should_equal_to("password_warning",self.password_warning)
        return self.driver.find_element(By.XPATH,self.password_warning).text.__eq__(message)





    def enter_firstname(self,intialname):

        # self.type_into_text("firstname",self.firstname,intialname)
        self.driver.find_element(By.XPATH,self.firstname).send_keys(intialname)

    def enter_lastname(self,finalname):
        # self.type_into_text("lastname",self.lastname,finalname)
        self.driver.find_element(By.XPATH,self.lastname).send_keys(finalname)

    def enter_email(self,sendemail):
        # self.type_into_text("email",self.email,sendemail)
        self.driver.find_element(By.XPATH,self.email).send_keys(sendemail)

    def enter_telephone(self,sendtele):
        # self.type_into_text("telephone",self.telephone,sendtele)
        self.driver.find_element(By.XPATH,self.telephone).send_keys(sendtele)

    def enter_pass(self,sendpass):
        # self.type_into_text("password",self.password,sendpass)
        self.driver.find_element(By.XPATH,self.password).send_keys(sendpass)

    def enter_confirmpass(self,confirmsendpass):
        # self.type_into_text("confirmpassword",self.confirmpassword,confirmsendpass)
        self.driver.find_element(By.XPATH,self.confirmpassword).send_keys(confirmsendpass)

    def click_checkbox(self):
        # self.click_on_element("checkboxclick",self.checkboxclick)
        self.driver.find_element(By.XPATH,self.checkboxclick).click()

    def clickon_continue(self):
        # self.click_on_element("continuebutton",self.continuebutton)
        self.driver.find_element(By.XPATH,self.continuebutton).click()
        return AccountPage(self.driver)

    def enter_newsletter(self):
        # self.click_on_element("newsletter",self.newsletter)
        self.driver.find_element(By.XPATH,self.newsletter).click()

    def proper_warningmsg(self,text):
        # return self.element_text_should_equal_to("warningmsg",self.warningmsg,text)
        return self.driver.find_element(By.XPATH,self.warningmsg).__eq__(text)



