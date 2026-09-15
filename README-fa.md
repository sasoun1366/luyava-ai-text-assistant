# Luyava AI Text Assistant 1.0

یک اسکریپت پایتون برای خلاصه‌سازی متن، استخراج نکات کلیدی، بازنویسی حرفه‌ای و پاسخ‌گویی متنی با API سازگار با OpenAI. این محصول برای استفاده شخصی و کسب‌وکار طراحی شده و کلید API را فقط از متغیر محیطی می‌خواند.

## نصب

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
```

در `.env` مقدار `AI_API_KEY` را قرار بده. در صورت استفاده از پراکسی یا سرویس سازگار، مقدار `AI_API_BASE` را هم تنظیم کن.

## اجرا

```bash
python ai_assistant.py "متن طولانی شما" --mode summarize
python ai_assistant.py --file input.txt --mode extract
python ai_assistant.py "این متن را رسمی‌تر کن" --mode rewrite
```

حالت‌های `summarize`، `extract`، `rewrite` و `answer` در دسترس هستند. مدل پیش‌فرض `gpt-5-mini` است و با `AI_MODEL` قابل تغییر است.

## امنیت و حریم خصوصی

کلید API را داخل کد، فایل ZIP، Git یا چت قرار نده. قبل از ارسال اسناد محرمانه، اطلاعات شخصی و اسرار کسب‌وکار را حذف یا ناشناس‌سازی کن. خروجی مدل را قبل از انتشار یا تصمیم‌گیری مهم بررسی انسانی کن.

این ابزار برای تولید محتوای مخرب، فیشینگ، سرقت اطلاعات، دورزدن کنترل دسترسی یا حمله به سامانه‌ها طراحی نشده است.
