from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/bombleebas")],
        [
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", callback_data="help"), 
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Bisubiarenak")],
    ]

    START = """
Hey {}

Welcome to {} 

ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴘᴇʀᴄᴀʏᴀ ʙᴏᴛ ɪɴɪ,  
1. ɢᴀᴜsᴀʜ ʙᴀᴄᴀ ᴘᴇsᴀɴ ɪɴɪ
2. ʙʟᴏᴋɪʀ ʙᴏᴛ ᴀᴛᴀᴜ ᴅᴇʟᴇᴛᴇ ᴄʜᴀᴛ

sᴛɪʟʟ ᴄᴏᴍᴍᴀɴᴅ?
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀsɪᴏɴ 𝟸) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

ʙʏ @Bisubiarenak
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @HiroStringbot

Group Support : [ɢᴀʙᴜɴɢ ᴋᴏɴᴛᴏʟ](https://t.me/hiroshisupport)

Framework : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

Language : [ᴘʏᴛʜᴏɴ](www.python.org)

Developer : @Bisubiarenak
    """
