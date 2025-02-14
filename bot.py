import random
import os
import asyncio
import multiprocessing
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from flask import Flask

# Get bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing! Set it in the environment variables.")

# Lists for random responses
love_messages = [
    "You are the reason I smile every day ❤️",
    "My heart beats only for you 💖",
    "Every moment with you is special 💕",
    "You make my life beautiful 🌹",
    "I love you more than words can say 😘"
]

hug_gifs = [
    "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
    "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
    "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif"
]

kiss_gifs = [
    "https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
    "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif",
    "https://media.giphy.com/media/KH1CTZtw1iP3W/giphy.gif"
]

date_ideas = [
    "Candlelight dinner at home 🍽️✨",
    "Late-night drive with your favorite songs 🎶",
    "Picnic in the park 🌳🥪",
    "Stargazing together 🌌💫",
    "Movie night with cozy blankets 🎬🍿"
]

secrets = [
    "I told her about my bullying past and I was very down that day. She helped me through it.",
    "Diwali - she sent me a pic in red suit. She looked so beautiful 😭😭 I wanted to simp hard but didn't.",
    "My ex returned out of nowhere. And I really made Ritika worried, but instead of leaving me, she helped me to get rid of her.",
    "I loved it when she asked me questions about my date preferences during truth and dare as it let me find out we had very similar preferences.",
]

special_message = (
    "Will you be my Valentine? Not only this year but for the rest of my life? ❤️\n"
    "I know it's a lot to ask for, but I can't lose you. You're the best thing that has happened to me. "
    "Thank you for coming into my life. I LOVE YOU RITIKA ❤️."
)

# Command Handlers
async def love(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(love_messages))

async def hug(update: Update, context: CallbackContext):
    await update.message.reply_animation(random.choice(hug_gifs))

async def kiss(update: Update, context: CallbackContext):
    await update.message.reply_animation(random.choice(kiss_gifs))

async def date(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(date_ideas))

async def secret(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(secrets))

async def mylove(update: Update, context: CallbackContext):
    if update.message.from_user.username == "your_mo0nlightt":
        await update.message.reply_text(special_message)
    else:
        await update.message.reply_text("This message is only for Ritika! ❤️")

# Flask app for Koyeb health check
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running!", 200

# Function to run Flask web server
def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

# Function to run Telegram bot
def run_bot():
    asyncio.set_event_loop(asyncio.new_event_loop())  # Create a new event loop
    loop = asyncio.get_event_loop()

    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("hug", hug))
    app.add_handler(CommandHandler("kiss", kiss))
    app.add_handler(CommandHandler("date", date))
    app.add_handler(CommandHandler("secret", secret))
    app.add_handler(CommandHandler("mylove", mylove))

    print("Bot is running...")
    loop.run_until_complete(app.run_polling())

# Run Flask & Telegram bot separately
if __name__ == "__main__":
    flask_process = multiprocessing.Process(target=run_flask)
    flask_process.start()  # Run Flask separately

    bot_process = multiprocessing.Process(target=run_bot)
    bot_process.start()  # Run Telegram bot separately

    flask_process.join()
    bot_process.join()
