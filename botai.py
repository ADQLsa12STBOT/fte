import telebot
import requests
import json

A_URL = "http://heliotropestarfish.onpella.app/ask"

bot = telebot.TeleBot("7858878701:AAH6NcEJXU7Nv_wWCej0EP16G4rLPzzszeU")

@bot.message_handler(commands=['start'])
def s_w(message):
    bot.reply_to(message, '''🌖أنا شات جي بي تي، أي أنني نموذج لغوي آلي كبير تم تدريبه باستخدام تقنية الذكاء الاصطناعي 
🐺لتوفير الإجابات والمحادثات للمستخدمين 
في مختلف المواضيع والمجالات
🧠اكدر اساعدك بشيء ؟ 
''')

@bot.message_handler(func=lambda message: True)
def h_m(message):
    q = message.text
    r = requests.post(A_URL, json={"qus": q})
    a = r.json().get("bot")
    bot.reply_to(message, a,parse_mode="Markdown")

bot.polling(none_stop=True, timeout=20)