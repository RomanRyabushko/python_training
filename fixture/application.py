from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import  SessionHelper


class Application:

     def __init__(self):
        #self.wd = webdriver.Firefox()
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


     def return_to_groups_page(self):
        wd = self.wd
        # return to groups page
        wd.find_element(By.LINK_TEXT, "group page").click()

     def return_to_home_page(self):
        wd = self.wd
        # return to home page
        wd.find_element(By.XPATH, "//*[text() = 'home']").click()

     def create_group(self,group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

     def create_contact(self, contact):
        wd = self.wd
        self.open_add_new_contact_page()
        # fill contact form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

     def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

     def open_add_new_contact_page(self):
        wd = self.wd
        # open add new contact page
        wd.find_element(By.LINK_TEXT, "add new").click()

     def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("https://localhost/addressbook/")

     def destroy(self):
        self.wd.quit()