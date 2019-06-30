from bit import Key


class User:
    def __init__(self, bot, tg_user):
        self.bot = bot
        self.tg_bot = bot.tg_bot
        self.tg_user = tg_user
        import eng
        self.lang = eng
        self.id = tg_user.id
        self.menu_id = self.get_property('menu_id')

    def change_menu(self, menu_id):
        if hasattr(self, 'menu_id'):
            self.set_property('prev_menu', self.menu_id)
        self.menu_id = menu_id
        self.set_property('menu_id', self.menu_id)
        menu = self.bot.get_menu(self)
        menu.show()

    def go_back(self):
        prev_menu = self.get_property('prev_menu')
        self.change_menu(prev_menu)

    def set_property(self, name, value):
        cursor = self.bot.connection.cursor()
        cursor.execute("UPDATE users SET " + name + "=%s WHERE id='%s'", (value, self.id))
        self.bot.connection.commit()
        return

    def get_property(self, name):
        cursor = self.bot.connection.cursor()
        cursor.execute("SELECT " + name + " FROM users WHERE id=%s", (self.id,))
        resp = cursor.fetchone()
        if resp is None:
            self.create()
            self.change_menu('StartMenu')
            return self.get_property(name)
        return resp[0]

    def create(self):
        import os, binascii, hashlib, base58
        fullkey = "80" + binascii.hexlify(os.urandom(32)).decode()
        sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
        sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
        WIF = base58.b58encode(binascii.unhexlify(fullkey + sha256b[:8]))
        priv = WIF.decode("utf-8")
        key = Key(priv)
        cursor = self.bot.connection.cursor()
        cursor.execute("INSERT INTO users (id, priv_key, address) VALUES(%s, %s, %s)", (self.id, WIF, key.address))
        self.bot.connection.commit()

    def get_balance(self):
        return self.get_property('balance')
        #key = Key(self.get_property('priv_key'))
        #return float(key.get_balance('btc'))

    def send_money(self, address, value, payment_type):
        try:
            cur = self.bot.connection.cursor()
            my_address = self.get_property('address')
            #key = Key(self.get_property('priv_key'))
            #outputs = [(address, value, 'btc')]
            #transaction = key.send(outputs))
            cur.execute("UPDATE users SET balance=balance-{:.8f} WHERE address='{}'".format(value, my_address))
            cur.execute("UPDATE users SET balance=balance+{:.8f} WHERE address='{}'".format(value, address))
            cur.execute("UPDATE users SET spent=spent+{:.8f} WHERE address='{}'".format(value, my_address))
            cur.execute("INSERT INTO transactions (address, sum, payment_type) VALUES(%s, %s, %s)", (my_address, value, payment_type))
            self.bot.connection.commit()
            return 1
        except Exception as e:
            print(e)
            return 0

    def perform_transaction(self, address, sum, payment_type):
        self.set_property('transaction_address', address)
        self.set_property('transaction_sum', sum)
        self.set_property('payment_type', payment_type)
        self.change_menu('PaymentMenu')

    def add_transaction(self, sum):
        cursor = self.bot.connection.cursor()
        cursor.execute("INSET INTO transactions (user_id, sum) VALUES(%s, %s)", (self.id, sum))
        cursor.commit()

    def get_transactions(self):
        cursor = self.bot.connection.cursor()
        cursor.execute("SELECT * FROM transactions WHERE address=%s", (self.get_property('address'),))
        return cursor.fetchall()
