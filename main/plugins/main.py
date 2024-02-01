#TG:Sunrises24BotUpdates 
#@sunrises_24
#telegram

import os
from .. import Drone 
from telethon import events, Button
from main.plugins.rename import media_rename
from main.plugins.compressor import compress
from main.plugins.trimmer import trim
from main.plugins.convertor import mp3, flac, wav, mp4, mkv, webm, file, video
from main.plugins.encoder import encode
from main.plugins.ssgen import screenshot

@Drone.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def compin(event):
    if event.is_private:
        media = event.media
        if media:
            video = event.file.mime_type
            if 'video' in video:
                await event.reply("📽",
                            buttons=[
                                [Button.inline("ENCODE💻", data="encode"),
                                 Button.inline("COMPRESS🗜️", data="compress")],
                                [Button.inline("CONVERT🔁", data="convert"),
                                 Button.inline("RENAME📝", data="rename")],
                                [Button.inline("SSHOTS📸", data="sshots"),
                                 Button.inline("TRIM✂️", data="trim")]
                            ])
            elif 'png' in video:
                return
            elif 'jpeg' in video:
                return
            elif 'jpg' in video:
                return    
            else:
                await event.reply('📦',
                            buttons=[  
                                [Button.inline("RENAME", data="rename")]])
                
@Drone.on(events.callbackquery.CallbackQuery(data="encode"))
async def _encode(event):
    await event.edit("**🔀ENCODE**",
                    buttons=[
                        [Button.inline("240p", data="240"),
                         Button.inline("360p", data="360")],
                        [Button.inline("480p", data="480"),
                         Button.inline("576P", data="576")],
                        [Button.inline("720p", data="720"),
                         Button.inline("1080P", data="1080")],
                        [Button.inline("4K", data="2160"),
                         Button.inline("x264", data="264")],
                        [Button.inline("x265", data="265"),
                        Button.inline("BACK", data="back")]])

@Drone.on(events.callbackquery.CallbackQuery(data="compress"))
async def _compress(event):
    await event.edit("**🗜COMPRESS**",
                    buttons=[
                        [Button.inline("HEVC COMPRESS🗜️", data="hcomp"),
                         Button.inline("FAST COMPRESS🗜️", data="fcomp")],
                        [Button.inline("BACK", data="back")]])
                                          
@Drone.on(events.callbackquery.CallbackQuery(data="convert"))
async def convert(event):
    await event.edit("**🔃CONVERT**",
                    buttons=[
                        [Button.inline("MP3", data="mp3"),
                         Button.inline("FLAC", data="flac"),
                         Button.inline("WAV", data="wav")],
                        [Button.inline("MP4", data="mp4"),
                         Button.inline("WEBM", data="webm"),
                         Button.inline("MKV", data="mkv")],
                        [Button.inline("FILE", data="file"),
                         Button.inline("VIDEO", data="video")],
                        [Button.inline("BACK", data="back")]])
                        
@Drone.on(events.callbackquery.CallbackQuery(data="back"))
async def back(event):
    await event.edit("📽", buttons=[
                    [Button.inline("ENCODE💻", data="encode"),
                     Button.inline("COMPRESS🗜️", data="compress")],
                    [Button.inline("CONVERT🔁", data="convert"),
                     Button.inline("RENAME📝", data="rename")],
                    [Button.inline("SSHOTS📸", data="sshots"),
                     Button.inline("TRIM✂️", data="trim")]])
    
#-----------------------------------------------------------------------------------------

@Drone.on(events.callbackquery.CallbackQuery(data="mp3"))
async def vtmp3(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await mp3(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="flac"))
async def vtflac(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await flac(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="wav"))
async def vtwav(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await wav(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="mp4"))
async def vtmp4(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await mp4(event, msg)
    
@Drone.on(events.callbackquery.CallbackQuery(data="mkv"))
async def vtmkv(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await mkv(event, msg)  
    
@Drone.on(events.callbackquery.CallbackQuery(data="webm"))
async def vtwebm(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await webm(event, msg)  
    
@Drone.on(events.callbackquery.CallbackQuery(data="file"))
async def vtfile(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await file(event, msg)    

@Drone.on(events.callbackquery.CallbackQuery(data="video"))
async def ftvideo(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await video(event, msg)
    
@Drone.on(events.callbackquery.CallbackQuery(data="rename"))
async def rename(event):                            
    button = await event.get_message()
    msg = await button.get_reply_message()  
    await event.delete()
    markup = event.client.build_reply_markup(Button.force_reply())
    async with Drone.conversation(event.chat_id) as conv: 
        cm = await conv.send_message("Send me a new name for the file as a `reply` to this message.\n\n**NOTE:** `.ext` is not required.", buttons=markup)                              
        try:
            m = await conv.get_reply()
            new_name = m.text
            await cm.delete()                    
            if not m:                
                return await cm.edit("No response found.")
        except Exception as e: 
            print(e)
            return await cm.edit("An error occured while waiting for the response.")
    await media_rename(event, msg, new_name)                     
                   
@Drone.on(events.callbackquery.CallbackQuery(data="hcomp"))
async def hcomp(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("compressmedia"):
        await event.delete()
        os.mkdir("compressmedia")
        cmd = '-preset ultrafast -vcodec libx265 -crf 28 -acodec copy'
        await compress(event, msg, cmd)
        os.rmdir("compressmedia")
    else:
        await event.edit("Another process in progress!")
 
@Drone.on(events.callbackquery.CallbackQuery(data="fcomp"))
async def fcomp(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("compressmedia"):
        await event.delete()
        os.mkdir("compressmedia")
        cmd = '-vf scale=-1:360 -c:v libx265 -crf 22 -preset ultrafast -c:a copy'
        await compress(event, msg, cmd)
        os.rmdir("compressmedia")
    else:
        await event.edit("Another process in progress!")
  
@Drone.on(events.callbackquery.CallbackQuery(data="265"))
async def _265(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("compressmedia"):
        await event.delete()
        os.mkdir("compressmedia")
        cmd = '-preset ultrafast -vcodec libx265 -crf 23 -acodec copy'
        await compress(event, msg, cmd, "**ENCODING:**")
        os.rmdir("compressmedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="264"))
async def _264(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("compressmedia"):
        await event.delete()
        os.mkdir("compressmedia")
        cmd = '-preset ultrafast -vcodec libx264 -crf 23 -acodec copy'
        await compress(event, msg, cmd, ps_name="**ENCODING:**")
        os.rmdir("compressmedia")
    else:
        await event.edit("Another process in progress!")
    

@Drone.on(events.callbackquery.CallbackQuery(data="240"))
async def _240(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia")
        #cmd = '-preset ultrafast -c:v libx265 -pix_fmt yuv420p -s 320x240 -crf 28'
        await encode(event, msg, scale=240)
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="360"))
async def _360(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia")
        #cmd = 'ffmpeg -i -preset ultrafast -c:v libx265 -pix_fmt yuv420p -s 640x360 -crf 28'
        await encode(event, msg, scale=360)        
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="480"))
async def _480(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia")
        cmd = '-preset ultrafast -vcodec libx265 -pix_fmt yuv420p10le -crf 28 -s 852x480 -metadata title="𝐄𝐍𝐂𝐎𝐃𝐄𝐃 𝐁𝐘 𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒 𝐇𝐀𝐑𝐒𝐇𝐀 ✨" -metadata:s:v title="𝐄𝐍𝐂𝐎𝐃𝐄𝐃 𝐁𝐘 𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒 𝐇𝐀𝐑𝐒𝐇𝐀 ✨"  -metadata:s:s title="𝗛𝗔𝗥𝗦𝗛𝗔 𝟮𝟰 ~ 𝐒𝐮𝐧𝐫𝐢𝐬𝐞𝐬𝟐𝟒𝐑𝐢𝐩𝐬" -metadata:s:a title="𝗛𝗔𝗥𝗦𝗛𝗔 𝟮𝟰 ~ 𝐒𝐮𝐧𝐫𝐢𝐬𝐞𝐬𝟐𝟒𝐑𝐢𝐩𝐬" -map 0:v -c:a opus -b:a 128k -map 0:a -c:s copy -map 0:s? -strict -2'   
        await encode(event, msg, cmd)
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="576"))
async def _576(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia")
        #cmd = 'ffmpeg -i -preset ultrafast -c:v libx265 -pix_fmt yuv420p -s 960x540 -crf 28'
        await encode(event, msg, scale=576)       
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="720"))
async def _720(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia")
        cmd = f'ffmpeg -i """{new_name}""" -preset ultrafast -vcodec libx265 -pix_fmt yuv420p10le -crf 28 -s 1280x720 -metadata title="𝐄𝐍𝐂𝐎𝐃𝐄𝐃 𝐁𝐘 𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒 𝐇𝐀𝐑𝐒𝐇𝐀 ✨" -metadata:s:v title="𝐄𝐍𝐂𝐎𝐃𝐄𝐃 𝐁𝐘 𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒 𝐇𝐀𝐑𝐒𝐇𝐀 ✨"  -metadata:s:s title="𝗛𝗔𝗥𝗦𝗛𝗔 𝟮𝟰 ~ 𝐒𝐮𝐧𝐫𝐢𝐬𝐞𝐬𝟐𝟒𝐑𝐢𝐩𝐬" -metadata:s:a title="𝗛𝗔𝗥𝗦𝗛𝗔 𝟮𝟰 ~ 𝐒𝐮𝐧𝐫𝐢𝐬𝐞𝐬𝟐𝟒𝐑𝐢𝐩𝐬" -map 0:v -c:a opus -b:a 192k -map 0:a -c:s copy -map 0:s? -strict -2  """{out}""" -y'
        await encode(event, msg, cmd)
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="1080"))
async def _1080(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia") 
        #cmd = 'ffmpeg -i -preset ultrafast -c:v libx265 -pix_fmt yuv420p -s 1920x1080 -crf 28'
        await encode(event, msg, scale=1080)
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="2160"))
async def _2160(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("encodemedia"):
        await event.delete()
        os.mkdir("encodemedia") 
        #cmd = 'ffmpeg -i -preset ultrafast -c:v libx265 -pix_fmt yuv420p -s 3840x2160 -crf 28'
        await encode(event, msg, 2160)
        os.rmdir("encodemedia")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="sshots"))
async def ss_(event):
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    await screenshot(event, msg) 
    
@Drone.on(events.callbackquery.CallbackQuery(data="trim"))
async def vtrim(event):                            
    button = await event.get_message()
    msg = await button.get_reply_message()  
    await event.delete()
    markup = event.client.build_reply_markup(Button.force_reply())
    async with Drone.conversation(event.chat_id) as conv: 
        try:
            xx = await conv.send_message("send me the start time of the video you want to trim from as a reply to this. \n\nIn format hh:mm:ss , for eg: `01:20:29` ", buttons=markup)
            x = await conv.get_reply()
            st = x.text
            await xx.delete()                    
            if not st:               
                return await xx.edit("No response found.")
        except Exception as e: 
            print(e)
            return await xx.edit("An error occured while waiting for the response.")
        try:
            xy = await conv.send_message("send me the end time of the video you want to trim till as a reply to this.  \n\nIn format hh:mm:ss , for eg: `01:20:48` ", buttons=markup)
            y = await conv.get_reply()
            et = y.text
            await xy.delete()                    
            if not et:                
                return await xy.edit("No response found.")
        except Exception as e: 
            print(e)
            return await xy.edit("An error occured while waiting for the response.")
        await trim(event, msg, st, et)
            
