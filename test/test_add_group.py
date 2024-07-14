from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="qqq", header="www", footer="ууу"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



