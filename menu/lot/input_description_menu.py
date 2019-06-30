from menu.lot.lot_basic_menu import LotBasicMenu


class InputDescriptionMenu(LotBasicMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.INPUT_DESCRIPTION)

    def handle_message(self, message):
        if super().handle_message(message):
            return 1
        title = message.text
        if self.lot_id and (message.text == '/skip' or message.text == '/sk'):
            title = self.lots_manager.get_property(self.lot_id, 'description')

        if len(title) > 2500 or not self.str_correct(title):
            self.user.change_menu('InputDescriptionMenu')
            return
        self.user.set_property('lot_description', title)
        self.tg_bot.send_message(self.tg_user.id, text=self.lang.VALUE_SET_SUCCESS)
        self.user.change_menu('InputPriceMenu')