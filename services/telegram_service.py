import requests
from config import Config


def send_telegram(message):
    url = f"https://api.telegram.org/bot{Config.TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": Config.CHAT_ID, "text": message}
    requests.post(url, json=payload, timeout=5)


def send_photo(photo_url):
    url = f"https://api.telegram.org/bot{Config.TELEGRAM_TOKEN}/sendPhoto"
    payload = {"chat_id": Config.CHAT_ID, "photo": photo_url}
    requests.post(url, json=payload, timeout=5)
