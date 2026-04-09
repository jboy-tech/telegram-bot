from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# MENU BUTTONS
menu = [
    ["📊 Signals", "💰 Profit"],
    ["👥 Referrals", "⚙️ Settings"],
    ["❓ Help"]
]

reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to Profitable Engine FX 📈🔥\n\nChoose an option below:",
        reply_markup=reply_markup
    )

# BUTTON HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📊 Signals":
        await update.message.reply_text("No signals yet. Stay tuned 📊")

    elif text == "💰 Profit":
        await update.message.reply_text("Your profit: $0 💰")

    elif text == "👥 Referrals":
        await update.message.reply_text("You have 0 referrals 👥")

    elif text == "⚙️ Settings":
        await update.message.reply_text("Settings coming soon ⚙️")

    elif text == "❓ Help":
        await update.message.reply_text("Contact admin for help")

# MAIN FUNCTION
app = ApplicationBuilder().token("8782431947:AAEs9RFFIX6BEbttiXVNoOlL_KvcpgD1fRs").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot is running...")

app.run_polling()