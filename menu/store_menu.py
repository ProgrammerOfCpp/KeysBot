from menu.lots_list_menu import LotsListMenu
from telebot import types


class StoreMenu(LotsListMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.STORE_MSG)

    def get_lots(self):
        return self.bot.lots_manager.get_lots(self.user)

    def handle_message(self, message):
        if super().handle_message(message):
            return 1
        keyword = message.text
        lots = self.bot.lots_manager.search_lots(self.user, keyword)
        if len(lots) == 0:
            self.respond(self.lang.STORE_NOT_FOUND, types.InlineKeyboardMarkup())
        else:
            markup = self.build_lots_markup(lots)
            self.respond(self.lang.SEARCH_RESULTS, markup)
        return 1
