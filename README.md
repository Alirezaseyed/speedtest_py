# Speed Test CLI with Telegram Notification

This Python script measures your internet speed (download, upload, and ping), logs the results, calculates historical averages, and sends the latest test results to a Telegram bot.

## Features
- Measures **Download Speed**, **Upload Speed**, and **Ping**
- Automatically selects the best server for accurate results
- Logs test results into a JSON file (`speedtest_results.json`)
- Calculates historical **average speeds**
- Sends test results to a **Telegram bot** for real-time monitoring

## Requirements
Make sure you have Python installed, then install the required dependencies:
```bash
pip install speedtest-cli requests
```

## Setup
### 1. Configure Telegram Bot
- Create a bot via [BotFather](https://t.me/botfather) on Telegram.
- Get your **Bot Token**.
- Find your **Chat ID** using [this bot](https://t.me/userinfobot).
- Replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` in the script.

### 2. Run the Script
```bash
python speedtest.py
```

## Sample Output
```
{
    "timestamp": "2025-02-14 12:34:56",
    "ISP": "Your ISP",
    "IP Address": "192.168.1.1",
    "Test Server": "New York, USA",
    "Ping (ms)": 20.5,
    "Download Speed (Mbps)": 150.25,
    "Upload Speed (Mbps)": 50.75
}
```

## Contributions
Feel free to fork the repository, improve the script, and submit a pull request! 🚀

