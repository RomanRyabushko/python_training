from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.session import  SessionHelper
from fixture.group import GroupHelper


class Application:

     def __init__(self):
        #self.wd = webdriver.Firefox()
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

     def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("https://localhost/addressbook/")

     def destroy(self):
        self.wd.quit()