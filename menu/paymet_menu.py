from menu.interface_menu import InterfaceMenu
from telebot import types


class PaymentMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        sum = self.user.get_property('transaction_sum')
        self.lot_id = self.user.get_property('lot_id')
        self.msgs.append(self.lang.PAYMENT_WARNING.format(sum))
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(types.InlineKeyboardButton(text=self.lang.PAYMENT_YES,
                                                   callback_data=self.lang.PAYMENT_YES),
                        types.InlineKeyboardButton(text=self.lang.PAYMENT_NO,
                                                   callback_data=self.lang.PAYMENT_NO))

    def handle_callback(self, call):
        if call.data == self.lang.PAYMENT_YES:
            money = self.user.get_balance()

            address = self.user.get_property('transaction_address')
            sum = self.user.get_property('transaction_sum')
            payment_type = self.user.get_property('payment_type')
            if sum > money:
                self.tg_bot.send_message(self.user.id, text=self.lang.PAYMENT_LOW_BALANCE)
                self.user.go_back()

            if payment_type == 'buy':
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text=self.lang.PAYMENT_LIKE,
                                                       callback_data=self.lang.PAYMENT_LIKE),
                                types.InlineKeyboardButton(text=self.lang.PAYMENT_DISLIKE,
                                                       callback_data=self.lang.PAYMENT_DISLIKE))
                key = self.bot.lots_manager.get_key(self.lot_id)
                if key is None:
                    self.respond(self.lang.KEYS_OVER)
                else:
                    if self.user.send_money(address, sum, payment_type):
                        self.respond(self.lang.PAYMENT_SUCCESS_BUY, types.InlineKeyboardMarkup())
                        self.respond(key, markup)
                        self.bot.lots_manager.clear_key(self.lot_id)
                    else:
                        self.respond(self.lang.TRANSACTION_ERROR, types.InlineKeyboardMarkup())
            else:
                if self.user.send_money(address, sum, payment_type):
                    self.respond(self.lang.PAYMENT_SUCCESS_SEND, types.InlineKeyboardMarkup())
                    self.user.go_back()
                else:
                    self.respond(self.lang.TRANSACTION_ERROR, types.InlineKeyboardMarkup())
            return 1
        if call.data == self.lang.PAYMENT_NO:
            self.user.go_back()
            return 1
        if call.data == self.lang.PAYMENT_LIKE:
            self.bot.lots_manager.put_like(self.lot_id, self.user.id)
            self.user.go_back()
            return 1
        if call.data == self.lang.PAYMENT_DISLIKE:
            self.bot.lots_manager.put_dislike(self.lot_id, self.user.id)
            self.user.go_back()
            return 1
