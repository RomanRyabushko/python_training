from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="123", header="456", footer="789"))
    app.session.logout()
