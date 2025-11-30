import os
import requests
from telethon import TelegramClient, events

# Pega configurações das Variáveis de Ambiente do Easypanel
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
# Importante: A sessão será salva na pasta /data para persistência
session_name = '/data/userbot_session' 
webhook_url = os.getenv('WEBHOOK_URL')

# Seus canais alvo (pode ser via env também se quiser ser chique)
target_channels = [-100123456789] 

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=target_channels))
async def handler(event):
    try:
        payload = {
            "text": event.message.message,
            "chat_id": event.chat_id,
            "link": f"https://t.me/c/{str(event.chat_id)[4:]}/{event.message.id}" # Tenta gerar link
        }
        # Timeout curto para não travar o bot se o n8n demorar
        requests.post(webhook_url, json=payload, timeout=5)
    except Exception as e:
        print(f"Erro: {e}")

print("Iniciando Monitoramento...")
client.start()
client.run_until_disconnected()