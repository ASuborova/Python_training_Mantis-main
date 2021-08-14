from model.progect import Progect
import random
import time


def test_del_some_progect(app):
    app.ses_h.login("administrator", "root")
    if len(app.pog_h.get_list_progect()) == 0:
        app.pog_h.create(Progect(name=app.gen.random_string('progect', 7)))
        time.sleep(3)
    old_list_progect = app.pog_h.get_list_progect()
    progect = random.choice(old_list_progect)
    app.pog_h.del_progect_by_name(progect.name)
    new_list_progect = app.pog_h.get_list_progect()
    assert len(old_list_progect) - 1 == len(new_list_progect)
    old_list_progect.remove(progect)
    assert old_list_progect == new_list_progect

