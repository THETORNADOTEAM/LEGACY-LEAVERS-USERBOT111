# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio
from userbot import CMD_HELP, DEFAULTUSER
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help_handler(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"#WRONG\n**PLUGIN** : `{args}` â **\nPlease Type the Plugin Name Correctly.**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\tð  "
        await event.edit("â¡")
        await asyncio.sleep(2.5)
        await event.edit(f"**[â¡ðð²ð´ð®ð°ð-ððððð½ððâ¡](t.me/LEGACY_LEAVERS_UB_SUPPORT)**\n\n"
                         f"**âÂ» Bá´á´ á´ê° {DEFAULTUSER}**\n**âÂ» PÊá´É¢ÉªÉ´ : {len(modules)}**\n\n"
                         "**â¢ Má´ÉªÉ´ Má´É´á´ :**\n"
                         f"â°âº| {string} ââ\n\n"
                         f"**License : [Raphielscape Public License 1.d](https://github.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS/blob/Lynx-Userbot/LICENSE)**\n"
                         f"**Copyright Â© 2021 [Legacy-Userbot LLC Company](https://github.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS/)**")
        await event.reply(f"\n**Example** : Type Â» `.help admin` for Admin Plugin Usage Information.")
        await asyncio.sleep(1000)
        await event.delete()
