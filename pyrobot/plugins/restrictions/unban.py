from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.extract_user import extract_user
from pyrobot.helper_functions.cust_p_filters import admin_fliter


@Client.on_message(
    filters.command(["unban", "unmute"], COMMAND_HAND_LER) & admin_fliter
)
async def un_ban_user(_, message):
    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Okay, changed ... now "
                 f "for user_first_name"
                 "You can join the group!"
             )
         else:
             await message.reply_text (
                 "Okay, changed ... now"
                 f "<a href='tg://user?id={user_id}'>"
                 f "{user_first_name}"
                 "</a> to"
                 "You can join the group!"
             )
