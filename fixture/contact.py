from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.XPATH, "//*[@alt='Edit']")[index].click()

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
        self.select_edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.XPATH, "//*[@type = 'checkbox' and @name = 'selected[]']"))

    contact_cache = None

    #def get_contact_list(self):
    #    if self.contact_cache is None:
    #        wd = self.app.wd
    #        self.return_to_home_page()
    #        self.contact_cache = []
    #        for element in wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]'):
    #            cells = element.find_elements(By.TAG_NAME, 'td')
    #            for t in cells:
    #                print(t.text)
    #            text1 = element.find_element(By.XPATH, "td[3]").text
    #            text2 = element.find_element(By.XPATH, "td[2]").text
    #            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
    #            self.contact_cache.append(Contact(firstname=text1, lastname=text2, id=id))
    #    return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
           wd = self.app.wd
           self.return_to_home_page()
           self.contact_cache = []
           for element in wd.find_elements(By.NAME, 'entry'):
                cells = element.find_elements(By.TAG_NAME, 'td')
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element(By.TAG_NAME, 'input').get_attribute("value")
                #email = cells[4].find_element(By.TAG_NAME, 'a').text
                all_phones = cells[5].text
                all_email = cells[4].text
                print(all_email)
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address, all_email=all_email, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        #row = wd.find_elements(By.CSS_SELECTOR, "tr[name=entry]")[index]
        #cells = row.find_element(By.XPATH, "td")
        #cells[8].find_element(By.XPATH, "a").click()
        #wd.find_element(By.XPATH, '//*[@name="entry"]/td[8]/a').click()
        wd.find_elements(By.XPATH, "//*[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        #row = wd.find_elements(By.NAME, 'entry')[index]
        #cell = row.find_element(By.TAG_NAME, 'td')[7]
        #cell.row.find_element(By.TAG_NAME, 'a').click()
        wd.find_elements(By.XPATH, "//*[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        homephone = wd.find_element(By.NAME, 'home').get_attribute('value')
        workphone = wd.find_element(By.NAME, 'work').get_attribute('value')
        mobilephone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        secondaryphone = wd.find_element(By.NAME, 'phone2').get_attribute('value')
        address = wd.find_element(By.NAME, 'address').get_attribute('value')
        email_1 = wd.find_element(By.NAME, 'email').get_attribute('value')
        email_2 = wd.find_element(By.NAME, 'email2').get_attribute('value')
        email_3 = wd.find_element(By.NAME, 'email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, email_1=email_1, email_2=email_2, email_3=email_3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, 'content').text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        for element in wd.find_elements(By.ID, 'content'):
            email = element.find_element(By.TAG_NAME, 'a').text
            full_name = '\n'.join(text.split()[0:3])
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, full_name=full_name, email_=email)












