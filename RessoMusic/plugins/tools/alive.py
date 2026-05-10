from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import MUSIC_BOT_NAME
from RessoMusic import app


@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    bot = await app.get_me()

    # User clickable mention
    user_mention = message.from_user.mention

    # Bot clickable mention
    bot_mention = f"<a href='https://t.me/{bot.username}'>{bot.first_name}</a>"

    await message.reply_video(
        video="https://files.catbox.moe/l8duqz.jpg",

        caption=f"""❤️ ʜᴇʏ {user_mention}\n\n🤖 ɪ ᴀᴍ {bot_mention}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🤍
""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="☆ 𝐎ᴡɴᴇʀ ☆",
                        url="https://t.me/II_NOBITA_DEFAULTERS_II"
                    ),

                    InlineKeyboardButton(
                        text="☆ 𝐒ᴜᴘᴘᴏʀᴛ ☆",
                        url="https://t.me/+S0Q1-J_EQLA3YmU1"
                    ),
                ],

                [
                    InlineKeyboardButton(
                        text="☆ 𝐔ᴘᴅᴀᴛᴇ ☆",
                        url="https://t.me/NOBITA_SUPP0RT"
                    ),

                    InlineKeyboardButton(
                        text="★ 𝐂ʟᴏsᴇ ★",
                        callback_data="close"
                    ),
                ]
            ]
        ),

        parse_mode=enums.ParseMode.HTML
    )
