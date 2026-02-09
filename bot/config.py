import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
OOS_ALERT_THRESHOLD = float(os.getenv('OOS_ALERT_THRESHOLD', 0.15))