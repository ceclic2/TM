class Flags:
    def __init__(self):
        self.add_rect=False
        self.del_rect=False
        self.edit_rect=False

    def change_flags(self,flag):
        if flag=='add':
            self.add_rect=True if not self.add_rect else False
        if flag=='del':
            self.del_rect=True if not self.del_rect else False
        if flag=='edit':
            self.edit_rect=True if not self.edit_rect else False