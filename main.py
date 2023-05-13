from pyrogram import Client, filters
from pyrogram.types import message 
from pyrogram.types import InlineKeyboardMarkup InlineKeyboardButton 


API_ID = "12360947"
API_HASH = "3dddbb5be694212e7954f7fdd5960a24"
BOT_TOKEN = "6234163890:AAEoUtCd5AX6401sQqdw7pggp1bfMLpNl7k"


BOT = Client(
    name="Telegram bot"
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
START_BUTTON= [[
  InlineKeyboardButton("Owner", url="t.me/Lion_098765")
  ],[
  InlineKeyboardButton("group", url="t.me/rrmovie0987")
  ]]


@BOT.on_message(filters.command("start"))
async def start_command(bot, message):
    await message.reply_text(
        text="hai hello"
        reply_markup=
    
  )
@BOT.on_message(filter.command("help"))
async def help_command(bot, message):
     await message.reply_text(
           
        

print("Bot started")

BOT.run()
