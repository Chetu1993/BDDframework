import time

from behave import *
from features.steps import loginpage

from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'when i goto the search product page')
def step_impl(context):
    context.homepage=HomePage(context.driver)

    expected_title="Your Store"
    context.homepage.check_title(expected_title)
    # assert context.driver.title.__eq__(expected_title)






@when(u'i have entered the product "{productname}" in search box')
def step_impl(context,productname):
    context.homepage=HomePage(context.driver)


    context.homepage.search(productname)

    # context.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("hp")


@when(u'i click on the search button')
def step_impl(context):
    context.homepage=HomePage(context.driver)

    context.loginpage=context.homepage.searchbuttonclick()
    # context.driver.find_element(By.XPATH,"//span[@class='input-group-btn']").click()


@then(u'valid product should be visible')
def step_impl(context):

    product=context.loginpage.productvisible()
    # product=context.driver.find_element(By.XPATH,"//a[text()='HP LP3065']").text

    assert 'HP LP3065' in product




@when(u'i have entered the invalid "{productname}" product')
def step_impl(context,productname):
    context.homepage=HomePage(context.driver)
    context.homepage.search(productname)
    # context.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("abcd")



@then(u'proper message should be visible')
def step_impl(context):

    message=context.homepage.wrong_entry()
    # message=context.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']")
    assert "There" in message



@when(u'i dont enter anything in search box field')
def step_impl(context):
    context.homepage=HomePage(context.driver)
    # context.driver.find_element(By.XPATH,"//div[@id='search']//input")
    context.homepage.searchbox_withoutdetails()



