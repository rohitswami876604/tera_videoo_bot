import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your actual function to get the direct download link from Terabox
def get_terabox_direct_link(link):
    # This is a placeholder function. You need to implement this based on Terabox's API or web scraping.
    # For now, it just returns the same link.
    return link

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome! Send me a Terabox video link to download.')

# Handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Check if the message is a Terabox link (you might want to add more robust checks)
    if "terabox.com" in user_message:
        direct_link = get_terabox_direct_link(user_message)
        
        if direct_link:
            await update.message.reply_text(f'Downloading video from: {direct_link}')
            
            # Download the video
            response = requests.get(direct_link)
            if response.status_code == 200:
                with open('video.mp4', 'wb') as f:
                    f.write(response.content)
                
                # Send the video back to the user
                await update.message.reply_video(video=open('video.mp4', 'rb'))
            else:
                await update.message.reply_text('Failed to download the video.')
        else:
            await update.message.reply_text('Invalid Terabox link.')
    else:
        await update.message.reply_text('Please send a valid Terabox video link.')

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Main function to run the bot
if __name__ == '__main__':
    application = ApplicationBuilder().token('7629704240:AAHHyFuVPBtf247hFDnRrYZp9yHb7FuUT5U').build()
    
    # Add handlers
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    # Run the bot
    application.run_polling()
