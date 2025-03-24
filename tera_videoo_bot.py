import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from pytube import YouTube

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the token you get from BotFather on Telegram
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the YouTube Downloader Bot!\n"
        "Send me a YouTube video URL, and I'll download it for you."
    )

# Function to handle YouTube URL messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    
    # Check if the message contains a YouTube URL
    if "youtube.com" in message_text or "youtu.be" in message_text:
        await update.message.reply_text("Processing your video... Please wait.")
        try:
            # Download the video
            video_file = download_youtube_video(message_text)
            
            # Send the video file to the user
            with open(video_file, 'rb') as video:
                await update.message.reply_video(video=video, supports_streaming=True)
            
            # Clean up: remove the downloaded file
            os.remove(video_file)
            
            await update.message.reply_text("Video sent successfully!")
            
        except Exception as e:
            await update.message.reply_text(f"An error occurred: {str(e)}")
    else:
        await
