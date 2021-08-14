# -*- coding: utf-8 -*-
import time

from model.progect import Progect


def test_create_new_progect(app):
    new_progect = Progect(name=app.gen.random_string('progect', 7))
    app.ses_h.login("administrator", "root")
    old_list_progect = app.pog_h.get_list_progect()
    app.pog_h.create(new_progect)
    time.sleep(3)
    new_list_progect = app.pog_h.get_list_progect()
    assert len(old_list_progect) + 1 == len(new_list_progect)
    old_list_progect.append(new_progect)
    assert sorted(old_list_progect, key=Progect.name) == sorted(new_list_progect, key=Progect.name)




