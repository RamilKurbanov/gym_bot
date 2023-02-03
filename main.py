from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from controller import *
import os

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE ) -> None:
    await update.message.reply_text(f'Приветсвую тебя дорогой пользователь, для того что бы узнать мои команды, введи - /help')


app = ApplicationBuilder().token("6178929885:AAGDVWngpb7-auo4HEwnPXxXNjChPFPrh70").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("days", days))
app.add_handler(CommandHandler("monday", Monday))
app.add_handler(CommandHandler("tuesday", Tuesday))
app.add_handler(CommandHandler("wednesday", Wednesday))
app.add_handler(CommandHandler("thursday", Thursday))
app.add_handler(CommandHandler("friday", Friday))
app.add_handler(CommandHandler("saturday", Saturday))
app.add_handler(CommandHandler("sunday", Sunday))


app.run_polling()