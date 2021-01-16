from pyrogram import Filters

from ..config import Config
from ..screenshotbot import ScreenShotBot

UPDATES_CHANNEL = 'Discovery_Updates'
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

@ScreenShotBot.on_message(Filters.private &  Filters.command("set_watermark"))
async def _(c, m):
    ## Doing Force Sub 🤣
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                   chat_id=m.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/linux_repo).",
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
                text="Something went Wrong. Contact my [Support Group](https://t.me/linux_repo).",
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
    
    if len(m.command) == 1:
        await m.reply_text(
            text="You can add custom watermark text to the screenshots.\n\nUsage: `/set_watermark text`. Text should not Exceed 30 characters.",
            quote=True,
            parse_mode="markdown"
        )
        return
    
    watermark_text = ' '.join(m.command[1:])
    if len(watermark_text) > 30:
        await m.reply_text(
            text=f"The watermark text you provided (__{watermark_text}__) is `{len(watermark_text)}` characters long! You cannot set watermark text greater than 30 characters.",
            quote=True,
            parse_mode="markdown"
        )
        return
    
    await c.db.update_watermark_text(m.chat.id, watermark_text)
    await m.reply_text(
        text=f"You have successfully set __{watermark_text}__ as your watermark text. From now on this will be applied to your screenshots! To remove watermark text see /settings.",
        quote=True,
        parse_mode="markdown"
    )
