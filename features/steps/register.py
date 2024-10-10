from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage
from utilities import email_generator


@given(u'i navigate to Register page')
def step_impl(context):

    context.homepage=HomePage(context.driver)
    context.homepage.click_on_myaccount()
    context.homepage.register_click()




    # context.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    # context.driver.find_element(By.XPATH,"(//a[text()='Register'])[1]").click()




@when(u'i enter the below details in mandatory fields')
def step_impl(context):


    context.registerpage=RegisterPage(context.driver)


    for row in context.table:

        context.registerpage.enter_firstname(row["firstname"])
        context.registerpage.enter_lastname(row["lastname"])

        email = email_generator.email_timestamp_generator()
        context.registerpage.enter_email(email)
        context.registerpage.enter_telephone(row["telephone"])
        context.registerpage.enter_pass(row["password"])
        context.registerpage.enter_confirmpass(row["confirmpassword"])
        context.registerpage.click_checkbox()
    # context.driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("chetan")
    # context.driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("kumar")
    # timestamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # email="chetan"+timestamp+"@gmail.com"
    # context.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(email)
    # context.driver.find_element(By.XPATH,"//input[@name='telephone']").send_keys('1234567890')
    # context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("chetan789")
    # context.driver.find_element(By.XPATH,"//input[@name='confirm']").send_keys("chetan789")
    # context.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()





@when(u'i click on Continue button')
def step_impl(context):

    context.accountpage=context.registerpage.clickon_continue()
    time.sleep(5)
    # context.driver.find_element(By.XPATH,"//input[@type='submit']").click()



@then(u'Account should get created')
def step_impl(context):
    accountname="Congratulations! Your new account has been successfully created!"
    # context.driver.find_element(By.XPATH,"//div[@id='content']//h1[text()='Your Account Has Been Created!']").text.__eq__(accountname)
    context.accountpage=AccountPage(context.driver)
    context.accountpage.accountcreated(accountname)





@when(u'i enter with all below fields')
def step_impl(context):
    # context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("chetan")
    # context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("kumar")
    # timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # email = "chetan" + timestamp + "@gmail.com"
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(email)
    # context.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys('1234567890')
    # context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("chetan789")
    # context.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("chetan789")
    # context.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    # context.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

    context.registerpage = RegisterPage(context.driver)
    for row in context.table:
        context.registerpage.enter_firstname(row["firstname"])
        context.registerpage.enter_lastname(row["lastname"])

        email = email_generator.email_timestamp_generator()
        context.registerpage.enter_email(email)
        context.registerpage.enter_telephone(row["telephone"])
        context.registerpage.enter_pass(row["password"])
        context.registerpage.enter_confirmpass(row["confirmpassword"])
        context.registerpage.enter_newsletter()
        context.registerpage.click_checkbox()







@when(u'i enter all the below mentioned fields into details field except email field')
def step_impl(context):
    context.registerpage = RegisterPage(context.driver)
    for row in context.table:
        context.registerpage.enter_firstname(row["firstname"])
        context.registerpage.enter_lastname(row["lastname"])

        context.registerpage.enter_telephone(row["telephone"])
        context.registerpage.enter_pass(row["password"])
        context.registerpage.enter_confirmpass(row["confirmpassword"])
        context.registerpage.click_checkbox()


    # context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("chetan")
    # context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("kumar")
    # context.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys('1234567890')
    # context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("chetan456")
    # context.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("chetan456")
    # context.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()







@when(u'i enter existing account email into email field')
def step_impl(context):

    context.registerpage=RegisterPage(context.driver)
    context.registerpage.enter_email("schetankumar123@gmail.com")
    # context.driver.find_element(By.XPATH,"//input[@type='email']").send_keys("schetankumar123@gmail.com")




@then(u'proper warning message with duplicate account should be displayed')
def step_impl(context):
    message = "Warning: E-Mail Address is already registered!"
    time.sleep(3)
    # context.registerpage=RegisterPage(context.driver)
    context.registerpage.proper_warningmsg(message)

    # context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(message)



@then(u'proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    privacy_warning1="Warning: You must agree to the Privacy Policy!"
    # assert context.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text.__contains__(privacy_warning)

    context.registerpage=RegisterPage(context.driver)
    context.registerpage.proper_warningmsg(privacy_warning1)


    firstname_warning="First Name must be between 1 and 32 characters!"
    lastname_warning="Last Name must be between 1 and 32 characters!"
    email_warning="E-Mail Address does not appear to be valid!"
    telephone_warning="Telephone must be between 3 and 32 characters!"
    password_warning="Password must be between 4 and 20 characters!"

    context.registerpage.first_namewarn(firstname_warning)
    context.registerpage.lastname_warn(lastname_warning)
    context.registerpage.email_warn(email_warning)
    context.registerpage.telephone_warn(telephone_warning)
    context.registerpage.password_warn(password_warning)

    # assert context.driver.find_element(By.XPATH,"//div[@class='text-danger'][text()='First Name must be between 1 and 32 characters!']").text.__contains__(firstname_warning)
    # assert context.driver.find_element(By.XPATH,"//div[@class='text-danger'][text()='Last Name must be between 1 and 32 characters!']").text.__contains__(lastname_warning)
    # assert context.driver.find_element(By.XPATH,"//div[@class='text-danger'][text()='E-Mail Address does not appear to be valid!']").text.__contains__(email_warning)
    # assert context.driver.find_element(By.XPATH,"//div[@class='text-danger'][text()='Telephone must be between 3 and 32 characters!']").text.__contains__(telephone_warning)
    # assert context.driver.find_element(By.XPATH,"//div[@class='text-danger'][text()='Password must be between 4 and 20 characters!']").text.__contains__(password_warning)


@when(u'i dont enter anything into the fields')
def step_impl(context):
    context.registerpage = RegisterPage(context.driver)
    context.registerpage.enter_firstname("")
    context.registerpage.enter_lastname("")

    context.registerpage.enter_email("")
    context.registerpage.enter_telephone("")
    context.registerpage.enter_pass("")
    context.registerpage.enter_confirmpass("")




    # context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("")
    # context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("")
    #
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("")
    # context.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys('')
    # context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
    # context.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("")







