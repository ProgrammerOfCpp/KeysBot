from menu.interface_menu import InterfaceMenu


class LotBasicMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.lot_id = user.get_property('lot_id')
        self.lots_manager = bot.lots_manager

    @staticmethod
    def str_correct(str):
        prev = ' '
        for x in str:
            if (prev == '\n' or prev == ' ') and x == '/':
                return False
            prev = x
        return True
