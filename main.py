from telegram.ext import Application, CommandHandler, MessageHandler, filters

import os

# עדיף למשוך מה־env ברנדר
TOKEN = os.getenv("TOKEN")
TARGET_ID = int(os.getenv("TARGET_ID", "0"))

async def start(update, context):
    if update.effective_user.id == TARGET_ID:
        await update.message.reply_text(
            "🚨 שים לב: ההודעות שלך מתועדות. הפצת מספרים או הטרדה זה עבירה פלילית. המשך בזה = דיווח + חסימה."
        )

async def warn(update, context):
    if update.effective_user.id == TARGET_ID:
        await update.message.reply_text(
            "🚨 שים לב: ההודעות שלך מתועדות. הפצת מספרים או הטרדה זה עבירה פלילית. המשך בזה = דיווח + חסימה."
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, warn))
    app.run_polling()

if __name__ == "__main__":
    main()
