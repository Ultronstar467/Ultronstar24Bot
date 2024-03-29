#TG:Sunrises24BotUpdates 
#@sunrises_24

import os
from .. import Drone, AUTH_USERS
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG0 as file
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention
from ethon.mystarts import vc_menu
from main.plugins.actions import heroku_restart

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'👋 Hey [{event.sender.first_name}](tg://user?id={event.sender_id}) ♡\n\nI am Telegram Most Powerful Video Convertor Bot\n\nUse Help Button to know How to use me\n\nMaintained By : @Sunrises24BotUpdates', 
                      buttons=[[
                         Button.inline("𝐒𝐄𝐓 𝐓𝐇𝐔𝐌𝐁🖼️", data="sett"),
                         Button.inline("𝐃𝐄𝐋 𝐓𝐇𝐔𝐌𝐁🗑️", data='remt')],
                         [
                         Button.inline("𝐇𝐄𝐋𝐏 🌟", data="plugins"),
                         Button.url("𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢", url=f"{SUPPORT_LINK}")],
                         [
                         Button.inline("𝐑𝐄𝐒𝐓𝐀𝐑𝐓 🔁", data="restart"),    
                         Button.inline("𝐂𝐋𝐎𝐒𝐄 ❌", data="close")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)

@Drone.on(events.callbackquery.CallbackQuery(data="close"))
async def close(event):
    await event.delete()
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[
                       Button.inline("NOTICE", data="notice")],
                       [
                       Button.inline("𝐂𝐋𝐎𝐒𝐄 ❌", data="close")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")
    
@Drone.on(events.callbackquery.CallbackQuery(data="restart"))
async def res(event):
    if not f'{event.sender_id}' == f'{int(AUTH_USERS)}':
        return await event.edit("Only authorized user can restart!")
    result = await heroku_restart()
    if result is None:
        await event.edit("You have not filled `HEROKU_API` and `HEROKU_APP_NAME` vars.")
    elif result is False:
        await event.edit("An error occured!")
    elif result is True:
        await event.edit("Restarting app, wait for a minute.")


