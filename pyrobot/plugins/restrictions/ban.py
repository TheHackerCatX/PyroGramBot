from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.extract_user import extract_user
from pyrobot.helper_functions.string_handling import extract_time
from pyrobot.helper_functions.cust_p_filters import admin_fliter


@Client.on_message(filters.command("ban", COMMAND_HAND_LER) & admin_fliter)
async def ban_user(_, message):
    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.ban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is dusting it off..! "
                f"{user_first_name}"
                " Is forbidden."
            )
        else:
            await message.reply_text(
                "Someone else is dusting it off..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " Is forbidden."
            )


@Client.on_message(filters.command("tban", COMMAND_HAND_LER) & admin_fliter)
async def temp_ban_user(_, message):
    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time type specified.  "
                 "Expected m, h, or d, obtained: {}"
            ).format(message.command[1][-1])
        )
        return

    try:
        await message.chat.ban_member(user_id=user_id, until_date=until_date_val)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Someone else is dusting it off..! "
                f"{user_first_name}"
                f" banned for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "Someone else is dusting it off..! "
                f"<a href='tg://user?id={user_id}'>"
                "Leave"
                "</a>"
                f" banned for {message.command[1]}!"
            )
