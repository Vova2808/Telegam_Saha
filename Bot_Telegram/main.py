import requests
from bs4 import BeautifulSoup
import telebot
import time
from telebot import types

bot = telebot.TeleBot('YOUR_TOKEN')

@bot.message_handler(commands=['help'])
def help(message):
    hellp_text = '''Привет Пока Что Это Тестовый Бот Вот Что Он Умеет
    1. /obunga
    2. id - Твой Id
    3. /Taymer
    4. /Photo_Saha
    5. ПК Саши
    6. если кто-то хочет что-то добавить \n   то пишите мне @Vova17109'''
    bot.send_message(message.chat.id, hellp_text)

@bot.message_handler(commands=['Taymer'])
def novogogoda(message):
    timer_donovogogoda = 123
    while True:
        while (timer_donovogogoda > 0):
            time.sleep(1)
            bot.send_message(message.chat.id,"До нового года осталось ", str(timer_donovogogoda), ' секунд')
            timer_donovogogoda = timer_donovogogoda - 1
            if timer_donovogogoda == 0:
                bot.send_message(message.chat.id, 'Ура Новый Год')

@bot.message_handler(commands=['start'])
def strt(message):
    bot.send_message(message.chat.id, '<b>Привет это тестовый бот если \nхочешь узнать больше напиши /help</b>', parse_mode='html')

@bot.message_handler(commands=['DDOS_Saha'])
def ddossaha(message):
    bot.send_message(message.chat.id, 'Ты Что Саша')
    time.sleep(5)
    if message.text == 'да':
        bot.send_message(message.chat.id, '<b>ХИХИХИХА</b>', parse_mode='html')
        time.sleep(2)
        while True:
            bot.send_message(message.chat.id, 'https://youtu.be/CrQ8RdsTLz4')
    elif message.text == 'ДА':
        bot.send_message(message.chat.id, '<b>ХИХИХИХА</b>', parse_mode='html')
        time.sleep(2)
        while True:
            bot.send_message(message.chat.id, 'https://youtu.be/CrQ8RdsTLz4')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, '<b>ХИХИХИХА</b>', parse_mode='html')
        time.sleep(2)
        while True:
            bot.send_message(message.chat.id, 'https://youtu.be/CrQ8RdsTLz4')
    else:
        bot.send_message(message.chat.id, '<b>НУ ладно</b>', parse_mode='html')
    while True:
        bot.send_message(message.chat.id, 'https://youtu.be/CrQ8RdsTLz4')


@bot.message_handler(commands=['Photo_Saha'])
def photosaha(message):
    bot.send_message(message.chat.id, 'Пока что это все фото которые есть у меня ')
    photo = open('Saha.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo1 = open('Saha1.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo1)
    photo2 = open('Saha3.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo2)
    photo3 = open('Saha4.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    photo4 = open('Saha5.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo4)
    photo5 = open('Saha6.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo5)
    photo6 = open('Saha7.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo6)
    photo7 = open('Saha8.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo7)
    photo8 = open('Saha9.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo8)
    photo9 = open('Saha10.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo9)
    photo10 = open('Saha11.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo10)
    photo11 = open('Saha12.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo11)
    photo12 = open('Saha13.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo12)
    photo13 = open('Saha14.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo13)
    photo14 = open('Saha15.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo14)
    photo15 = open('Saha16.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo15)
    photo16 = open('Saha17.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo16)
    photo17 = open('Saha18.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo17)
    photo18 = open('Saha19.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo18)
    photo19 = open('Saha20.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo19)
    photo20 = open('Saha21.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo20)
    photo21 = open('Saha22.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo21)


#@bot.message_handler(commands=['game'])
#def gaem(message):
    #number = random.randint(1, 10)
    #bot.send_message(message.chat.id, "Я загадал число от 1 до 10 \nотгадай его")
    #while True:
        #if message.text == number:
            #bot.send_message(message.chat.id, 'Победа')
        #elif number < message.text:
            #bot.send_message(message.chat.id, 'Не верно')
            #break
        #elif number > message.text:
            #bot.send_message(message.chat.id, "Неверно")
        #else:
            #bot.send_message(message.chat.id, 'Это вообще не число')

@bot.message_handler(commands=['obunga'])
def obunga(message):
    bot.send_message(message.chat.id, 'https://memepedia.ru/wp-content/uploads/2018/07/cover-6-768x489.jpg')

@bot.message_handler(commands=['DDOS'])
def obunga_speed(message):
    while True:
        bot.send_message(message.chat.id, 'https://memepedia.ru/wp-content/uploads/2018/07/cover-6-768x489.jpg')

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, 'Это <b>Фото</b>', parse_mode='html')

@bot.message_handler(commands=['YouTube'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Мой канал" , url="https://www.youtube.com/channel/UC657UVzld-k3zgQDmN1R0XQ"))
    bot.send_message(message.chat.id, 'Мой канал', reply_markup=markup)

@bot.message_handler(commands=['websites'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    websites = types.InlineKeyboardButton('Веб Сайт', url="https://youtube.com")
    start = types.InlineKeyboardButton('Start', commands=['start'])
    markup.add(websites, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

#@bot.message_handler(commands=['python'])
#def python(message):
    #bot.send_message(message.chat.id, '''Ты хочешь научиться програмировать на Python
#То ты по адресу я могу порекомендовать
#Тебе для обучения пару книг хочешь получить
#Книгу то напиши боту /Python_Books там будет
#Ссылк на скачивание в папке будет книги по
#Кибербезопасносте и изучение Kali и Python
#А ещё могу порекомендовать блогеров которые
#Смогут научить тебя многому от взлома wifi до
#Перехвата трафик брутфорса подмена DNS и тд.
#Ну, если хочешь узнать их то напиши боту
#/Youtube_Blogers там их много но могу отметить
#Overbafer1 и David Bombal ну и it-спец
#А ещё я нашёл слитые курсы SkillBox Python если
#Надо то напиши боту /SkillBox там будет ссылка
#На торент трекер сам курс весит 32 гига
#Ну и мои просто рекоминдации посмотрите
#Серял Mr.Robot самый крутой серял про кб
#Если бы не он этого всего не было бы
#А так очень крутой серял советую посмотреть
#Всем ну на этом всё, пока друг ''')

@bot.message_handler(commands=['Python_Books'])
def Python_Boks(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Скачать", url='https://mega.nz/folder/HCA0lBYI#SDKB5laeFEjnqGmsWyv3yQ'))
    bot.send_message(message.chat.id, 'Книги для саморазвития', reply_markup=markup)

@bot.message_handler(commands=['SkillBox'])
def SkillBox(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Скачать', url='https://mega.nz/folder/HD4igJqS#UGRxNb-lW1_MCwrqA_Wm0Q'))
    bot.send_message(message.chat.id, 'Курсы SkillBox Python', reply_markup=markup)

@bot.message_handler(commands=['Youtube_Blogers'])
def blogers(message):
    blogers = '''1. David Bombal
2. Overbafer1
3. IT-спец. Денис Курец
4. NetworkChuck
5. PythonToday
6. UnderMind
7. Чёрный Треугольник
8. Хаскарь
Кажется Всё 
'''
    bot.send_message(message.chat.id, blogers)

@bot.message_handler(commands=['GDZ'])
def GDZ(message):
    #bot.send_message(message.chat.id, "Что за предмет: ")
    bot.reply_to(message, "Howdy, how are you doing?")
    if message.text == 'Алгебра':
        bot.send_message(message.chat.id, "Какой номер: ")
        url = 'https://gdz.ru/class-7/algebra/kolyagin-tkacheva/' + str(message.text) + "-nom/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        quotes = soup.find('div', class_='with-overtask')
        src = "https:" + quotes.find('img').get('src')
        src2 = "", str(src)

        for quote in src2:
            bot.send_message(message.chat.id, quote)
            #os.system("start " + str(quote))
            #os.system('start ' + str(url))

    elif message.text == 'Русский':
        bot.send_message(message.chat.id, "Какой номер: ")
        dz3 = int(message.text) + 5
        url = 'https://gdz.ru/class-7/russkii_yazik/razumovskaja-lvova-7/' + str(dz3) + "-nom/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        quotes = soup.find('div', class_='with-overtask')
        src = "https:" + quotes.find('img').get('src')
        src2 = "", str(src)

        for quote in src2:
            bot.send_message(message.chat.id, quote)
            #os.system('start ' + str(url))
            #os.system("start " + str(quote))

    else:
        bot.send_message(message.chat.id, "Пока что есть только русский и алгебра")


@bot.message_handler(content_types=["sticker"])
def sticker(message):
    bot.send_message(message.chat.id, 'Это <b>Это стикер</b>', parse_mode='html')

@bot.message_handler(content_types=["video"])
def video2(message):
    bot.send_message(message.chat.id, 'Это <b>Это видео</b>', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе Привет!')
    if message.text == 'Саша Васеленко':
        bot.send_message(message.chat.id, 'У Артёма нет пк')
    elif message.text == 'ПК Саши':
        Saha_PC = open('PC_Saha.mp4', 'rb')
        bot.send_video(message.chat.id, Saha_PC)
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID{message.from_user.id}')
    else:
        bot.send_message(message.chat.id, '<b>Я тебя не понимаю напиши <u>/help</u></b>', parse_mode='html')


bot.polling(none_stop=True)
