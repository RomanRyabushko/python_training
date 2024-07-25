from model.contact import Contact
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", lastname="2",  address="3")
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
