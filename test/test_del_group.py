from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_for_del", header="header_for_del", footer="footer_for_del"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.test_del_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
