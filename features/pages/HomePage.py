from selenium.webdriver.common.by import By


from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)



    myaccount=("//span[text()='My Account']")
    loginbutton=("//a[text()='Login']")
    searchbox="//input[@name='search']"
    searchbutton="//span[@class='input-group-btn']"
    wrong_product = "//p[text()='There is no product that matches the search criteria.']"
    searchfield="//div[@id='search']//input"
    register="(//a[text()='Register'])[1]"

    def register_click(self):
        # self.click_on_element("register",self.register).click()
        self.driver.find_element(By.XPATH,self.register).click()

    def getting_title(self,text):
        return self.driver.title.__eq__(text)


    def click_on_myaccount(self):
        # self.click_on_element("myaccount",self.myaccount).click()
        self.driver.find_element(By.XPATH,self.myaccount).click()

    def click_login(self):
        # self.click_on_element("loginbutton",self.loginbutton).click()

        self.driver.find_element(By.XPATH,self.loginbutton).click()
        return LoginPage(self.driver)

    def check_title(self,expected_title):


        # return self.verify_title(expected_title)

        self.driver.title.__eq__(expected_title)

    def search(self,productname):
        # self.type_into_text("searchbox",self.searchbox,productname)
        self.driver.find_element(By.XPATH,self.searchbox).send_keys(productname)


    def wrong_entry(self):
        # return self.get_element("wrong_product",self.wrong_product).text


        return self.driver.find_element(By.XPATH,self.wrong_product).text

    def nothing(self):
        # return self.get_element("nothing_product",self.nothing_product).text
        return self.driver.find_element(By.XPATH,self.nothing_product).text

    def searchbox_withoutdetails(self):
        # self.type_into_text("searchfield",self.searchfield,"")
        self.driver.find_element(By.XPATH,self.searchfield).send_keys("")

    def searchbuttonclick(self):
        # self.click_on_element("searchbutton",self.searchbutton)
        self.driver.find_element(By.XPATH,self.searchbutton).click()
        return LoginPage(self.driver)




