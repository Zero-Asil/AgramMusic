import re
import sys
import time
from config import (API_ID, API_HASH, BOT_TOKEN)

from agram import Client

StartTime = time.time()

app = Client(
    "agramMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)
