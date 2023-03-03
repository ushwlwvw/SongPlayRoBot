import logging
from pyrogram import Client
from config import ايبي_هاش, ايبي_ايدي, توكن_بوت

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

app = Client("SongPlayRoBot", bot_token=BOT_TOKEN, api_hash=API_HASH, api_id=API_ID)
