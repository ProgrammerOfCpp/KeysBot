from menu.interface_menu import InterfaceMenu
from telebot import types
import btc_helper

CODE = 'manage_lot@'


class LotsListMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.lots_manager = bot.lots_manager
        lots = self.get_lots()
        self.markup = self.build_lots_markup(lots)

    def get_lots(self):
        return []

    def build_lots_markup(self, lots):
        markup = types.InlineKeyboardMarkup()
        for lot in lots:
            id = lot[0]
            title = self.lots_manager.get_property(id, 'title')
            price = self.lots_manager.get_property(id, 'price')
            user_id = self.lots_manager.get_property(id, 'user_id')
            active = self.lots_manager.get_property(id, 'active')
            keys_count = self.lots_manager.get_keys_count(id)
            if (active and keys_count > 0) or user_id == self.user.id:
                markup.add(types.InlineKeyboardButton
                                (text=self.user.lang.LOT_TITLE.format(title, price),
                                 callback_data=CODE + title))
        return markup

    def handle_callback(self, call):
        if call.data.startswith(CODE):
            title = call.data.split('@')[1]
            lot = self.lots_manager.get_lot_by_title(title)
            self.user.set_property('lot_id', lot[0])
            self.lots_manager.show_info(lot[0], self.user)
            return 1
        lot_id = self.user.get_property('lot_id')
        if lot_id:
            if call.data == self.lang.ACTIVATE_BTN:
                self.lots_manager.set_property(lot_id, 'active', 1)
                self.tg_bot.send_message(self.user.id, self.lang.LOT_ACTIVATED, parse_mode="HTML")
                return 1
            elif call.data == self.lang.DEACTIVATE_BTN:
                self.lots_manager.set_property(lot_id, 'active', 0)
                self.tg_bot.send_message(self.user.id, self.lang.LOT_DEACTIVATED, parse_mode="HTML")
                return 1
            elif call.data == self.lang.DELETE_BTN:
                self.lots_manager.delete_lot(lot_id)
                self.tg_bot.send_message(self.user.id, self.lang.LOT_DELETED, parse_mode="HTML")
                return 1
            elif call.data == self.lang.EDIT_BTN:
                self.user.change_menu("InputTitleMenu")
                return 1
            elif call.data == self.lang.BUY_FOR:
                address = self.lots_manager.get_owner_address(lot_id)
                price = self.lots_manager.get_property(lot_id, 'price')
                sum = btc_helper.eur_to_btc(price)
                self.user.perform_transaction(address, sum, 'buy')
                return 1
        return super().handle_callback(call)
