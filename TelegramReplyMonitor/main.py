from telethon import TelegramClient, events
from flask import Flask
from threading import Thread
import os

# =========================
# Настройки Telethon
# =========================
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
phone = os.environ['PHONE']

client = TelegramClient('session', api_id, api_hash)

# Укажи username или ID группы
group = '@testovayasssss'  # можно заменить на -100XXXXXXXXXX

# =========================
# Логируем все сообщения группы
# =========================
@client.on(events.NewMessage(chats=group))
async def handler(event):
    print("Получено сообщение:", event.message.text)  # проверка в логах Render
    await client.send_message('me', f"Из группы: {event.message.text}")  # пересылаем себе

# =========================
# Keep-Alive через Flask
# =========================
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

# =========================
# Запуск Telethon
# =========================
client.start(phone)
client.run_until_disconnected()
