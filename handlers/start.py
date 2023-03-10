import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from agram import Client, filters
from agram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZp7eIAACpv1jYIbWhI9JPBkvLLSLwPxc-8yu2QACDgcAAruXGFbarx8_grqJYh4E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()}Β , π₯\n\n
ΰΉ This is [{bn}](t.me/{bu}) ,Β  !
β» The most Powerful telegram music  bot with some awesome and useful features.

ββββββββββββββββββ
ΰΉ  All of my command can be used with My command handle : ( / . β’ $ ^ ~ + * ? )
β» Made π€ by : [πππ¬π₯](https://t.me/{me}) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βΒ AddΒ meΒ toΒ yourΒ Group", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "π¨ Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "π¨ Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "π€ Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "π¨βπ» Developer ", url=f"https://t.me/export_gabbar"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "β Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "π‘ Git repo", url="https://github.com/MrProgrammer72/GJ516VCBOT"
                    )]
            ]
       ),
    )
