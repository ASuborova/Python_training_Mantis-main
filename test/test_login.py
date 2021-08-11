

def test_login(app):
    app.ses_h.login("administrator", "root")
    assert app.ses_h.is_logged_in_as("administrator")
