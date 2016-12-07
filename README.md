# Facebook-Messenger-Bot

A simple bot which echoes back the message which you have typed in your facebook page.

# Tools used : 
Django, Ngrok, Facebook Graph API

Ngrok sets up secure tunnels to our localhost i.e. Ngrok gives web accessible URLs and tunnels all traffic from that URL to our localhost. Webhooks, a part of the Facebook Graph API, are used to send payload to the url provided by Ngrok and will be later handled by the bot.

# Installing Ngrok
Go to [Ngrok's download page](https://ngrok.com/), download the zip file, unzip. 

Setting up Ngrok:

    ./ngrok http 8000

For information about how to get page access token and subscription for your page refer to this [link](https://developers.facebook.com/docs/messenger-platform/webhook-reference)
# Quick start

Run the following commands. You will need Python 3 setup

    git clone https://github.com/Gurupradeep/FBMessengerBot.git
    cd bot
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py runserver

Edit the `VERIFY_TOKEN` variable in `https://github.com/PrajwalaTM/Facebook-Messenger-Bot/blob/master/mybot/views.py` to include the Verify token.
It is currently set to `bot_token`. This can be any token as long as it matches the one entered while setting up webhooks.

Once you have your webhook setup, get your Page Access Token. Then set the `PAGE_ACCESS_TOKEN` variable in the file `https://github.com/PrajwalaTM/Facebook-Messenger-Bot/blob/master/mybot/views.py` to your page access token. 
