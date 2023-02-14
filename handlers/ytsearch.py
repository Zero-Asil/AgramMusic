# the logging things
import logging

from agram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from agram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import agram

logging.getLogger("agram").setLevel(logging.WARNING)

@app.on_message(agram.filters.command(["search"]))
async def ytsearch(_, message: Message):
    await message.delete()
    try:
        if len(message.command) < 2:
            await message.reply_text(" Give some text to search!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"📌 Title : {results[i]['title']}\n"
            text += f"⏱ duration : {results[i]['duration']}\n"
            text += f"👀 views : {results[i]['views']}\n"
            text += f"📣 channel : {results[i]['channel']}\n"
            text += f"🔗 link : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
