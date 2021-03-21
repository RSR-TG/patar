from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/mizolibrary")],
        [InlineKeyboardButton("Group" , url="https://t.me/rsrtginfo")],
            "Report Bugs ", url="https://t.me/rsrtginfo")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b> hit\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
