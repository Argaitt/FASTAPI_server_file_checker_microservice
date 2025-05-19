# Используем официальный образ Python
FROM python:3.13.2

# Рабочая директория в контейнере
WORKDIR /app

# Копируем зависимости
COPY ./requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY ./ .

# Запускаем сервер
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]