"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime, timezone


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet_in_constellation(update, context):
    planets = {
    'mars':    ephem.Mars,
    'venus':   ephem.Venus,
    'jupiter': ephem.Jupiter,
    'saturn':  ephem.Saturn,
    'mercury': ephem.Mercury,
    'uranus':  ephem.Uranus,
    'neptune': ephem.Neptune    
    }
    text_from_user = update.message.text
    splitted_text_from_user = text_from_user.split()
    now = datetime.now(timezone.utc).strftime('%Y/%m/%d')

    del splitted_text_from_user[0]
 
    if len(splitted_text_from_user) >= 1:
        for word in splitted_text_from_user:
            word = word.lower()
            print(word)
            if word not in planets:
                    print('Перечень планет: Mars, Venus, Jupiter, Saturn, Mercury, Uranus, Neptune')
                    update.message.reply_text(f'Перечень планет: Mars, Venus, Jupiter, Saturn, Mercury, Uranus, Neptune')
            else:            
                try:                      
                    planet = planets[word](now)              
                    answer = ephem.constellation(planet)
                    print(answer)    
                    update.message.reply_text(f'{word.capitalize()} сейчас в созвездии {answer[1]}')
                except ValueError:
                    update.message.reply_text(f'Не удалось определить созвездие для {word}')
    else:
        update.message.reply_text(f'Перечень планет: Mars, Venus, Jupiter, Saturn, Mercury, Uranus, Neptune')
        
def main():
    # mybot = Updater("8784351488:AAGIW4Oe1mCM_dYiVUAZgk_e55-teEeJd9M", request_kwargs=PROXY, use_context=True)
    mybot = Updater("8784351488:AAGIW4Oe1mCM_dYiVUAZgk_e55-teEeJd9M", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_in_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
