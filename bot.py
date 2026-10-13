from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8826066609:AAG1gUhUywDub7jmnkzC9PaotfsJJH63EZQ"
QUESTIONS=[{"q":"ما عاصمة اليمن؟","o":["صنعاء","عدن","تعز"],"a":0}]

async def start(u,c):
 await u.message.reply_text("أهلا! اكتب /quiz")
async def quiz(u,c):
 q=QUESTIONS[0]
 await u.message.reply_text(f"{q['q']}\n1-{q['o'][0]}\n2-{q['o'][1]}\n3-{q['o'][2]}")
async def ans(u,c):
 await u.message.reply_text("وصلت! /quiz لسؤال جديد")

def main():
 app=Application.builder().token(TOKEN).build()
 app.add_handler(CommandHandler("start",start))
 app.add_handler(CommandHandler("quiz",quiz))
 app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,ans))
 app.run_polling()

if __name__=="__main__":
 main()
