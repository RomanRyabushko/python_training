from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    app.contact.test_modify_first_contact(Contact(firstname="modify_firstname1", lastname="modify_lastname1", address="modify_address1"))


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    app.contact.test_modify_first_contact(Contact(firstname="modify_firstname2"))
