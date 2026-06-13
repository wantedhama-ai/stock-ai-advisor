import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


class TelegramService:

    def send_message(self, text):

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        }

        response = requests.post(url, data=payload)

        print(response.text)  # 디버깅용