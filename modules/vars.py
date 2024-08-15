import os

API_ID    = os.environ.get("API_ID", "18156248")
API_HASH  = os.environ.get("API_HASH", "db946fb6805b1a698c679626b617e77a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
