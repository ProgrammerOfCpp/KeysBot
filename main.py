from bot import Bot
import time

while True:
    try:
        bot = Bot()
    except Exception as e:
        print(e)