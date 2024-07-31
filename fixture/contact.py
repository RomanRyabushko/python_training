from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        # open add new contact page
        wd.find_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements(By.XPATH, "//*[text() = 'Select all']")) > 0):
            wd.find_element(By.XPATH, "//*[text() = 'home']").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def test_del_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.XPATH, "//*[text() = 'home']")
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//*[@value = 'Delete' and @onclick = 'DeleteSel()']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def test_del_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.XPATH, "//*[text() = 'home']")
        # select contact by index
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//*[@value = 'Delete' and @onclick = 'DeleteSel()']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)

    def test_modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.XPATH, "//*[text() = 'home']")
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "(//*[@title= 'Edit' and @alt= 'Edit'])[1]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element(By.XPATH, "//*[text() = 'home']")
        index = str(index)
        wd.find_element(By.XPATH, "(//*[@title= 'Edit' and @alt= 'Edit'])["+index+"]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.XPATH, "//*[@type = 'checkbox' and @name = 'selected[]']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.XPATH, "//*[@name = 'entry']/td[3]"):
                text1 = element.text
                text2 = element.find_element(By.XPATH, "//*[@name = 'entry']/td[2]").text
                id = element.find_element(By.XPATH, "//*[@name = 'selected[]']").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text1, lastname=text2, id=id))
        return list(self.contact_cache)
