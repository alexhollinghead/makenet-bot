# makenet-bot
A bot for Princeton's MakeNet Discord Server. This bot is named **Stripes**, and he's written in Python.  

# Getting Started
To get Stripes up and running, you'll need the following Python libraries:
* [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

If you want to develop and extend Stripes, you'll need to invite him to a test server of your making. To do so, first create a file in the bot directory named `.env`. Inside this file, add the line `TOKEN=`. You'll get the value of this token from Discord's website. Visit https://discord.com/developers/applications and create a new application for the bot. You can fill in the General Information to your liking. Next, navigate to the "Bot" tab on the Developer Portal and disable the option "Requires OAuth2 Code Grant". After this, you'll need to get your bot token. Click on the copy button below the text that reads "Click to Reveal Token" and it will be copied to your clipboard. You can paste this value into your `.env` file. **NOTE:** `.env` is in this repository's `.gitignore` file. Make sure your copy of gitignore includes `.env` as well, or you may inadvertently publish your bot token publicly. 

After that, navigate to the OAtuh2 tab and scroll to the "OAuth2 URL Generator" section. From there, check the "bot" box. Beneath the newly generated link, you can select the permissions you'd like to grant the bot and generate a URL to add it to your server. As of now, Stripes requires the following permissions:
* View Channels
* Send Messages
* Read Message History

Once the libraries are installed and you have invited Stripes to a test server, you will be able to start the bot with the command

`python3 main.py`

# References
Please refer to the discord.py library guide: 

https://discordpy.readthedocs.io/en/async/api.html

And the Discord Developer Documentation:

https://discord.com/developers/docs/intro