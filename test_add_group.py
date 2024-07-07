# -*- coding: utf-8 -*-
import pytest
from group import Group
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="qqq", header="www", footer="ууу"))
        app.logout()

def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="1", lastname="2", address="3"))
        app.logout()

