# CryptoWorld Bot — Telegram-бот-конвертер валют

Простой Telegram-бот, который позволяет быстро и удобно конвертировать одну валюту в другую по текущему курсу. Работает через API обменного сервиса
[open.er-api.com] 
(https://open.er-api.com/v6/latest/).

Функции

- Получение актуального курса валют
- Поддержка популярных валют: доллар, евро, рубль
- Команда `/values` — список доступных валют
- Команды `/start` и `/help` — подсказка по использованию

Как использовать

Отправьте сообщение в формате:

<валюта_из> <валюта_в> <количество>
Пример:

доллар рубль 100

Бот ответит:

100 доллар = 7890.00 рубль

Установка 

1. Клонируйте репозиторий:

git clone https://github.com/StixDager/My_Project.git
cd My_Project
2. Активируйте виртуальное окружение и установите зависимости:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Убедитесь, что вы добавили свой TOKEN в config.py.

4. Запустите бота:

python3 crypto_bot/Mybot.py

🛠️ Структура проекта

project/
│
├── crypto_bot/
│   ├── Mybot.py           # основной файл бота
│   ├── extensions.py      # логика API и конвертации
│   ├── config.py          # настройки: токен и валюты
│
├── requirements.txt       # зависимости
├── README.md              # этот файл

Используемые технологии
Python 3.x

Библиотека pyTelegramBotAPI

open.er API

Автор
Кирилл Рабчинский
