import telebot
import mysql.connector
import sys
import inspect
from lots_manager import LotsManager
from user import User
from menu_imports import *

hostname = 'localhost'
username = 'root'
password = ''
database = 'keys_sender'


class Bot:
    def __init__(self):
        self.menus = self.register_menus()
        self.connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database)
        self.tg_bot = telebot.TeleBot('883779953:AAFqXJwT-FcXYq4Dz5TdefXaK-EQYwhc4EY')
        self.lots_manager = LotsManager(self)

        @self.tg_bot.message_handler()
        def handle_message(message):
            user = User(self, message.from_user)
            menu = self.get_menu(user)
            menu.handle_message(message)

        @self.tg_bot.callback_query_handler(func=lambda call: True)
        def handle_callback(call):
            user = User(self, call.from_user)
            menu = self.get_menu(user)
            menu.handle_callback(call)

        self.tg_bot.polling()

    def stop(self):
        print('Stopping...')
        self.connection.close()

    def get_menu(self, user):
        try:
            menu_class = self.menus[user.menu_id]
        except Exception as e:
            print(e)
            user.change_menu('SupportMenu')
            return self.get_menu(user)
        return menu_class(self, user)

    def register_menus(self):
        from menu.menu import Menu
        menus = {}
        class_members = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for (name, cls) in class_members:
            if (issubclass(cls, Menu)):
                menus[name] = cls
        return menus
