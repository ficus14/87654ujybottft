# -*-coding: utf-8 -*-
import logging
import sqlite3
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import quote_html
from aiogram.types import ContentTypes
from aiogram.types import ContentType
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
from decimal import Decimal
import requests
from pycoingecko import CoinGeckoAPI

logging.basicConfig(level=logging.INFO)


# CoinGeckoAPI
api = CoinGeckoAPI()

# bot init
bot = Bot(token='6028541327:AAGYzWpH8dErakb3PbOeDyguWVcvfdFhflM')
dp = Dispatcher(bot)

# datebase
connect = sqlite3.connect("users.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    skin_id INT,
    level INT,
    balance INT,
    bank BIGINT,
    deposit INT,
    bitkoin INT,
    Ecoins INT,
    energy INT,
    expe INT,
    games INT,
    game INT,
    user_name STRING,
    user_status STRING,
    deposit_status INT,
    rating INT,
    work INT,
    pet1 INT,
    pet2 INT,
    pet3 INT,
    pet4 INT,
    pet5 INT,
    pet6 INT,
    pet7 INT,
    pet8 INT,
    pet9 INT,
    pet10 INT,
    pet_name STRING,
    pet_hp INT,
    pet_eat INT,
    pet_mood INT,
    checking INT,
    checking1 INT,
    checking2 INT,
    checking3 INT,
    status_block STRING
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS mine(
    user_id BIGINT,
    user_name STRING,
    iron INT,
    gold INT,
    diamonds INT,
    amethysts INT,
    aquamarine INT,
    emeralds INT,
    matter INT,
    plasma INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS workshop(
    user_id BIGINT,
    user_name STRING,
    work_shop INT,
    workshop_c INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
    user_id BIGINT,
    user_name STRING,
    linen INT,
    cotton INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS property(
    user_id BIGINT,
    user_name STRING,
    have STRING,
    yacht INT,
    cars INT,
    plane INT,
    helicopter INT,
    house INT,
    phone INT,
    business INT,
    farm INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_bonus(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_merii(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_work(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot_craft(
    user_id INT,
    last_stavka INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ban_list(
    user_id INT,
    user_name STRING,
    Cause STRING
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS admins(
    user_id BIGINT,
    user_name STRING,
    user_status STRING
)
""")


# start command
@dp.message_handler(text=['Статистика бота','статистика бота'])
async def stats(message):
     user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
     user_name = str(user_name[0])
    
     sqlite_select_query = """SELECT * from users"""
     cursor.execute(sqlite_select_query)
     records = cursor.fetchall()

     await bot.send_message(message.chat.id, f"{user_name}, статистика бота  📊\n🤵 | Игроков: {len(records)}", parse_mode='html')

@dp.message_handler(lambda message: message.text.lower() == 'КНБ')
async def process_command_1(message: types.Message):
    
    button1 = InlineKeyboardButton('🗿Камень', callback_data = '1')
    button2 = InlineKeyboardButton('✂️Ножницы', callback_data = '2')
    button3 = InlineKeyboardButton('📄Бумага', callback_data = '3')
    buttons = InlineKeyboardMarkup().add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Я готов играть!\nВыбери предмет, что бы сыграть со мной🎭", reply_markup= buttons)

@dp.callback_query_handler(lambda c: c.data == '1')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал 🗿Камень")
    if rand == '🗿Камень':
        await callback.message.answer("У нас ничья🤝")
    elif rand == '✂️Ножницы':
        await callback.message.answer("Ты выиграл🥇")
    else:
        await callback.message.answer("Я победил🥇")

@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы")
    if rand == '🗿Камень':
        await callback.message.answer("Я победил🥇")
    elif rand == '✂️Ножницы':
        await callback.message.answer("У нас ничья🤝")
    else:
        await callback.message.answer("Ты победил🥇")

@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы")
    if rand == '🗿Камень':
        await callback.message.answer("Я победил🥇")
    elif rand == '✂️Ножницы':
        await callback.message.answer("У нас ничья🤝")
    else:
        await callback.message.answer("Ты победил🥇")

@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы")
    if rand == '🗿Камень':
        await callback.message.answer("Я победил🥇")
    elif rand == '✂️Ножницы':
        await callback.message.answer("У нас ничья🤝")
    else:
        await callback.message.answer("Ты победил🥇")

@dp.callback_query_handler(lambda c: c.data == '3')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал 📄Бумага")
    if rand == '🗿Камень':
        await callback.message.answer("Ты победил🥇")
    elif rand == '✂️Ножницы':
        await callback.message.answer("Я победил🥇")
    else:
        await callback.message.answer("У нас ничья🤝")
 
@dp.message_handler(commands=['start'])
async def start_cmd(message):
    msg = message
    pet_name = "name"
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    user_status = "Player"
    have = 'off'
    status_block = 'off'
    chat_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ? , ?, ? , ? , ? , ? , ? , ? , ? , ?);",
                       (user_id, 1, 1, 10000, 0, 0, 0, 0, 10, 0, 0, user_name, user_status, 0, 0, 0, 0, 0,0,0,0,0,0,0,0, 0, pet_name,0,0,0, 0, 0, 0, 0, status_block))
        cursor.execute("INSERT INTO property VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (user_id, user_name, have, 0, 0, 0, 0, 0, 0, 0, 0))
        cursor.execute("INSERT INTO mine VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (user_id, user_name, 0, 0, 0, 0, 0, 0, 0, 0))
        cursor.execute("INSERT INTO farm VALUES(?, ?, ?, ?);", (user_id, user_name, 0, 0))
        cursor.execute("INSERT INTO workshop VALUES(?, ?, ?, ?);", (user_id, user_name, 0, 0))
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        cursor.execute("INSERT INTO bot_bonus VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_merii VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_work VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_craft VALUES(?, ?);", (user_id, 0))
        connect.commit()
    else:
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        cursor.execute("INSERT INTO bot_bonus VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_merii VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_work VALUES(?, ?);", (user_id, 0))
        cursor.execute("INSERT INTO bot_craft VALUES(?, ?);", (user_id, 0))
        connect.commit()
        return

    name1 = message.from_user.get_mention(as_html=True)
    await message.reply(
        f' 👋Привет {name1}\nЯ бот для игры в различные игры.\nТебе выдан подарок в размере 10.000$.\n\nТак же ты можешь добавить меня в беседу для игры с друзьями.\n🆘 Чтобы узнать все команды введи "Помощь"\nПриятной игры!😊',
                         parse_mode='html')



@dp.message_handler(text=['Инфо','инфо'])
async def info_user(message: types.Message):
    
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.full_name
    skin_id = cursor.execute("SELECT skin_id from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
    skin_id = int(skin_id[0])
    level = cursor.execute("SELECT level from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    level = int(level[0])
    balance = cursor.execute("SELECT balance from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    balance = int(balance[0])
    bank = cursor.execute("SELECT bank from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    bank = int(bank[0])
    deposit = cursor.execute("SELECT deposit from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    deposit = int(deposit[0])
    bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    bitkoin = int(bitkoin[0])
    Ecoins = cursor.execute("SELECT Ecoins from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    Ecoins = int(Ecoins[0])
    rating = cursor.execute("SELECT rating from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    rating = int(rating[0])
    user_status_reply = cursor.execute("SELECT user_status from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    user_status_reply = str(user_status_reply[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    name = message.from_user.get_mention(as_html=True)

    if user_status_reply == 'Player':
        user_status_reply2 = 'Игрок'
    if user_status_reply == 'Admin':
        user_status_reply2 = 'Администратор'
    if user_status_reply == 'Rab':
        user_status_reply2 = 'Разработчик'

    balance2 = '{:,}'.format(balance)
    bank2 = '{:,}'.format(bank)
    Ecoins2 = '{:,}'.format(Ecoins)
    rating2 = '{:,}'.format(rating)
    bitkoin2 = '{:,}'.format(bitkoin)
    deposit2 = '{:,}'.format(deposit)
    if user_status == 'Rab':
        await bot.send_message(message.chat.id, f'''
{name}, информация о игроке:

    👫Ник: {user_name}
    🔎ID: {user_id}
    👕Skin_ID: {skin_id}
    💰Деньги: {balance2}$
    🏛Банк: {bank2}$
    📧E-coins: {Ecoins2}
    👑Рейтинг: {rating2} 
    🏪Депозит: {deposit2}
    💽Биткоины: {bitkoin2}
    🧊Статус: {user_status_reply2}
    👑Наш канал: В разработке
''', parse_mode='html')
        return
    if user_status == 'Admin':
        await bot.send_message(message.chat.id, f'''
{name}, информация о игроке:

    👫Ник: {user_name}
    🔎ID: {user_id}
    👕Skin_ID: {skin_id}
    💰Деньги: {balance2}$
    🏛Банк: {bank2}$
    👑Рейтинг: {rating2} 
    💽Биткоины: {bitkoin2}
    🧊Статус: {user_status_reply2}
    👑Наш канал: В разработке
''', parse_mode='html')
        return
    else:
        await bot.send_message(message.chat.id, f'{name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰. Наш telegram канал - В разработке', parse_mode='html')


@dp.message_handler(commands=['ping', 'пинг'], commands_prefix=["/", "!"])
async def ping(message: types.Message):
    a = time.time()
    bot_msg = await message.answer(f'⚙ Проверка пинга....')
    if bot_msg:
        b = time.time()
        await bot_msg.edit_text(f'🏓 Пинг: {round((b - a) * 1000)} ms')
                        
@dp.message_handler(lambda t: t.text.startswith("Шанс"))
async def fff(message: types.Message):
       h = ["37%","20%","29%","10%","100%","21%,","22%","52%","55%","2%","6%","8%","7%","11%","54%","45%","21%","1%","87%","0%","12%","76%"]
       g = random.choice(h)
       await message.reply(f"""Шанс этого {g} """)   
       
@dp.message_handler(lambda t: t.text.startswith("Шар"))
async def fff(message: types.Message):
       h = ["Мой ответ - нет","Мне кажется - да","Сейчас нельзя предсказать","Мне кажется - нет","Знаки говорят - нет","Да","Нет","Можешь быть уверен в этом"]
       g = random.choice(h)
       await message.reply(f"""{g} """)                                                                
@dp.message_handler(lambda t: t.text.startswith("Выбери"))
async def fff(message: types.Message):
       h = ["Мне кажется,что 1 вариант лучше","Однозначно второй","Однозначно первый","Второй вариант лучше","Первый вариант лучше"]
       g = random.choice(h)
       await message.reply(f"""{g} """) 
                                             
@dp.message_handler(lambda msg: msg.text.lower() == 'бот') 
async def check_bot(message): 
    await message.reply('✅Бот работает!')             
#Репутация
@dp.message_handler(lambda msg: msg.text.lower().startswith('+'))
async def plus_rep(message):
   if not message.reply_to_message:
      await message.reply("Эта команда должна быть ответом на сообщение!")
      return
   if message.from_user.id == message.reply_to_message.from_user.id:
      await message.reply("А нельзя накручивать себе репутацию!🖕")
      return
      db.UpdateUserValue('reputation', 1, message.reply_to_message.from_user.id)
      db.con.commit()
      await message.reply("Повышение репутации засчитано👍")

@dp.message_handler(lambda msg: msg.text.lower().startswith('-'))
async def minus_rep(message):
   if not message.reply_to_message:
      await message.reply("Эта команда должна быть ответом на сообщение!")
      return
   if message.from_user.id == message.reply_to_message.from_user.id:
      await message.reply("Накручивать репутацию запрещено!🖕")
      return
   db.UpdateUserValueMinus('reputation', 1, message.reply_to_message.from_user.id)
   db.con.commit()
   await message.reply("Понижение репутации засчитано👎")               

@dp.message_handler(commands=['r'])
async def report(message: types.Message):
  try:
    if message.text == '/report' or message.text == '/r' or not message.reply_to_message:
      await bot.send_message(message.chat.id, '''Вот информация за систему репортов ⛔️

⚠️ | Правила по использованию репортов
     [1️⃣] Материться, оскорблять кого-либо, проявлять неуважение к администрации и тому подобное.
      [2️⃣] Капсить, писать неразборчиво, использовать спам, писать один и тот-же текст несколько раз получивши на него ответ.
      [3️⃣] Всячески дразнить администрацию и отвлекать от работы.
      [4️⃣] Запрещено интересоваться/писать вещи которые ни коем образом ни относятся к игре
      [5️⃣] Запрещена реклама в любом её проявлении
      [6️⃣] Запрещено обращаться к своим друзьям администраторам по личным вопросам
      7️⃣ | Запрещено клеветать на игроков, обвинять их в нарушениях, которые они не совершали.
      [8️⃣] Репорт работает по принципу - Вопрос/Просьба/Жалоба (исключение - Приветствие) и не иначе. Иные формы обращения будут оставаться без ответа и будет выдано наказание.

[⚠️] | Форма отправки репорта - /report [сообщение]

[⛔️] | Прошу вас соблюдать правила отправки репорта
Для связи - @Ficus1_1
Наш telegram канал - В разработке''')
    else:
      members = await message.chat.get_member(message.reply_to_message.from_user.id)
      info = await bot.get_chat_member(message.chat.id, message.from_user.id)
      report = message.text.replace('/r ', '')
      report = report.replace('/report ', '')
      admins = await bot.get_chat_administrators('@' + message.chat.username)
      send = 0
      for admin in admins:
        if admin.user.username != 'Group_Moder_bot':
          try:
            await bot.send_message(admin.user.id, f'[📬] | Репорт по причине: ' + str(report) + f'\n\nhttps://t.me/{message.chat.username}/{message.reply_to_message.message_id}')
          except:
            pass
          send += 1

      if send == 0:
        await bot.send_message(message.chat.id, '[👮] | Админы не оповещены, для отправки им репортов надо чтобы они запустили меня в лс!')
      else:
        await bot.send_message(message.chat.id, '''[✅] | ваш репорт был успешно отправлен администрации''')
  except:
    pass
   
@dp.message_handler(text=['Пост'])
async def posting(message):
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_id = message.from_user.id
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    text = message.text[5:]
    
    if user_status == 'Rab':
       rows = cursor.execute('SELECT user_id FROM users').fetchall()
       for row in rows:
          await bot.send_message(row[0], text)        
                  
@dp.message_handler(commands=['bind', 'привязать', 'привязка', 'пр'], commands_prefix='!./')
async def privazka(message):
  db.cursor.execute(f"SELECT name FROM aleks_bot where id = {message.from_user.id}")
  if db.cursor.fetchone() == None:
    db.InsertValues(message.from_user.first_name, message.from_user.id)
  if message.chat.type == 'supergroup':
    cdb.cursor.execute(f"SELECT chat_name, chat_id FROM chats_aleks where chat_id = {message.chat.id}")
    if cdb.cursor.fetchone() == None:
      cdb.InsertChatValues(message.chat.title, message.chat.id)
      await message.reply('Вы привязали бота к чату 🛡')
    else:
      await message.reply('Бот уже привязан к чату ✅')
  if message.chat.type == 'private':
    await message.reply('Введите эту команду в своем чате 👻') 
        
@dp.message_handler(commands=['ping', 'пинг'], commands_prefix=["/", "!"])
async def ping(message: types.Message):
 a = time.time()
 bot_msg = await message.answer(f'Проверка пинга...')
 if bot_msg:
  b = time.time()
 await bot_msg.edit_text(f'Пинг бота: {round((b-a)*1000)} мс')  
                                                             
        
###########################################БАЛАНС###########################################
@dp.message_handler()
async def prof_user(message: types.Message):
    name = message.from_user.get_mention(as_html=True)
    status_block = cursor.execute("SELECT status_block from users where user_id = ?",
                                  (message.from_user.id,)).fetchone()
    status_block = str(status_block[0])
    status_reg = 'on'

    if status_block == 'off':
        if message.forward_date != None:
            rx = ['😌', '🥱', '🙄', '😎', '😏']
            rdrx = random.choice(rx)
            await bot.send_message(message.chat.id, f)
            return
        
        if message.text.lower() in ["купить питомца 1", "Купить питомца 1"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 1000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet1 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐥 | {user_name}, вы успешно купили цыплёнка за 1.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet1 = {pet1 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet1 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')     

        if message.text.lower() in ["купить питомца 2", "Купить питомца 2"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 100000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet2 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐈 | {user_name}, вы успешно купили кота за 100.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet2 = {pet2 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet2 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')     

        if message.text.lower() in ["купить питомца 3", "Купить питомца 3"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 500000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet3 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐕 | {user_name}, вы успешно купили пса за 500.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet3 = {pet3 + c} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet3 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

        if message.text.lower() in ["купить питомца 4", "Купить питомца 4"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 1000000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet4 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🦜 | {user_name}, вы успешно купили попугая за 1.000.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet4 = {pet4 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet4 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

        if message.text.lower() in ["купить питомца 5", "Купить питомца 5"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 50000000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet5 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🦄 | {user_name}, вы успешно купили единорога за 50.000.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet5 = {pet5 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet5 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')  

        if message.text.lower() in ["купить питомца 6", "Купить питомца 6"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 100000000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet6 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐒 | {user_name}, вы успешно купили обезьяну за 100.000.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet6 = {pet6 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet6 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html')                        

        if message.text.lower() in ["купить питомца 7", "Купить питомца 7"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 500000000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet7 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐬 | {user_name}, вы успешно купили дельфина за 500.000.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet7 = {pet7 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet7 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

        if message.text.lower() in ["купить питомца 8", "Купить питомца 8"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 10000000000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet8 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐅 | {user_name}, вы успешно купили тигра за 10.000.000.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet8 = {pet8 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet8 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

        if message.text.lower() in ["купить питомца 9", "Купить питомца 9"]:    
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            msg = message
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            user_id = msg.from_user.id
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            summ = 100000000000000
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            print(pets)
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if int(pets) == 0:
                if pet9 == 0:
                    if int(balance) >= int(summ):
                        await bot.send_message(message.chat.id, f'🐉 | {user_name}, вы успешно купили дракона за 100.000.000.000.000$ 🎉', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet9 = {pet9 + c} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                        connect.commit()    
                        return
                    else:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                        return
                if pet9 == 1:
                    await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас уже есть данный питомец! {rloser}', parse_mode='html')     
                    return
            if pets == 1:
                await bot.send_message(message.chat.id, f'ℹ️ |{user_name}, у вас уже есть питомец! {rloser}', parse_mode='html') 

        if message.text.lower() in ["мой питомец", "Мой питомец"]:        
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')    
            if pet1 == 1:
                
                await message.bot.send_message(message.chat.id, f'🐥 | {user_name}, ваш питомец: цыплёнок \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')            
            if pet2 == 1:     
               
                await message.bot.send_message(message.chat.id, f'🐈 | {user_name}, ваш питомец: кот \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                    
            if pet3 == 1:   
                
                await message.bot.send_message(message.chat.id, '🐕 | {user_name}, ваш питомец: пёс \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                            
            if pet4 == 1:           
                
                await message.bot.send_message(message.chat.id, f'🦜 | {user_name}, ваш питомец: попугай \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                            
            if pet5 == 1:
                
                await message.bot.send_message(message.chat.id, f'🦄 | {user_name}, ваш питомец: единорог \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
            if pet6 == 1:
                
                await message.bot.send_message(message.chat.id, f'🐒 | {user_name}, ваш питомец: обезьяна \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
            if pet7 == 1:
                
                await message.bot.send_message(message.chat.id, f'🐬 | {user_name}, ваш питомец: дельфин \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
            if pet8 == 1:
                
                await message.bot.send_message(message.chat.id, f'🐅 | {user_name}, ваш питомец: тигр \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       
            if pet9 == 1: 
                
                await message.bot.send_message(message.chat.id, f'🐉 | {user_name}, ваш питомец: дракон \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                      
            if pet10 == 1:
                
                await message.bot.send_message(message.chat.id, f'☃️ | {user_name}, ваш питомец: снеговик \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу', parse_mode='html')                                       

        if message.text.lower() in ["вылечить питомца", "Вылечить питомца"]:  
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
            c = Decimal((100 - pet_hp) * 10000)
            c2 = (100 - pet_hp) * 10000
            hp = 100 - pet_hp
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')  
            if pet1 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet2 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet3 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet4 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet5 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet6 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet7 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet8 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')
            if pet9 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')

            if pet10 == 1:
                if pet_hp < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'❤ | {user_name}, вы вылечили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_hp == 100:
                    await bot.send_message(message.chat.id, f'❤ | {user_name}, ваш питомец не нуждается в лечении!', parse_mode='html')

        if message.text.lower() in ["покормить питомца", "Покормить питомца"]:  
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
            c = Decimal((100 - pet_eat) * 10000)
            c2 = (100 - pet_eat) * 10000
            eat = 100 - pet_eat
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')  
            if pet1 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден! {rloser}', parse_mode='html')
            if pet2 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
            if pet3 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
            if pet4 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
            if pet5 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден! {rloser}', parse_mode='html')
            if pet6 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
            if pet7 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
            if pet8 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')
            if pet9 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')

            if pet10 == 1:
                if pet_eat < 100:
                    if c <= balance:
                        await bot.send_message(message.chat.id, f'🍗 | {user_name}, вы покормили своего питомца за {c}!', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                        cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
                    if c > balance:
                        await bot.send_message(message.chat.id, f'💰 | {user_name}, недостаточно средств! {rloser}', parse_mode='html')
                if pet_eat == 100:
                    await bot.send_message(message.chat.id, f'🍗 | {user_name}, ваш питомец не голоден!', parse_mode='html')

        if message.text.lower() in ["выгулять питомца", "Выгулять питомца"]:  
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10
            c = Decimal((100 - pet_mood) * 10000)
            mood = 100 - pet_mood
            checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking = round(int(checking[0]))
            if checking == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')  
            if pet1 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet2 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet3 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet4 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet5 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet6 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet7 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet8 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')
            if pet9 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')

            if pet10 == 1:
                if pet_mood < 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, вы выгуляли своего питомца!', parse_mode='html')
                    cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
                if pet_mood == 100:
                    await bot.send_message(message.chat.id, f'🌳 {user_name}, ваш питомец не хочет гулять!', parse_mode='html')

        if message.text.startswith("питомец имя"): 
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            name = str(message.text.split()[2])
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')
            if pet1 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet2 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet3 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet4 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet5 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet6 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet7 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet8 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet9 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')

        if message.text.startswith("Питомец имя"): 
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            name = str(message.text.split()[2])
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')
            if pet1 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet2 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet3 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet4 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet5 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet6 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet7 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet8 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
            if pet9 == 1:
                await bot.send_message(message.chat.id, f'✏️ | {user_name}, вы успешно поменяли имя своего питомца на: {name}!', parse_mode='html')
                cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')

        if message.text.lower() in ["продать питомца", "Продать питомца"]:
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
            if pets == 0:
                await bot.send_message(message.chat.id, f'ℹ️ | {user_name}, у вас нету питомца! {rloser}', parse_mode='html')
            if pet1 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 750.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 750000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet1 = {pet1 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet2 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 75.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 75000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet2 = {pet2 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet3 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 375.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 375000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet3 = {pet3 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet4 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 750.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 750000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet4 = {pet4 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet5 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 37.500.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 37500000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet5 = {pet5 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet6 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 75.000.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 75000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet6 = {pet6 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"')
            if pet7 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 375.000.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 375000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet7 = {pet7 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet8 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 7.500.000.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 7500000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet8 = {pet8 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"')
            if pet9 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 75.000.000.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 75000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet9 = {pet9 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
            if pet10 == 1:
                await bot.send_message(message.chat.id, f'💰 | {user_name}, вы успешно продали своего питомца за 22.000.000.000.000$', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 22000000000000} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet10 = {pet10 - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 



        if message.text.lower() in ["питомцы", "Питомцы"]:
            user_name = message.from_user.get_mention(as_html=True)
            chat_id = message.chat.id
            await bot.send_message(message.chat.id, f"{user_name}, доступные питомцы:\n🐥 1. Цыплёнок - 1.000.000$\n🐈 2. Кот - 100.000.000$\n🐕 3. Пёс - 500.000.000$\n🦜 4. Попугай - 1.000.000.000$\n🦄 5. Единорог - 50.000.000.000$\n🐒 6. Обезьяна - 100.000.000.000$\n🐬 7. Дельфин - 500.000.000.000$\n🐅 8. Тигр - 10.000.000.000.000$\n🐉 9. Дракон - 100.000.000.000.000$\n\n🛒 Для покупки питомца введите: Купить питомца [номер]\nℹ Для просмотра информации о своем питомце введите: Мой питомец", parse_mode='html')
        
        if message.text.startswith("Бой"):
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                balance2 = '{:,}'.format(balance) 
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10

            summ = int(msg.text.split()[1])
            print(summ)
            name1 = message.from_user.get_mention(as_html=True)
            period = 5
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
            games = round(int(games[0]))
            game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
            game = int(game[0])
            get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
            rhp = random.randint(10, 20)
            reat = random.randint(10, 20)
            rmood = random.randint(10, 20)
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            coff = random.randint(1,2)
            if stavkatime > period:
                if balance >= summ:
                    if summ > 0:
                        if int(pets) >= 1:
                            if pet_hp >= 20:
                                if pet_eat >= 20:
                                    if pet_mood >= 20:
                                        await bot.send_message(chat_id, f'⚔️ | {name1}, вы успешно подали заявку на участие в сражениях на питомцах!\n⏳ | До начала сражения осталось 5 секунд!', parse_mode='html') 
                                        cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"') 
                                        cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                                        connect.commit() 
                                        await asyncio.sleep(5)   
                                        if coff == 1:
                                            c = Decimal(summ * 2)
                                            c2 = round(c)
                                            c2 = '{:,}'.format(c2)
                                            await bot.send_message(chat_id, f'🎉 | {name1}, ваш питомец победил в сражении! Ваш выигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                                            cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 2)} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                                            cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                                            cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                                            connect.commit() 
                                            return 
                                        if coff == 2:
                                            c = Decimal(summ)
                                            c2 = round(c)
                                            c2 = '{:,}'.format(c2)
                                            await bot.send_message(chat_id, f'{rloser} | {name1}, ваш питомец проиграл в сражении! Ваш проигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                                            cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                                            cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                                            connect.commit()
                                    if pet_mood == 0:
                                        await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца нету настроения! {rloser}', parse_mode='html')
                                if pet_eat == 0:
                                    await bot.send_message(chat_id, f'ℹ️ | {name1}, ваш питомец голоден! {rloser}', parse_mode='html')
                            if pet_hp == 0:
                                await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца недостаточно здоровья! {rloser}', parse_mode='html')
                        if int(pets) == 0:
                            await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету питомца! {rloser}', parse_mode='html') 
                    elif summ <= 0:
                        await bot.send_message(chat_id, f'ℹ️ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
                elif int(balance) <= int(summ):
                    await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
            else:
                await bot.send_message(chat_id, f'ℹ️ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
                return
        if message.text.startswith("бой"):
            user_name = message.from_user.get_mention(as_html=True)
            pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet1 = int(pet1[0])
            pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet2 = int(pet2[0])
            pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet3 = int(pet3[0])
            pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet4 = int(pet4[0])
            pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet5 = int(pet5[0])
            pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet6 = int(pet6[0])
            pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet7 = int(pet7[0])
            pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet8 = int(pet8[0])
            pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet9 = int(pet9[0])
            pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet10 = int(pet10[0])
            pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_name = str(pet_name[0])
            pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_hp = int(pet_hp[0])
            pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_eat = int(pet_eat[0])
            pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
            pet_mood = int(pet_mood[0])
            chat_id = message.chat.id
            user_id = message.from_user.id
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                balance2 = '{:,}'.format(balance) 
            checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking1 = round(int(checking1[0]))
            if checking1 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking2 = round(int(checking2[0]))
            if checking2 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
            checking3 = round(int(checking3[0]))
            if checking3 == 1:
                await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
                return
            c = 1
            pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10

            summ = int(message.text.split()[1])
            print(summ)
            name1 = message.from_user.get_mention(as_html=True)
            period = 5
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
            games = round(int(games[0]))
            game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
            game = int(game[0])
            get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
            rhp = random.randint(10, 20)
            reat = random.randint(10, 20)
            rmood = random.randint(10, 20)
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            coff = random.randint(1,2)
            if stavkatime > period:
                if balance >= summ:
                    if summ > 0:
                        if int(pets) >= 1:
                            if pet_hp >= 20:
                                if pet_eat >= 20:
                                    if pet_mood >= 20:
                                        await bot.send_message(chat_id, f'⚔️ | {name1}, вы успешно подали заявку на участие в сражениях на питомцах!\n⏳ | До начала сражения осталось 5 секунд!', parse_mode='html') 
                                        cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"') 
                                        cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                                        connect.commit() 
                                        await asyncio.sleep(5)   
                                        if coff == 1:
                                            c = Decimal(summ * 2)
                                            c2 = round(c)
                                            c2 = '{:,}'.format(c2)
                                            await bot.send_message(chat_id, f'🎉 | {name1}, ваш питомец победил в сражении! Ваш выигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                                            cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 2)} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                                            cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                                            cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                                            connect.commit() 
                                            return 
                                        if coff == 2:
                                            c = Decimal(summ)
                                            c2 = round(c)
                                            c2 = '{:,}'.format(c2)
                                            await bot.send_message(chat_id, f'{rloser} | {name1}, ваш питомец проиграл в сражении! Ваш проигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}', parse_mode='html')
                                            cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                                            cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                                            cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{user_id}"')
                                            connect.commit()
                                    if pet_mood == 0:
                                        await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца нету настроения! {rloser}', parse_mode='html')
                                if pet_eat == 0:
                                    await bot.send_message(chat_id, f'ℹ️ | {name1}, ваш питомец голоден! {rloser}', parse_mode='html')
                            if pet_hp == 0:
                                await bot.send_message(chat_id, f'ℹ️ | {name1}, у вашего питомца недостаточно здоровья! {rloser}', parse_mode='html')
                        if int(pets) == 0:
                            await bot.send_message(chat_id, f'ℹ️ | {name1}, у вас нету питомца! {rloser}', parse_mode='html') 
                    elif summ <= 0:
                        await bot.send_message(chat_id, f'ℹ️ | {name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                                       
                elif int(balance) <= int(summ):
                    await bot.send_message(chat_id, f'💰 | {name1}, недостаточно средств! {rloser}', parse_mode='html')
            else:
                await bot.send_message(chat_id, f'ℹ️ | {name1}, играть можно каждые 5 секунд! {rloser}', parse_mode='html')
                return

        if message.text.lower() in ["баланс", "Баланс", "Б", "б"]:
            msg = message
            user_id = msg.from_user.id

            user_name = msg.from_user.full_name
            chat_id = message.chat.id
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])
            bitkoin2 = '{:,}'.format(bitkoin)
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            skin_id = cursor.execute("SELECT skin_id from users where user_id = ?", (message.from_user.id,)).fetchone()
            skin_id = int(skin_id[0])
            balance2 = '{:,}'.format(balance)
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = round(int(bank[0]))
            bank2 = '{:,}'.format(bank)
            c = 999999999999999999999999
            if skin_id == 1:
                skin_id2 = open(f'C:/Users/Ficus/Desktop/Python/Бот gfg/Skins/s1.png', 'rb')
            if skin_id == 2:
                skin_id2 = open(f'C:/Users/Ficus/Desktop/Python/Бот gfg/Skins/s2.png', 'rb')
            if skin_id == 3:
                skin_id2 = open(f'C:/Users/Ficus/Desktop/Python/Бот gfg/Skins/s3.png', 'rb')
            if skin_id == 4:
                skin_id2 = open(f'C:/Users/Ficus/Desktop/Python/Бот gfg/Skins/s4.png', 'rb')
            else:
                pass
            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                balance2 = '{:,}'.format(balance)
            else:
                pass
            if bank >= 999999999999999999999999:
                bank = 999999999999999999999999
                cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                bank2 = '{:,}'.format(bank)
            else:
                pass
            if bitkoin >= 999999999999999999999999:
                biktoin = 999999999999999999999999
                cursor.execute(f'UPDATE users SET bitkoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
            await bot.send_photo(message.chat.id,skin_id2,
                                 f"👫Ник: {user_name} \n👔Skin ID: {skin_id}\n💰 Деньги: {balance2}$\n🏦Банк: {bank2}$\n💽Биткоины: {bitkoin2}🌐")
        ################################################КУПИТЬ Энергию######################################################
        if message.text.startswith('Купить энергию'):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            summ = int(message.text.split()[0])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            ob_summ = summ + energy
            c = 1000000000000
            ob_summ2 = c * summ
            ob_summ3 = '{:,}'.format(ob_summ2)
            if ob_summ <= 10:
                if ob_summ <= balance:
                    await bot.send_message(message.chat.id,
                                           f'{name}, вы успешно купили {summ} ⚡️ за {ob_summ3}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET energy = {energy + summ}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance - ob_summ2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id, f'{name}, у вас нехватает средств! {rloser}',
                                           parse_mode='html')
            else:
                await bot.send_message(message.chat.id,
                                       f'{name}, нельзя делать покупку Энергии больше лимита {rloser}\nЛимит: 10 ⚡️',
                                       parse_mode='html')

        ################################################ПРОФИЛЬ#############################################################
        if message.text.lower() in ["профиль", "Профиль"]:
            msg = message
            chat_id = message.chat.id
            name1 = message.from_user.get_mention(as_html=True)
            user_name = msg.from_user.full_name
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])
            level = cursor.execute("SELECT level from users where user_id = ?", (message.from_user.id,)).fetchone()
            level = int(level[0])
            work = cursor.execute("SELECT work from users where user_id = ?", (message.from_user.id,)).fetchone()
            work = int(work[0])
            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            expe2 = '{:,}'.format(expe)
            games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
            games = int(games[0])
            work_shop = cursor.execute("SELECT work_shop from workshop where user_id = ?", (message.from_user.id,)).fetchone()
            work_shop = int(work_shop[0])
            games2 = '{:,}'.format(games)
            balance = int(balance[0])
            bank = int(bank[0])
            rating = int(rating[0])
            Ecoins = cursor.execute("SELECT Ecoins from users where user_id = ?", (message.from_user.id,)).fetchone()
            Ecoins = int(Ecoins[0])
            Ecoins2 = "{:,}".format(Ecoins)
            have = cursor.execute("SELECT have from property where user_id = ?", (message.from_user.id,)).fetchone()
            have = str(have[0])
            c = 999999999999999999999999

            yacht = cursor.execute("SELECT yacht from property where user_id = ?", (message.from_user.id,)).fetchone()
            yacht = int(yacht[0])
            cars = cursor.execute("SELECT cars from property where user_id = ?", (message.from_user.id,)).fetchone()
            cars = int(cars[0])
            plane = cursor.execute("SELECT plane from property where user_id = ?", (message.from_user.id,)).fetchone()
            plane = int(plane[0])
            helicopter = cursor.execute("SELECT helicopter from property where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            helicopter = int(helicopter[0])
            house = cursor.execute("SELECT house from property where user_id = ?", (message.from_user.id,)).fetchone()
            house = int(house[0])
            phone = cursor.execute("SELECT phone from property where user_id = ?", (message.from_user.id,)).fetchone()
            phone = int(phone[0])
            besiness = cursor.execute("SELECT business from property where user_id = ?",
                                      (message.from_user.id,)).fetchone()
            besiness = int(besiness[0])
            farm = cursor.execute("SELECT farm from property where user_id = ?", (message.from_user.id,)).fetchone()
            farm = int(farm[0])

            if work == 0:
                work2 = 'Безработный'
                zp = '0$'
            if work == 1:
                work2 = 'Фермер🍎'
                zp = '54,000,000$'
            if work == 2:
                work2 = 'Шахтёр⛏'
                zp = '100,000,000$'
            if work == 3:
                work2 = 'Строитель🧱'
                zp = '167,000,000$'
            if work == 4:
                work2 = 'Сантехник🛠'
                zp = '532,000,000$'
            if work == 5:
                work2 = 'Електрик💡'
                zp = '1,236,000,000$'
            if work == 6:
                work2 = 'Пожарник🧯'
                zp = '5,115,000,000$'
            if work == 7:
                work2 = 'Официант☕️'
                zp = '15,000,000,000$'
            if work == 8:
                work2 = 'Повар🍰'
                zp = '50,000,000,000$'
            if work == 9:
                work2 = 'Полицейский👮‍♂'
                zp = '674,000,000,000$'
            if work == 10:
                work2 = 'Доктор👨‍⚕'
                zp = '1,300,000,000,000$'
            if work == 11:
                work2 = 'Педагог👩‍🏫'
                zp = '5,000,000,000,000$'
            if work == 12:
                work2 = 'Пилот✈️'
                zp = '12,000,000,000,000$'
            if work == 13:
                work2 = 'Генерал👨‍✈️'
                zp = '45,000,000,000,000$'
            if work == 14:
                work2 = 'Бизнесмен💍'
                zp = '55,000,000,000,000$'
            if work == 15:
                work2 = 'Программист🖥'
                zp = '100,000,000,000,000$'

            # Фермы
            if farm == 0:
                farm2 = ''
            if farm == 1:
                farm2 = '🔋 Ферма: TI-Miner'
            if farm == 2:
                farm2 = '🔋 Ферма: Saturn'
            if farm == 3:
                farm2 = '🔋 Ферма: Calisto'
            if farm == 4:
                farm2 = '🔋 Ферма: HashMiner'
            if farm == 5:
                farm2 = '🔋 Ферма: MegaWatt'
            # Бизнесы
            if besiness == 0:
                besiness2 = ''
            if besiness == 1:
                besiness2 = '💼 Бизнес: Шаурмечная'
            if besiness == 2:
                besiness2 = '💼 Бизнес: Ночной клуб'
            if besiness == 3:
                besiness2 = '💼 Бизнес: Кальянная'
            if besiness == 4:
                besiness2 = '💼 Бизнес: АЗС'
            if besiness == 5:
                besiness2 = '💼 Бизнес: Порностудия'
            if besiness == 6:
                besiness2 = '💼 Бизнес: Маленький офис'
            if besiness == 7:
                besiness2 = '💼 Бизнес: Нефтевышка'
            if besiness == 8:
                besiness2 = '💼 Бизнес: Космическое агентство'
            if besiness == 9:
                besiness2 = '💼 Бизнес: Межпланетный экспресс'
            if besiness == 10:
                besiness2 = '💼 Бизнес: Генератор материи'
            if besiness == 11:
                besiness2 = '💼 Бизнес: Генератор материи'
            # Телефоны
            if phone == 0:
                phone2 = ''
            if phone == 1:
                phone2 = '📱 Телефон: Nokia 3310'
            if phone == 2:
                phone2 = '📱 Телефон: ASUS ZenFone 4'
            if phone == 3:
                phone2 = '📱 Телефон: BQ Aquaris X'
            if phone == 4:
                phone2 = '📱 Телефон: Huawei P40'
            if phone == 5:
                phone2 = '📱 Телефон: Samsung Galaxy S21 Ultra'
            if phone == 6:
                phone2 = '📱 Телефон: Xiaomi Mi 11'
            if phone == 7:
                phone2 = '📱 Телефон: iPhone 11 Pro'
            if phone == 8:
                phone2 = '📱 Телефон: iPhone 12 Pro Max'
            if phone == 9:
                phone2 = '📱 Телефон: Blackberry'
            # Дома
            if house == 0:
                house2 = ''
            if house == 1:
                house2 = '🏠 Дом: Коробка'
            if house == 2:
                house2 = '🏠 Дом: Подвал'
            if house == 3:
                house2 = '🏠 Дом: Сарай'
            if house == 4:
                house2 = '🏠 Дом: Маленький домик'
            if house == 5:
                house2 = '🏠 Дом: Квартира'
            if house == 6:
                house2 = '🏠 Дом: Огромный дом'
            if house == 7:
                house2 = '🏠 Дом: Коттедж'
            if house == 8:
                house2 = '🏠 Дом: Вилла'
            if house == 9:
                house2 = '🏠 Дом: Загородный дом'
            if house == 10:
                house2 = '🏠 Дом: Небоскрёб'
            if house == 11:
                house2 = '🏠 Дом: Дом на мальдивах'
            if house == 12:
                house2 = '🏠 Дом: Технологичный небосрёб'
            if house == 13:
                house2 = '🏠 Дом: Собственный остров'
            if house == 14:
                house2 = '🏠 Дом: Дом на марсе'
            if house == 15:
                house2 = '🏠 Дом: Остров на марсе'
            if house == 16:
                house2 = '🏠 Дом: Свой марс'

            # Вертолёты
            if helicopter == 0:
                helicopter2 = ''
            if helicopter == 1:
                helicopter2 = '🚁 Вертолёт: Воздушный шар'
            if helicopter == 2:
                helicopter2 = '🚁 Вертолёт: RotorWay Exec 162F'
            if helicopter == 3:
                helicopter2 = '🚁 Вертолёт: Robinson R44'
            if helicopter == 4:
                helicopter2 = '🚁 Вертолёт: Hiller UH-12C'
            if helicopter == 5:
                helicopter2 = '🚁 Вертолёт: AW119 Koala'
            if helicopter == 6:
                helicopter2 = '🚁 Вертолёт: MBB BK 117'
            if helicopter == 7:
                helicopter2 = '🚁 Вертолёт: Eurocopter EC130'
            if helicopter == 8:
                helicopter2 = '🚁 Вертолёт: Leonardo AW109 Power'
            if helicopter == 9:
                helicopter2 = '🚁 Вертолёт: Sikorsky S-76'
            if helicopter == 10:
                helicopter2 = '🚁 Вертолёт: Bell 429WLG'
            if helicopter == 11:
                helicopter2 = '🚁 Вертолёт: NHI NH90'
            if helicopter == 12:
                helicopter2 = '🚁 Вертолёт: Kazan Mi-35M'
            if helicopter == 13:
                helicopter2 = '🚁 Вертолёт: Bell V-22 Osprey'
            # Самолёты
            if plane == 0:
                plane2 = ''
            if plane == 1:
                plane2 = '✈️ Самолёт: Параплан'
            if plane == 2:
                plane2 = '✈️ Самолёт: АН-2'
            if plane == 3:
                plane2 = '✈️ Самолёт: Cessna-172E'
            if plane == 4:
                plane2 = '✈️ Самолёт: BRM NG-5'
            if plane == 5:
                plane2 = '✈️ Самолёт: Cessna T210'
            if plane == 6:
                plane2 = '✈️ Самолёт: Beechcraft 1900D'
            if plane == 7:
                plane2 = '✈️ Самолёт: Cessna 550'
            if plane == 8:
                plane2 = '✈️ Самолёт: Hawker 4000'
            if plane == 9:
                plane2 = '✈️ Самолёт: Learjet 31'
            if plane == 10:
                plane2 = '✈️ Самолёт: Airbus A318'
            if plane == 11:
                plane2 = '✈️ Самолёт: F-35A'
            if plane == 12:
                plane2 = '✈️ Самолёт: Boeing 747-430'
            if plane == 13:
                plane2 = '✈️ Самолёт: C-17A Globemaster III'
            if plane == 14:
                plane2 = '✈️ Самолёт: F-22 Raptor'
            if plane == 15:
                plane2 = '✈️ Самолёт: Airbus 380 Custom'
            if plane == 16:
                plane2 = '✈️ Самолёт: B-2 Spirit Stealth Bomber'
            # Машины
            if cars == 0:
                cars2 = ''
            if cars == 1:
                cars2 = '🚗 Машина: Самокат'
            if cars == 2:
                cars2 = '🚗 Машина: Велосипед'
            if cars == 3:
                cars2 = '🚗 Машина: Гироскутер'
            if cars == 4:
                cars2 = '🚗 Машина: Сегвей'
            if cars == 5:
                cars2 = '🚗 Машина: Мопед'
            if cars == 6:
                cars2 = '🚗 Машина: Мотоцикл'
            if cars == 7:
                cars2 = '🚗 Машина: ВАЗ 2109'
            if cars == 8:
                cars2 = '🚗 Машина: Квадроцикл'
            if cars == 9:
                cars2 = '🚗 Машина: Багги'
            if cars == 10:
                cars2 = '🚗 Машина: Вездеход'
            if cars == 11:
                cars2 = '🚗 Машина: Лада Xray'
            if cars == 12:
                cars2 = '🚗 Машина: Audi Q7'
            if cars == 13:
                cars2 = '🚗 Машина: BMW X6'
            if cars == 14:
                cars2 = '🚗 Машина: Toyota FT-HS'
            if cars == 15:
                cars2 = '🚗 Машина: BMW Z4 M'
            if cars == 16:
                cars2 = '🚗 Машина: Subaru WRX STI'
            if cars == 17:
                cars2 = '🚗 Машина: Lamborghini Veneno'
            if cars == 18:
                cars2 = '🚗 Машина: Tesla Roadster'
            if cars == 19:
                cars2 = '🚗 Машина: Yamaha YZF R6'
            if cars == 20:
                cars2 = '🚗 Машина: Bugatti Chiron'
            if cars == 21:
                cars2 = '🚗 Машина: Thrust SSC'
            if cars == 22:
                cars2 = '🚗 Машина: Ferrari LaFerrari'
            if cars == 23:
                cars2 = '🚗 Машина: Koenigsegg Regear'
            if cars == 24:
                cars2 = '🚗 Машина: Tesla Semi'
            if cars == 25:
                cars2 = '🚗 Машина: Venom GT'
            if cars == 26:
                cars2 = '🚗 Машина: Rolls-Royce'
            # Яхты
            if yacht == 0:
                yacht2 = ''
            if yacht == 1:
                yacht2 = '🛥 Яхта: Ванна'
            if yacht == 2:
                yacht2 = '🛥 Яхта: Nauticat 331'
            if yacht == 3:
                yacht2 = '🛥 Яхта: Nordhavn 56 MS'
            if yacht == 4:
                yacht2 = '🛥 Яхта: Princess 60'
            if yacht == 5:
                yacht2 = '🛥 Яхта: Bayliner 288'
            if yacht == 6:
                yacht2 = '🛥 Яхта: Dominator 40M'
            if yacht == 7:
                yacht2 = '🛥 Яхта: Sessa Marine C42'
            if yacht == 8:
                yacht2 = '🛥 Яхта: Wider 150'
            if yacht == 9:
                yacht2 = '🛥 Яхта: Palmer Johnson 42M SuperSport'
            if yacht == 10:
                yacht2 = '🛥 Яхта: Serene'
            if yacht == 11:
                yacht2 = '🛥 Яхта: Dubai'
            if yacht == 12:
                yacht2 = '🛥 Яхта: Azzam'
            if yacht == 13:
                yacht2 = '🛥 Яхта: Streets of Monaco'

            if have == 'off':
                have2 = '😔 У вас нет имущества'

            if have == 'on':
                have2 = f"""
    📦 Имущество:
        {yacht2}
        {cars2}
        {plane2}
        {helicopter2}
        {house2}
        {phone2}
        {besiness2}
                """

            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
            else:
                pass
            if int(balance) in range(0, 1000):
                balance3 = cursor.execute("SELECT balance from users where user_id = ?",
                                          (message.from_user.id,)).fetchone()
                balance3 = int(balance3[0])
            if int(balance) in range(1000, 999999):
                balance1 = balance / 1000
                balance2 = round(balance1)
                balance3 = f'{balance2} тыс'
            if int(balance) in range(1000000, 999999999):
                balance1 = balance / 1000000
                balance2 = round(balance1)
                balance3 = f'{balance2} млн'
            if int(balance) in range(1000000000, 999999999999):
                balance1 = balance / 1000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} млрд'
            if int(balance) in range(1000000000000, 999999999999999):
                balance1 = balance / 1000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} трлн'
            if int(balance) in range(1000000000000000, 999999999999999999):
                balance1 = balance / 1000000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} квдр'
            if int(balance) in range(1000000000000000000, 999999999999999999999):
                balance1 = balance / 1000000000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} квнт'
            if int(balance) in range(1000000000000000000000, 999999999999999999999999):
                balance1 = balance / 1000000000000000000000
                balance2 = round(balance1)
                balance3 = f'{balance2} скст'
            if bank >= 999999999999999999999999:
                bank = 999999999999999999999999
                cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
            else:
                pass
            if int(bank) in range(0, 1000):
                bank3 = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
                bank3 = int(bank3[0])
            if int(bank) in range(1000, 999999):
                bank1 = bank / 1000
                bank2 = round(bank1)
                bank3 = f'{bank2} тыс'
            if int(bank) in range(1000000, 999999999):
                bank1 = bank / 1000000
                bank2 = round(bank1)
                bank3 = f'{bank2} млн'
            if int(bank) in range(1000000000, 999999999999):
                bank1 = bank / 1000000000
                bank2 = round(bank1)
                bank3 = f'{bank2} млрд'
            if int(bank) in range(1000000000000, 999999999999999):
                bank1 = bank / 1000000000000
                bank2 = round(bank1)
                bank3 = f'{bank2} трлн'
            if int(bank) in range(1000000000000000, 999999999999999999):
                bank1 = bank / 1000000000000000
                bank2 = round(bank1)
                bank3 = f'{bank2} квдр'
            if int(bank) in range(1000000000000000000, 999999999999999999999):
                bank1 = bank / 1000000000000000000
                bank2 = round(bank1)
                bank3 = f'{bank2} квнт'
            if int(bank) in range(1000000000000000000000, 999999999999999999999999):
                bank1 = bank / 1000000000000000000000
                bank2 = round(bank1)
                bank3 = f'{bank2} скст'
            if rating >= 999999999999999999999999:
                rating = 999999999999999999999999
                cursor.execute(f'UPDATE users SET rating = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
            else:
                pass
            if int(rating) in range(0, 1000):
                rating3 = cursor.execute("SELECT rating from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
                rating3 = int(rating3[0])
            if int(rating) in range(1000, 999999):
                rating1 = rating / 1000
                rating2 = round(rating1)
                rating3 = f'{rating2} тыс'
            if int(rating) in range(1000000, 999999999):
                rating1 = rating / 1000000
                rating2 = round(rating1)
                rating3 = f'{rating2} млн'
            if int(rating) in range(1000000000, 999999999999):
                rating1 = rating / 1000000000
                rating2 = round(rating1)
                rating3 = f'{rating2} млрд'
            if int(rating) in range(1000000000000, 999999999999999):
                rating1 = rating / 1000000000000
                rating2 = round(rating1)
                rating3 = f'{rating2} трлн'
            if int(rating) in range(1000000000000000, 999999999999999999):
                rating1 = rating / 1000000000000000
                rating2 = round(rating1)
                rating3 = f'{rating2} квдр'
            if int(rating) in range(1000000000000000000, 999999999999999999999):
                rating1 = rating / 1000000000000000000
                rating2 = round(rating1)
                rating3 = f'{rating2} квнт'
            if int(rating) in range(1000000000000000000000, 999999999999999999999999):
                rating1 = rating / 1000000000000000000000
                rating2 = round(rating1)
                rating3 = f'{rating2} скст'
            if bitkoin > 999999999999999999999999:
                bitkoin = 999999999999999999999999
                cursor.execute(f"UPDATE users SET bitkoin = {999999999999999999999999}  WHERE user_id = ?", (user_id,))
                connect.commit()
            else:
                pass
            if int(bitkoin) in range(0, 1000):
                bitkoin3 = cursor.execute("SELECT bitkoin from users where user_id = ?",
                                          (message.from_user.id,)).fetchone()
                bitkoin3 = int(bitkoin3[0])
            if int(bitkoin) in range(1000, 999999):
                bitkoin1 = bitkoin / 1000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} тыс'
            if int(bitkoin) in range(1000000, 999999999):
                bitkoin1 = bitkoin / 1000000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} млн'
            if int(bitkoin) in range(1000000000, 999999999999):
                bitkoin1 = bitkoin / 1000000000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} млрд'
            if int(bitkoin) in range(1000000000000, 999999999999999):
                bitkoin1 = bitkoin / 1000000000000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} трлн'
            if int(bitkoin) in range(1000000000000000, 999999999999999999):
                bitkoin1 = bitkoin / 1000000000000000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} квдр'
            if int(bitkoin) in range(1000000000000000000, 999999999999999999999):
                bitkoin1 = bitkoin / 1000000000000000000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} квнт'
            if int(bitkoin) in range(1000000000000000000000, 999999999999999999999999):
                bitkoin1 = bitkoin / 1000000000000000000000
                bitkoin2 = round(bitkoin1)
                bitkoin3 = f'{bitkoin2} скст'                
            if user_status[0] == 'Rab':
                user_status2 = '🧛‍♂️ Разработчик'
                     
            if user_status[0] == 'Admin':
                user_status2 = '👨‍🦰 Aдминистратор' 
                        
            if user_status[0] == 'Player':
                user_status2 = '💤 Игрок'
            await bot.send_message(message.chat.id,
                                   f"{name1},ваш профиль:\n 🔎ID: {user_id}\n📌Префикс: {user_status2} \n💰Деньги: {balance3}$\n🏦В банке: {bank3}$\n💽Биткоины: {bitkoin3}\n📈Работа: {work2}\n💵Зарплата: {zp}\n👑Рейтинг: {rating3}\n✨Репутация: в разработке\n🏋️Энергия: {energy}\n📊Уровень: {level}\n{have2}",
                                   parse_mode='html')
        ################################################КУРС РУДЫ###############################################################
        if message.text.lower() in ['курс руды', 'Курс руды']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name} , курс руды:
    ⛓ 1 железо - 230.000$
    🌕 1 золото - 1.000.000$
    💎 1 алмаз - 116.000.000$
    🎆 1 аметист - 216.000.000$
    💠 1 аквамарин - 302.000.000$
    🍀 1 изумруд - 366.000.000$
    🌌 1 материя - 412.000.000$
    💥 1 плазма - 632.000.000$
    ''', parse_mode='html')
        ###############################################ОГРАБИТЬ МЭРИЮ###########################################################
        if message.text.lower() == 'ограбить казну':
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            rx = random.randint(0, 50)
            rx_money = random.randint(100000000000, 500000000000)
            rx_money2 = '{:,}'.format(rx_money)

            period = 86400
            get = cursor.execute("SELECT last_stavka FROM bot_merii WHERE user_id = ?",
                                 (message.from_user.id,)).fetchone()
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            if stavkatime > period:
                if int(rx) in range(0, 10):
                    await bot.send_message(message.chat.id, f'{name}, к сожалению вам не удалось ограбить казну ❎',
                                           parse_mode='html')

                if int(rx) in range(11, 50):
                    await bot.send_message(message.chat.id,
                                           f'{name}, вы успешно ограбили казну. На ваш баланс зачислено {rx_money2}$ ✅',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + rx_money}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_merii SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                    return
            else:
                await bot.send_message(message.chat.id,
                                       f'{name}, вы уже грабили казну сегодня. Бегите скорее, полиция уже в пути 🚫',
                                       parse_mode='html')
        ##############################################ИНВЕНТАРЬ#################################################################
        if message.text.lower() in ['Инвентарь', 'инвентарь']:
            name = message.from_user.get_mention(as_html=True)
            iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
            iron = int(iron[0])

            gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
            gold = int(gold[0])

            diamonds = cursor.execute("SELECT diamonds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            diamonds = int(diamonds[0])

            amethysts = cursor.execute("SELECT amethysts from mine where user_id = ?",
                                       (message.from_user.id,)).fetchone()
            amethysts = int(amethysts[0])

            aquamarine = cursor.execute("SELECT aquamarine from mine where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            aquamarine = int(aquamarine[0])

            emeralds = cursor.execute("SELECT emeralds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            emeralds = int(emeralds[0])

            matter = cursor.execute("SELECT matter from mine where user_id = ?", (message.from_user.id,)).fetchone()
            matter = int(matter[0])

            plasma = cursor.execute("SELECT plasma from mine where user_id = ?", (message.from_user.id,)).fetchone()
            plasma = int(plasma[0])

            linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
            linen = int(linen[0])

            cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
            cotton = int(cotton[0])

            await bot.send_message(message.chat.id, f'''
    {name}
    ⛓ Железо: {iron} шт.
    🌕 Золото: {gold} шт.
    💎 Алмазы: {diamonds} шт.
    🎆 Аметисты: {amethysts} шт.
    💠 Аквамарин: {aquamarine} шт.
    ❇️ Изумруды: {emeralds} шт.
    🌌 Материя: {matter} шт.
    🎇 Плазма: {plasma} шт.
    🍃 Лён: {linen} шт.
    🌿 Хлопок {cotton} шт.
    ''', parse_mode='html')
        #######################################БЕСЕДА#############################################

        if message.text.lower() in ['!беседа', '!Беседа']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} 💬Официальная беседа бота - В разработке', parse_mode='html')
        #######################################РП Команды#########################################
        if message.text.lower() in ['отлизать', 'отлизать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} отлизал(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Отсосать', 'отсосать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} отсосал(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Облизать', 'облизать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} облизал(а) всего  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Шлепнуть', 'шлепнуть']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} шлепнул(а) {reply_name}', parse_mode='html')
        if message.text.lower() in ['Убить', 'убить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} убил(а) с оружия {reply_name}', parse_mode='html')
        if message.text.lower() in ['Укусить', 'укусить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} укусил(а) {reply_name}', parse_mode='html')
        if message.text.lower() in ['Ударить', 'ударить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} ударил(а) по голове  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Уебать', 'уебать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} жоско уебал(а) по ебалу {reply_name}', parse_mode='html')
        if message.text.lower() in ['Ущепнуть', 'ущепнуть']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} ущепнул(а) {reply_name}', parse_mode='html')
        if message.text.lower() in ['Трахнуть', 'трахнуть']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} занялся(лась) сексом в анал с {reply_name}',
                                   parse_mode='html')
        if message.text.lower() in ['Сжечь', 'сжечь']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} спалил(а) на костре  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Секс', 'секс']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} пошёл(а) заниматься сексом с  {reply_name}',
                                   parse_mode='html')
        if message.text.lower() in ['Расстрелять', 'расстрелять']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} расстрелял(а) на палигоне  {reply_name}',
                                   parse_mode='html')
        if message.text.lower() in ['Покормить', 'Покормить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} покормил(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Пнуть', 'пнуть']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} дал по жопе с ноги  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Дать по лбу', 'дать по лбу']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} дал лычку  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Погладить', 'погладить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} погладил(а) по голове  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Понюхать', 'понюхать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} принюхался(лась) к  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Похвалить', 'похвалить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} похвалил(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Послать нахуй', 'послать нахуй']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} послал(а) нахуй  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Пожать руку', 'пожать руку']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} пожал(а) руку очень крепко  {reply_name}',
                                   parse_mode='html')
        if message.text.lower() in ['Потрогать', 'потрогать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} потрогал(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Прижать', 'прижать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} прижал(а) к себе  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Поцеловать', 'поцеловать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} поцеловал(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Поздравить', 'поздравить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} поздравил с праздником  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Отдаться', 'отдаться']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} отдался(лась) в кровате  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Отравить', 'отравить']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} отравил(а) ядом  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Обнять', 'Обнять']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} обнял(а) очень крепко  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Лизь', 'Лизь']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} лизнул(а)  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Лизнуть', 'лизнуть']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} лизнуть в щёку  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Кастрировать', 'кастрировать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} пошёл кастрировать  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Кусь', 'кусь']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} куснул  {reply_name}', parse_mode='html')
        if message.text.lower() in ['Изнасиловать', 'изнасиловать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} изнасиловал {reply_name}', parse_mode='html')
        if message.text.lower() in ['Извиниться', 'извиниться']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} извинилься перед {reply_name}', parse_mode='html')
        if message.text.lower() in ['Испугать', 'испугать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} испугал(а) {reply_name}', parse_mode='html')
        if message.text.lower() in ['Дать пять', 'дать пять']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} дал(а) пять {reply_name}', parse_mode='html')
        if message.text.lower() in ['Выебать', 'выебать']:
            name = message.from_user.get_mention(as_html=True)
            reply_name = message.reply_to_message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name} пошел(ла) заниматься интимом с {reply_name}',
                                   parse_mode='html')
        if message.text.lower() in ['Рп Команды', 'рп команды']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name}, вот все доступные РП команды:
    1) Выебать
    2) Дать пять
    3) Испугать
    4) Ивиниться
    5) Изнасиловать
    6) Кусь
    7) Кастрировать
    8) Лизнуть
    9) Лизь
    10) Обнять
    11) Отравить
    12) Отдаться
    13) Поздравить
    14) Поцеловать
    15) Прижать
    16) Потрогать
    17) Пожать руку
    18) Послать нахуй
    19) Похвалить
    20) Понюхать
    21) Погладить
    22) Дать по лбу
    23) Пнуть
    24) Покормить
    25) Расстрелять
    26) Секс
    27) Сжечь
    28) Трахнуть
    29) Ущепнуть
    30) Уебать
    31) Ударить
    32) Укусить
    33) Убить
    34) Шлепнуть
    35) Куснуть
    36) Облизать
    37) Отсосать
    38) Отлизать
    ''', parse_mode='html')

        #######################################НИК################################################
        if message.text.lower() in ['Мой ник', 'мой ник']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name}, на данный моммент команда ещё в разработке ❌',
                                   parse_mode='html')
        if message.text.lower() in ['Сменить ник', 'сменить ник']:
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            await bot.send_message(message.chat.id,
                                   f'{name}, что бы сменить ник введите команду "Сменить ник [Ваш ник]" {rloser}',
                                   parse_mode='html')
        if message.text.startswith('Сменить ник'):
            name = message.from_user.get_mention(as_html=True)

            nik = str(message.text.split()[2])

            await bot.send_message(message.chat.id, f'{name}, на данный моммент команда ещё в разработке ❌',
                                   parse_mode='html')
        ######################################КАЗНА###############################################
        if message.text.lower() in ['Казна', 'казна']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id,
                                   f'{name}, 💰 На данный момент казна штата составляет 70.326.975.785.225.897$',
                                   parse_mode='html')
        ##################################ЕЖЕДНЕВНЫЙ БОНУС########################################
        if message.text.lower() == 'ежедневный бонус':
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])

            emeralds = cursor.execute("SELECT emeralds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            emeralds = int(emeralds[0])

            matter = cursor.execute("SELECT matter from mine where user_id = ?", (message.from_user.id,)).fetchone()
            matter = int(matter[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])

            rx = random.randint(0, 125)

            rx_money = random.randint(100000000000, 500000000000)
            rx_money2 = '{:,}'.format(rx_money)

            rx_bitcoin = random.randint(1000, 100000)
            rx_bitcoin2 = '{:,}'.format(rx_bitcoin)

            rx_emeralds = random.randint(10, 100)
            rx_emeralds2 = '{:,}'.format(rx_emeralds)

            rx_matter = random.randint(1, 10)
            rx_matter2 = '{:,}'.format(rx_matter)

            rx_expe = random.randint(100, 500)

            period = 86400
            get = cursor.execute("SELECT last_stavka FROM bot_bonus WHERE user_id = ?",
                                 (message.from_user.id,)).fetchone()
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            if stavkatime > period:
                if int(rx) in range(0, 25):
                    await bot.send_message(message.chat.id,
                                           f'{name}, вам был выдан ежедневный бонус в размере {rx_money2}$ ✅',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + rx_money}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_bonus SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                    return
                if int(rx) in range(26, 50):
                    await bot.send_message(message.chat.id,
                                           f'{name}, вам был выдан ежедневный бонус в размере {rx_bitcoin2} BTC 🌐',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET bitkoin = {bitkoin + rx_bitcoin}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_bonus SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                    return
                if int(rx) in range(51, 75):
                    await bot.send_message(message.chat.id,
                                           f'{name}, вам был выдан ежедневный бонус в размере {rx_emeralds2} изумрудов ❇️ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET emeralds = {emeralds + rx_emeralds}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_bonus SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                    return
                if int(rx) in range(76, 100):
                    await bot.send_message(message.chat.id,
                                           f'{name}, вам был выдан ежедневный бонус в размере {rx_matter2} материи 🌌 ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET matter = {matter + rx_matter}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_bonus SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                    return
                if int(rx) in range(101, 125):
                    await bot.send_message(message.chat.id,
                                           f'{name}, вам был выдан ежедневный бонус в размере {rx_expe} опыта 🏆 ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET expe = {expe + rx_expe}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_bonus SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                    return
            else:
                await bot.send_message(message.chat.id, f'{name}, бонус можно получать раз в 24ч ⌛️', parse_mode='html')
        ###########################################БИТКОИН########################################
        if message.text.lower() in ['Биткоины', 'биткоины']:
            name = message.from_user.get_mention(as_html=True)

            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])
            bitkoin2 = '{:,}'.format(bitkoin)

            await bot.send_message(message.chat.id, f'{name}, на вашем балансе {bitkoin2} ВТС 🌐', parse_mode='html')
        if message.text.lower() in ['Биткоин продать', 'биткоин продать']:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])
            bitkoin2 = '{:,}'.format(bitkoin)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            c = api.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']

            summ = bitkoin * c
            summ2 = '{:,}'.format(summ)

            if bitkoin > 0:
                await bot.send_message(message.chat.id, f'{name}, вы успешно продали {bitkoin2} BTC за {summ2}$ {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + summ}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET bitkoin = {bitkoin - bitkoin}  WHERE user_id = "{user_id}"')
                connect.commit()
            else:
                await bot.send_message(message.chat.id, f'{name}, недостаточно средств! {rloser}', parse_mode='html')

        if message.text.startswith('Биткоин продать'):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            bitcoin_c = int(message.text.split()[2])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            c = api.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']

            summ = bitcoin_c * c
            summ2 = '{:,}'.format(summ)

            if bitcoin_c <= bitkoin:
                if bitcoin_c > 0:
                    await bot.send_message(message.chat.id,
                                           f'{name}, вы успешно продали {bitcoin_c} BTC за {summ2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + summ}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET bitkoin = {bitkoin - bitcoin_c}  WHERE user_id = "{user_id}"')
                    connect.commit()
                    return
                else:
                    await bot.send_message(message.chat.id, f'{name}, нельзя продать отрицательное число {rloser}',
                                           parse_mode='html')
                    return
            else:
                await bot.send_message(message.chat.id, f'{name}, недостаточно средств! {rloser}', parse_mode='html')
                return
        if message.text.startswith('биткоин продать'):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            bitcoin_c = int(message.text.split()[2])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            c = api.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']

            summ = bitcoin_c * c
            summ2 = '{:,}'.format(summ)

            if bitcoin_c <= bitkoin:
                if bitcoin_c > 0:
                    await bot.send_message(message.chat.id,
                                           f'{name}, вы успешно продали {bitcoin_c} BTC за {summ2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + summ}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET bitkoin = {bitkoin - bitcoin_c}  WHERE user_id = "{user_id}"')
                    connect.commit()
                    return
                else:
                    await bot.send_message(message.chat.id, f'{name}, нельзя продать отрицательное число {rloser}',
                                           parse_mode='html')
                    return
            else:
                await bot.send_message(message.chat.id, f'{name}, недостаточно средств! {rloser}', parse_mode='html')
                return

        if message.text.startswith('биткоин купить'):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            bitcoin_c = int(message.text.split()[2])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            c = api.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']

            summ = bitcoin_c * c
            summ2 = '{:,}'.format(summ)

            if summ <= balance:
                if bitcoin_c > 0:
                    await bot.send_message(message.chat.id,
                                           f'{name}, вы успешно купили {bitcoin_c} BTC за {summ2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET bitkoin = {bitkoin + bitcoin_c}  WHERE user_id = "{user_id}"')
                    connect.commit()
                    return
                else:
                    await bot.send_message(message.chat.id, f'{name}, нельзя купить отрицательное число {rloser}',
                                           parse_mode='html')
                    return
            else:
                await bot.send_message(message.chat.id, f'{name}, недостаточно средств! {rloser}', parse_mode='html')
                return

        if message.text.startswith('Биткоин купить'):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            bitcoin_c = int(message.text.split()[2])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            bitkoin = cursor.execute("SELECT bitkoin from users where user_id = ?", (message.from_user.id,)).fetchone()
            bitkoin = int(bitkoin[0])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            c = api.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']

            summ = bitcoin_c * c
            summ2 = '{:,}'.format(summ)

            if summ <= balance:
                if bitcoin_c > 0:
                    await bot.send_message(message.chat.id,
                                           f'{name}, вы успешно купили {bitcoin_c} BTC за {summ2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET bitkoin = {bitkoin + bitcoin_c}  WHERE user_id = "{user_id}"')
                    connect.commit()
                    return
                else:
                    await bot.send_message(message.chat.id, f'{name}, нельзя купить отрицательное число {rloser}',
                                           parse_mode='html')
                    return
            else:
                await bot.send_message(message.chat.id, f'{name}, недостаточно средств! {rloser}', parse_mode='html')
                return

        if message.text.lower() in ['Биткоин курс', 'биткоин курс']:
            name = message.from_user.get_mention(as_html=True)

            c = api.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']

            c2 = '{:,}'.format(c)

            await bot.send_message(message.chat.id, f'{name}, на данный момент курс 1 BTC состовляет - {c2}🌐',
                                   parse_mode='html')

        #########################################РАБОТЫ###########################################
        if message.text.lower() == 'Уволиться':
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            work = cursor.execute("SELECT work from users where user_id = ?", (message.from_user.id,)).fetchone()
            work = int(work[0])

            if work > 0:
                await bot.send_message(message.chat.id, f'{name}, вы уволены с вашей работы {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET work = {0}  WHERE user_id = "{user_id}"')
                connect.commit()
            else:
                await bot.send_message(message.chat.id, f'{name}, вы уже без работний {rloser}', parse_mode='html')
        if message.text.lower() == 'работать':
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            level = cursor.execute("SELECT level from users where user_id = ?", (message.from_user.id,)).fetchone()
            level = int(level[0])
            work = cursor.execute("SELECT work from users where user_id = ?", (message.from_user.id,)).fetchone()
            work = int(work[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            if work == 1:
                rabota = ['собрали яблоки🍎', 'покормили коров🐮', "зарезали свинью🐷", "покормили курочек🐔"]
                rx_rabota = random.choice(rabota)
                zp = 54000000
                zp2 = '{:,}'.format(zp)
            if work == 2:
                rabota = ['выкопали шахту⛏', 'подорвали шахту🧨']
                rx_rabota = random.choice(rabota)
                zp = 100000000
                zp2 = '{:,}'.format(zp)
            if work == 3:
                rabota = ['построили дом🏠', 'принесли кирпичи🧱', "построили квартиру🧱", "построили банк🏦"]
                rx_rabota = random.choice(rabota)
                zp = 167000000
                zp2 = '{:,}'.format(zp)
            if work == 4:
                rabota = ['починили кран🚰', 'отремонтировали ванну🛁 ', "провели воду🚿", "почистили туалет🚽"]
                rx_rabota = random.choice(rabota)
                zp = 532000000
                zp2 = '{:,}'.format(zp)
            if work == 5:
                rabota = ['починили розетку🔌', 'провели ТВ 📡', "провели интернет🌐", "почистили электронику🧰"]
                rx_rabota = random.choice(rabota)
                zp = 1236000000
                zp2 = '{:,}'.format(zp)
            if work == 6:
                rabota = ['потушили дом🏚', 'выехали на вызов🚒', "потушили квартиру🧯", "потушили лес🔥"]
                rx_rabota = random.choice(rabota)
                zp = 5115000000
                zp2 = '{:,}'.format(zp)
            if work == 7:
                rabota = ['принесли чашку кофе☕️', 'принесли блинчики🥞', "принесли гамбургер 🍔",
                          "принесли кусочек торта 🍰"]
                rx_rabota = random.choice(rabota)
                zp = 15000000000
                zp2 = '{:,}'.format(zp)
            if work == 8:
                rabota = ['приготовили чашку кофе☕️', 'сделали блинчики🥞', "приготовили гамбургер 🍔",
                          "спекли кусочек торта 🍰"]
                rx_rabota = random.choice(rabota)
                zp = 50000000000
                zp2 = '{:,}'.format(zp)
            if work == 9:
                rabota = ['остонавили ограбление💰', 'поймали наркомана💉', "нашли закладку🚬",
                          "поймали преступника🔫 "]
                rx_rabota = random.choice(rabota)
                zp = 673000000000
                zp2 = '{:,}'.format(zp)
            if work == 10:
                rabota = ['спасли человеку жизнь👨‍⚕️', 'вылечили от COVID-19 😷', "сделали укол 💉",
                          "сделали операцию 👨‍⚕️"]
                rx_rabota = random.choice(rabota)
                zp = 1300000000000
                zp2 = '{:,}'.format(zp)
            if work == 11:
                rabota = ['выдержали урок с 8-В🥳', 'помогли директору школы 💼', "провели ЗНО 🎓", "провели 7 уроков🛎"]
                rx_rabota = random.choice(rabota)
                zp = 5000000000000
                zp2 = '{:,}'.format(zp)
            if work == 12:
                rabota = ['пролетели маршрут Киев-Москва🛩', 'пролетели маршрут Саратов-Дубай 🛬',
                          "пролетели маршрут Харьков-Египет ✈️", "пролетели маршрут Сант-Петербург-Нью-Йорк 🛫"]
                rx_rabota = random.choice(rabota)
                zp = 12000000000000
                zp2 = '{:,}'.format(zp)
            if work == 13:
                rabota = ['проведали школу МВД🚓', 'провели собеседование 💬', "нашли шпиона 🥷️",
                          "провели проверку в Москве👨‍✈️"]
                rx_rabota = random.choice(rabota)
                zp = 45000000000000
                zp2 = '{:,}'.format(zp)
            if work == 14:
                rabota = ['оформили продажу одного своего бизнеса 🏗', 'купили новый бизнес 🏭', "купили новый банк 🏦",
                          "продали новый музей 🏛"]
                rx_rabota = random.choice(rabota)
                zp = 55000000000000
                zp2 = '{:,}'.format(zp)
            if work == 15:
                rabota = ['написали телеграм бота 🤖', 'написали сайт 🖥', "выполнили заказ на фрилансе 🧮",
                          "написали скрипт  ⚙️"]
                rx_rabota = random.choice(rabota)
                zp = 100000000000000
                zp2 = '{:,}'.format(zp)

            period = 300
            get = cursor.execute("SELECT last_stavka FROM bot_work WHERE user_id = ?",
                                 (message.from_user.id,)).fetchone()
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            if work > 0:
                if stavkatime > period:
                    await bot.send_message(message.chat.id, f'{name}, вы успешно {rx_rabota} и получили зарплату {zp2}$  ✅',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + zp}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET level = {level + 1}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_work SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, нельзя так часто работать, отдохните 5 минут {rloser}',
                                           parse_mode='html')
                    return
            else:
                await bot.send_message(message.chat.id, f'{name}, куда работать? вы без работний {rloser}', parse_mode='html')

        if message.text.startswith('устроится'):
            name = message.from_user.get_mention(as_html=True)

            level = cursor.execute("SELECT level from users where user_id = ?", (message.from_user.id,)).fetchone()
            level = int(level[0])
            work = cursor.execute("SELECT work from users where user_id = ?", (message.from_user.id,)).fetchone()
            work = int(work[0])
            user_id = message.from_user.id

            nomer_work = int(message.text.split()[1])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            if work == 0:
                if nomer_work == 1:
                    if level >= 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Фермер" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 2:
                    if level >= 2:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Шахтёр" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 3:
                    if level >= 3:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Строитель" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 4:
                    if level >= 5:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Сантехник" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 5:
                    if level >= 7:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Электрик" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 6:
                    if level >= 8:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Пожарник" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 7:
                    if level >= 10:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Официант" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 8:
                    if level >= 11:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Повар" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 9:
                    if level >= 16:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Полицейский" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 10:
                    if level >= 21:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Доктор" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 11:
                    if level >= 29:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Педагог" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 12:
                    if level >= 35:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Пилот" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 13:
                    if level >= 49:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Генерал" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 14:
                    if level >= 57:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Бизнесмен" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 15:
                    if level >= 69:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Программист" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                else:
                    await bot.send_message(message.chat.id, f'{name}, такой вакансии нету к сожелению {rloser}',
                                           parse_mode='html')
            else:
                await bot.send_message(message.chat.id,
                                       f'{name}, вы решили работать сразу на 2 работах? Увольтесь для начала {rloser}',
                                       parse_mode='html')

        if message.text.startswith('Устроиться'):
            name = message.from_user.get_mention(as_html=True)

            level = cursor.execute("SELECT level from users where user_id = ?", (message.from_user.id,)).fetchone()
            level = int(level[0])
            work = cursor.execute("SELECT work from users where user_id = ?", (message.from_user.id,)).fetchone()
            work = int(work[0])
            user_id = message.from_user.id

            nomer_work = int(message.text.split()[1])

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            if work == 0:
                if nomer_work == 1:
                    if level >= 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Фермер" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 2:
                    if level >= 2:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Шахтёр" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 3:
                    if level >= 3:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Строитель" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 4:
                    if level >= 5:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Сантехник" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 5:
                    if level >= 7:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Электрик" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 6:
                    if level >= 8:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Пожарник" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 7:
                    if level >= 10:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Официант" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 8:
                    if level >= 11:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Повар" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 9:
                    if level >= 16:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Полицейский" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 10:
                    if level >= 21:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Доктор" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 11:
                    if level >= 29:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Педагог" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 12:
                    if level >= 35:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Пилот" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 13:
                    if level >= 49:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Генерал" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 14:
                    if level >= 57:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Бизнесмен" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                if nomer_work == 15:
                    if level >= 69:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно устроились на работу "Программист" {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET work = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                        return
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас не достаточный уровень {rloser}',
                                               parse_mode='html')
                        return
                else:
                    await bot.send_message(message.chat.id, f'{name}, такой ваканции нету к сожелению {rloser}',
                                           parse_mode='html')
            else:
                await bot.send_message(message.chat.id,
                                       f'{name}, вы решили работать сразу на 2 работах? Увольтесь для начала {rloser}',
                                       parse_mode='html')

        if message.text.lower() == 'вакансии':
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
{name}, вот все доступные вакансии📑
🍎 1 Фермер -54,000,000$ [1lvl]
⛏ 2 Шахтёр - 100,000,000$ [2lvl]
🧱 3 Строитель - 167,000,000$ [3lvl]
🛠 4 Сантехник - 532,000,000$ [5lvl]
💡 5 Электрик - 1,236,000,000$ [7lvl]
🧯 6 Пожарник - 5,115,000,000$ [8lvl]
☕️ 7 Официант - 15,000,000,000$ [10lvl]
🍰 8 Повар - 50,000,000,000$ [11lvl]
👮‍♂ 9 Полицейский - 674,000,000,000$ [16lvl]
👨‍⚕ 10 Доктор - 1,300,000,000,000$ [21lvl]
👩‍🏫 11 Педагог - 5,000,000,000,000$ [29lvl]
✈️ 12 Пилот - 12,000,000,000,000$ [35lvl]
👨‍✈️ 13 Генерал - 45,000,000,000,000$ [49lvl]
💍 14 Бизнесмен - 55,000,000,000,000$ [57lvl]
🖥 15 Программист - 100,000,000,000,000$ [69lvl]

📌Что бы устроиться на работу введите команду "Устроиться [номер]"

Наш telegram канал - В разработке
''', parse_mode='html')
        if message.text.lower() == 'Центр занятости':
            name1 = message.from_user.get_mention(as_html=True)
            user_name = message.from_user.full_name
            level = cursor.execute("SELECT level from users where user_id = ?", (message.from_user.id,)).fetchone()
            level = int(level[0])
            work = cursor.execute("SELECT work from users where user_id = ?", (message.from_user.id,)).fetchone()
            work = int(work[0])

            if work == 0:
                work2 = 'Без работный'
                zp = '0$'
            if work == 1:
                work2 = 'Фермер🍎'
                zp = '54,000,000$'
            if work == 2:
                work2 = 'Шахтёр⛏'
                zp = '100,000,000$'
            if work == 3:
                work2 = 'Строитель🧱'
                zp = '167,000,000$'
            if work == 4:
                work2 = 'Сантехник🛠'
                zp = '532,000,000$'
            if work == 5:
                work2 = 'Электрик💡'
                zp = '1,236,000,000$'
            if work == 6:
                work2 = 'Пожарник🧯'
                zp = '5,115,000,000$'
            if work == 7:
                work2 = 'Официант☕️'
                zp = '15,000,000,000$'
            if work == 8:
                work2 = 'Повар🍰'
                zp = '50,000,000,000$'
            if work == 9:
                work2 = 'Полицейский👮‍♂'
                zp = '674,000,000,000$'
            if work == 10:
                work2 = 'Доктор👨‍⚕'
                zp = '1,300,000,000,000$'
            if work == 11:
                work2 = 'Педагог👩‍🏫'
                zp = '5,000,000,000,000$'
            if work == 12:
                work2 = 'Пилот✈️'
                zp = '12,000,000,000,000$'
            if work == 13:
                work2 = 'Генерал👨‍✈️'
                zp = '45,000,000,000,000$'
            if work == 14:
                work2 = 'Бизнесмен💍'
                zp = '55,000,000,000,000$'
            if work == 15:
                work2 = 'Программист🖥'
                zp = '100,000,000,000,000$'

            await bot.send_message(message.chat.id, f'''
{name1}, добро пожаловать в центр занятости🏢
   👫 Ник: {user_name}
   📊 Уровень: {level}
   📈 Работа: {work2}
   💵 Зарплата: {zp}
''', parse_mode='html')
        ###########################################БАНК###########################################
        # bank
        if message.text.lower() in ["Банк", "банк"]:
            msg = message
            chat_id = message.chat.id
            name1 = message.from_user.get_mention(as_html=True)
            user_name = msg.from_user.full_name
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            deposit_status = cursor.execute("SELECT deposit_status from users where user_id = ?",
                                            (message.from_user.id,)).fetchone()
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            deposit = cursor.execute("SELECT deposit from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            deposit_status = int(deposit_status[0])
            deposit = int(deposit[0])
            balance = int(balance[0])
            bank = int(bank[0])
            rating = int(rating[0])
            balance2 = '{:,}'.format(balance)
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = round(int(bank[0]))
            bank2 = '{:,}'.format(bank)
            deposit2 = '{:,}'.format(deposit)
            if deposit_status == 0:
                deposit_status2 = 'Обычный'
            if deposit_status == 0:
                deposit_status3 = 6
            c = 999999999999999999999999
            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                balance2 = '{:,}'.format(balance)
            else:
                pass
            if bank >= 999999999999999999999999:
                bank = 999999999999999999999999
                cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                bank2 = '{:,}'.format(bank)
            else:
                pass
            if deposit >= 999999999999999999999999:
                deposit = 999999999999999999999999
                cursor.execute(f'UPDATE users SET deposit = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                deposit2 = '{:,}'.format(deposit)
            await bot.send_message(message.chat.id, f'''
    {name1} , вот данные о вашем банке 🏦

👨‍💼 Владелец: {user_name} 
🏛  Основной счёт: {bank2} $
💼 Хранительный счёт: 0$
🔐 Деньги на депозите: 0$
     💎 Статус депозита: Обычный
     📈 Процент под депозит: 6%
      💵 Деньги на вывод: 0$
    ''', parse_mode='html')

        if message.text.startswith("Банк положить"):
            msg = message
            chat_id = message.chat.id
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)

            bank_p = int(msg.text.split()[2])
            print(f"{name} положил в банк: {bank_p}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = round(int(bank[0]))
            bank2 = '{:,}'.format(bank_p)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            if bank_p > 0:
                if balance >= bank_p:
                    await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили в банк {bank2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"')
                    connect.commit()

                elif int(balance) < int(bank_p):
                    await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                           parse_mode='html')

            if bank_p <= 0:
                await bot.send_message(message.chat.id,
                                       f'{user_name}, нельзя положить в банк отрицательное число! {rloser}',
                                       parse_mode='html')
        if message.text.startswith("банк положить"):
            msg = message
            chat_id = message.chat.id
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)

            bank_p = int(msg.text.split()[2])
            print(f"{name} положил в банк: {bank_p}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = round(int(bank[0]))
            bank2 = '{:,}'.format(bank_p)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            if bank_p > 0:
                if balance >= bank_p:
                    await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили в банк {bank2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"')
                    connect.commit()

                elif int(balance) < int(bank_p):
                    await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                           parse_mode='html')

            if bank_p <= 0:
                await bot.send_message(message.chat.id,
                                       f'{user_name}, нельзя положить в банк отрицательное число! {rloser}',
                                       parse_mode='html')

        if message.text.startswith("Банк снять"):
            msg = message
            chat_id = message.chat.id
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)

            bank_s = int(msg.text.split()[2])
            print(f"{name} снял с банка: {bank_s}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = round(int(bank[0]))
            bank2 = '{:,}'.format(bank_s)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            if bank_s > 0:
                if bank >= bank_s:
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, вы успешно сняли с банковского счёта {bank2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"')
                    connect.commit()

                elif int(bank) < int(bank_s):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, недостаточно средств на банковском счету! {rloser}',
                                           parse_mode='html')
        if message.text.startswith("банк снять"):
            msg = message
            chat_id = message.chat.id
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)

            bank_s = int(msg.text.split()[2])
            print(f"{name} снял с банка: {bank_s}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
            bank = round(int(bank[0]))
            bank2 = '{:,}'.format(bank_s)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            if bank_s > 0:
                if bank >= bank_s:
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, вы успешно сняли с банковского счёта {bank2}$ {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"')
                    connect.commit()

                elif int(bank) < int(bank_s):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, недостаточно средств на банковском счету! {rloser}',
                                           parse_mode='html')

            if bank_s <= 0:
                await bot.send_message(message.chat.id,
                                       f'{user_name}, нельзя снять с банка отрицательное число! {rloser}',
                                       parse_mode='html')

        ###########################################АДМИН КОМАНДЫ###########################################
        if message.text.lower() == 'Выдать админ' :
            user_name = message.from_user.get_mention(as_html=True)
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            reply_user_id = msg.reply_to_message.from_user.id
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            if user_status[0] == 'Rab':
                await bot.send_message(message.chat.id, f'Вы успешно выдали администратора игроку {reply_user_name} {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET user_status = "Admin"  WHERE user_id = "{reply_user_id}"')
                connect.commit()
            else:
                await bot.send_message(message.chat.id, f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰', parse_mode='html')
        if message.text.lower() == 'выдать адм' :
            user_name = message.from_user.get_mention(as_html=True)
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            reply_user_id = msg.reply_to_message.from_user.id
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            if user_status[0] == 'Rab':
                await bot.send_message(message.chat.id, f'Вы успешно выдали администратора игроку {reply_user_name} {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET user_status = "Admin"  WHERE user_id = "{reply_user_id}"')
                connect.commit()
            else:
                await bot.send_message(message.chat.id, f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰', parse_mode='html')
        if message.text.lower() == 'unban':
            user_name = message.from_user.get_mention(as_html=True)
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            reply_user_id = msg.reply_to_message.from_user.id
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            if user_status[0] == 'Rab':
                await message.reply(f'Администратор снял бан игроку {reply_user_name} ⛔️', parse_mode='html')
                cursor.execute(f'UPDATE users SET status_block = "off" WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Admin':
                await message.reply(f'Администратор снял бан игроку {reply_user_name} ⛔️', parse_mode='html')
                cursor.execute(f'UPDATE users SET status_block = "off" WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Player':
                await message.reply(
                    f'ℹ{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')
        if message.text.lower() == 'ban':
            user_name = message.from_user.get_mention(as_html=True)
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            reply_user_id = msg.reply_to_message.from_user.id
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            if user_status[0] == 'Rab':
                await message.reply(f'Администратор выдал бан игроку {reply_user_name} ⛔️', parse_mode='html')
                cursor.execute(f'UPDATE users SET status_block = "on" WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Admin':
                await message.reply(f'Администратор выдал бан игроку {reply_user_name} ⛔️', parse_mode='html')
                cursor.execute(f'UPDATE users SET status_block = "on" WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Player':
                await message.reply(
                    f'ℹ{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

        if message.text.startswith("Выдать"):
            msg = message
            user_name = message.from_user.get_mention(as_html=True)
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            perevod = int(msg.text.split()[1])
            reply_user_id = msg.reply_to_message.from_user.id
            perevod2 = '{:,}'.format(perevod)
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])
            if user_status[0] == 'Rab':
                await message.reply(f'💵 Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}',
                                    parse_mode='html')

                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            elif user_status[0] == 'admin':
                await message.reply(
                    f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

            elif user_status[0] == 'Player':
                await message.reply(
                    f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

        if message.text.startswith("забрать"):
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            user_name = message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            perevod = int(msg.text.split()[1])
            reply_user_id = msg.reply_to_message.from_user.id
            perevod2 = '{:,}'.format(perevod)
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])
            if user_status[0] == 'Rab':
                await message.reply(f'💵 Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Admin':
                await message.reply(f'💵 Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}',
                                    parse_mode='html')
                
            elif user_status[0] == 'admin':
                await message.reply(
                    f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

            elif user_status[0] == 'Player':
                await message.reply(
                    f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

        if message.text.startswith("Забрать"):
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            perevod = int(msg.text.split()[1])
            reply_user_id = msg.reply_to_message.from_user.id
            perevod2 = '{:,}'.format(perevod)
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])
            if user_status[0] == 'Rab':
                await message.reply(f'💵 Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Admin':
                await message.reply(f'💵 Вы забрали {perevod2}$ у игрока {reply_user_name} {rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            elif user_status[0] == 'Player':
                await message.reply(
                    f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

        if message.text.lower() in ["обнулить", "Обнулить"]:
            msg = message
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            reply_user_id = msg.reply_to_message.from_user.id
            user_id = msg.from_user.id
            user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            if user_status[0] == 'Rab':
                await message.reply(f'💵 | Вы успешно обнулили игрока {reply_user_name} {rwin}', 
                parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Admin':
                await message.reply(f'💵 | Вы успешно обнулили игрока {reply_user_name} {rwin}', parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Player':
                await message.reply(
                    f'ℹ{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')

        #######################################################ДОМА#############################################################
        if message.text.startswith("Купить дом"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            house = cursor.execute("SELECT house from property where user_id = ?", (message.from_user.id,)).fetchone()
            house = int(house[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 500000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Коробка" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 1000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Подвал" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 3000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Сарай" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 5000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Маленький домик" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 7000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Квартира" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 10000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Огромный дом" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 50000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Коттедж" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 100000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Вилла" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 5000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Загородный дом" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 50000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Небоскрёб" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 200000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Дом на мальдивах" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 1000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили дом "Технологичный небосрёб" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 5000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили дом "Собственный остров" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 14:
                price = 15000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Дом на марсе" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 15:
                price = 25000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Остров на марсе" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 16:
                price = 50000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Свой марс" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {16}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

        if message.text.startswith("купить дом"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            house = cursor.execute("SELECT house from property where user_id = ?", (message.from_user.id,)).fetchone()
            house = int(house[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 500000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Коробка" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 1000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Подвал" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 3000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Сарай" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 5000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Маленький домик" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 7000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Квартира" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 10000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Огромный дом" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 50000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Коттедж" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 100000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Вилла" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 5000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Загородный дом" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 50000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Небоскрёб" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 200000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Дом на мальдивах" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 1000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили дом "Технологичный небосрёб" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 5000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили дом "Собственный остров" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 14:
                price = 15000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Дом на марсе" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 15:
                price = 25000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Остров на марсе" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 16:
                price = 50000000000000
                if balance >= price:
                    if house < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили дом "Свой марс" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET house = {16}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть дом {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

        if message.text.lower() in ['Продать дом', "продать дом"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            house = cursor.execute("SELECT house from property where user_id = ?", (message.from_user.id,)).fetchone()
            house = int(house[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)

            if house > 0:
                if house == 1:
                    price = 500000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 2:
                    price = 1000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 3:
                    price = 3000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 4:
                    price = 5000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 5:
                    price = 7000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 6:
                    price = 10000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 7:
                    price = 50000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 8:
                    price = 100000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 9:
                    price = 5000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 10:
                    price = 50000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 11:
                    price = 200000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 12:
                    price = 1000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 13:
                    price = 5000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 14:
                    price = 15000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 15:
                    price = 25000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if house == 16:
                    price = 50000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали дом за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET house = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
        if message.text.lower() in ['дома', 'Дома']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name}, доступные дома:
    🏠 1. Коробка - 500.000$
    🏠 2. Подвал - 1.000.000$
    🏠 3. Сарай - 3.000.000$
    🏠 4. Маленький домик - 5.000.000$
    🏠 5. Квартира - 7.000.000$
    🏠 6. Огромный дом - 10.000.000$
    🏠 7. Коттедж - 50.000.000$
    🏠 8. Вилла - 100.000.000$
    🏠 9. Загородный дом - 5.000.000.000$
    🏠 10. Небоскрёб - 50.000.000.000$
    🏠 11. Дом на мальдивах - 200.000.000.000$
    🏠 12. Технологичный небосрёб - 1.000.000.000.000$
    🏠 13. Собственный остров - 5.000.000.000.000$
    🏠 14. Дом на марсе - 15.000.000.000.000$
    🏠 15. Остров на марсе - 25.000.000.000.000$
    🏠 16. Свой марс - 50.000.000.000.000$
    
    🛒 Для покупки дома введите "Купить дом [номер]"
    
    Наш telegram канал - В разработке
    ''', parse_mode='html')
        #######################################################КЕЙСЫ############################################################
        if message.text.lower() in ['Кейсы', 'кейсы']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'{name}, данная команда ещё в разработке ❌')
        ######################################################ЯХТЫ##############################################################
        if message.text.lower() in ['Продать вертолёт', "продать вертолёт"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            yacht = cursor.execute("SELECT yacht from property where user_id = ?", (message.from_user.id,)).fetchone()
            yacht = int(yacht[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)

            if yacht > 0:
                if yacht == 1:
                    price = 1000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 2:
                    price = 10000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 3:
                    price = 30000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 4:
                    price = 100000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 5:
                    price = 500000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 6:
                    price = 800000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 7:
                    price = 5000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 8:
                    price = 15000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 9:
                    price = 40000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 10:
                    price = 90000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 11:
                    price = 200000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 12:
                    price = 600000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if yacht == 13:
                    price = 1600000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали яхту за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET yacht = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
        if message.text.startswith("купить яхту"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            yacht = cursor.execute("SELECT yacht from property where user_id = ?", (message.from_user.id,)).fetchone()
            yacht = int(yacht[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 1000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Ванна" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 10000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Nauticat 331" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 30000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Nordhavn 56 MS" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 100000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Princess 60" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 500000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Bayliner 288" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 800000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Dominator 40M" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 5000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Sessa Marine C42" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 15000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Wider 150" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 40000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили яхту "Palmer Johnson 42M SuperSport" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 90000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Serene" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 200000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Dubai" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 600000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Azzam" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 1600000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили яхту "Streets of Monaco" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.startswith("Купить яхту"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            yacht = cursor.execute("SELECT yacht from property where user_id = ?", (message.from_user.id,)).fetchone()
            yacht = int(yacht[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 1000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Ванна" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 10000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Nauticat 331" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 30000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Nordhavn 56 MS" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 100000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Princess 60" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 500000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Bayliner 288" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 800000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Dominator 40M" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 5000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Sessa Marine C42" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 15000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Wider 150" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 40000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили яхту "Palmer Johnson 42M SuperSport" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 90000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Serene" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 200000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Dubai" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 600000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили яхту "Azzam" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 1600000000000
                if balance >= price:
                    if yacht < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили яхту "Streets of Monaco" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET yacht = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть яхта {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['Яхты', 'яхты']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name}, доступные яхты:
    🛳 1. Ванна - 1.000.000$
    🛳 2. Nauticat 331 - 10.000.000$
    🛳 3. Nordhavn 56 MS - 30.000.000$
    🛳 4. Princess 60 - 100.000.000$
    🛳 5. Bayliner 288 - 500.000.000$
    🛳 6. Dominator 40M - 800.000.000$
    🛳 7. Sessa Marine C42 - 5.000.000.000$
    🛳 8. Wider 150 - 15.000.000.000$
    🛳 9. Palmer Johnson 42M SuperSport - 40.000.000.000$
    🛳 10. Serene - 90.000.000.000$
    🛳 11. Dubai - 200.000.000.000$
    🛳 12. Azzam - 600.000.000.000$
    🛳 13. Streets of Monaco - 1.600.000.000.000$
    
    🛒 Для покупки яхты введите "Купить яхту [номер]"
    
    Наш telegram канал - В разработке
    ''', parse_mode='html')
        ######################################################ВЕРТОЛЁТЫ#########################################################
        if message.text.startswith("Купить вертолёт"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            helicopter = cursor.execute("SELECT helicopter from property where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            helicopter = int(helicopter[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 100000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Воздушный шар" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 350000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "RotorWay Exec 162F" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 700000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "Robinson R44" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 1000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Hiller UH-12C" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 1400000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "AW119 Koala" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 2600000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "MBB BK 117" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 5500000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Eurocopter EC130" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 8800000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Leonardo AW109 Power" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 450000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Sikorsky S-76" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 800000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "Bell 429WLG" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 1600000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "NHI NH90" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 2250000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "Kazan Mi-35M" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 3500000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Bell V-22 Osprey" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.startswith("купить вертолёт"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            helicopter = cursor.execute("SELECT helicopter from property where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            helicopter = int(helicopter[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 100000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Воздушный шар" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 350000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "RotorWay Exec 162F" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 700000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "Robinson R44" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 1000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Hiller UH-12C" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 1400000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "AW119 Koala" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 2600000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "MBB BK 117" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 5500000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Eurocopter EC130" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 8800000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Leonardo AW109 Power" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 450000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Sikorsky S-76" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 800000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "Bell 429WLG" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 1600000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "NHI NH90" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 2250000000000
                if balance >= price:
                    if helicopter < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили вертолёт "Kazan Mi-35M" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET helicopter = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 3500000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили вертолёт "Bell V-22 Osprey" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть вертолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['Продать вертолёт', "продать вертолёт"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            helicopter = cursor.execute("SELECT helicopter from property where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            helicopter = int(helicopter[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)

            if helicopter > 0:
                if helicopter == 1:
                    price = 100000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 2:
                    price = 3500000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 3:
                    price = 10000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 4:
                    price = 30000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 5:
                    price = 63400000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 6:
                    price = 150000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 7:
                    price = 350000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 8:
                    price = 750000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 9:
                    price = 1240000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 10:
                    price = 8890000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 11:
                    price = 88330000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 12:
                    price = 225750000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if helicopter == 13:
                    price = 945300000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали вертолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET helicopter = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()

        if message.text.lower() in ['Вертолёты', 'вертолёты']:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name}, доступные вертолёты:
    🚁 1. Воздушный шар - 100.000$
    🚁 2. RotorWay Exec 162F - 3.500.000$
    🚁 3. Robinson R44 - 10.000.000$
    🚁 4. Hiller UH-12C - 30.000.000$
    🚁 5. AW119 Koala - 63.400.000$
    🚁 6. MBB BK 117 - 150.000.000$
    🚁 7. Eurocopter EC130 - 350.000.000$
    🚁 8. Leonardo AW109 Power - 750.000.000$
    🚁 9. Sikorsky S-76 - 1.240.000.000$
    🚁 10. Bell 429WLG - 8.890.000.000$
    🚁 11. NHI NH90 - 88.330.000.000$
    🚁 12. Kazan Mi-35M - 225.750.000.000$
    🚁 13. Bell V-22 Osprey - 945.300.000.000$
    
    🛒 Для покупки вертолёта введите "Купить вертолет [номер]"
    
    Наш telegram канал - В разработке
    ''', parse_mode='html')
        ######################################################САМОЛЁТЫ##########################################################
        if message.text.lower() in ['Продать самолёт', "продать самолёт"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            plane = cursor.execute("SELECT plane from property where user_id = ?", (message.from_user.id,)).fetchone()
            plane = int(plane[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)

            if plane > 0:
                if plane == 1:
                    price = 100000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 2:
                    price = 350000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 3:
                    price = 700000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 4:
                    price = 1000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 5:
                    price = 1400000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 6:
                    price = 2600000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 7:
                    price = 5500000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 8:
                    price = 8800000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 9:
                    price = 450000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 10:
                    price = 800000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 11:
                    price = 1600000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 12:
                    price = 2250000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 13:
                    price = 3500000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 14:
                    price = 4000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 15:
                    price = 6000000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if plane == 16:
                    price = 13500000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали самолёт за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET plane = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()

        if message.text.startswith("купить самолёт"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            plane = cursor.execute("SELECT plane from property where user_id = ?", (message.from_user.id,)).fetchone()
            plane = int(plane[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 100000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Параплан" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 350000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Параплан" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 700000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Cessna-172E" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 1000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "BRM NG-5" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 1400000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Cessna T210" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 2600000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "Beechcraft 1900D" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 5500000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Cessna 550" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 8800000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Hawker 4000" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 450000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Learjet 31" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 800000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Airbus A318" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 1600000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "F-35A" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 2250000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "Boeing 747-430" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 3500000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "C-17A Globemaster III" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 14:
                price = 4000000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "F-22 Raptor" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 15:
                price = 6000000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "Airbus 380 Custom" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 16:
                price = 13500000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "B-2 Spirit Stealth Bomber" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {16}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.startswith("Купить самолёт"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            plane = cursor.execute("SELECT plane from property where user_id = ?", (message.from_user.id,)).fetchone()
            plane = int(plane[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 100000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Параплан" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 350000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Параплан" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 700000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Cessna-172E" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 1000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "BRM NG-5" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 1400000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Cessna T210" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 2600000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "Beechcraft 1900D" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 5500000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Cessna 550" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 8800000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Hawker 4000" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 450000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Learjet 31" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 800000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "Airbus A318" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 1600000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "F-35A" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 2250000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "Boeing 747-430" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 3500000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "C-17A Globemaster III" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 14:
                price = 4000000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили самолёт "F-22 Raptor" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 15:
                price = 6000000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "Airbus 380 Custom" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 16:
                price = 13500000000000
                if balance >= price:
                    if plane < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили самолёт "B-2 Spirit Stealth Bomber" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET plane = {16}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть самолёт {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['Самолёты', "самолёты"]:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name}, доступные самолеты:
    ✈️ 1. Параплан - 100.000.000$
    ✈️ 2. АН-2 - 350.000.000$
    ✈️ 3. Cessna-172E - 700.000.000$
    ✈️ 4. BRM NG-5 - 1.000.000.000$
    ✈️ 5. Cessna T210 - 1.400.000.000$
    ✈️ 6. Beechcraft 1900D - 2.600.000.000$
    ✈️ 7. Cessna 550 - 5.500.000.000$
    ✈️ 8. Hawker 4000 - 8.800.000.000$
    ✈️ 9. Learjet 31 - 450.000.000.000$
    ✈️ 10. Airbus A318 - 800.000.000.000$
    ✈️ 11. F-35A - 1.600.000.000.000$
    ✈️ 12. Boeing 747-430 - 2.250.000.000.000$
    ✈️ 13. C-17A Globemaster III - 3.500.000.000.000$
    ✈️ 14. F-22 Raptor - 4.000.000.000.000$
    ✈️ 15. Airbus 380 Custom - 6.000.000.000.000$
    ✈️ 16. B-2 Spirit Stealth Bomber - 13.500.000.000.000$
    
    🛒 Для покупки самолёта введите "Купить самолёт [номер]"
    
    Наш telegram канал - В разработке
    ''', parse_mode='html')
        ####################################################ТЕЛЕФОНЫ############################################################
        if message.text.startswith("Купить телефон"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            phone = cursor.execute("SELECT phone from property where user_id = ?", (message.from_user.id,)).fetchone()
            phone = int(phone[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 100000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Nokia 3310" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 3500000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили телефон "ASUS ZenFone 4" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 10000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "BQ Aquaris X" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 30000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Huawei P40" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 63400000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили телефон "Samsung Galaxy S21 Ultra" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 150000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Xiaomi Mi 11" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 350000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "iPhone 11 Pro" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 750000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили телефон "iPhone 12 Pro Max" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 1240000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Blackberry" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.startswith("купить телефон"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            phone = cursor.execute("SELECT phone from property where user_id = ?", (message.from_user.id,)).fetchone()
            phone = int(phone[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 100000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Nokia 3310" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 3500000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили телефон "ASUS ZenFone 4" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 10000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "BQ Aquaris X" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 30000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Huawei P40" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 63400000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили телефон "Samsung Galaxy S21 Ultra" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 150000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Xiaomi Mi 11" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 350000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "iPhone 11 Pro" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 750000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили телефон "iPhone 12 Pro Max" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 1240000000
                if balance >= price:
                    if phone < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили телефон "Blackberry" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET phone = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть телефон {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['Продать телефон', "продать телефон"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            phone = cursor.execute("SELECT phone from property where user_id = ?", (message.from_user.id,)).fetchone()
            phone = int(phone[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)

            if phone > 0:
                if phone == 1:
                    price = 100000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 2:
                    price = 3500000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 3:
                    price = 10000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 4:
                    price = 30000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 5:
                    price = 63400000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 6:
                    price = 150000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 7:
                    price = 350000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 8:
                    price = 750000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if phone == 9:
                    price = 1240000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали телефон за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET phone = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()

        if message.text.lower() in ['Телефоны', "телефоны"]:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
    {name}, доступные телефоны:
    📱 1. Nokia 3310 - 100.000$
    📱 2. ASUS ZenFone 4 - 3.500.000$
    📱 3. BQ Aquaris X - 10.000.000$
    📱 4. Huawei P40 - 30.000.000$
    📱 5. Samsung Galaxy S21 Ultra - 63.400.000$
    📱 6. Xiaomi Mi 11 - 150.000.000$
    📱 7. iPhone 11 Pro - 350.000.000$
    📱 8. iPhone 12 Pro Max - 750.000.000$
    📱 9. Blackberry - 1.240.000.000$
    
    🛒 Для покупки телефона введите "Купить телефон [номер]"
    
    Наш telegram канал - В разработке''', parse_mode='html')
        #####################################################МАШИНЫ#############################################################
        if message.text.lower() in ['Продать машину', "продать машину"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            cars = cursor.execute("SELECT cars from property where user_id = ?", (message.from_user.id,)).fetchone()
            cars = int(cars[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)

            if cars > 0:
                if cars == 1:
                    price = 10000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 2:
                    price = 15000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 3:
                    price = 30000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 4:
                    price = 50000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 5:
                    price = 90000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 6:
                    price = 100000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 7:
                    price = 250000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 8:
                    price = 400000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 9:
                    price = 600000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 10:
                    price = 900000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 11:
                    price = 1400000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 12:
                    price = 2500000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 13:
                    price = 6000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 14:
                    price = 8000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 15:
                    price = 10000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 16:
                    price = 40000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 17:
                    price = 100000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 18:
                    price = 300000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 19:
                    price = 500000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 20:
                    price = 700000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 21:
                    price = 900000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 22:
                    price = 210000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 23:
                    price = 310000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 24:
                    price = 443000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 25:
                    price = 643000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
                if cars == 26:
                    price = 943000000000
                    price2 = price / 2
                    price3 = '{:,}'.format(price2)

                    await bot.send_message(message.chat.id, f'{name}, вы успешно продали машину за {price3}$ ',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + price2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE property SET cars = {0}  WHERE user_id = "{user_id}"')
                    connect.commit()
            else:
                await bot.send_message(message.chat.id, f'{name}, у вас нет данного имущества {rloser}')

        if message.text.startswith("Купить машину"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            cars = cursor.execute("SELECT cars from property where user_id = ?", (message.from_user.id,)).fetchone()
            cars = int(cars[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 10000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Самокат" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 15000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Велосипед" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 30000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Гироскутер" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 50000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Сегвей" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 90000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Мопед" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 100000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Мотоцикл" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 250000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "ВАЗ 2109" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 400000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Квадроцикл" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 600000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Багги" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 900000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Вездеход" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 1400000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Лада Xray" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 2500000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Audi Q7" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 6000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "BMW X6" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 14:
                price = 8000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Toyota FT-HS" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 15:
                price = 10000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "BMW Z4 M" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 16:
                price = 40000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Subaru WRX STI" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {16}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 17:
                price = 100000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили машину "Lamborghini Veneno" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {17}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 18:
                price = 300000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Tesla Roadster" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {18}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 19:
                price = 500000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Yamaha YZF R6" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {19}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 20:
                price = 700000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Bugatti Chiron" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {20}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 21:
                price = 900000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Thrust SSC" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {21}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 22:
                price = 2100000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили машину "Ferrari LaFerrari" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {22}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 23:
                price = 3100000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили машину "Koenigsegg Regear" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {23}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 24:
                price = 4430000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Tesla Semi" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {24}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 25:
                price = 6430000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Venom GT" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {25}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 26:
                price = 9430000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Rolls-Royce" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {26}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            else:
                await bot.send_message(message.chat.id, f'{name}, такого номера нету в продаже {rloser}',
                                       parse_mode='html')
        if message.text.startswith("купить машину"):
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            cars = cursor.execute("SELECT cars from property where user_id = ?", (message.from_user.id,)).fetchone()
            cars = int(cars[0])

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            nomer = int(message.text.split()[2])

            if nomer == 1:
                price = 10000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Самокат" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {1}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 2:
                price = 15000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Велосипед" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {2}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 3:
                price = 30000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Гироскутер" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {3}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 4:
                price = 50000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Сегвей" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {4}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 5:
                price = 90000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Мопед" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {5}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 6:
                price = 100000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Мотоцикл" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {6}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 7:
                price = 250000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "ВАЗ 2109" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {7}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 8:
                price = 400000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Квадроцикл" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {8}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 9:
                price = 600000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Багги" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {9}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 10:
                price = 900000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Вездеход" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {10}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 11:
                price = 1400000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Лада Xray" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {11}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

            if nomer == 12:
                price = 2500000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Audi Q7" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {12}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 13:
                price = 6000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "BMW X6" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {13}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 14:
                price = 8000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Toyota FT-HS" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {14}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 15:
                price = 10000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "BMW Z4 M" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {15}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 16:
                price = 40000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Subaru WRX STI" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {16}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 17:
                price = 100000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили машину "Lamborghini Veneno" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {17}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 18:
                price = 300000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Tesla Roadster" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {18}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 19:
                price = 500000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Yamaha YZF R6" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {19}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 20:
                price = 700000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Bugatti Chiron" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {20}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 21:
                price = 900000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Thrust SSC" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {21}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 22:
                price = 2100000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили машину "Ferrari LaFerrari" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {22}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 23:
                price = 3100000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id,
                                               f'{name}, вы успешно купили машину "Koenigsegg Regear" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {23}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 24:
                price = 4430000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Tesla Semi" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {24}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 25:
                price = 6430000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Venom GT" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {25}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')
            if nomer == 26:
                price = 9430000000000
                if balance >= price:
                    if cars < 1:
                        await bot.send_message(message.chat.id, f'{name}, вы успешно купили машину "Rolls-Royce" 🎉',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE property SET have = "on"  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET balance = {balance - price}  WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE property SET cars = {26}  WHERE user_id = "{user_id}"')
                        connect.commit()
                    else:
                        await bot.send_message(message.chat.id, f'{name}, у вас уже есть машина {rloser}',
                                               parse_mode='html')
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, у вас недостаточно средств для покупки данного имущества {rloser}',
                                           parse_mode='html')

        if message.text.lower() in ['Машины', "машины"]:
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''{name}, доступные машины:
    🚗 1. Самокат - 10.000.000$
    🚗 2. Велосипед - 15.000.000$
    🚗 3. Гироскутер - 30.000.000$
    🚗 4. Сегвей - 50.000.000$
    🚗 5. Мопед - 90.000.000$
    🚗 6. Мотоцикл - 100.000.000$
    🚗 7. ВАЗ 2109 - 250.000.000$
    🚗 8. Квадроцикл - 400.000.000$
    🚗 9. Багги - 600.000.000$
    🚗 10. Вездеход - 900.000.000$
    🚗 11. Лада Xray - 1.400.000.000$
    🚗 12. Audi Q7 - 2.500.000.000$
    🚗 13. BMW X6 - 6.000.000.000$
    🚗 14. Toyota FT-HS - 8.000.000.000$
    🚗 15. BMW Z4 M - 10.000.000.000$
    🚗 16. Subaru WRX STI - 40.000.000.000$
    🚗 17. Lamborghini Veneno - 100.000.000.000$
    🚗 18. Tesla Roadster - 300.000.000.000$
    🚗 19. Yamaha YZF R6 - 500.000.000.000$
    🚗 20. Bugatti Chiron - 700.000.000.000$
    🚗 21. Thrust SSC - 900.000.000.000$
    🚗 22. Ferrari LaFerrari - 2.100.000.000.000$
    🚗 23. Koenigsegg Regear - 3.100.000.000.000$
    🚗 24. Tesla Semi - 4.430.000.000.000$
    🚗 25. Venom GT - 6.430.000.000.000$
    🚗 26. Rolls-Royce - 9.430.000.000.000$
    
    🛒 Для покупки машины введите "Купить машину [номер]"''', parse_mode='html')

        ##########################################ШАХТА#########################################################################
        if message.text.lower() in ['Моя шахта', 'моя шахта']:
            msg = message
            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            expe2 = '{:,}'.format(expe)

            name = message.from_user.get_mention(as_html=True)

            if expe >= 0:
                lvl = '''
    ⛏ Ваш уровень: Железо ⛓
    ➡️ Следующий уровень: Золото 🌕'''
            if expe > 500:
                lvl = '''
    ⛏ Ваш уровень: Золото 🌕
    ➡️ Следующий уровень: Алмазы 💎'''
            if expe > 2000:
                lvl = '''
    ⛏ Ваш уровень: Алмазы 💎
    ➡️ Следующий уровень: Аметисты ☄️'''
            if expe > 10000:
                lvl = '''
    ⛏ Ваш уровень: Аметисты ☄
    ➡️ Следующий уровень: Аквамарин  💠️'''
            if expe > 25000:
                lvl = '''
    ⛏ Ваш уровень: Аквамарин  💠️
    ➡️ Следующий уровень: Изумруды ❇️'''
            if expe > 60000:
                lvl = '''
    ⛏ Ваш уровень: Изумруды ❇
    ➡️ Следующий уровень: Материя 🌌️'''
            if expe > 100000:
                lvl = '''
    ⛏ Ваш уровень: Материя 🌌️
    ➡️ Следующий уровень: Плазма 🎇'''
            if expe >= 500000:
                lvl = '''
    ⛏ Ваш уровень: Плазма 🎇
    ➡️ Максимальный уровень 🏆'''

            await bot.send_message(message.chat.id, f'''
    {name}, это ваш профиль шахты:
    🏆 Опыт: {expe2}
    ⚡️ Энергия: {energy}
    {lvl}''', parse_mode='html')

        if message.text.lower() in ['продать плазму', 'Продать плазму']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            plasma = cursor.execute("SELECT plasma from mine where user_id = ?", (message.from_user.id,)).fetchone()
            plasma = int(plasma[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = plasma * 632000000
            price2 = '{:,}'.format(price)

            if plasma <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет плазмы {rloser}', parse_mode='html')
            if plasma > 0:
                await bot.send_message(message.chat.id, f'вы продали всю свою плазму за {price2}$ ✅', parse_mode='html')
                cursor.execute(f'UPDATE mine SET plasma = {plasma - plasma}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать плазму"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            plasma = cursor.execute("SELECT plasma from mine where user_id = ?", (message.from_user.id,)).fetchone()
            plasma = int(plasma[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 632000000
            price2 = '{:,}'.format(price)

            if quantity > plasma:
                await bot.send_message(message.chat.id, f'{name}, у вас нет плазму {rloser}', parse_mode='html')
            if quantity <= plasma:
                await bot.send_message(message.chat.id, f'вы продали {quantity} плазму за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET plasma = {plasma - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("продать плазму"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            plasma = cursor.execute("SELECT plasma from mine where user_id = ?", (message.from_user.id,)).fetchone()
            plasma = int(plasma[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 632000000
            price2 = '{:,}'.format(price)

            if quantity > plasma:
                await bot.send_message(message.chat.id, f'{name}, у вас нет плазму {rloser}', parse_mode='html')
            if quantity <= plasma:
                await bot.send_message(message.chat.id, f'вы продали {quantity} плазму за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET plasma = {plasma - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать материю', 'Продать материю']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            matter = cursor.execute("SELECT matter from mine where user_id = ?", (message.from_user.id,)).fetchone()
            matter = int(matter[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = matter * 412000000
            price2 = '{:,}'.format(price)

            if matter <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет материи {rloser}', parse_mode='html')
            if matter > 0:
                await bot.send_message(message.chat.id, f'вы продали всю свою материю за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET matter = {matter - matter}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать материю"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            matter = cursor.execute("SELECT matter from mine where user_id = ?", (message.from_user.id,)).fetchone()
            matter = int(matter[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 412000000
            price2 = '{:,}'.format(price)

            if quantity > matter:
                await bot.send_message(message.chat.id, f'{name}, у вас нет материи {rloser}', parse_mode='html')
            if quantity <= matter:
                await bot.send_message(message.chat.id, f'вы продали {quantity} материи за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET matter = {matter - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать материю"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            matter = cursor.execute("SELECT matter from mine where user_id = ?", (message.from_user.id,)).fetchone()
            matter = int(matter[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 412000000
            price2 = '{:,}'.format(price)

            if quantity > matter:
                await bot.send_message(message.chat.id, f'{name}, у вас нет материи {rloser}', parse_mode='html')
            if quantity <= matter:
                await bot.send_message(message.chat.id, f'вы продали {quantity} материи за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET matter = {matter - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать изумруды', 'Продать изумруды']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            emeralds = cursor.execute("SELECT emeralds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            emeralds = int(emeralds[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = emeralds * 366000000
            price2 = '{:,}'.format(price)

            if emeralds <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет изумрудов {rloser}', parse_mode='html')
            if emeralds > 0:
                await bot.send_message(message.chat.id, f'вы продали все свои изумруды за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET emeralds = {emeralds - emeralds}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать изумруды"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            emeralds = cursor.execute("SELECT emeralds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            emeralds = int(emeralds[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 366000000
            price2 = '{:,}'.format(price)

            if quantity > emeralds:
                await bot.send_message(message.chat.id, f'{name}, у вас нет изумрудов {rloser}', parse_mode='html')
            if quantity <= emeralds:
                await bot.send_message(message.chat.id, f'вы продали {quantity} изумруды за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET emeralds = {emeralds - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать изумруды"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            emeralds = cursor.execute("SELECT emeralds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            emeralds = int(emeralds[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 366000000
            price2 = '{:,}'.format(price)

            if quantity > emeralds:
                await bot.send_message(message.chat.id, f'{name}, у вас нет изумрудов {rloser}', parse_mode='html')
            if quantity <= emeralds:
                await bot.send_message(message.chat.id, f'вы продали {quantity} изумруды за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET emeralds = {emeralds - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать аквамарин', 'Продать аквамарин']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            aquamarine = cursor.execute("SELECT aquamarine from mine where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            aquamarine = int(aquamarine[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = aquamarine * 302000000
            price2 = '{:,}'.format(price)

            if aquamarine <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет аквамарина {rloser}', parse_mode='html')
            if aquamarine > 0:
                await bot.send_message(message.chat.id, f'вы продали все свой аквамарин за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET aquamarine = {aquamarine - aquamarine}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать аквамарин"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            aquamarine = cursor.execute("SELECT aquamarine from mine where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            aquamarine = int(aquamarine[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 302000000
            price2 = '{:,}'.format(price)

            if quantity > aquamarine:
                await bot.send_message(message.chat.id, f'{name}, у вас нет аквамарина {rloser}', parse_mode='html')
            if quantity <= aquamarine:
                await bot.send_message(message.chat.id, f'вы продали {quantity} аквамарин за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET aquamarine = {aquamarine - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать аквамарин"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            aquamarine = cursor.execute("SELECT aquamarine from mine where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            aquamarine = int(aquamarine[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 302000000
            price2 = '{:,}'.format(price)

            if quantity > aquamarine:
                await bot.send_message(message.chat.id, f'{name}, у вас нет аквамарина {rloser}', parse_mode='html')
            if quantity <= aquamarine:
                await bot.send_message(message.chat.id, f'вы продали {quantity} аквамарин за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET aquamarine = {aquamarine - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать аметисты', 'Продать аметисты']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            amethysts = cursor.execute("SELECT amethysts from mine where user_id = ?",
                                       (message.from_user.id,)).fetchone()
            amethysts = int(amethysts[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = amethysts * 216000000
            price2 = '{:,}'.format(price)

            if amethysts <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет аметистов {rloser}', parse_mode='html')
            if amethysts > 0:
                await bot.send_message(message.chat.id, f'вы продали все свои аметисты за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET amethysts = {amethysts - amethysts}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать аметисты"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            amethysts = cursor.execute("SELECT amethysts from mine where user_id = ?",
                                       (message.from_user.id,)).fetchone()
            amethysts = int(amethysts[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 266000000
            price2 = '{:,}'.format(price)

            if quantity > amethysts:
                await bot.send_message(message.chat.id, f'{name}, у вас нет аметистов {rloser}', parse_mode='html')
            if quantity <= amethysts:
                await bot.send_message(message.chat.id, f'вы продали {quantity} аметистов за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET amethysts = {amethysts - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать аметисты"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            amethysts = cursor.execute("SELECT amethysts from mine where user_id = ?",
                                       (message.from_user.id,)).fetchone()
            amethysts = int(amethysts[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 266000000
            price2 = '{:,}'.format(price)

            if quantity > amethysts:
                await bot.send_message(message.chat.id, f'{name}, у вас нет аметистов {rloser}', parse_mode='html')
            if quantity <= amethysts:
                await bot.send_message(message.chat.id, f'вы продали {quantity} аметистов за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET amethysts = {amethysts - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать алмазы', 'Продать алмазы']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            diamonds = cursor.execute("SELECT diamonds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            diamonds = int(diamonds[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = diamonds * 116000000
            price2 = '{:,}'.format(price)

            if diamonds <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет алмазов {rloser}', parse_mode='html')
            if diamonds > 0:
                await bot.send_message(message.chat.id, f'вы продали все свои алмазы за {price2}$ ✅', parse_mode='html')
                cursor.execute(f'UPDATE mine SET diamonds = {diamonds - diamonds}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать алмазы"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            diamonds = cursor.execute("SELECT diamonds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            diamonds = int(diamonds[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 166000000
            price2 = '{:,}'.format(price)

            if quantity > diamonds:
                await bot.send_message(message.chat.id, f'{name}, у вас нет алмазов {rloser}', parse_mode='html')
            if quantity <= diamonds:
                await bot.send_message(message.chat.id, f'вы продали {quantity} алмазов за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET diamonds = {diamonds - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать алмазы"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            diamonds = cursor.execute("SELECT diamonds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            diamonds = int(diamonds[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 166000000
            price2 = '{:,}'.format(price)

            if quantity > diamonds:
                await bot.send_message(message.chat.id, f'{name}, у вас нет алмазов {rloser}', parse_mode='html')
            if quantity <= diamonds:
                await bot.send_message(message.chat.id, f'вы продали {quantity} алмазов за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET diamonds = {diamonds - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать золото', 'Продать золото']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
            gold = int(gold[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = gold * 1000000
            price2 = '{:,}'.format(price)

            if gold <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет золото {rloser}', parse_mode='html')
            if gold > 0:
                await bot.send_message(message.chat.id, f'вы продали все своё золото за {price2}$ ✅', parse_mode='html')
                cursor.execute(f'UPDATE mine SET gold = {gold - gold}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать золото"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
            gold = int(gold[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 1000000
            price2 = '{:,}'.format(price)

            if quantity > gold:
                await bot.send_message(message.chat.id, f'{name}, у вас нет золото {rloser}', parse_mode='html')
            if quantity <= gold:
                await bot.send_message(message.chat.id, f'вы продали {quantity} золото за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET gold = {gold - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать золото"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
            gold = int(gold[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 1000000
            price2 = '{:,}'.format(price)

            if quantity > gold:
                await bot.send_message(message.chat.id, f'{name}, у вас нет золото {rloser}', parse_mode='html')
            if quantity <= gold:
                await bot.send_message(message.chat.id, f'вы продали {quantity} золото за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET gold = {gold - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['продать железо', 'Продать железо']:
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
            iron = int(iron[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = iron * 230000
            price2 = '{:,}'.format(price)

            if iron <= 0:
                await bot.send_message(message.chat.id, f'{name}, у вас нет железа {rloser}', parse_mode='html')
            if iron > 0:
                await bot.send_message(message.chat.id, f'вы продали все своё железо за {price2}$ ✅', parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron - iron}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать железо"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
            iron = int(iron[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 230000
            price2 = '{:,}'.format(price)

            if quantity > iron:
                await bot.send_message(message.chat.id, f'{name}, у вас нет железа {rloser}', parse_mode='html')
            if quantity <= iron:
                await bot.send_message(message.chat.id, f'вы продали {quantity} железо за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать железо"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
            iron = int(iron[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 230000
            price2 = '{:,}'.format(price)

            if quantity > iron:
                await bot.send_message(message.chat.id, f'{name}, у вас нет железа {rloser}', parse_mode='html')
            if quantity <= iron:
                await bot.send_message(message.chat.id, f'вы продали {quantity} железо за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.lower() in ['копать плазму', 'Копать плазму']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            plasma = cursor.execute("SELECT plasma from mine where user_id = ?", (message.from_user.id,)).fetchone()
            plasma = int(plasma[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(10, 50)
            rx2 = random.randint(10, 40)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 100000:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} плазмы.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET plasma = {plasma + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать плазму вам требуется 500.000 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать материю', 'Копать материю']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            matter = cursor.execute("SELECT matter from mine where user_id = ?", (message.from_user.id,)).fetchone()
            matter = int(matter[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(10, 50)
            rx2 = random.randint(10, 40)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 100000:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} материи.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET matter = {matter + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать материю вам требуется 100.000 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать изумруды', 'Копать изумруды']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            emeralds = cursor.execute("SELECT emeralds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            emeralds = int(emeralds[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(10, 50)
            rx2 = random.randint(10, 40)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 60000:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} изумрудов.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET emeralds = {emeralds + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать изумруды вам требуется 60.000 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать аквамарин', 'Копать аквамарин']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            aquamarine = cursor.execute("SELECT aquamarine from mine where user_id = ?",
                                        (message.from_user.id,)).fetchone()
            aquamarine = int(aquamarine[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(10, 50)
            rx2 = random.randint(10, 40)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 25000:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} аквамаринов.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET aquamarine = {aquamarine + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать аквамарин вам требуется 25.000 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать аметисты', 'Копать аметисты']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            amethysts = cursor.execute("SELECT amethysts from mine where user_id = ?",
                                       (message.from_user.id,)).fetchone()
            amethysts = int(amethysts[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(10, 50)
            rx2 = random.randint(10, 40)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 10000:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} аметистов.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET amethysts = {amethysts + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать аметисты вам требуется 10.000 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать алмазы', 'Копать алмазы']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            diamonds = cursor.execute("SELECT diamonds from mine where user_id = ?", (message.from_user.id,)).fetchone()
            diamonds = int(diamonds[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(20, 65)
            rx2 = random.randint(10, 40)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 2000:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} алмазов.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET diamonds = {diamonds + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать алмазы вам требуется 2.000 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать золото', 'Копать золото']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
            gold = int(gold[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(15, 60)
            rx2 = random.randint(5, 30)

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')
            if energy >= 1:
                if expe >= 500:
                    await bot.send_message(message.chat.id,
                                           f'{name}, +{rx} золото.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE mine SET gold = {gold + rx}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await bot.send_message(message.chat.id,
                                           f'{name}, чтобы копать золото вам требуется 500 опыта {rloser}',
                                           parse_mode='html')
        if message.text.lower() in ['копать железо', 'Копать железо']:

            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
            iron = int(iron[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(25, 75)
            rx2 = random.randint(1, 25)

            if energy >= 1:
                await bot.send_message(message.chat.id, f'{name}, +{rx} железо.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron + rx}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                connect.commit()

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')

        if message.text.lower() in ['Шахта', "шахта"]:
            name = message.from_user.get_mention(as_html=True)
            await bot.send_message(message.chat.id, f'''{name}, это шахта. Здесь вы сможете добыть ресурсы для дальнейшей продажи. На шахте можно добыть - железо, золото, алмазы, аметисты, материю. Чтобы копать вам понадобиться энергия.
    
     ✅ Как начать работать и добывать ресурсы?
    Используйте команды «копать железо», «копать золото», «копать алмазы», «копать аметисты», «копать аквамарин», «копать изумруды», «копать материю», «копать плазму».
    
    ♻️ Как продавать ресурсы?
    Используйте команды «продать железо», «продать золото», «продать алмазы», «продать аметисты», «продать аквамарин», «продать изумруды», «продать материю», «продать плазму»
    
    📜 Как посмотреть свою статистику?
    Используйте команду "Моя шахта", вы сможете просмотреть ваш опыт, сколько не хватает до следующего уровня, а также какая следующая стадия.''',
                                   parse_mode='html')
        ########################################ФЕРМА####################################################
        if message.text.lower() == 'продать лён':
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
            linen = int(linen[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = linen * 43300000
            price2 = '{:,}'.format(price)

            if 0 == linen:
                await bot.send_message(message.chat.id, f'{name}, у вас нет лён {rloser}', parse_mode='html')
            if 1 <= linen:
                await bot.send_message(message.chat.id, f'вы продали {linen} лёна за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET linen = {linen - linen}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.lower() == 'продать хлопок':
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
            cotton = int(cotton[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            price = cotton * 23300000
            price2 = '{:,}'.format(price)

            if 0 == cotton:
                await bot.send_message(message.chat.id, f'{name}, у вас нет хлопка {rloser}', parse_mode='html')
            if 1 <= cotton:
                await bot.send_message(message.chat.id, f'вы продали {cotton} хлопка за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET cotton = {cotton - cotton}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать хлопок"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
            cotton = int(cotton[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 23300000
            price2 = '{:,}'.format(price)

            if quantity > cotton:
                await bot.send_message(message.chat.id, f'{name}, у вас нет хлопка {rloser}', parse_mode='html')
            if quantity <= cotton:
                await bot.send_message(message.chat.id, f'вы продали {quantity} хлопка за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET cotton = {cotton - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()

        if message.text.startswith("Продать хлопок"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
            cotton = int(cotton[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 23300000
            price2 = '{:,}'.format(price)

            if quantity > cotton:
                await bot.send_message(message.chat.id, f'{name}, у вас нет хлопка {rloser}', parse_mode='html')
            if quantity <= cotton:
                await bot.send_message(message.chat.id, f'вы продали {quantity} хлопка за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET cotton = {cotton - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("продать лён"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
            linen = int(linen[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 43300000
            price2 = '{:,}'.format(price)

            if quantity > linen:
                await bot.send_message(message.chat.id, f'{name}, у вас нет лёна {rloser}', parse_mode='html')
            if quantity <= linen:
                await bot.send_message(message.chat.id, f'вы продали {quantity} лёна за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET linen = {linen - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.startswith("Продать лён"):
            user_id = message.from_user.id
            name = message.from_user.get_mention(as_html=True)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
            linen = int(linen[0])

            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])

            quantity = int(message.text.split()[2])

            price = quantity * 43300000
            price2 = '{:,}'.format(price)

            if quantity > linen:
                await bot.send_message(message.chat.id, f'{name}, у вас нет лёна {rloser}', parse_mode='html')
            if quantity <= linen:
                await bot.send_message(message.chat.id, f'вы продали {quantity} лёна за {price2}$ ✅',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET linen = {linen - quantity}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + price}  WHERE user_id = "{user_id}"')
                connect.commit()
        if message.text.lower() == 'собрать хлопок':
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
            cotton = int(cotton[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(10, 15)
            rx2 = random.randint(1, 25)

            if energy >= 1:
                await bot.send_message(message.chat.id,
                                       f'{name}, +{rx} хлопка 🌿.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET cotton = {cotton + rx}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                connect.commit()

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')

        if message.text.lower() == 'собрать лён':
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])
            energy2 = energy - 1

            linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
            linen = int(linen[0])

            expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
            expe = int(expe[0])
            rx2 = random.randint(1, 25)
            expe2 = expe + rx2
            expe3 = '{:,}'.format(expe2)

            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            rx = random.randint(1, 5)
            rx2 = random.randint(1, 25)

            if energy >= 1:
                await bot.send_message(message.chat.id, f'{name}, +{rx} лёна🍃.\n💡 Энергия: {energy2}, опыт: {expe3}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE farm SET linen = {linen + rx}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET energy = {energy2}  WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET expe = {expe2}  WHERE user_id = "{user_id}"')
                connect.commit()

            if energy <= 0:
                await  bot.send_message(message.chat.id, f'{name}, у вас закончилась энергия {rloser}',
                                        parse_mode='html')

        if message.text.lower() == 'ферма':
            name = message.from_user.get_mention(as_html=True)

            await bot.send_message(message.chat.id, f'''
{name}, это ферма. Здесь вы сможете добыть ресурсы для дальнейшей продажи. На ферме можно добыть - лён🍃 , хлопок🌿. Чтобы копать вам понадобиться энергия.

✅ Как начать работать и добывать ресурсы?
Используйте команды «собрать лён», «собрать хлопок».

♻️ Как продавать ресурсы?
Используйте команды «продать лён», «продать хлопок».

Наш telegram канал с обновлениями - В разработке
''', parse_mode='html')

        ######################################Энергия####################################################
        if message.text.lower() in ['Энергия', "энергия", "енергия", "Енергия"]:
            name = message.from_user.get_mention(as_html=True)
            user_id = message.from_user.id

            energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
            energy = int(energy[0])

            period = 30
            get = cursor.execute("SELECT energy FROM energy WHERE user_id = ?",
                                 (message.from_user.id,)).fetchone()
            energy = f"{int(get[0])}"
            energytime = time.time() - float(energy)
            if enegry > period:
            	if int(rx) in range(0, 10):
            		await bot.send_message(message.chat.id, f'{name}, на данный момент у тебя {energy} ⚡️', parse_mode='html')

       ###########################################АДМИН############################################
        if message.text.lower() in ["админ", "Админ"]:
            help = InlineKeyboardMarkup(row_width=2)
            admin = InlineKeyboardButton(text='💡 Админ-команды', callback_data='admin')
            help.add(admin)
            name1 = message.from_user.get_mention(as_html=True)
            await bot.send_message(message.chat.id,
                                   f'{name1}, выбери категорию:\n   🟢Админ-команды',                  
                                   reply_markup=help, parse_mode='html')
        ###########################################ПОМОЩЬ###########################################
        if message.text.lower() in ["помощь", "Помощь"]:
            help = InlineKeyboardMarkup(row_width=2)
            main = InlineKeyboardButton(text='💡 Основные Команды', callback_data='main')
            games = InlineKeyboardButton(text='🎲 Игры', callback_data='games')
            entertainment = InlineKeyboardButton(text='💥 Развлекательное', callback_data='entertainment')
            #clan = InlineKeyboardButton(text='🏰 Кланы (В разработке...)', callback_data='clan')
            moderatia = InlineKeyboardButton(text='🛠Модерация чата', callback_data='moderatia')
            donat = InlineKeyboardButton(text='💸Донат', callback_data='donat')
            help.add(main, games, entertainment, moderatia, donat)
            name1 = message.from_user.get_mention(as_html=True)
            await bot.send_message(message.chat.id,
                                   f'{name1}, выберите категорию:\n   1️⃣ Основное\n   2️⃣ Игры\n   3️⃣ Развлекательное\n    5️⃣Модерация чата\n   6️⃣Донат\n\n💬 Так же у нас есть канал с обновлениями - В разработке\n🆘 По всем вопросам - @ficus1_1',                  
                                   reply_markup=help, parse_mode='html')

######################шанс казино#########################
        if message.text.lower() in ['казино шансы', "Казино шансы"]:
            name = message.from_user.get_mention(as_html=True)
            await bot.send_message(message.chat.id, f''' {name}, шансы казино💭
Шансы проигрыша:
⚖️ х0 - 30%
⚖️ х0.25 - 33%
⚖️ х0.3 - 34%
⚖️ х0.5 - 34%
⚖️ х0.75 - 37%

Шансы выигрыша:
⚖️ х1 - 36%
⚖️ х1.25 - 37%
⚖️ х1.5 - 34%
⚖️ х2 - 30%
⚖️ х5 - 20%
⚖️ х10 - 10%''',
                                   parse_mode='html')
        ###########################################СПИН#############################################
        if message.text.startswith("спин"):
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            balance2 = '{:,}'.format(balance)
            msg = message
            user_id = msg.from_user.id
            chat_id = message.chat.id
            rx = random.randint(0, 110)
            msg = message
            name1 = message.from_user.get_mention(as_html=True)
            name = msg.from_user.last_name
            summ = int(msg.text.split()[1])
            print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            period = 5
            getе = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
            last_stavka = f"{int(getе[0])}"
            stavkatime = time.time() - float(last_stavka)
            loz = ['💩|👑|👑', '💩|🖕|👑', '💎|🖕|👑', '💎|💣|🍌', '👑|🍌|🖕', '💎|🍓|💣']
            win = ['💎|🍓|🍌', '👑|💎|🍓', '🍓|👑|💎', '💎|🍓|🍌', '💎|🍓|🍓', '🍌|🍌|💎']
            Twin = ['💎|💎|💎', '🍓|🍓|🍓', '👑|👑|👑', '🍌|🍌|🍌']
            smtwin = ['🤯', '🤩', '😵', '🙀']
            smwin = ['🙂', '😋', '😄', '🤑', '😃']
            loser = ['😔', '😕', '😣', '😞', '😢']
            rsmtwin = random.choice(smtwin)
            rsmtwin2 = random.choice(smtwin)
            rtwin = random.choice(Twin)
            rloser = random.choice(loser)
            rloser2 = random.choice(loser)
            rwin = random.choice(win)
            rloz = random.choice(loz)
            rsmwin = random.choice(smwin)
            rsmwin2 = random.choice(smwin)
            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                balance2 = '{:,}'.format(balance)
            if stavkatime > period:
                if balance >= summ:
                    if summ > 0:
                        if int(rx) in range(0, 30):
                            c = Decimal(summ * 2)
                            c2 = round(c)
                            c2 = '{:,}'.format(c2)
                            await bot.send_message(chat_id,
                                                   f'{name1}, вот ваши результаты\n——————\n{rwin} - вы выиграли {c2}${rsmwin}',
                                                   parse_mode='html')
                            cursor.execute(
                                f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                            connect.commit()
                            return

            if stavkatime > period:
                if balance >= summ:
                    if summ > 0:
                        if int(rx) in range(35, 100):
                            c = Decimal(summ * 0)
                            c2 = round(c)
                            c2 = '{:,}'.format(c2)
                            await bot.send_message(chat_id,
                                                   f'{name1}, вот ваши результаты\n——————\n{rloz} - вы проиграли {c2}${rloser}',
                                                   parse_mode='html')
                            cursor.execute(
                                f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                            connect.commit()
                            return
            if stavkatime > period:
                if balance >= summ:
                    if summ > 0:
                        if int(rx) in range(101, 104):
                            c = Decimal(summ * 25)
                            c2 = round(c)
                            c2 = '{:,}'.format(c2)
                            await bot.send_message(chat_id,
                                                   f'{name1}, вот ваши результаты\n——————\n{rtwin} - ДЖЕКПОТ, ВЫ ВЫИГРАЛИ {c2}${rsmtwin}',
                                                   parse_mode='html')
                            cursor.execute(
                                f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                            connect.commit()
                            return
                    elif summ <= 1:
                        await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                               parse_mode='html')
                elif int(balance) <= int(summ):
                    await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
            else:
                await bot.send_message(chat_id, f'{name1}, играть можно каждые 5 секунд.Подожди немного. {rloser}',
                                       parse_mode='html')
                return
        if message.text.startswith("Спин"):
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            balance2 = '{:,}'.format(balance)
            msg = message
            user_id = msg.from_user.id
            chat_id = message.chat.id
            rx = random.randint(0, 110)
            msg = message
            name1 = message.from_user.get_mention(as_html=True)
            name = msg.from_user.last_name
            summ = int(msg.text.split()[1])
            print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            period = 5
            get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            loz = ['💩|👑|👑', '💩|🖕|👑', '💎|🖕|👑', '💎|💣|🍌', '👑|🍌|🖕', '💎|🍓|💣']
            win = ['💎|🍓|🍌', '👑|💎|🍓', '🍓|👑|💎', '💎|🍓|🍌', '💎|🍓|🍓', '🍌|🍌|💎']
            Twin = ['💎|💎|💎', '🍓|🍓|🍓', '👑|👑|👑', '🍌|🍌|🍌']
            smtwin = ['🤯', '🤩', '😵', '🙀']
            smwin = ['🙂', '😋', '😄', '🤑', '😃']
            loser = ['😔', '😕', '😣', '😞', '😢']
            rsmtwin = random.choice(smtwin)
            rsmtwin2 = random.choice(smtwin)
            rtwin = random.choice(Twin)
            rloser = random.choice(loser)
            rloser2 = random.choice(loser)
            rwin = random.choice(win)
            rloz = random.choice(loz)
            rsmwin = random.choice(smwin)
            rsmwin2 = random.choice(smwin)
            if balance >= 999999999999999999999999:
                balance = 999999999999999999999999
                cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
                connect.commit()
                balance2 = '{:,}'.format(balance)
            if stavkatime > period:
                if balance >= summ:
                    if summ > 0:
                        if int(rx) in range(0, 30):
                            c = Decimal(summ * 2)
                            c2 = round(c)
                            c2 = '{:,}'.format(c2)
                            await bot.send_message(chat_id,
                                                   f'{name1}, вот ваши результаты\n——————\n{rwin} - вы выиграли {c2}${rsmwin}',
                                                   parse_mode='html')
                            cursor.execute(
                                f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                            connect.commit()
                            return

                        if int(rx) in range(35, 100):
                            c = Decimal(summ * 0)
                            c2 = round(c)
                            c2 = '{:,}'.format(c2)
                            await bot.send_message(chat_id,
                                                   f'{name1}, вот ваши результаты\n——————\n{rloz} - вы проиграли {c2}${rloser}',
                                                   parse_mode='html')
                            cursor.execute(
                                f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                            connect.commit()
                            return

                        if int(rx) in range(101, 104):
                            c = Decimal(summ * 25)
                            c2 = round(c)
                            c2 = '{:,}'.format(c2)
                            await bot.send_message(chat_id,
                                                   f'{name1}, вот ваши результаты\n——————\n{rtwin} - ДЖЕКПОТ, ВЫ ВЫИГРАЛИ {c2}${rsmtwin}\n——————\nПОЗДРАВЛЯЮ У ВАС ДЖЕКПОТ!{rsmtwin2}',
                                                   parse_mode='html')
                            cursor.execute(
                                f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                            cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                            connect.commit()
                            return
                    elif summ <= 1:
                        await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                               parse_mode='html')
                elif int(balance) <= int(summ):
                    await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
            else:
                await bot.send_message(chat_id, f'{name1}, играть можно каждые 5 секунд.Подожди немного. {rloser}',
                                       parse_mode='html')
                return
  
              ###########################################КАЗИНО###########################################

        ###########################################РЕЙТИНГ###########################################
        if message.text.lower() in ["рейтинг", "Рейтинг"]:
            msg = message
            name1 = message.from_user.get_mention(as_html=True)

            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = int(rating[0])
            rating2 = '{:,}'.format(rating)

            await bot.send_message(message.chat.id, f'{name1}, ваш рейтинг {rating2}👑', parse_mode='html')

        if message.text.startswith("Купить рейтинг"):
            msg = message
            user_id = msg.from_user.id
            chat_id = message.chat.id
            user_name = message.from_user.get_mention(as_html=True)
            summ = int(msg.text.split()[2])
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = int(rating[0])
            rating2 = '{:,}'.format(summ)
            c = summ * 150000000
            c2 = '{:,}'.format(c)
            if summ > 0:
                if int(balance) >= int(summ * 150000000):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
                    connect.commit()

                if int(balance) < int(summ * 150000000):
                    await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                           parse_mode='html')

            if summ <= 0:
                await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                       parse_mode='html')

        if message.text.startswith("Продать рейтинг"):
            msg = message
            user_id = msg.from_user.id
            chat_id = message.chat.id
            user_name = message.from_user.get_mention(as_html=True)
            summ = int(msg.text.split()[2])
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = int(rating[0])
            c = summ * 100000000
            c2 = '{:,}'.format(c)
            rating2 = '{:,}'.format(summ)
            if summ > 0:
                if int(rating) >= int(summ):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
                    connect.commit()

                if int(rating) < int(summ):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, у вас недостаточно рейтинга для его продажи! {rloser}',
                                           parse_mode='html')

            if summ <= 0:
                await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}',
                                       parse_mode='html')

        if message.text.startswith("купить рейтинг"):
            msg = message
            user_id = msg.from_user.id
            user_name = message.from_user.get_mention(as_html=True)
            summ = int(msg.text.split()[2])
            chat_id = message.chat.id
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = int(rating[0])
            rating2 = '{:,}'.format(summ)
            c = summ * 150000000
            c2 = '{:,}'.format(c)
            if summ > 0:
                if int(balance) >= int(summ * 150000000):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
                    connect.commit()

                if int(balance) < int(summ * 150000000):
                    await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                           parse_mode='html')

            if summ <= 0:
                await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}',
                                       parse_mode='html')

        if message.text.startswith("продать рейтинг"):
            msg = message
            user_id = msg.from_user.id
            chat_id = message.chat.id
            user_name = message.from_user.get_mention(as_html=True)
            summ = int(msg.text.split()[2])
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = int(balance[0])
            rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
            rating = int(rating[0])
            c = summ * 100000000
            c2 = '{:,}'.format(c)
            rating2 = '{:,}'.format(summ)
            if summ > 0:
                if int(rating) >= int(summ):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}',
                                           parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
                    connect.commit()

                if int(rating) < int(summ):
                    await bot.send_message(message.chat.id,
                                           f'{user_name}, у вас недостаточно рейтинга для его продажи! {rloser}',
                                           parse_mode='html')

            if summ <= 0:
                await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}',
                                       parse_mode='html')

        ###########################################ПЕРЕВОДЫ###########################################
        if message.text.startswith("передать"):
            msg = message
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            rname = msg.reply_to_message.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            reply_user_id = msg.reply_to_message.from_user.id
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            perevod = int(msg.text.split()[1])
            perevod2 = '{:,}'.format(perevod)
            print(f"{user_name},вы передали {perevod}$ игроку{rname}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])

            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return

            if reply_user_id == user_id:
                await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}',
                                                     parse_mode='html')
                return

            if perevod > 0:
                if balance >= perevod:
                    await message.reply_to_message.reply(f'{user_name},вы передали {perevod2}$ игроку - {reply_user_name} {rwin}',
                                                         parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                    connect.commit()

                elif int(balance) <= int(perevod):
                    await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

            if perevod <= 0:
                await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

        if message.text.startswith("Передать"):
            msg = message
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            rname = msg.reply_to_message.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            reply_user_id = msg.reply_to_message.from_user.id
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            perevod = int(msg.text.split()[1])
            perevod2 = '{:,}'.format(perevod)
            print(f"{user_name},вы передали {perevod}$ игроку - {rname}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])

            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return

            if reply_user_id == user_id:
                await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}',
                                                     parse_mode='html')
                return

            if perevod > 0:
                if balance >= perevod:
                    await message.reply_to_message.reply(f'{user_name},вы передали {perevod2}$ игроку - {reply_user_name} {rwin}',
                                                         parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                    connect.commit()

                elif int(balance) <= int(perevod):
                    await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

            if perevod <= 0:
                await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

        if message.text.startswith("дать"):
            msg = message
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            rname = msg.reply_to_message.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            reply_user_id = msg.reply_to_message.from_user.id
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            perevod = int(msg.text.split()[1])
            perevod2 = '{:,}'.format(perevod)
            print(f"{user_name},вы передали {perevod}$ игроку{rname}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])

            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return

            if reply_user_id == user_id:
                await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}',
                                                     parse_mode='html')
                return

            if perevod > 0:
                if balance >= perevod:
                    await message.reply_to_message.reply(f'{user_name},вы передали {perevod2}$ игроку - {reply_user_name} {rwin}',
                                                         parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                    connect.commit()

                elif int(balance) <= int(perevod):
                    await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

            if perevod <= 0:
                await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

        if message.text.startswith("Дать"):
            msg = message
            user_id = msg.from_user.id
            name = msg.from_user.last_name
            rname = msg.reply_to_message.from_user.last_name
            user_name = message.from_user.get_mention(as_html=True)
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            reply_user_id = msg.reply_to_message.from_user.id
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)

            perevod = int(msg.text.split()[1])
            perevod2 = '{:,}'.format(perevod)
            print(f"{user_name},вы передали {perevod}$ игроку - {rname}")

            cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
            balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
            balance = round(int(balance[0]))
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])

            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return

            if reply_user_id == user_id:
                await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}',
                                                     parse_mode='html')
                return

            if perevod > 0:
                if balance >= perevod:
                    await message.reply_to_message.reply(f'{user_name},вы передали {perevod2}$ игроку - {reply_user_name} {rwin}',
                                                         parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                    connect.commit()

                elif int(balance) <= int(perevod):
                    await message.reply(f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

            if perevod <= 0:
                await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

            ###########################################ТОП###########################################
        if message.text.lower() in ["топ", "Топ"]:
            list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
            top_list = []
            chat_id = message.chat.id
            name = message.from_user.get_mention(as_html=True)
            num = 0
            for user in list:
                if user[14] >= 999999999999999999999999:
                    c6 = 999999999999999999999999
                else:
                    c6 = user[14]

                if int(user[3]) < 0:
                    balance3 = 0
                if int(user[3]) in range(1000, 999999):
                    balance1 = user[3] / 1000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} тыс'

                if int(user[3]) in range(1000000, 999999999):
                    balance1 = user[3] / 1000000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} млн'

                if int(user[3]) in range(1000000000, 999999999999):
                    balance1 = user[3] / 1000000000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} млрд'

                if int(user[3]) in range(1000000000000, 999999999999999):
                    balance1 = user[3] / 1000000000000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} трлн'

                if int(user[3]) in range(1000000000000000, 999999999999999999):
                    balance1 = user[3] / 1000000000000000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} квдр'

                if int(user[3]) in range(1000000000000000000, 999999999999999999999):
                    balance1 = user[3] / 1000000000000000000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} квнт'

                if int(user[3]) in range(1000000000000000000000, 999999999999999999999999):
                    balance1 = user[3] / 1000000000000000000000
                    balance2 = round(balance1)
                    balance3 = f'{balance2} скст'
                
                num += 1

                c = Decimal(c6)
                c2 = '{:,}'.format(c)

                top_list.append(f"[{num}]. {user[11]}  — 👑{c2} | ${balance3}")
            top = "\n".join(top_list)
            await bot.send_message(message.chat.id, f"{name}, топ 10 игроков бота:\n" + top, parse_mode='html')
    else:
        await bot.send_message(message.chat.id,
                               f'{name}, вы находитесь в чс проекта,для разбана своего аккаунта обратитесь к разработчику бота👨‍🦰',
                               parse_mode='html')



@dp.callback_query_handler(text='main')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer(f'''
   👑 Рейтинг
   👑 Продать рейтинг
   ⚡️  Энергия
   ⛏ Шахта
   🌾 Ферма
   🚗 Машины
   📱 Телефоны
   ✈️ Самолёты
   🛥  Яхты
   🚁 Вертолёты
   🏠 Дома
   💸 Б/Баланс
   📦 Инвентарь
   📊 Курс руды
   🏢 Ограбить казну
   💰 Банк положить [сумма]
   💰 Банк снять [сумма]
   🤝  Передать [сумма] [ID Игрока]
   🤝  Дать [сумма] [ID Игрока]
   🌐 Биткоин курс
   🌐 Биткоин купить [кол-во]
   🌐 Биткоин продать [кол-во]
   ⚱️  Биткоины
   💈  Ежедневный бонус
   💷 Казна
   💢 Сменить ник [новый ник]
   👨 Мой ник - узнать ник
   ⚖️ РП Команды - узнать РП команды
   💭 !Беседа - беседа бота''', 
     parse_mode='html')


@dp.callback_query_handler(text='games')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer('''
   🎮 Спин [ставка]
   🎰 Казино [ставка]''')


@dp.callback_query_handler(text='entertainment')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer('''
    🔋 Купить энергию [количество]
    
    🏢Центр занятости
        🖊  Устроиться [Номер]
        📈 Работать 
        📉 Уволиться
        📑 Вакансии

    🐶 Питомцы
        ✏️ Питомец имя [имя]
        ❤️ Вылечить питомца
        🍗 Покормить питомца
        🌳 Выгулять питомца
        🐶 Мой питомец - узнать о своём питомце

   🔮 Шар [фраза]
   💬 Выбери [фраза] или [фраза2]
   📈 Шанс [фраза]
   🚀 Игра
    ''')


@dp.callback_query_handler(text='clan')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer('😕 На данный момент \'Кланы\' в разработке.')


@dp.callback_query_handler(text='moderatia')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer('''
        🔴  .бан
   🟢  .разбан
   🔇 .мут [время]
   🔊 .размут
   👮‍♀️/report [сообщение]
   ♨️Все команды модериции работают ответом на сообщение!
    ''')


@dp.callback_query_handler(text='donat')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer('''
   🆙Список доступного доната
         1️⃣ Admin status
         2️⃣ Игровая валюта
         3️⃣Префиксы
         4️⃣Скины
   🔹Для покупки доната обращайтесь к создателю бота - @ficus1_1 (Автовыдача в разработке)

    ''')


@dp.callback_query_handler(text='admin')
async def inlinebutton(callback: types.CallbackQuery):
    await callback.message.answer('''
   ⚠️ Команды создателя⤵️
   🏧 Выдать админ
   🏧 Забрать админ

   ⚠️Команды админа⤵️
   🌀Обнулить - обнуление баланса игрока
   ♻️Выдать - выдача денег игроку
   ♻️Забрать - забрать деньги у игрока
   ❓Инфо - узнать профиль игрока
   🟥ban - чс проекта игроку
   🟩unban - снять чс проекта игроку
   📊Статистика бота - посмотреть статистику бота
    ''')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
