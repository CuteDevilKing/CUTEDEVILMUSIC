from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from BADMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("donate")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d39fad4925de55b86e96.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 𝐃ᴏɴᴀᴛᴇ 🎁", url=f"https://t.me/CuteDevil_Music")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("donate")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d39fad4925de55b86e96.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 𝐃ᴏɴᴀᴛᴇ 🎁", url=f"https://t.me/CuteDevil_Music")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("donate")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d39fad4925de55b86e96.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 𝐃ᴏɴᴀᴛᴇ 🎁", url=f"https://t.me/CuteDevil_Music")
                ]
            ]
        ),
    )
