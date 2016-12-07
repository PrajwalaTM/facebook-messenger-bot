# Facebook-Messenger-Bot

A simple bot which echoes back the message typed in your Facebook page.

# Tools used : 
Django, Ngrok, Facebook Graph API

Ngrok sets up secure tunnels to our localhost i.e. Ngrok gives web accessible URLs and tunnels all traffic from that URL to our localhost. Webhooks, a feature provided by the Facebook Graph API, is used to send a HTTP POST request to the callback url of the app (provided by Ngrok), which will later be handled by the bot.

# Installing Ngrok
Go to [Ngrok's download page](https://ngrok.com/), download the zip file, unzip. 

Setting up Ngrok:

    ./ngrok http 8000

For information about how to get the page access token and subscription for your Facebook page refer [link](https://developers.facebook.com/docs/messenger-platform/webhook-reference)
# Quick start

Run the following commands. You need to setup Python 3:

    git clone https://github.com/PrajwalaTM/Facebook-Messenger-Bot.git
    virtualenv fb-bot
    source fb-bot/bin/activate
    pip install -r requirements.txt
    python manage.py runserver

Edit the `VERIFY_TOKEN` variable in `https://github.com/PrajwalaTM/Facebook-Messenger-Bot/blob/master/mybot/views.py` to include the Verify token.
It is currently set to `bot_token`. This can be any token as long as it matches the one entered while setting up webhooks.

Once you have your webhook setup, get your Page Access Token. Then set the `PAGE_ACCESS_TOKEN` variable in the file `https://github.com/PrajwalaTM/Facebook-Messenger-Bot/blob/master/mybot/views.py` to your page access token. 
