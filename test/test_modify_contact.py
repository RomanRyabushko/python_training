from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname", address="test_address"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="modify_firstname5", lastname="modify_lastname5", address="modify_address5")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test_contact"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(firstname="modify_firstname2")
#    app.contact.test_modify_first_contact(contact)
#    contact.id = old_contacts[0].id
#    app.contact.test_modify_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

