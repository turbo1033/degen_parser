from telethon import TelegramClient, events
import asyncio
import random

API_ID = '21624015'  # Получи API ID на https://my.telegram.org
API_HASH = '965bafa712ca522dd5888af4e9679887'  # Получи API HASH на https://my.telegram.org
PHONE_NUMBER = '+6281213953112'  # Ваш номер телефона в формате +1234567890

degen_CHANNELS = [-1001608851478, -1001774085954, -1002415859616, -1001251782083,
              -1001230726405, -1001956398204, -1001965634796, -1001576457836,
              -1002125969105, -1001828950564, -1001866386442, -1001590515612,
              -1001681492663, -1001275381155, -1002000591951, -1001397814771
              -1001730573347, -1001373928880, -1001625535630, -1001877593793]

shitpost_channels = [-1002116976604, -1001192195592, -1002249169983, -1001700361896,
                     -1001950573084, -1002141098158, -1002005254569, -1002064164863, -1002250659480]

ALL_CHANNELS = degen_CHANNELS + shitpost_channels
print(ALL_CHANNELS)

# Целевые каналы для пересылки сообщений
TARGET_CHANNEL_1 = '@degen_prs'
TARGET_CHANNEL_2 = '@shitposter_prs'


client = TelegramClient("session_name", API_ID, API_HASH)

@client.on(events.NewMessage(chats=ALL_CHANNELS))
async def handler(event):
    chat_username = event.chat.username
    chat_id = event.chat_id
    target_chat = ''
    message = ''

    if chat_id in degen_CHANNELS or chat_username in degen_CHANNELS:
        target_chat = TARGET_CHANNEL_1
        message = event.message
    elif chat_id in shitpost_channels or chat_username in shitpost_channels:
        target_chat = TARGET_CHANNEL_2
        message = event.message

    await asyncio.sleep(random.uniform(1, 3))  # Имитируем задержку
    await client.forward_messages(target_chat, message)

async def main():
    await client.start(phone=PHONE_NUMBER)
    print("Бот запущен и слушает каналы...")
    await asyncio.Event().wait()

with client:
    client.loop.run_until_complete(main())


