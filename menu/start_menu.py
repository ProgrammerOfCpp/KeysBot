from menu.interface_menu import InterfaceMenu
from telebot import types


class StartMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.START_MSG)

        self.markup = types.ReplyKeyboardMarkup()
        eng_btn = types.KeyboardButton(self.lang.ENG_BTN_TEXT)
        rus_btn = types.KeyboardButton(self.lang.RUS_BTN_TEXT)
        self.markup.row(eng_btn, rus_btn)

    def handle_message(self, message):
        if message.text == self.lang.ENG_BTN_TEXT:
            self.user.set_property('lang', 'en')
        elif message.text == self.lang.RUS_BTN_TEXT:
            self.user.set_property('lang', 'rus')
        else:
            return super().handle_message(message)
        self.user.change_menu('SupportMenu')
        return 1