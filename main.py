from telethon import TelegramClient, events
import asyncio
import random

API_ID = '21624015'  # Получи API ID на https://my.telegram.org
API_HASH = '965bafa712ca522dd5888af4e9679887'  # Получи API HASH на https://my.telegram.org
PHONE_NUMBER = '+6281213953112'  # Ваш номер телефона в формате +1234567890

# Каналы, которые ты хочешь мониторить
CHANNELS = ['@sol_TOP', '@workIncrypts', '@thecyberomanovsmoment', '@ruslan55richhh',
            '@Last_Trade161', '@miguelrarechannel', '@dchnecrypto', '@ded_blog',
            '@spekulyantcrypto', '@olegnoc4p', '@phtcrypto', '@jungle_chain',
            '@goosebarn', '@CryptoLamer', '@testoviyyyi'
            ]

TARGET_CHANNEL = '@degen_prs'

# Создаём клиент для доступа через личный аккаунт
client = TelegramClient("session_name", API_ID, API_HASH)

# Слушаем сообщения на каналах
@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    message = event.message
    await asyncio.sleep(random.uniform(1, 3))
    await client.forward_messages(TARGET_CHANNEL, message)

# Запуск клиента
async def main():
    await client.start(phone=PHONE_NUMBER)  # Вводим номер при первом запуске
    print("Бот запущен и слушает каналы...")
    await asyncio.Event().wait()

# Запускаем приложение
with client:
    client.loop.run_until_complete(main())


