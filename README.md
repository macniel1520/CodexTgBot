# CodexTgBot

Telegram bot that receives a photo of food, identifies the dish and returns calories, protein, fats and carbohydrates per 100 grams.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file based on `.env.example` and provide your tokens.

## Run

```bash
python bot.py
```

Start the bot and send it a photo of food. It will reply with the dish name and its nutritional values per 100 grams.
