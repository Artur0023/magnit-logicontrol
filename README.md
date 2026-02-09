## Magnit LogiControl

### Учебно-практический проект по аналитике цепочки поставок: от генерации данных и BI-аналитики до A/B тестирования и бизнес-выводов..

### Проект выполнен как самостоятельный продукт и ориентирован на реальные задачи ритейла (МАГНИТ).


## Цель проекта

### Смоделировать реальный data-проект в ритейле (логистика / supply chain), включающий:
- Генерацию и хранение данных (SQLite)
- Аналитические ноутбуки (EDA, KPI)
- Веб-дашборд
- Telegram-бот для менеджеров
- A/B тест логистического улучшения
- Интерпретацию результатов с бизнес-точки зрения


## Бизнес-метрики

### В проекте рассчитываются и используются:
- DOH (Days of Hand) — дни запаса
- OOS Risk — риск Out-of-Stock (HIGH / MEDIUM / LOW)
- SLA поставок — доля поставок без задержек
- Задержка поставок — фактическое отклонение от плана
- Проблемные SKU и поставщики


## Архитектура проекта
```text
magnit-logicontrol
│
├── data_platform      # Генерация данных + БД (как prod-слой)
│├── db                # SQLAlchemy модели + SQLite
│├── generators        # Генераторы справочников и событий
│
├── analytics          # EDA и аналитика
│├── notebooks         # Исследовательские ноутбуки
│├── src/db.py         # Подключение к БД
│
├── ab_test            # Финальный A/B тест
│├── data              # CSV датасет для эксперимента
│├── notebooks         # Анализ эксперимента
│├── src               # assignment, метрики, статистика
│
├── app                # Web-дашборд (Flask)
├── bot                # Telegram-бот для KPI
│
├── scripts             # ETL / генерация данных
├── data                # SQLite + CSV
└── README.md
```

## Запуск проекта

### 1. Клонирование репозитория
git clone https://github.com/Artur0023/magnit-logicontrol.git
cd magnit-logicontrol

### 2. Установка зависимостей
pip install -r requirements.txt

### 3. Генерация данных
python -m data_platform.db.init_db
python -m scripts.generate_reference_data
python -m scripts.generate_daily_data

**В результате будет создана:** 
- база данных data/logistics.db
- CSV-датасеты для аналитики и A/B теста

### 4. Запуск web-дашборда
python -m app.main
**Открыть в браузере:**
http://127.0.0.1:8000

### 5. Запуск Telegram-бота
python -m bot.bot

*(не забудь указать токен в .env)*


## Данные и платформа (data_platform)
### Что реализовано:

- SQLite база данных (logistics.db)
- SQLAlchemy модели:
    - DistributionCenter
    - SKU
    - Supplier
    - Shipment
    - Stock / Sales
- Генераторы:
    - Cправочники (DC, SKU, Suppliers)
    - Eжедневные логистические события

### Зачем это нужно:
Чтобы A/B тест и аналитика работали на реалистичных данных, а не искусственном CSV.


## Аналитика и EDA (analytics)
### Notebook: supply_chain_eda.ipynb

- Анализ задержек поставок
- Распределения delay_days
- KPI логистики
- Подготовка гипотез для эксперимента

Используемые инструменты:

- pandas
- matplotlib
- SQL (через SQLite)


## A/B тест (ab_test)
### Бизнес-гипотеза:

- H₀: изменение SLA поставщиков не влияет на задержки
- H₁: новая логика SLA снижает среднюю задержку поставок

### Эксперимент:
- Юнит эксперимента: shipment
- Метрика: delay_days
- Группы:
    - Control — текущая логика
    - Treatment — улучшенная логика SLA


## Реализация
### Assignment:

- assign_groups(df)
- Фиксированное разбиение
- Воспроизводимость
- Отсутствие data leakage

### Метрики

- mean delay
- delta (treatment - control)
- bootstrap confidence interval

### Статистика

- Bootstrap (вместо t-test)
- Оценка распределений
- Power analysis

### Почему bootstrap:
Метрика имеет асимметричное распределение, t-test некорректен.


## Результаты:

- Среднее снижение задержки: ~1 день
- 95% CI bootstrap: не включает 0
- Power ≥ 0.9 при n ≥ 100

### Вывод: Эффект статистически значим и бизнес-существенен.


## Финальный бизнес-вывод:

- Улучшение SLA реально снижает задержки
- Эффект стабилен и масштабируем
- Можно рекомендовать rollout на всю сеть

### Рекомендации бизнесу:

1. Запустить пилот на 1–2 регионах
2. Контролировать supplier mix
3. Мониторить KPI первые 2 недели


## Дополнительно:
### Web Dashboard

- Flask-приложение
- KPI, поставки, остатки

### Telegram Bot

- Быстрый доступ к метрикам
- Использование того же data layer\


## Что можно улучшить:
- Перенос БД на PostgreSQL
- Airflow для оркестрации генерации и ETL
- ML-модель для прогноза OOS
- Авторизация и роли в web-дашборде
- CI/CD для автотестов


## Технологии

- Python (pandas, numpy)
- matplotlib/seaborn
- SQLite + SQLAlchemy
- Flask
- Telegram Bot API
- Jupyter Notebook


## Статус проекта:
Завершен


## Автор:
Artur Bekteshev