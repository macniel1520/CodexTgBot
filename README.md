# CodexTgBot

Telegram-бот на aiogram, который принимает фото блюда и возвращает его КБЖУ на 100 грамм с использованием OpenAI Vision API.

## Структура проекта

```
/project-root
│
├── /app                      # Основная папка с приложением
│   ├── __init__.py            # Инициализация пакета
│   ├── main.py                # Точка входа в приложение
│   ├── bot.py                 # Настройка и запуск бота
│   ├── config.py              # Конфигурация проекта
│   ├── dependencies.py        # Зависимости и внедрение зависимостей
│   ├── /handlers              # Хэндлеры команд и сообщений
│   ├── /middlewares           # Middleware для бота
│   ├── /services              # Сервисы и бизнес-логика
│   ├── /models                # Модели базы данных (SQLAlchemy)
│   ├── /keyboards             # Клавиатуры для бота
│   ├── /utils                 # Вспомогательные функции
│   ├── /templates             # Шаблоны сообщений
│   └── /exceptions            # Пользовательские исключения
│
├── /migrations                # Миграции базы данных
├── /tests                     # Тесты проекта
├── /docker                    # Конфигурации Docker
├── /scripts                   # Скрипты для развертывания и миграций
├── /docs                      # Документация проекта
├── .env                       # Файл с переменными окружения
├── .gitignore                 # Игнорируемые Git файлы и папки
├── requirements.txt           # Зависимости проекта
└── README.md                  # Описание проекта
```

## Установка и настройка

### Предварительные требования

- Docker
- Docker Compose
- Git

### Клонирование репозитория

```bash
git clone https://github.com/FaceX-geo/telegram_bot_base.git
cd telegram_bot_base
```

### Настройка `.env` файла

Заполните файл `.env` необходимыми переменными окружения:

```
TELEGRAM_TOKEN=your_telegram_token
DATABASE_URL=postgresql+asyncpg://user:password@db:5432/dbname
YOOMONEY_API_KEY=your_yoomoney_api_key
CHATGPT_API_KEY=your_chatgpt_api_key

POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=your_db_name
```

### Установка зависимостей

Используйте Docker для установки зависимостей:

```bash
docker-compose run bot pip install -r requirements.txt
```

### Миграции базы данных

**Создание миграций**

```bash
docker-compose run bot alembic revision --autogenerate -m "Initial migration"
```

**Применение миграций**

```bash
docker-compose run bot alembic upgrade head
```

### Docker и Docker Compose

**Описание Dockerfile**

```
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
```

**Описание `docker-compose.yml`**

```
version: '3.8'

services:
  bot:
    build: .
    env_file:
      - .env
    depends_on:
      - db
    volumes:
      - .:/app
    restart: always

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - '5432:5432'
    restart: always

volumes:
  postgres_data:
```

### Запуск приложения

Запустите все сервисы с использованием Docker Compose:

```bash
docker-compose up --build
```

## Описание компонентов приложения

### `/app`

Основная директория приложения, содержащая всю логику бота:

- `main.py`: Точка входа в приложение.
- `bot.py`: Настройка и запуск бота.
- `config.py`: Конфигурация проекта (использует Pydantic).
- `handlers/`: Хэндлеры команд и сообщений.
- `middlewares/`: Middleware для обработки запросов (логирование, аутентификация и т.д.).
- `services/`: Бизнес-логика приложения (работа с БД, платежи, внешние API).
- `models/`: Модели базы данных (SQLAlchemy).
- `keyboards/`: Клавиатуры для бота (ReplyKeyboardMarkup, InlineKeyboardMarkup).
- `utils/`: Вспомогательные функции.
- `templates/`: Шаблоны сообщений для бота.
- `exceptions/`: Пользовательские исключения.

### `/migrations`

Миграции базы данных с использованием Alembic.

### `/tests`

Тесты проекта, разделенные на модульные и интеграционные.

### `/docker`

Конфигурации Docker и Docker Compose.

### `/scripts`

Скрипты для автоматизации задач, таких как миграции и запуск бота.

### `/docs`

Документация проекта, включая архитектуру и API.

## Запуск без Docker

```bash
python app/main.py
```
