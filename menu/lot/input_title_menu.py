from menu.lot.lot_basic_menu import LotBasicMenu


class InputTitleMenu(LotBasicMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.INPUT_TITLE)
        if self.lot_id:
            self.msgs.append(self.lang.SKIP_HINT)

    def handle_message(self, message):
        if super().handle_message(message):
            return 1
        title = message.text
        if not self.lots_manager.is_title_free(title):
            self.tg_bot.send_message(self.tg_user.id, text=self.lang.TRY_ANOTHER_TITLE)
            self.user.change_menu('InputTitleMenu')
            return 1

        if self.lot_id and (message.text == '/skip' or message.text == '/sk'):
            title = self.lots_manager.get_property(self.lot_id, 'title')

        if len(title) > 100 or not self.str_correct(title):
            self.user.change_menu('InputTitleMenu')
            return 1
        self.user.set_property('lot_title', title)
        self.tg_bot.send_message(self.tg_user.id, text=self.lang.VALUE_SET_SUCCESS)
        self.user.change_menu('InputDescriptionMenu')
