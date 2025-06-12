# HypeBot Server

Серверная версия бота для мониторинга релизов кроссовок и уличной моды с автоматической генерацией контента через AI.

## Функционал

- 🔍 Мониторинг источников (SneakerNews, Hypebeast, Highsnobiety)
- 🤖 Автоматическая генерация описаний через GPT-4
- 🎨 Создание обложек через DALL-E 3
- 📸 Анализ изображений через GPT-4 Vision
- ⏰ Планировщик публикаций
- 🏷 Система тегов и фильтров
- ⭐️ Избранное и авто-публикация
- 💭 Посты-размышления
- 🌍 Поддержка временных зон
- 📊 REST API для управления

## Быстрый старт

### 1. Клонирование репозитория

\`\`\`bash
git clone https://github.com/thealinfix/hypebot-server.git
cd hypebot-server
\`\`\`

### 2. Установка зависимостей

\`\`\`bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

pip install -r requirements.txt
\`\`\`

### 3. Настройка окружения

\`\`\`bash
cp .env.example .env
# Отредактируйте .env и добавьте свои ключи
\`\`\`

### 4. Запуск базы данных

\`\`\`bash
docker-compose -f infrastructure/docker/docker-compose.yml up -d db redis
\`\`\`

### 5. Миграции

\`\`\`bash
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
\`\`\`

### 6. Запуск сервера

\`\`\`bash
# Development
python -m src.main

# Production
docker-compose -f infrastructure/docker/docker-compose.yml up
\`\`\`

## API Endpoints

- GET /api/v1/health - Проверка здоровья
- POST /api/v1/webhooks/telegram - Webhook для Telegram
- GET /api/v1/posts - Список постов
- POST /api/v1/posts/{id}/publish - Публикация поста
- POST /api/v1/generation/text - Генерация текста
- POST /api/v1/generation/image - Генерация изображения
- GET /api/v1/schedule - Запланированные посты
- POST /api/v1/schedule - Создание расписания

## Структура проекта

\`\`\`
hypebot-server/
├── src/
│   ├── api/           # REST API endpoints
│   ├── bot/           # Telegram bot handlers
│   ├── core/          # Core configuration
│   ├── models/        # Database models
│   ├── services/      # Business logic
│   └── utils/         # Utilities
├── infrastructure/    # Docker, K8s configs
├── migrations/        # Database migrations
├── tests/            # Tests
└── requirements.txt
\`\`\`

## Технологии

- **Backend**: FastAPI, SQLAlchemy, Aiogram
- **Database**: PostgreSQL, Redis
- **AI**: OpenAI GPT-4, DALL-E 3
- **Deployment**: Docker, Kubernetes
- **Monitoring**: Prometheus, Grafana

## Лицензия

MIT
