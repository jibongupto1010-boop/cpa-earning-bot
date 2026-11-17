import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    users.setdefault(uid, 0)

    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    keyboard.row("📢 Ads & Tasks", "💰 My Balance")
    keyboard.row("👥 Refer Friends", "💳 Withdraw")

    bot.send_message(
        uid,
        "Welcome to CPA Earning BD!\n"
        "এটি একটি Demo Bot।",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: True)
def menu(message):
    uid = message.from_user.id
    users.setdefault(uid, 0)

    if message.text == "📢 Ads & Tasks":
        bot.reply_to(
            message,
            "এখনো কোনো অনুমোদিত Offer যুক্ত করা হয়নি।"
        )

    elif message.text == "💰 My Balance":
        bot.reply_to(
            message,
            f"Your Demo Balance: {users[uid]} Points"
        )

    elif message.text == "👥 Refer Friends":
        bot.reply_to(
            message,
            f"Your Telegram ID: {uid}"
        )

    elif message.text == "💳 Withdraw":
        bot.reply_to(
            message,
            "Demo Mode: এখন Withdrawal চালু নেই।"
        )

    else:
        bot.reply_to(message, "Menu থেকে একটি অপশন বেছে নাও।")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing")

bot.infinity_polling()
