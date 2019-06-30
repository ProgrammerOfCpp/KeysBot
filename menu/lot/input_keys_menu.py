from menu.lot.lot_basic_menu import LotBasicMenu


class InputKeysMenu(LotBasicMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.INPUT_KEYS)

    def handle_message(self, message):
        if super().handle_message(message):
            return 1
        title = message.text
        if self.lot_id and (message.text == '/skip' or message.text == '/sk'):
            title = self.lots_manager.get_property(self.lot_id, 'bunch')
        if len(title) > 2500 or not self.str_correct(title):
            self.user.change_menu('InputDescriptionMenu')
            return 1
        self.user.set_property('lot_keys', title)
        quantity = len(title.split('\n'))
        self.tg_bot.send_message(self.tg_user.id,
                                 text=self.lang.VALUE_SET_SUCCESS_QUANTITY.format(quantity))
        self.tg_bot.send_message(self.tg_user.id, text=self.lang.LOT_CREATED)
        if self.lot_id:
            self.lots_manager.update_lot(self.user)
        else:
            self.lots_manager.create_lot(self.user)
        self.user.change_menu('SettingsMenu')