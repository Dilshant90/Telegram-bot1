import random
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from flask import Flask

# Securely get bot token from environment variables
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
    "When Nikku gave her a dare to put matching pfp with me, I was honestly very happy because I was afraid to ask her to put matching pfp.",
    "When I asked her if we should keep the pfp after the dare was over, I was afraid she'll say no, as she might have just done it for the dare. But she said we can keep it, it made me happy.",
    "When people shipped me with her, I liked it a lot even when I was not sure if I love her. I loved getting shipped with her.",
    "When she sent the reel with santra date saying I deserve a date like this, I thought for 2 minutes if I should send it or not. But then I said fuck it and sent 'Chalo is date pe'. And when she said yes, I couldn't believe it and was on cloud nine.",
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

# Function to run Telegram bot
async def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("hug", hug))
    app.add_handler(CommandHandler("kiss", kiss))
    app.add_handler(CommandHandler("date", date))
    app.add_handler(CommandHandler("secret", secret))
    app.add_handler(CommandHandler("mylove", mylove))

    print("Bot is running...")
    await app.run_polling()

# Flask app to keep Koyeb's health check happy
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running!", 200  # ✅ This keeps Koyeb's health check from failing

# Start both Flask (web server) and Telegram bot
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Start Flask web server
    from threading import Thread
    Thread(target=lambda: flask_app.run(host="0.0.0.0", port=8000)).start()

    # Start Telegram bot
    loop.run_until_complete(run_bot())
