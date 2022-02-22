from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot

UPDATES_CHANNEL = 'Discovery_Updates'
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    ## Doing Force Sub 🤣
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                   chat_id=m.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Developer/Owner](https://t.me/jettastic).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="Something went Wrong. Contact my [Developer/Owner](https://t.me/jettastic).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    ##
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"#PING_SS: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started!"
        )
    
    await m.reply_text(
        text=f"Hi, [{m.from_user.first_name}](tg://user?id={m.chat.id}).\n\nI'm Vidrox AH Bot. I can provide screenshots from your video files with out downloading the entire file. For more details check /help.",
        parse_mode="markdown",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Updates Channel', url='https://t.me/jetbots'),
                    InlineKeyboardButton('Developer/Owner', url='https://t.me/jettastic')
                ],
                [
                    InlineKeyboardButton('Our Other Bots', url='https://t.me/jetbots/26')
                    InlineKeyboardButton('Leech/Mirror/Encoding Groups', url='https://t.me/jetbots/26')
                ]
            ]
        )
    )
