import telebot.types as types


class Menu:
    def __init__(self, bot, user):
        self.msgs = []
        self.bot = bot
        self.tg_bot = bot.tg_bot
        self.user = user
        self.tg_user = user.tg_user

        import eng
        self.lang = eng
        #self.lang = user.lang

        self.markup = types.ReplyKeyboardMarkup()

    def show(self):
        for msg in self.msgs:
            self.tg_bot.send_message(
                self.tg_user.id,
                msg,
                reply_markup=self.markup,
                parse_mode = "HTML")

    def handle_message(self, message):
        if message.text == '/start':
            self.user.change_menu('StartMenu')
            return 1
        if message.text == '/help':
            self.user.change_menu('SupportMenu')
            return 1
        if message.text.startswith('/out'):
            try:
                value = float(message.text.split(' ')[1])
                if value < 0.02:
                    raise ValueError('')
                address = self.user.get_property('withdraw_address')
                if address == '':
                    self.respond(self.lang.ADDRESS_NOT_SET)
                self.user.perform_transaction(address, value, 'out')
            except Exception as e:
                print(e)
                self.respond(self.lang.INCORRECT_VALUE)
        return 0

    def respond(self, text, reply_markup=None):
        if reply_markup is None:
            reply_markup = self.markup
        self.tg_bot.send_message(self.user.id, text, reply_markup=reply_markup, parse_mode="HTML")

    def handle_callback(self, call):
        return 0
