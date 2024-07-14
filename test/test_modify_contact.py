from model.contact import Contact
def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_modify(Contact(firstname="4", lastname="5", address="6"))
    app.session.logout()
