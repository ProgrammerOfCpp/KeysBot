from menu.interface_menu import InterfaceMenu
import btc_helper


class InputAddressMenu(InterfaceMenu):
    def __init__(self, bot, user):
        super().__init__(bot, user)
        self.msgs.append(self.lang.INPUT_ADDRESS_TEXT)

    def handle_message(self, message):
        if super().handle_message(message):
            return 1
        address = message.text
        if btc_helper.validate(address):
            self.user.set_property('withdraw_address', address)
            self.respond(self.lang.INPUT_ADDRESS_SUCCESS.format(address))
            self.user.go_back()
            return 1
        else:
            self.respond(self.lang.INCORRECT_VALUE)
            return 1
