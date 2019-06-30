from menu.lots_list_menu import LotsListMenu
from telebot import types

CODE = 'manage_lot@'


class ManageLotsMenu(LotsListMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.LOTS_LIST)

    def get_lots(self):
        return self.bot.lots_manager.get_lots(self.user, only_created=True)

    def handle_callback(self, call):
        return super().handle_callback(call)





