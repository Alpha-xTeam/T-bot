from flask import Flask, request, jsonify
from telegram import Bot, Update
import json
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Get token from environment
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN environment variable not set")

# Create bot instance
bot = Bot(token=TELEGRAM_TOKEN)


def send_message(chat_id, text, reply_to_message_id=None):
    """Send a message to a chat"""
    try:
        bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=reply_to_message_id
        )
        return True
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        return False


def handle_start(chat_id, message_id):
    """Handle /start command"""
    text = (
        "مرحباً بك! 👋\n\n"
        "أنا بوت يرد على رسائلك.\n"
        "استخدم /help للمزيد من المعلومات"
    )
    send_message(chat_id, text, message_id)


def handle_help(chat_id, message_id):
    """Handle /help command"""
    text = (
        "الأوامر المتاحة:\n"
        "/start - ابدأ المحادثة\n"
        "/help - اعرض المساعدة\n"
        "/about - عن البوت\n\n"
        "أو فقط أرسل أي رسالة وسأرد عليها! 😊"
    )
    send_message(chat_id, text, message_id)


def handle_about(chat_id, message_id):
    """Handle /about command"""
    text = (
        "معلومات عن البوت 🤖\n\n"
        "اسم البوت: رد التطبيق\n"
        "النسخة: 2.0\n"
        "تم إنشاؤه بـ: Flask + python-telegram-bot"
    )
    send_message(chat_id, text, message_id)


def handle_message(chat_id, user_name, text, message_id):
    """Handle regular messages"""
    response = f"مرحباً {user_name}! 👋\n\nأنت قلت: {text}"
    send_message(chat_id, response, message_id)


@app.route('/api/bot', methods=['POST'])
def webhook():
    """Handle webhook updates from Telegram"""
    try:
        data = request.get_json()
        
        # Create update object
        update = Update.de_json(data, bot)
        
        # Ignore updates without messages
        if not update.message:
            return jsonify({"status": "ok"})
        
        chat_id = update.message.chat.id
        user_name = update.effective_user.first_name or "صديقي"
        message_id = update.message.message_id
        text = update.message.text or ""
        
        # Handle commands
        if text.startswith("/start"):
            handle_start(chat_id, message_id)
        elif text.startswith("/help"):
            handle_help(chat_id, message_id)
        elif text.startswith("/about"):
            handle_about(chat_id, message_id)
        elif text:  # Regular text message
            handle_message(chat_id, user_name, text, message_id)
        
        return jsonify({"status": "ok"})
        
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/bot', methods=['GET'])
def status():
    """Health check endpoint"""
    return jsonify({"message": "Bot is running!", "status": "ok"})


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "name": "Telegram Bot",
        "version": "2.0",
        "status": "running",
        "webhook": "/api/bot"
    })


if __name__ == "__main__":
    app.run(debug=False)
