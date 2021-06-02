# [Copilot examples](../README.md) › [Publish a Tweet](/README.md) (Ruby)

In this example we write some Ruby to publish a Tweet with the assumption that you have no prior experience of doing so, nor knowledge of what 3rd party Ruby Gems or code snippets can be used.

We assume you have (created) a Twitter account and that you're somewhat familiar with Ruby, Ruby gems, Bundler, etc. Oh yeah, and that GitHub Copilot is installed :)

## Setup:

Before you start, ceate a new read+write app on the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard) and keep a note of the following values: 

* `TWITTER_CONSUMER_KEY`
* `TWITTER_CONSUMER_SECRET`
* `TWITTER_ACCESS_TOKEN`
* `TWITTER_ACCESS_TOKEN_SECRET`

## Steps:

- Create a new file called `script.rb`

- Type `"""Publish text and image on Twitter"""` on line 1 and press <kbd>CTRL</kbd> + <kbd>RETURN</kbd> to view suggestions.

- Accept the following solution:

  ```ruby
  require 'twitter'

  # Create a new Twitter API object
  client = Twitter::REST::Client.new do |config|
    config.consumer_key        = ENV['TWITTER_CONSUMER_KEY']
    config.consumer_secret     = ENV['TWITTER_CONSUMER_SECRET']
    config.access_token        = ENV['TWITTER_ACCESS_TOKEN']
    config.access_token_secret = ENV['TWITTER_ACCESS_TOKEN_SECRET']
  end

  # Create a new message
  message = Twitter::Tweet.new do |tweet|
    tweet.text = 'Hello world'
  end

  # Publish the message
  client.update(message)
  ```

- If you haven't already, set the environment variables on your machine with `setenv`, `export`, etc. E.g. on macOS that would be
  
  ```bash
  export YOUR_CONSUMER_KEY=foobar
  export YOUR_CONSUMER_SECRET=foobar
  export YOUR_ACCESS_TOKEN=foobar
  export YOUR_ACCESS_TOKEN_SECRET=foobar
  ```

- Replace the "Test" string in `client.update("Test")` with the message of your choice e.g.

  ```ruby
  client.update("I posted this Tweet using code provided by by GitHub Copilot! 🤯")
  ```

- Run the script and take a look at your Twitter profile to see your Tweet.

- Now, let's see if we can post an image too. Remove the following code:

  ```ruby
  # Publish the message
  client.update(message)
  ```


- Type `# Publish a Tweet with an image` on the final and press <kbd>CTRL</kbd> + <kbd>RETURN</kbd> to view suggestions. Accept the following suggestion:

  ```ruby
  # Publish a tweet with an image
  client.update_with_media('Hello World!', 'image.jpg')
  ```

- Edit the script text and image to your liking to run it again.

That's it. Hopefully you didn't run to any problems. We tried to keep this example simple and lacking in error-handling. Hopefully any issues are straightforward to troubleshoot.

#

‹ [back to list of Copilot examples](../README.md)
