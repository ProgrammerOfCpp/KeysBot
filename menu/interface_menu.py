from menu.menu import Menu
from telebot import types


class InterfaceMenu(Menu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.markup = types.ReplyKeyboardMarkup()
        store_btn = types.KeyboardButton(self.lang.STORE_BTN_TEXT)
        support_btn = types.KeyboardButton(self.lang.SUPPORT_BTN_TEXT)
        wallet_btn = types.KeyboardButton(self.lang.WALLET_BTN_TEXT)
        settings_btn = types.KeyboardButton(self.lang.SETTINGS_BTN_TEXT)
        self.markup.row(store_btn, support_btn)
        self.markup.row(wallet_btn, settings_btn)

    def handle_message(self, message):
        if message.text == self.lang.STORE_BTN_TEXT:
            self.user.change_menu('StoreMenu')
        elif message.text == self.lang.WALLET_BTN_TEXT:
            self.user.change_menu('WalletMenu')
        elif message.text == self.lang.SETTINGS_BTN_TEXT:
            self.user.change_menu('SettingsMenu')
        elif message.text == self.lang.SUPPORT_BTN_TEXT:
            self.user.change_menu('SupportMenu')
        else:
            return super().handle_message(message)
        return 1