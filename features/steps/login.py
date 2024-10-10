from datetime import datetime

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import email_generator


@given(u'i goto the login website')
def step_impl(context):

    context.homepage=HomePage(context.driver)

    context.homepage.click_on_myaccount()
    context.loginpage=context.homepage.click_login()






@given(u'entering the username as "{username}" and password as "{password}"')
def step_impl(context,username,password):
    context.loginpage=LoginPage(context.driver)

    context.loginpage.enter_email(username)
    context.loginpage.enter_password(password)

    # context.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("schetankumar123@gmail.com")
    # context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("chetan456")


@given(u'click on the login button')
def step_impl(context):


    context.accountpage=context.loginpage.click_login()

    # context.driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(4)


@then(u'i should get logged in')
def step_impl(context):



    loggedin=context.accountpage.account()

    # loggedin=context.driver.find_element(By.XPATH,"//div[@id='content']//h2[text()='My Account']").text

    assert "My Account" in loggedin




@given(u'entering the invalid username as "{invalid_username}" and valid password as "{valid_password}"')
def step_impl(context,invalid_username,valid_password):

    context.loginpage = LoginPage(context.driver)
    context.loginpage.enter_email(invalid_username)
    context.loginpage.enter_password(valid_password)
    # context.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(invalid_username)
    # context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("chetan456")



@then(u'i need to get error message')
def step_impl(context):
    error_email=context.loginpage.warning_msg()
    # error_email=context.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text
    assert "Address" in error_email





@given(u'entering the valid username as "{username}" and invalid password as "{password}"')
def step_impl(context,username,password):

    context.loginpage=LoginPage(context.driver)
    context.loginpage.enter_email(username)
    context.loginpage.enter_password(password)
    # context.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("schetankumar123@gmail.com")
    # context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("chetan")



@given(u'entering the invalid username and invalid password as "{password}"')
def step_impl(context,password):

    invalid_username=email_generator.email_timestamp_generator()
    context.loginpage = LoginPage(context.driver)
    context.loginpage.enter_email(invalid_username)
    context.loginpage.enter_password(password)
    # context.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(invalid_username)
    # context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("welcome")



@given(u'without entering the username and password into fields')
def step_impl(context):
    context.loginpage = LoginPage(context.driver)
    context.loginpage.enter_email("")
    context.loginpage.enter_password("")
    # context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
    # context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")


