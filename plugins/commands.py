"""
RadioPlayerV2, Telegram Voice Chat Bot
Copyright (C) 2021  Asm Safone <https://t.me/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "šš» **ļ¼Øļ¼„ļ¼¹  ŹÉŖį“į“Ź  [{}](tg://user?id={})**,\n

šµ š  ššŗ š šØš¹ššæš® š ššš¶š° š£š¹š®šš²šæ ā ļø\n\nā šš ššš¦š ā­ [š šš'š¦ š¦š¢š”š šš¢š§](https://t.me/mhd_creation_4_bot)\n\nā šš šš§š°šš« ā­ **[š šš_š§ššš”š­ššš„](https://t.me/mhd_thanzeer)**/nššš¢š­ šš **/help** ššØš« ššØš«š ššØš°šš« š"
HELP = """š·ļø **Need Help?** š¤
__(Join @SafoTheBot For Support)__

š·ļø **Common Commands**:
\u2022 `/play` reply to an audio to play or queue it
\u2022 `/help` shows help for commands
\u2022 `/playlist` shows the playlist
\u2022 `/current` shows playing time of current track
\u2022 `/song` [song name] download the song as audio

š·ļø **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot

š·ļø **Developer: @I_Am_Only_One_1** š
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('CHANNEL', url='https://t.me/AsmSafone'),
        InlineKeyboardButton('SUPPORT', url='https://t.me/SafoTheBot'),
    ],
    [
        InlineKeyboardButton('MORE BOTS', url='https://t.me/AsmSafone/12'),
        InlineKeyboardButton('SOURCE CODE', url='https://github.com/AsmSafone/RadioPlayerV2'),
    ],
    [
        InlineKeyboardButton('āļø HELP āļø', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
