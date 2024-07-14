from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(firstname="modify_firstname1", lastname="modify_lastname1", address="modify_address1"))
    app.session.logout()


def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify_first_contact(Contact(firstname="modify_firstname2"))
    app.session.logout()
