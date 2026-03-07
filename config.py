import os


class Config:
    CLIENT_ID = os.environ.get("ML_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("ML_CLIENT_SECRET")
    SECRET_KEY = os.environ.get("FORM_SECRET")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
