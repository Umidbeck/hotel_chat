FROM python:3.11-slim

# Ishchi papkani o'rnatamiz
WORKDIR /app

# requirements.txt faylini ko'chiramiz
COPY requirements.txt /app/

# Kutubxonalarni o'rnatamiz
RUN pip install --upgrade pip && pip install -r requirements.txt

# Backend papkasini ko'chiramiz (bu manage.py, bot.py va boshqa modullarni o'z ichiga oladi)
ENV PYTHONPATH=/app

# Python modullarni tanitish uchun
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=config.settings

# Migrations + Daphne + Telegram botni ishga tushirish
CMD sh -c "python manage.py migrate && daphne -b 0.0.0.0 -p 8000 config.asgi:application & python bot/bot.py"

