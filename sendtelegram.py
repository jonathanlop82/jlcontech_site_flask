import requests

import local_settings

TOKEN = local_settings.TOKEN
chat_id = local_settings.chat_id
def send_telegram_message(message):
    message = message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message
