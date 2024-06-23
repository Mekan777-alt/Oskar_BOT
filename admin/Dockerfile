FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Установите переменные окружения для режима продакшн
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV DEBUG=False

# Создайте директорию для статических файлов
RUN mkdir -p /app/staticfiles

# Выполните collectstatic
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
