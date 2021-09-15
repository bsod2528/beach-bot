# Beach-Bot

Beach Bot is a fun and simple template / guide on how to create an amazing DISCORD BOT using Python Language. In this repository, one will learn how to create and run their very own discord bot! 

***PRE REQUISITE -->***
- Install Python:
    Version 3.8 and above version of [python](https://www.python.org/downloads/release/python-380/)
    
- Install GIT:
  - GIT needs to be installed to install discord.py on your computer
  - Click [here](https://git-scm.com/downloads) to download git    \n-> Git needs to be in PATH for it to be usable, try googling `how to add git to Path` to add git to PATH if it isn't already. Example for Windows [here]( https://stackoverflow.com/questions/26620312/git-installing-git-in-path-with-github-client-for-windows)
  -  Run `git` on your command prompt, if it sends a lot of help spam then you're good to go to the next step
   
- Install discord.py:    
  - Run the below command in your [command prompt](https://www.lifewire.com/command-prompt-2625840)
  - `pip install -U git+https://github.com/Rapptz/discord.py` <-- Run this to install Discord.py 2.0

- Some popular Editors to get started with your bot:
  -  [VSCode](https://code.visualstudio.com/download) - Best IDE for people who don't know Python
  -  [Atom](https://atom.io/) - good lightweight and easy to use editor
  -  [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) - heavier IDE for people with more python experience

***Creating an Application (Bot) -->***
You then need to create an application at [Discord Developer Portal](https://discord.com/developers/applications). The following steps show how:- 
- You head over to the portal, go to  `Applications` tab. Click on `New Application`. Give a name for your application and select Create [ Blue Button ]
- You head over to `Bot` under the settings and you click on `Add Bot`. 
And Hence, you have sucessfully created your first bot, all that remains is coding it [:pepeleave:](https://cdn.discordapp.com/emojis/886950503374815312.gif?v=1)

***A Gist of What the Other things in the Portal are -->***
  - UNDER `GENERAL INFORMATION:-`
    - Interaction Endpoint URLs : You can give in links for HTTP POSTs, give in Terms and Conditions and a Privacy Policy Link for you BOT.
    - Application ID : We all have ID's. You can do that by right clicking on your self ( or another user ) and get their ID. If this option is not available, enable `Developer Mode` in Settings of your Discord.

  - UNDER `OAuth2:-`
    - Client Information : Gives basic details such as ID and secret key.
    - Redirect : Where you will paste the invite link for your bot
    - OAuth2 URL Generator : Where you generate your very own invite link for your bot. NOTE --> ONE MUST SELECT `SCOPE` AS `BOT` AND GIVE IN PERMISSIONS GRANDTED TO IT.
  
  - UNDER `BOT:-`
    - This is where one selects basic options for their bot.
    
  - UNDER `RICH PRESENCE:-`
    - Rich Presence is a new feature from Discord that allows you to surface unique, interesting, and actionable data inside a Discord user's profile when they play your game Rich Presence data should give others a clear understanding of what someone is doing so they can decide if they want to play together or not.
    
***Getting your Bot Folder Ready -->***
After you all get this done, open your File Explorer and make a folder called `Discord Bot`. This folder will be specifically used to store the files for our Discord - Bot.
