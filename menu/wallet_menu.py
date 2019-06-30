from menu.interface_menu import InterfaceMenu
from telebot import types
import btc_helper


class WalletMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        balance = self.user.get_balance()
        spent = self.user.get_property('spent')
        loaded = self.user.get_property('loaded')
        self.msgs.append(self.lang.WALLET_MSG.format(balance, loaded, spent))
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(types.InlineKeyboardButton(text=self.lang.WALLET_LOAD_BTN,
                                                   callback_data=self.lang.WALLET_LOAD_BTN),
                        types.InlineKeyboardButton(text=self.lang.WALLET_SEND_BTN,
                                                   callback_data=self.lang.WALLET_SEND_BTN))
        self.markup.add(types.InlineKeyboardButton(text=self.lang.WALLET_HISTORY_BTN,
                                                   callback_data=self.lang.WALLET_HISTORY_BTN))

    def handle_callback(self, call):
        if call.data == self.lang.WALLET_HISTORY_BTN:
            trs = self.user.get_transactions()
            msg = self.lang.RECENT_TRANSACTIONS
            for t in trs:
                sum = t[2]
                time = t[3]
                payment_type = ''
                if t[4] == 'buy':
                    payment_type = self.lang.PAYMENT_TYPE_BUY
                if t[4] == 'out':
                    payment_type = self.lang.PAYMENT_TYPE_SEND
                msg = msg + self.lang.TRANSACTION.format(time, sum, payment_type)
            self.tg_bot.send_message(self.user.id, text=msg, parse_mode="HTML")
            return 1
        if call.data == self.lang.WALLET_LOAD_BTN:
            address = self.user.get_property('address')
            usd_price = btc_helper.get_latest_bitcoin_price('USD')
            eur_price = btc_helper.get_latest_bitcoin_price('EUR')
            msg = self.lang.WALLET_LOAD_MSG.format(address, usd_price, eur_price)
            self.tg_bot.send_message(self.user.id, text=msg, parse_mode="HTML")
            return 1
        return super().handle_callback(call)