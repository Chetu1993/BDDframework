import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service

from utilities import configreader


def before_scenario(context,scenario):
    browser_name=configreader.read_configuration("basic info","browser")
    if browser_name.__eq__('chrome'):
        service = Service("C:\\Users\\cks_1\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        context.driver = webdriver.Chrome(service=service)

    # elif browser_name.__eq__("firefox"):
    #     service = Service("C:\\Users\\cks_1\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
    #     context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()
    context.driver.get(configreader.read_configuration("basic info","url"))

def after_scenario(context,scenario):
    context.driver.quit()

def after_step(context,step):
    if step.status=='failed':
        allure.attach(context.driver.get_screenshot_as_png(),name='failed_screenshot.png',
                      attachment_type=AttachmentType.PNG)