"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`░█████╗░██╗░█████╗░░█████╗░██╗\n██╔══██╗██║██╔══██╗██╔══██╗██║\n██║░░╚═╝██║███████║██║░░██║██║\n██║░░██╗██║██╔══██║██║░░██║╚═╝\n╚█████╔╝██║██║░░██║╚█████╔╝██╗\n░╚════╝░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝\n\nCiao! Sono sempre tnove, ma con un bot installato nel mio account!\"n
                     "`Il mio capo`: @TnOvE2O22\n\n"
                     "(Non sono un hacker e non posso hackerarvi, state tranquilli è solo un userbot)")
