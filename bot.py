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
    "Diwali - she sent me a pic in red suit, she looked so beautiful 😭😭 I wanted to simp hard but didn't.",
    "My ex returned out of nowhere, and I really made Ritika worried, but instead of leaving me, she helped me to get rid of her.",
    "I loved it when she asked me questions about my date preferences during truth and dare as it let me find out we had very similar preferences.",
    "When Nikku gave her a dare to put matching pfp with me, I was honestly very happy because I was afraid to ask her to put matching pfp.",
    "When I asked her if we should keep the pfp after the dare was over, I was afraid she'd say no, as she might have just done it for the dare. But she said we can keep it, and it made me happy.",
    "When people shipped me with her, I liked it a lot even when I was not sure if I loved her. I loved getting shipped with her.",
    "When she sent the reel with the santra date saying I deserve a date like this, I thought for 2 minutes if I should send it or not. But then I said, 'F*** it' and sent 'Chalo is date pe,' and when she said yes, I couldn't believe it and was on cloud nine.",
    "I once told her that Anam asked me some weird questions, and I told her what she asked, but I skipped one essential question: 'What would I tell her if the world was ending?' When Anam asked me that, I was confused about what to say. So I thought and said, 'I would tell her I am thankful I met her.' And Anam said, 'Bas ye?' To which I said, 'No, I'll say I loved her.' That's when I realized—yes, I love her.",
    "This one's a little embarrassing, but when we just started talking in DM, I read somewhere that Raat me ye log (Mickey and you) talk in VC. I thought you and Mickey were close lol. And I was jealous and disappointed that I couldn't talk at night. Otherwise, I would've joined. But some days later, I saw Mickey and others in VC at night, and they were tagging her, but she was talking with me in DM instead. I was shocked, happy, confused—everything all at once. I thought, 'Why would she choose me? Mickey has a good sense of humor, can talk with her in VC, and is probably more fun than me.'",
    "When we were in the double date GC, once Nikku was flirting with Anam. Mujhe bhi man kiya ki karu usse flirt. And when I said I'm lonely, she said, 'Dw, God will always be with you.' And I said, 'You're my God.' That felt good, the frustration was over.",
    "Whenever she's making something and I ask 'Mujhe bhi khana?' and she says 'Aajao khila dungi,' I imagine a scenario. There was a song I loved when I was a kid, and in its music video, the girl feeds the boy strawberries as they were making something. I imagine the same thing with us whenever she says that 'Aajao khila dungi.'"
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
