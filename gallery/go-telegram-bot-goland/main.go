package main

import (
	tb "gopkg.in/tucnak/telebot.v2"
	"log"
	"os"
	"time"
)
func main() {
	bot, err := tb.NewBot(tb.Settings{
        Token:  os.Getenv("TELEGRAM_TOKEN"),
        Poller: &tb.LongPoller{Timeout: 10 * time.Second},
    })
	if err != nil {
        log.Fatal(err)
    }
	bot.Handle("/start", func(m *tb.Message) {
        bot.Send(m.Sender, "Hello from copilot, "+m.Sender.FirstName+"!")
    })
	bot.Start()

}
