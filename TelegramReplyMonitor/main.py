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

group = 'testovayasssss'
message_id = 4

@client.on(events.NewMessage(chats=group))
async def forward_thread(event):
    if event.message.is_reply:
        if event.message.reply_to_msg_id == message_id:
            await client.send_message('me', f"Новый ответ: {event.message.text}")

# =========================
# Keep-Alive через Flask
# =========================
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

Thread(target=run_flask).start()

# =========================
# Запуск Telethon
# =========================
client.start(phone)
client.run_until_disconnected()
