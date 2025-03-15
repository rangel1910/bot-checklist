from telegram import Update
from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv(HTTP API:7758787377:AAEZsse9EvsaFwZkJqKw9PEA9_XRt6Sw3W0)

async def start(update: Update, context):
    await update.message.reply_text("Olá! Sou seu bot de checklist de revisão de carro.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot está rodando...")
app.run_polling()
