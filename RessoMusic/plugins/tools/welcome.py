from RessoMusic import app
from pyrogram.errors import RPCError
from pyrogram.types import (
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram import filters, enums
from logging import getLogger

LOGGER = getLogger(__name__)


# ------------------------------------------------------------------- #

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]


wlcm = WelDatabase()


class temp:
    MELCOW = {}


# ------------------------------------------------------------------- #
# WELCOME ON / OFF COMMAND
# ------------------------------------------------------------------- #

@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):

    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /welcome [on|off]**"

    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id

    user = await app.get_chat_member(
        message.chat.id,
        message.from_user.id
    )

    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):

        A = await wlcm.find_one(chat_id)

        state = message.text.split(None, 1)[1].strip().lower()

        if state == "off":

            if A:
                await message.reply_text(
                    "**ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !**"
                )

            else:
                await wlcm.add_wlcm(chat_id)

                await message.reply_text(
                    f"**ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}"
                )

        elif state == "on":

            if not A:
                await message.reply_text(
                    "**ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.**"
                )

            else:
                await wlcm.rm_wlcm(chat_id)

                await message.reply_text(
                    f"**ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}"
                )

        else:
            await message.reply_text(usage)

    else:
        await message.reply(
            "**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**"
        )


# ------------------------------------------------------------------- #
# TEXT WELCOME MESSAGE
# ------------------------------------------------------------------- #

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):

    chat_id = member.chat.id

    count = await app.get_chat_members_count(chat_id)

    A = await wlcm.find_one(chat_id)

    if A:
        return

    user = (
        member.new_chat_member.user
        if member.new_chat_member
        else member.from_user
    )

    if (
        member.new_chat_member
        and not member.old_chat_member
        and member.new_chat_member.status != "kicked"
    ):

        if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:

            try:
                await temp.MELCOW[
                    f"welcome-{member.chat.id}"
                ].delete()

            except Exception as e:
                LOGGER.error(e)

        try:

            button_text = "๏ ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ ๏"
            add_button_text = "✙ ᴀᴅᴅ ᴍᴇ ✙"

            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"

            username = (
                f"@{user.username}"
                if user.username
                else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
            )

            temp.MELCOW[
                f"welcome-{member.chat.id}"
            ] = await app.send_message(
                member.chat.id,
                text=f"""
**⎊────☵ ᴡᴇʟᴄᴏᴍᴇ ☵────⎊**

**▬▭▬▭▬▭▬▭▬▭▬▭▬▭**

**☉ ɴᴀᴍᴇ ⧽** {user.mention}
**☉ ɪᴅ ⧽** `{user.id}`
**☉ ᴜsᴇʀɴᴀᴍᴇ ⧽** {username}
**☉ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs ⧽** {count}

❖ ᴍᴀᴅᴇ ʙʏ  ➛ [𝚴 𝐎 𝐁 𝚰 𝐓 𝚲 🜲]

**▬▭▬▭▬▭▬▭▬▭▬▭▬▭**

**⎉────▢✭ 侖 ✭▢────⎉**
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                button_text,
                                url=deep_link
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text=add_button_text,
                                url=add_link
                            )
                        ],
                    ]
                ),
                disable_web_page_preview=True,
            )

        except Exception as e:
            LOGGER.error(e)
