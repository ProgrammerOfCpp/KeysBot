from telebot import types


class LotsManager:
    def __init__(self, bot):
        self.bot = bot
        self.connection = bot.connection

    def get_lots(self, user, only_created=False):
        cur = self.connection.cursor()
        show_all = user.get_property('show_all')
        if show_all:
            if not only_created:
                cur.execute("SELECT * FROM lots")
            else:
                cur.execute("SELECT * FROM lots WHERE user_id=%s", (user.id,))
        else:
            cur.execute("SELECT * FROM lots WHERE id IN(SELECT lot_id FROM favourite WHERE user_id=%s)", (user.id,))
        return cur.fetchall()

    def search_lots(self, user, keyword):
        cur = self.connection.cursor()
        show_all = user.get_property('show_all')
        if show_all:
            cur.execute("SELECT * FROM lots WHERE title LIKE %s", ('%' + keyword + '%',))
        else:
            cur.execute("""SELECT * FROM lots WHERE title LIKE %s AND 
            id IN(SELECT lot_id FROM favourite WHERE user_id=%s)""", ('%' + keyword + '%', user.id,))
        return cur.fetchall()

    def get_lot_by_title(self, title):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM lots WHERE title=%s", (title,))
        resp = cur.fetchone()
        return resp

    def is_title_free(self, title):
        return self.get_lot_by_title(title) is None

    def create_lot(self, user):
        title = user.get_property('lot_title')
        desc = user.get_property('lot_description')
        price = user.get_property('lot_price')
        keys = user.get_property('lot_keys')
        basic_keys_count = len(keys.split('\n'))
        cur = self.connection.cursor()
        cur.execute("INSERT INTO lots (title, description, bunch, price, basic_keys_count, user_id) "
                    "VALUES(%s, %s, %s, %s, %s, %s)", (title, desc, keys, price, basic_keys_count, user.id))
        self.connection.commit()

    def update_lot(self, user):
        id = user.get_property('lot_id')
        title = user.get_property('lot_title')
        desc = user.get_property('lot_description')
        price = user.get_property('lot_price')
        keys = user.get_property('lot_keys')
        cur = self.connection.cursor()
        cur.execute("UPDATE lots SET title=%s, description=%s, price=%s, bunch=%s WHERE id=%s", (title, desc, price, keys, id))
        self.connection.commit()

    def get_property(self, id, name):
        cursor = self.bot.connection.cursor()
        cursor.execute("SELECT " + name + " FROM lots WHERE id=%s", (id,))
        resp = cursor.fetchone()
        return resp[0]

    def set_property(self, id, name, value):
        cursor = self.bot.connection.cursor()
        cursor.execute("UPDATE lots SET " + name + "=%s WHERE id=%s", (value, id))
        self.connection.commit()

    def delete_lot(self, id):
        cursor = self.bot.connection.cursor()
        cursor.execute("DELETE FROM lots WHERE id=%s", (id,))
        self.connection.commit()

    def get_owner_address(self, id):
        owner_id = self.get_property(id, 'user_id')
        cursor = self.bot.connection.cursor()
        cursor.execute("SELECT address FROM users WHERE id=%s", (owner_id,))
        return cursor.fetchone()[0]

    def put_like(self, id, user_id):
        cursor = self.bot.connection.cursor()
        cursor.execute("UPDATE lots SET likes=likes+1 WHERE id=%s", (id,))
        cursor.execute("INSERT INTO favourite (user_id, lot_id) VALUES(%s, %s)", (user_id, id))
        self.connection.commit()

    def put_dislike(self, id, user_id):
        cursor = self.bot.connection.cursor()
        cursor.execute("UPDATE lots SET dislikes=dislikes+1 WHERE id=%s", (id,))
        cursor.execute("DELETE FROM favourite WHERE user_id=%s AND lot_id=%s", (user_id, id))
        self.connection.commit()

    def get_keys_count(self, id):
        bunch = self.get_property(id, 'bunch')
        if bunch == '':
            return 0
        else:
            return len(bunch.split('\n'))

    def get_key(self, id):
        bunch = self.get_property(id, 'bunch')
        if bunch == '':
            return None
        else:
            keys = bunch.split('\n')
            return keys[0]

    def clear_key(self, id):
        bunch = self.get_property(id, 'bunch')
        if bunch == '':
            return
        else:
            keys = bunch.split('\n')
            bunch = ''
            for i in range(1, len(keys)):
                bunch = bunch + keys[i]
                if i + 1 < len(keys):
                    bunch = bunch + '\n'
            self.set_property(id, 'bunch', bunch)

    def show_info(self, lot_id, user):
        title = self.get_property(lot_id, 'title')
        desc = self.get_property(lot_id, 'description')
        status = self.get_property(lot_id, 'active')
        likes = self.get_property(lot_id, 'likes')
        dislikes = self.get_property(lot_id, 'dislikes')
        available = self.get_keys_count(lot_id)
        all = self.get_property(lot_id, 'basic_keys_count')
        sold = all - available
        msg_text = user.lang.LOT_INFO.format(title, desc, status, all, sold, available, likes, dislikes)

        markup = types.InlineKeyboardMarkup()
        user_id = self.get_property(lot_id, 'user_id')
        price = self.get_property(lot_id, 'price')
        if user_id == user.id:
            markup.add(types.InlineKeyboardButton(text=user.lang.ACTIVATE_BTN,
                                                  callback_data=user.lang.ACTIVATE_BTN),
                       types.InlineKeyboardButton(text=user.lang.DEACTIVATE_BTN,
                                                  callback_data=user.lang.DEACTIVATE_BTN))
            markup.add(types.InlineKeyboardButton(text=user.lang.EDIT_BTN,
                                                  callback_data=user.lang.EDIT_BTN),
                       types.InlineKeyboardButton(text=user.lang.DELETE_BTN,
                                                  callback_data=user.lang.DELETE_BTN))
        else:
            markup.add(types.InlineKeyboardButton(text=user.lang.BUY_FOR.format(price),
                                                  callback_data=user.lang.BUY_FOR))

        self.bot.tg_bot.send_message(user.id, text=msg_text, reply_markup=markup, parse_mode="HTML")
    