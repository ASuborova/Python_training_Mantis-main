from selenium.webdriver.support.ui import Select
from model.progect import Progect


class ProgectHelper:

    def __init__(self, pog_h):
        self.pog_h = pog_h

    def open_manage_page(self):
        wd = self.pog_h.wd
        wd.find_element_by_link_text("Manage").click()

    def open_manage_projects_page(self):
        wd = self.pog_h.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def attributes_progect(self, progect):
        wd = self.pog_h.wd
        self.change_field("name", progect.name)
        self.change_field("status", progect.status)
        self.change_field("view_state", progect.view_state)
        self.change_field("description", progect.description)

    def change_field(self, field_name, text):
        wd = self.pog_h.wd
        if text is not None:
            if field_name in ('status', 'view_state'):
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def create(self, progect):
        wd = self.pog_h.wd
        self.pog_h.open_home_page()
        self.open_manage_page()
        self.open_manage_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.attributes_progect(progect)
        wd.find_element_by_css_selector("input.button").click()
        self.progect_cash = None

    def del_progect_by_name(self, progect):
        wd = self.pog_h.wd
        self.pog_h.open_home_page()
        self.open_manage_page()
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//a[contains(text(),'" + progect + "')]").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.progect_cash = None

    progect_cash = None

    def get_list_progect(self):
        if self.progect_cash is None:
            wd = self.pog_h.wd
            self.pog_h.open_home_page()
            self.open_manage_page()
            self.open_manage_projects_page()
            self.progect_cash = []
            for element in (wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")):
                if element.get_attribute("class") not in ('', 'row-category'):
                    cells = element.find_elements_by_tag_name("td")
                    name = cells[0].text
                    self.progect_cash.append(Progect(name=name))
        return list(filter(None, self.progect_cash))


