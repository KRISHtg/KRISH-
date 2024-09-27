from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Update", url="https://t.me/+9U8Td9WZ2dk1ZGU1"),
        InlineKeyboardButton("Support", url="https://t.me/+Kus9t8btLPRhYzll")],
        [ InlineKeyboardButton("Buy Premium", url= "t.me/its_me_krish_tg"),
         InlineKeyboardButton("Help", url="https://graph.org/vTelegraphBot-09-27-5")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://te.legra.ph/file/dea69b6de713db64628d5.jpg",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
