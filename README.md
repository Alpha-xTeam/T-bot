# بوت Telegram في Vercel

بوت Telegram بسيط يرد على الرسائل ويعمل على منصة Vercel.

## المميزات 🌟

- ✅ الرد على الرسائل النصية
- ✅ معالجة الأوامر (/start, /help, /about)
- ✅ توزيع بدون خادم على Vercel
- ✅ دعم اللغة العربية

## المتطلبات 📋

- Python 3.11 أو أحدث
- حساب على Vercel
- بوت Telegram (من @BotFather على Telegram)

## الخطوات 🚀

### 1. إنشاء البوت

اتصل بـ @BotFather على Telegram:
```
/start
/newbot
```

سيعطيك **توكن** (مفتاح). احفظه!

### 2. إعداد المشروع محلياً

```bash
# انسخ ملف البيئة
cp .env.example .env

# ثم عدّل .env واضف التوكن:
# TELEGRAM_TOKEN=your_actual_bot_token
```

### 3. تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

### 4. توزيع على Vercel

#### أ. باستخدام Vercel CLI

```bash
# تثبيت Vercel CLI
npm install -g vercel

# تسجيل الدخول
vercel login

# توزيع المشروع
vercel
```

#### ب. باستخدام GitHub

1. ادفع المشروع إلى GitHub
2. اذهب إلى [vercel.com](https://vercel.com)
3. انقر على "New Project"
4. اختر repository من GitHub
5. أضف متغيرات البيئة في الإعدادات:
   - `TELEGRAM_TOKEN` = توكن البوت الخاص بك

#### ج. إعداد Webhook

بعد التوزيع، احصل على URL الخاص بك (مثلاً: `https://your-project.vercel.app`)

ثم استخدم هذا الأمر (استبدل القيم):

```bash
curl -X POST https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook \
  -d "url=https://your-project.vercel.app/api/bot"
```

أو استخدم أداة مثل Postman.

## الهيكل 📁

```
.
├── api/
│   └── bot.py          # ملف البوت الرئيسي
├── requirements.txt    # المتطلبات
├── vercel.json        # إعدادات Vercel
├── .env.example       # ملف البيئة (مثال)
└── README.md          # هذا الملف
```

## المتغيرات البيئية 🔐

- `TELEGRAM_TOKEN`: توكن البوت من BotFather

## استكشاف الأخطاء 🐛

### البوت لا يستجيب

1. تحقق من أن التوكن صحيح
2. تأكد من أن Webhook تم تعيينه بشكل صحيح
3. افحص السجلات في Vercel Dashboard

### الخطأ 401

عادة توكن غير صحيح. احصل على توكن جديد من @BotFather

## موارد مفيدة 📚

- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Vercel Python Runtime](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

## الترخيص 📄

MIT License

---

**ملاحظة**: تأكد من عدم مشاركة توكن البوت الخاص بك مع أحد! 🔒
