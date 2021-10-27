# go-telegram-bot-goland  

This is a basic Telegram bot built using github copilot. It uses [telebot module](https://github.com/tucnak/telebot).

After you installed the Copilot plugin and enabled it, you can follow below steps to build your bot.

Create a new project, e.g. `go-telegram-bot-goland`
- add `github.com/tucnak/telebot` to your project by running `go get -u gopkg.in/tucnak/telebot`
- create a new file `main.go` in your project
- import `tb "github.com/tucnak/telebot"`
- in your main func() type `bot, err := tb.NewBot(` and press ALT+\ to invoke copilot.
- by pressing ALT+\ a few more times you can add error checking, command handlers and a call to Start() the bot.
  
To run the telegram bot:
  - You need to use `BotFather` in Telegram to create a new bot and get its token.
  - You'll use the token to create a bot instance. 
  - As a best practice, store the token in the environment variable `TELEGRAM_BOT_TOKEN` and in your code retrieve it from the environment.
    - Start the bot and interact with it in Telegram.

