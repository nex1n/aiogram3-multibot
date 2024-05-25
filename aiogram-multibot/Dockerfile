FROM python:3.12.3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Копируем все остальные файлы в рабочую директорию

# Команда по умолчанию для запуска приложения
CMD ["python", "__main__.py"]