#  Copyright (C) 2021 sandrolort
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ----------------------------------------------------------------------------------------------------------------------
# Code attempts to do the job efficiently, without spamming requests. Therefore (in case it's used) it'll take a while,
# but will do the job safely. You can remove "Await" on line 51 and add a time delay instead if you want something
# faster, but this isn't recommended. Speed depends on how fast your internet is, my guess would be roughly 2 hours
# for 10-20k messages. Then again...
# ----------------------------------------------------------------------------------------------------------------------
# The project is for educational purposes relating to how discord API could be used for user accounts.
# As per license, I don't take any responsibility for what you do with it.
# Keep in mind, using this script in practice may result in a ban.
# "Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden,
# and can result in an account termination if found." - Discord TOS
# ----------------------------------------------------------------------------------------------------------------------

import discord

token = ""  # Token of account.
filter = ""  # The word or term that the code looks for.
channelids = []  # An array of channels to erase.

client = discord.Client()

@client.event
async def on_connect():
    counterChannel = 0
    for channelid in channelids:
        try:
            channel = await client.fetch_channel(channelid)
            temparray = channel.history(limit=40000)
        except:
            print("Error fetching the channel.")
            break
        try:
            channelname = channel.name
        except:
            channelname = channel.recipient.name
        counter = 0
        async for message in temparray:
            counter += 1
            if message.author == client.user:
                if filter in message.content.lower():
                    print("Deleted a message at " + str(counter) + " chat " + str(
                        "counterChannel = 0") + " (aka " + channelname + ")")
                    try:
                        await message.delete()
                    except:
                        print("Possible system message.")
        print("Temporarily done.")
    print("done")


client.run(token, bot=False)