from pyrogram import Client, filters


API_ID = "12360947"
API_HASH = "3dddbb5be694212e7954f7fdd5960a24"
BOT_TOKEN = "6234163890:AAEoUtCd5AX6401sQqdw7pggp1bfMLpNl7k"


BOT = Client(
    name="Telegram bot"
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)



print("Bot started")

BOT.run()
