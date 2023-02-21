import os
from pyrogram import Client, filters


from Geez import cmds

client=Client

def get_sudo_users():
    try:
        app_name = os.environ.get("HEROKU_APP_NAME")
        api_key = os.environ.get("HEROKU_API_KEY")
        config_var = client.get_config()
        sudo_users = config_var.get("SUDO_USERS", "").split(",")
        return [int(user_id) for user_id in sudo_users if user_id]
    except:
        return []
    
@Client.on_message(filters.command("addsudo", cmds) & filters.me)
async def add_sudo(client, message):
    # Check if the user is the bot owner
    if message.from_user.id == int(os.environ.get("OWNER_ID")):
        # Check if a user ID is provided after the command
        if len(message.command) == 2:
            user_id = int(message.command[1])
        # Otherwise, get the ID of the user who sent the message they're replying to
        elif message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            await message.reply("Please reply to a message or provide a user ID.")
            return
        # Get the existing sudo users from Heroku
        try:
            app_name = os.environ.get("HEROKU_APP_NAME")
            api_key = os.environ.get("HEROKU_API_KEY")
            config_var = await client.get_config()
            sudo_users = config_var.get("SUDO_USERS", "").split(",")
        except:
            app_name = None
            api_key = None
            await message.reply("Error: Failed to retrieve Heroku config vars.")
            return
        # Add the new user ID to the list of sudo users
        if user_id not in sudo_users:
            sudo_users.append(user_id)
            sudo_users_str = ",".join(str(user) for user in sudo_users)
            # Update the Heroku config vars if the app is found
            if app_name and api_key:
                config_var["SUDO_USERS"] = sudo_users_str
                await client.update_config(config_var)
                await message.reply(f"User {user_id} added as a sudo user.")
            else:
                message.reply("Error: Heroku app not found.")
        else:
            await message.reply(f"User {user_id} is already a sudo user.")

@Client.on_message(filters.command("addsudo", cmds) & filters.me)
async def remove_sudo(client, message):
    # Check if the user is the bot owner
    if message.from_user.id == int(os.environ.get("OWNER_ID")):
        # Check if a user ID is provided after the command
        if len(message.command) == 2:
            user_id = int(message.command[1])
            # Get the existing sudo users from Heroku
            try:
                app_name = os.environ.get("HEROKU_APP_NAME")
                api_key = os.environ.get("HEROKU_API_KEY")
                config_var = await client.get_config()
                sudo_users = config_var.get("SUDO_USERS", "").split(",")
            except:
                app_name = None
                api_key = None
                await message.reply("Error: Failed to retrieve Heroku config vars.")
                return
            # Remove the user ID from the list of sudo users
            if str(user_id) in sudo_users:
                sudo_users.remove(str(user_id))
                sudo_users_str = ",".join(sudo_users)
                # Update the Heroku config vars if the app is found
                if app_name and api_key:
                    config_var["SUDO_USERS"] = sudo_users_str
                    await client.update_config(config_var)
                    await message.reply(f"User {user_id} removed from sudo users.")
                else:
                    await message.reply("Error: Heroku app not found.")
            else:
                await message.reply(f"User {user_id} is not a sudo user.")
        else:
            await message.reply("Please provide a user ID to remove.")

@Client.on_message(filters.command("listsudo", cmds) & filters.me)
async def list_sudo(client, message):
    # Check if the user is a sudo user
    if message.from_user.id in get_sudo_users():
        # Get the existing sudo users from Heroku
        try:
            app_name = os.environ.get("HEROKU_APP_NAME")
            api_key = os.environ.get("HEROKU_API_KEY")
            config_var = await client.get_config()
            sudo_users = config_var.get("SUDO_USERS", "").split(",")
        except:
            app_name = None
            api_key = None
            await message.reply("Error: Failed to retrieve Heroku config vars.")
            return
        # Convert user IDs to usernames
        usernames = []
        for user_id in sudo_users:
            try:
                user = await client.get_users(int(user_id))
                usernames.append(user.username or user.first_name)
            except:
                pass
        # Send the list of sudo users as a message
        if len(usernames) > 0:
            message_text = "Sudo users:\n- " + "\n- ".join(usernames)
            await message.reply(message_text)
        else:
            await message.reply("No sudo users found.")
    else:
        await message.reply("You are not authorized to use this command.")