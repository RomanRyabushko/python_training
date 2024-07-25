from model.group import Group


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_for_del", header="header_for_del", footer="footer_for_del"))
    old_groups = app.group.get_group_list()
    app.group.test_del_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
