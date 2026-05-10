from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import MUSIC_BOT_NAME
from RessoMusic import app


@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    bot = await app.get_me()
    mention = f"[{bot.first_name}](https://t.me/{bot.username})"

    await message.reply_video(
        video="https://files.catbox.moe/l8duqz.jpg",
        caption=f"""❤️ ʜᴇʏ {message.from_user.mention}\n\n🤖 ɪ ᴀᴍ {mention}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴀɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ🤍 ...
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="☆ 𝐎ᴡɴᴇʀ ☆", url="https://t.me/II_NOBITA_DEFAULTERS_II"
                    ),
                    InlineKeyboardButton(
                        text="☆ 𝐒ᴜᴘᴘᴏʀᴛ ☆", url="https://t.me/+S0Q1-J_EQLA3YmU1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="☆ 𝐔ᴘᴅᴀᴛᴇ ☆", url="https://t.me/NOBITA_SUPP0RT"
                    ),
                    InlineKeyboardButton(
                        text="★ 𝐂ʟᴏsᴇ ★", callback_data="close"
                    ),
                ]
            ]
        ),
        parse_mode=enums.ParseMode.MARKDOWN
    )
