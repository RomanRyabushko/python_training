from sys import maxsize
class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None,
                 all_phones_from_home_page=None, all_email=None, email_1=None, email_2=None, email_3=None, full_name=None, email_=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_email = all_email
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.full_name = full_name
        self.email_ = email_

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and self.firstname == other.firstname and self.lastname == other.lastname
                and self.all_email == other.all_email and self.all_phones_from_home_page == other.all_phones_from_home_page)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
