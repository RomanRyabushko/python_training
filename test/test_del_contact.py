from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    app.contact.test_del_first_contact()
