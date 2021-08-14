from sys import maxsize

class Progect:
    def __init__(self, id_progect=None, name=None, status=None, inherit_global=None, view_state=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.id_progect = id_progect

    def __repr__(self):
        return "%s:%s" % (self.id_progect, self.name)

    def __eq__(self, other):
        return (self.id_progect is None or other.id_progect is None or self.id_progect == other.id_progect) \
               and self.name == other.name

    def name(self):
        if self.name:
            return self.name

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
