from menu.lot.lot_basic_menu import LotBasicMenu
import btc_helper
import consts


class InputPriceMenu(LotBasicMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        min_price = consts.MIN_LOT_PRICE_BTC * btc_helper.get_latest_bitcoin_price('EUR')
        self.msgs.append(self.lang.INPUT_PRICE.format(min_price))

    def handle_message(self, message):
        if super().handle_message(message):
            return 1
        title = message.text
        try:
            if self.lot_id and (message.text == '/skip' or message.text == '/sk'):
                title = self.lots_manager.get_property(self.lot_id, 'price')
            price = float(title)
            min_price = consts.MIN_LOT_PRICE_BTC * btc_helper.get_latest_bitcoin_price('EUR')
            if price < min_price:
                self.user.change_menu('InputPriceMenu')
                return 1
            self.user.set_property('lot_price', title)
            self.tg_bot.send_message(self.tg_user.id, text=self.lang.VALUE_SET_SUCCESS)
            self.user.change_menu('InputKeysMenu')
        except:
            self.user.change_menu('InputPriceMenu')