# RadymDownloadBot

[English](#english) | [Українська](#українська)

---

## English

### 📥 RadymDownloadBot 📥

This is a Telegram bot that allows you to download videos from TikTok, Instagram, and YouTube by simply sending a link. The bot is designed with a whitelist system, meaning only authorized users can interact with it.

### ✨ Features

- 🎬 **Video Downloads**: Download videos from TikTok, Instagram, and YouTube.
- 🔒 **Whitelist System**: Only users whose Chat IDs are in `whitelist.txt` can use the bot.
- 🚀 **Easy to Use**: Just send a link, and the bot does the rest.
- ⚙️ **Easy to Deploy**: A few simple steps to get your bot up and running.

### 🛠️ Local Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/radimbig/telegram-media-download-bot.git
    cd telegram-media-download-bot
    ```

2. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Install FFmpeg:**
    ```bash
    # macOS
    brew install ffmpeg

    # Ubuntu/Debian
    sudo apt update && sudo apt install ffmpeg

    # Windows
    # Download from https://ffmpeg.org/download.html
    ```

4. **Create a bot in Telegram:**
    - Talk to [@BotFather](https://t.me/BotFather) on Telegram.
    - Create a new bot and get the **token**.

5. **Create the `.env` file:**
    - Create a file named `.env` in the root of the project.
    - Add your bot token to it:
        ```
        BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
        ```

6. **Set up the whitelist:**
    - Create a file named `whitelist.txt` in the root of the project.
    - Add the Telegram Chat IDs of the users who are allowed to use the bot. Separate multiple IDs with commas.
        ```
        123456789,987654321
        ```
    - To find out a user's Chat ID, they can send any message to the bot (when it's running). The bot will reply with their Chat ID if they are not in the whitelist.

7. **Run the bot:**
    ```bash
    python bot.py
    ```

### 🤖 How to Use

1. **Start the bot:**
    - Find your bot in Telegram and press "Start".

2. **Send a link:**
    - Send a link to a video from TikTok, Instagram, or YouTube.

3. **Get the video:**
    - The bot will process the link, download the video, and send it to you in the chat.

---

## Українська

### 📥 RadymDownloadBot 📥

Це Telegram-бот, який дозволяє завантажувати відео з TikTok, Instagram та YouTube, просто надіславши посилання. Бот розроблений з системою "білого списку", що означає, що тільки авторизовані користувачі можуть взаємодіяти з ним.

### ✨ Функції

- 🎬 **Завантаження відео**: Завантажуйте відео з TikTok, Instagram та YouTube.
- 🔒 **Система "білого списку"**: Тільки користувачі, чиї Chat ID знаходяться в `whitelist.txt`, можуть використовувати бота.
- 🚀 **Простий у використанні**: Просто надішліть посилання, і бот зробить все інше.
- ⚙️ **Легке розгортання**: Кілька простих кроків, щоб запустити вашого бота.

### 🛠️ Локальна установка та налаштування

1. **Клонуйте репозиторій:**
    ```bash
    git clone https://github.com/radimbig/telegram-media-download-bot.git
    cd telegram-media-download-bot
    ```

2. **Встановіть залежності:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Встановіть FFmpeg:**
    ```bash
    # macOS
    brew install ffmpeg

    # Ubuntu/Debian
    sudo apt update && sudo apt install ffmpeg

    # Windows
    # Завантажте з https://ffmpeg.org/download.html
    ```

4. **Створіть бота в Telegram:**
    - Поговоріть з [@BotFather](https://t.me/BotFather) в Telegram.
    - Створіть нового бота та отримайте **токен**.

5. **Створіть файл `.env`:**
    - Створіть файл з назвою `.env` в корені проекту.
    - Додайте до нього токен вашого бота:
        ```
        BOT_TOKEN=ВАШ_ТЕЛЕГРАМ_БОТ_ТОКЕН
        ```

6. **Налаштуйте "білий список":**
    - Створіть файл з назвою `whitelist.txt` в корені проекту.
    - Додайте Telegram Chat ID користувачів, яким дозволено використовувати бота. Розділяйте кілька ID комами.
        ```
        123456789,987654321
        ```
    - Щоб дізнатися Chat ID користувача, він може надіслати будь-яке повідомлення боту (коли він запущений). Бот відповість його Chat ID, якщо його немає в "білому списку".

7. **Запустіть бота:**
    ```bash
    python bot.py
    ```

### 🤖 Як користуватися

1. **Запустіть бота:**
    - Знайдіть вашого бота в Telegram і натисніть "Start".

2. **Надішліть посилання:**
    - Надішліть посилання на відео з TikTok, Instagram або YouTube.

3. **Отримайте відео:**
    - Бот обробить посилання, завантажить відео та надішле його вам у чат.
