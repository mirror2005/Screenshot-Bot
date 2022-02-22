from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot

UPDATES_CHANNEL = 'Discovery_Updates'
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

HELP_TEXT = """
Hi {}
This is Vidrox AH Bot. You can use me to generate:

    1. Screenshots.
    2. Sample Video.
    3. Trimmed Video.

👉 I support any kind of **Telegram Video File**. But file should have proper mime-type and shouldn't be a currupted file. 
👉 I also support **Streaming URLs**. The URL should be a Streaming URL, non IP Specific, and should return proper response codes.

**General FAQ:**

👉 If the bot dosen't respond to telegram files you forward, first check /start and confirm bot is alive. Then make sure the file is a **video file** which satisfies above mentioned conditions. 
👉 If bot replies __Sorry! I cannot open the file__, than the file might be currupted or is malformatted.
"""


@ScreenShotBot.on_message(Filters.private & Filters.command("help"))
async def help(c, m):
    ## Doing Force Sub 🤣
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                   chat_id=m.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Channel](https://t.me/jetbots).",
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
                text="Something went Wrong. Contact my [Channel](https://t.me/jetbots).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    ##
    await m.reply_text(
        text=HELP_TEXT.format(m.from_user.first_name),
        quote=True
    )
