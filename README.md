# Telegram Bot with Mini-App Form

This project implements a Telegram bot with a mini-app integration for collecting user data through a form.

## Features

- Telegram bot built with aiogram
- Mini-app with a form for data collection
- Data submission from the mini-app to the bot
- Confirmation message after form submission

## Setup Instructions

### 1. Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send the command `/newbot` and follow the instructions to create a new bot
3. Once created, BotFather will provide you with a bot token
4. Copy this token and replace `YOUR_BOT_TOKEN` in the `config.py` file

### 2. Host the Mini-App

The mini-app needs to be hosted on a web server. You can use GitHub Pages, Netlify, or any other hosting service.

#### Using GitHub Pages:

1. Push this repository to GitHub
2. Go to repository settings > Pages
3. Set the source to the main branch
4. Wait for GitHub to deploy your site
5. Note the URL where your site is published (usually `https://yourusername.github.io/repository-name/`)
6. Update the `WEBAPP_URL` in `config.py` to point to the webapp directory: `https://yourusername.github.io/repository-name/webapp/`

### 3. Configure the Bot for Mini-Apps

1. Go back to [@BotFather](https://t.me/BotFather)
2. Send the command `/mybots` and select your bot
3. Select "Bot Settings" > "Menu Button" > "Configure menu button"
4. Set the menu button URL to your mini-app URL (same as `WEBAPP_URL` in config.py)

### 4. Install Dependencies

```bash
pip install aiogram
```

### 5. Run the Bot

```bash
python bot.py
```

## Usage

1. Start a chat with your bot on Telegram
2. Send the `/start` command
3. Click on the "Fill out form" button to open the mini-app
4. Fill out the form and submit
5. The bot will receive the data and send a confirmation message

## Project Structure

- `bot.py` - Main bot file with aiogram
- `config.py` - Configuration file for bot token and mini-app URL
- `webapp/` - Directory containing the mini-app files
  - `index.html` - HTML form
  - `style.css` - Styling for the form
  - `script.js` - JavaScript for form handling and Telegram WebApp integration

## Notes

- The mini-app uses the Telegram WebApp JavaScript library to communicate with the bot
- The form data is sent as JSON to the bot
- The bot processes the data and sends a confirmation message
