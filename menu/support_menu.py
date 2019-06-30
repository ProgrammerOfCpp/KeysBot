from menu.interface_menu import InterfaceMenu


class SupportMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.SUPPORT_MSG)

    def handle_message(self, message):
        return super().handle_message(message)