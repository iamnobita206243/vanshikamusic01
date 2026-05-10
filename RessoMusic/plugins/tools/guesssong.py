import os
import random
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pydub import AudioSegment

from RessoMusic import app

SONGS_PATH = "songs"
active_games = {}


@app.on_message(filters.command("guesssong"))
async def guess_song(client, message: Message):

    songs = [
        file for file in os.listdir(SONGS_PATH)
        if file.endswith(".mp3")
    ]

    if not songs:
        return await message.reply_text("❌ No songs found.")

    song = random.choice(songs)

    answer = os.path.splitext(song)[0].lower()

    song_path = os.path.join(SONGS_PATH, song)

    audio = AudioSegment.from_file(song_path)

    clip = audio[:10000]

    clip_path = "clip.mp3"

    clip.export(clip_path, format="mp3")

    active_games[message.chat.id] = answer

    await message.reply_audio(
        audio=clip_path,
        caption="🎵 Guess The Song!"
    )

    await asyncio.sleep(15)

    if message.chat.id in active_games:
        del active_games[message.chat.id]

        await message.reply_text(
            f"⌛ Time Up!\n\n✅ Answer: {answer}"
        )


@app.on_message(filters.text)
async def check_answer(client, message: Message):

    if message.chat.id not in active_games:
        return

    answer = active_games[message.chat.id]

    if message.text.lower() == answer:

        del active_games[message.chat.id]

        await message.reply_text(
            f"🏆 Correct! {message.from_user.mention}"
        )
