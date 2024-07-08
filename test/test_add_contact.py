from model.contact import Contact
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="1", lastname="2", address="3"))
    app.session.logout()
    #для коммита