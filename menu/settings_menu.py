from menu.interface_menu import InterfaceMenu
from telebot import types


class SettingsMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.lots_manager = bot.lots_manager
        self.msgs.append(self.lang.SETTINGS_MSG)
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(types.InlineKeyboardButton(text=self.lang.NEW_LOT_BTN,
                                                   callback_data=self.lang.NEW_LOT_BTN))
        self.markup.add(types.InlineKeyboardButton(text=self.lang.MANAGE_LOTS_BTN,
                                                   callback_data=self.lang.MANAGE_LOTS_BTN))
        self.markup.add(types.InlineKeyboardButton(text=self.lang.SET_NEW_ADDRESS_BTN,
                                                   callback_data=self.lang.SET_NEW_ADDRESS_BTN))
        self.markup.add(types.InlineKeyboardButton(text=self.lang.TOGGLE_STORE_MODE_BTN,
                                                   callback_data=self.lang.TOGGLE_STORE_MODE_BTN))

    def handle_message(self, message):
        return super().handle_message(message)

    def handle_callback(self, call):
        if call.data == self.lang.NEW_LOT_BTN:
            self.user.set_property('lot_id', 0)
            self.user.change_menu('InputTitleMenu')
            return 1
        if call.data == self.lang.MANAGE_LOTS_BTN:
            self.user.change_menu('ManageLotsMenu')
            return 1
        if call.data == self.lang.SET_NEW_ADDRESS_BTN:
            self.user.change_menu('InputAddressMenu')
            return 1
        if call.data == self.lang.TOGGLE_STORE_MODE_BTN:
            show_all = self.user.get_property('show_all')
            if show_all:
                show_all = 0
                self.respond(self.lang.FAV_MODE_ON, types.InlineKeyboardMarkup())
            else:
                show_all = 1
                self.respond(self.lang.FAV_MODE_OFF, types.InlineKeyboardMarkup())
            self.user.set_property('show_all', show_all)
            return 1
        return super().handle_callback(call)