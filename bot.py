import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ══════════════════════════════════════════════
# НАСТРОЙКИ
# ══════════════════════════════════════════════
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8849711401:AAEXVo84AcsbrjuplNquy0RUqh3u124v89Q")
ADMIN_ID = 342698056

# ══════════════════════════════════════════════
# ТЕКСТЫ
# ══════════════════════════════════════════════

WELCOME_TEXT = """
👋 Добро пожаловать!

Я помощник *Кристиана Девалкьера* —
биоэнергетика с 20-летним опытом
в области пси-технологий и телекинеза.

🌟 Хотите узнать о курсе *«ПРОБУЖДЕНИЕ»*?

Выберите что вас интересует 👇
"""

ABOUT_COURSE_TEXT = """
📚 *КУРС «ПРОБУЖДЕНИЕ»*
_Откройте Врата к Невидимым Силам_

За 2 дня вы научитесь:

⚡ Управлять внутренней и внешней энергией
⚡ Работать с биополем и энергетическими каналами
⚡ Квантовым и трансцендентальным медитациям
⚡ Развивать интуицию и концентрацию
⚡ Влиять на физические объекты

✨ *Результаты после курса:*
- Гармонизация жизни
- Снятие энергетических блоков
- Расширение восприятия
- Личностный рост

📍 *Формат:*
🔹 2 дня офлайн-интенсив
🔹 + 1 месяц онлайн-сопровождения
"""

PRICE_TEXT = """
💰 *СТОИМОСТЬ КУРСА*

~~99 999 ₽~~

✅ По промокоду *ТК* : *70 000 ₽*
_(~2 000 €)_

В стоимость входит:
✔️ 2 дня интенсивного обучения
✔️ 1 месяц онлайн-поддержки
✔️ Доступ в закрытое сообщество
✔️ Личные рекомендации от мастера
✔️ Эксклюзивный подарок при записи

⏰ *Осталось всего 5 мест!*
"""

ABOUT_MASTER_TEXT = """
👤 *КРИСТИАН ДЕВАЛКЬЕР*

Биоэнергетик и пионер в области
пси-технологий и телекинеза.

🔹 20+ лет опыта
🔹 Участник телепередач как эксперт
🔹 Уникальная авторская методика
🔹 Сочетает восточные практики с квантовой физикой

Кристиан обладает уникальной способностью
изменять структуры материи с помощью
собственного биополя.
"""

REGISTER_TEXT = """
🎉 *Отлично! Вы на правильном пути!*

Для записи на курс *«ПРОБУЖДЕНИЕ»*
свяжитесь с Кристианом напрямую:

📞 Телефон: +7 966 057 77 79
💬 WhatsApp: wa.me/79660577779
📱 Telegram: @DEVALCOEUR

🌐 Сайт: kristian250535-source.github.io/kurs-probuzhdenie/

_Используйте промокод ТК для скидки!_ 🎁
"""

# ══════════════════════════════════════════════
# КЛАВИАТУРЫ
# ══════════════════════════════════════════════

def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("📚 О курсе", callback_data="about_course")],
        [InlineKeyboardButton("💰 Стоимость", callback_data="price")],
        [InlineKeyboardButton("👤 О мастере", callback_data="about_master")],
        [InlineKeyboardButton("✍️ Записаться", callback_data="register")],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_keyboard():
    keyboard = [
        [InlineKeyboardButton("◀️ Назад", callback_data="back")],
        [InlineKeyboardButton("✍️ Записаться", callback_data="register")],
    ]
    return InlineKeyboardMarkup(keyboard)

def register_keyboard():
    keyboard = [
        [InlineKeyboardButton("💬 Написать в WhatsApp", url="https://wa.me/79660577779")],
        [InlineKeyboardButton("📱 Написать в Telegram", url="https://t.me/DEVALCOEUR")],
        [InlineKeyboardButton("🌐 Открыть сайт", url="https://kristian250535-source.github.io/kurs-probuzhdenie/")],
        [InlineKeyboardButton("◀️ Назад", callback_data="back")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ══════════════════════════════════════════════
# ОБРАБОТЧИКИ
# ══════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 Новый пользователь!\nИмя: {user.first_name}\nUsername: @{user.username}\nID: {user.id}"
        )
    except:
        pass
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=main_keyboard(),
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user

    if query.data == "about_course":
        try:
            await context.bot.send_message(chat_id=ADMIN_ID, text=f"👀 {user.first_name} (@{user.username}) смотрит информацию о курсе")
        except:
            pass
        await query.edit_message_text(ABOUT_COURSE_TEXT, reply_markup=back_keyboard(), parse_mode='Markdown')

    elif query.data == "price":
        try:
            await context.bot.send_message(chat_id=ADMIN_ID, text=f"💰 {user.first_name} (@{user.username}) смотрит стоимость курса!")
        except:
            pass
        await query.edit_message_text(PRICE_TEXT, reply_markup=back_keyboard(), parse_mode='Markdown')

    elif query.data == "about_master":
        await query.edit_message_text(ABOUT_MASTER_TEXT, reply_markup=back_keyboard(), parse_mode='Markdown')

    elif query.data == "register":
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"🔥🔥🔥 ГОРЯЧИЙ ЛИД!\n{user.first_name} (@{user.username}) хочет ЗАПИСАТЬСЯ!\nID: {user.id}\nСвяжитесь немедленно!"
            )
        except:
            pass
        await query.edit_message_text(REGISTER_TEXT, reply_markup=register_keyboard(), parse_mode='Markdown')

    elif query.data == "back":
        await query.edit_message_text(WELCOME_TEXT, reply_markup=main_keyboard(), parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.lower()
    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"💬 Сообщение от {user.first_name} (@{user.username}):\n{update.message.text}"
        )
    except:
        pass
    if any(word in text for word in ["цена", "стоимость", "сколько"]):
        await update.message.reply_text(PRICE_TEXT, reply_markup=back_keyboard(), parse_mode='Markdown')
    elif any(word in text for word in ["записаться", "запись", "хочу"]):
        await update.message.reply_text(REGISTER_TEXT, reply_markup=register_keyboard(), parse_mode='Markdown')
    elif any(word in text for word in ["курс", "программа"]):
        await update.message.reply_text(ABOUT_COURSE_TEXT, reply_markup=back_keyboard(), parse_mode='Markdown')
    else:
        await update.message.reply_text(WELCOME_TEXT, reply_markup=main_keyboard(), parse_mode='Markdown')

# ══════════════════════════════════════════════
# ЗАПУСК
# ══════════════════════════════════════════════

def main():
    logging.basicConfig(level=logging.INFO)
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущен!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
