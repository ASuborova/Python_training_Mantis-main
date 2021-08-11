
class SessionHelper:

    def __init__(self, ses_h):
        self.ses_h = ses_h

    def login(self, loginname, password):
        wd = self.ses_h.wd
        # open home page
        self.ses_h.open_home_page()
        # login
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(loginname)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_logout(self):
        wd = self.ses_h.wd
        if self.is_logged_in():
            self.logout()

    def logout(self):
        wd = self.ses_h.wd
        # logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("username")

    def is_login(self, loginname, password):
        wd = self.ses_h.wd
        if self.is_logged_in():
            if self.is_logged_in_as(loginname):
                return
            else:
                self.logout()
        self.login(loginname, password)

    def is_logged_in(self):
        wd = self.ses_h.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, loginname):
        wd = self.ses_h.wd
        return self.get_logged_user() == loginname

    def get_logged_user(self):
        wd = self.ses_h.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text


