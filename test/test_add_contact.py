from model.contact import Contact
def test_add_contact(app):
    app.contact.create(Contact(firstname="1", lastname="2", address="3"))

