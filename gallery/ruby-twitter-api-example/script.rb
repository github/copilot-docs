"""Publish text and image on Twitter"""

require 'twitter'

# Create a new Twitter API object
client = Twitter::REST::Client.new do |config|
  config.consumer_key        = ENV['TWITTER_CONSUMER_KEY']
  config.consumer_secret     = ENV['TWITTER_CONSUMER_SECRET']
  config.access_token        = ENV['TWITTER_ACCESS_TOKEN']
  config.access_token_secret = ENV['TWITTER_ACCESS_TOKEN_SECRET']
end

# Publish a tweet with an image
client.update_with_media('Hello World!', 'image.jpg')