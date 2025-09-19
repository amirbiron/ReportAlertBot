from telegram.ext import Application, MessageHandler, filters

# === ערוך כאן ===
TOKEN = "הכנס את הטוקן מה-BotFather"
TARGET_ID = 123456789  # ה-user_id של המטריד
# ================

async def warn(update, context):
    if update.effective_chat.id == TARGET_ID:
        await update.message.reply_text(
            "🚨 שים לב: ההודעות שלך מתועדות. הפצת מספרים או הטרדה זה עבירה פלילית. המשך בזה = דיווח + חסימה."
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, warn))
    app.run_polling()

if __name__ == "__main__":
    main()
