# Discord-Message-Purge
The lack of the feature is pretty annoying so... Thought i'd try to make something similar. Although be sure to read ReadMe before you hop in and use it.
# Warnings
The project is for educational purposes relating to how discord API could be used for user accounts.
As per license, I don't take any responsibility for what you do with it.
Keep in mind, using this script in practice may result in a ban.
"Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden,
and can result in an account termination if found." -Discord TOS
# How to run
The python script requires an enviornment where discord.py is installed.
# Obtaining Token
Open discord in browser. Hit F12, or open up inspector with a rightclick.
# Firefox:
1. Select "Storage" and select Local storage/discord.com
3. Select Responsive Design Mode (Ctrl+Shift+M)
4. Copy the text labeled as "token"
![image](https://user-images.githubusercontent.com/56764429/144904885-f22666a8-40df-4d00-b92b-210b2df83604.png)
# Chrome
1. Select "Application"
2. In storage select Local storage/discord.com
3. Select "Toogle Device toolbar" (Ctrl+Shift+M) (Pic provided)
4. Copy the text labeled as "token"

![firefox_un1xPlYeR1](https://user-images.githubusercontent.com/56764429/144905314-c9186e37-98dc-41a3-8428-d924d41c30bc.png)

# Obtaining Channel IDs
This one's fairly simple. Either
A. In browser, go to the channel you wish to erase and copy the end of the URL.
B. If you have Developer mode, just right click and copy ID.

# Using the script itself
![image](https://user-images.githubusercontent.com/56764429/144906127-90fedf3f-84cd-4116-bef5-b4ff3aeff1c8.png)
You'll really just need to use these 3. 
1. Token to insert your token
2. filter to insert a filter (in case you want to delete *preciesly* the embarassing times you told people you unironically liked your favourite series) 
3. channelids - The list of IDs of channels you want to clear. Allows you to just dump the IDs of your entire DM history to click run and forget.
(In case you somehow have 0 experience with python, token/filter should be between ""-s, while channel IDs should be written like ["channelID1","channelID2", ... ,"channelIDn"] (Amount of IDs isn't fixed, put in as many as you like. ChannelIDs usually are something like "682416856901050632" (Dummy ID, small chance it exists)

Once again, i remind you that using this may get one banned, the script is for educational purposes.
