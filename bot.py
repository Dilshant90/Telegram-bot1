import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

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
    "I once told her that Anam asked me some weird questions. And I told her what she asked. But I skipped one essential question. That was, 'What would I tell her if the world was ending?' When Anam asked me that, I was confused what to say. So I thought and said I would tell her I am thankful I met her. And Anam said, 'Bas ye?' So I said no, I'll tell her I loved her. That's when I realized yes, I love her.",
    "This one's a little embarrassing but when we just started talking in DM, I read somewhere that raat me ye log (Mickey and you) talk in VC. I thought you and Mickey are close lol. And I was jealous and disappointed that I can't talk at night, otherwise I would've joined. But some days later, I saw Mickey and others in VC at night and they were tagging her, but she was talking with me in DM instead. I was shocked, happy, confused, everything all at once. I thought why would she choose me? Mickey had a good sense of humor, could talk with her in VC, and was probably more fun than me.",
    "When we were in the double date GC, once Nikku was flirting with Anam. Mujhe bhi man kiya ki karu usse flirt. And when I said I'm lonely, she said 'Dw, God will always be with you.' And I said, 'You're my God.' That felt good, the frustration was over.",
    "Whenever she's making something and I ask 'Mujhe bhi khana,' and she says 'Aajao khila dungi,' I imagine a scenario. There was a song I loved when I was a kid, and in its music video, the girl feeds the boy strawberries as they were making something. I imagine the same thing with us whenever she says 'Aajao khila dungi.'"
]

special_message = (
    "Will you be my Valentine? Not only this year but for the rest of my life? ❤️\n"
    "I know it's a lot to ask for, but I can't lose you. You're the best thing that has happened to me. "
    "Thank you for coming into my life. I LOVE YOU RITIKA ❤️."
)

stored_images = {}

# Command Handlers
async def love(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(love_messages))

async def hug(update: Update, context: CallbackContext):
    await update.message.reply_animation(random.choice(hug_gifs))

async def kiss(update: Update, context: CallbackContext):
    await update.message.reply_animation(random.choice(kiss_gifs))

async def date(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(date_ideas))

async def sticker(update: Update, context: CallbackContext):
    await update.message.reply_sticker("CAACAgUAAxkBAAEKGlxlE8mQzJvXjwxXJd8RUqHugOwRYAACQAkAAvoLtFSVjeGxNkZMjLQE")  # Example sticker ID

async def secret(update: Update, context: CallbackContext):
    await update.message.reply_text(random.choice(secrets))

async def mylove(update: Update, context: CallbackContext):
    if update.message.from_user.username == "your_mo0nlightt":
        await update.message.reply_text(special_message)
    else:
        await update.message.reply_text("This message is only for Ritika! ❤️")

async def store(update: Update, context: CallbackContext):
    if update.message.reply_to_message and update.message.reply_to_message.photo:
        file_id = update.message.reply_to_message.photo[-1].file_id
        stored_images[len(stored_images) + 1] = file_id
        await update.message.reply_text(f"Image saved as {len(stored_images)}")
    else:
        await update.message.reply_text("Please reply to an image to store it.")

async def list_images(update: Update, context: CallbackContext):
    if not stored_images:
        await update.message.reply_text("No images stored yet.")
    else:
        img_list = "\n".join([f"{num}: Image" for num in stored_images.keys()])
        await update.message.reply_text(f"Stored images:\n{img_list}")

async def sendimg(update: Update, context: CallbackContext):
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /sendimg <image number>")
        return

    img_number = int(context.args[0])
    if img_number in stored_images:
        await update.message.reply_photo(stored_images[img_number])
    else:
        await update.message.reply_text("Invalid image number.")

# Main Function
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("love", love))
    app.add_handler(CommandHandler("hug", hug))
    app.add_handler(CommandHandler("kiss", kiss))
    app.add_handler(CommandHandler("date", date))
    app.add_handler(CommandHandler("sticker", sticker))
    app.add_handler(CommandHandler("secret", secret))
    app.add_handler(CommandHandler("mylove", mylove))
    app.add_handler(CommandHandler("store", store))
    app.add_handler(CommandHandler("list", list_images))
    app.add_handler(CommandHandler("sendimg", sendimg))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
