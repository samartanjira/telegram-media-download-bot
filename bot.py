import asyncio
import logging
import os
import uuid
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
TEMP_DIRECTORY = os.path.join(os.path.dirname(__file__), 'temp_videos')
os.makedirs(TEMP_DIRECTORY, exist_ok=True)

# --- Whitelist Configuration ---
WHITELIST_FILE = os.path.join(os.path.dirname(__file__), 'whitelist.txt')
WHITELISTED_CHAT_IDS = []

def load_whitelist():
    """Loads whitelisted chat IDs from the file."""
    global WHITELISTED_CHAT_IDS
    try:
        if os.path.exists(WHITELIST_FILE):
            with open(WHITELIST_FILE, 'r') as f:
                content = f.read().strip()
                if content:
                    # Split by comma and convert to integers
                    WHITELISTED_CHAT_IDS = [int(chat_id.strip()) for chat_id in content.split(',')]
                    logging.info(f"Whitelist loaded: {WHITELISTED_CHAT_IDS}")
                else:
                    logging.warning("Whitelist file is empty.")
        else:
            logging.warning("whitelist.txt not found. No one will be able to use the bot.")
    except Exception as e:
        logging.error(f"Error loading whitelist: {e}")

# Load the whitelist on startup
load_whitelist()
# --- End of Whitelist Configuration ---


# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Middleware to check for whitelist
@dp.message.middleware()
async def whitelist_middleware(handler, event: types.Message, data: dict):
    if event.chat.id not in WHITELISTED_CHAT_IDS:
        await event.reply(f"Your Chat ID is: {event.chat.id} send me a private message in my tiktok https://www.tiktok.com/@mryonair")
        return
    return await handler(event, data)


# Dictionary for identifying platform based on URL
PLATFORM_IDENTIFIERS = {
    "instagram.com": "Instagram",
    "tiktok.com": "TikTok",
    "facebook.com": "Facebook",
    "fb.com": "Facebook",
    "youtube.com": "YouTube",
    "youtu.be": "YouTube",
}

async def download_video(message: types.Message, bot: Bot, platform_name: str):
    """
    Handles video download for a given platform.
    """
    progress_msg = await message.reply(f"⏳ Processing {platform_name} link...")
    temp_video_path = None
    try:
        request_id = str(uuid.uuid4())[:8]
        filename = f"{platform_name.lower()}_{message.from_user.id}_{request_id}.%(ext)s"
        output_path = os.path.join(TEMP_DIRECTORY, filename)

        ytdlp_options = {
            'outtmpl': output_path,
            'format': 'best[ext=mp4]/best',
        }
        
        if platform_name.lower() == 'youtube':
            ytdlp_options['format'] = 'best[height<=1080][ext=mp4]/best[height<=1080]/best[ext=mp4]/best'
            ytdlp_options['merge_output_format'] = 'mp4'


        def run_ytdlp():
            with yt_dlp.YoutubeDL(ytdlp_options) as ydl:
                ydl.download([message.text])
                base_path = output_path.replace('.%(ext)s', '')
                for ext in ['.mp4', '.webm', '.mkv']:
                    potential_path = base_path + ext
                    if os.path.exists(potential_path):
                        return potential_path
                return None

        loop = asyncio.get_event_loop()
        temp_video_path = await loop.run_in_executor(None, run_ytdlp)

        if temp_video_path and os.path.exists(temp_video_path):
            await progress_msg.edit_text("✅ Download complete! Sending video...")
            video_file = FSInputFile(temp_video_path)
            await bot.send_video(chat_id=message.chat.id, video=video_file)
            await progress_msg.delete()
        else:
            await progress_msg.edit_text("❌ Failed to download video.")

    except Exception as e:
        logging.error(f"Error processing {platform_name} link: {e}")
        await progress_msg.edit_text(f"❌ An error occurred: {e}")
    finally:
        if temp_video_path and os.path.exists(temp_video_path):
            os.remove(temp_video_path)

async def handle_tiktok(message: types.Message, bot: Bot):
    await download_video(message, bot, "TikTok")

async def handle_instagram(message: types.Message, bot: Bot):
    await download_video(message, bot, "Instagram")

async def handle_youtube(message: types.Message, bot: Bot):
    await download_video(message, bot, "YouTube")


# Handler for /start command
@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.reply("Hello! I am bot radym. Send me a link to download a video.")

# Handler for /status command
@dp.message(Command(commands=["status"]))
async def send_status(message: types.Message):
    await message.reply("I am alive")

# Handler for messages containing links
@dp.message()
async def handle_link(message: types.Message):
    if message.text:
        url = message.text
        if "tiktok.com" in url:
            await handle_tiktok(message, bot)
        elif "instagram.com" in url:
            await handle_instagram(message, bot)
        elif "youtube.com" in url or "youtu.be" in url:
            await handle_youtube(message, bot)
        else:
            # This part might not be reached due to the whitelist middleware,
            # but it's good practice to keep it.
            is_platform_link = False
            for platform in PLATFORM_IDENTIFIERS:
                if platform in url:
                    is_platform_link = True
                    break
            if is_platform_link:
                 await message.reply("This platform is not yet supported for downloading.")
            # If it's not a link to a known platform, do nothing.

async def main():
    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
