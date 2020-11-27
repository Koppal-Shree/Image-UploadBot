from pyrogram import Client, filters
import os, shutil
from creds import my
from telegraph import upload_file
import logging

logging.basicConfig(level=logging.INFO)


TGraph = Client(
    "Image upload bot",
    bot_token = my.BOT_TOKEN,
    api_id = my.API_ID,
    api_hash = my.API_HASH
)


@TGraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(f"<b>Hello {message.from_user.first_name}, My Name Is MeG Telegraph Bot 🥳\n\nI'm A <u>Telegraph Uploader Bot.</u>\n\nSend Me Any <u>Image</u>& I'll Upload It To Telegra.ph & Send You Back A Link\n\n🙂 Join & Support Us Via 👉 @MeGLeech.\n\n 🌟 Powered By @MeGBots</b>", True)
 
@TGraph.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text(f"<b> 💁 Hey Its Not Tough To Ise Me...!!!\n\n Just Follow These Steps\n\n ▪️ Send Me Any Image (or) GIF (or) MP4 Below 5MB \n ▪️ Wait For To Generate Link For U\n\n 🌟 Powered By @MeGBots || @MeGLeech</b>", True)
  
@TGraph.on_message(filters.command("about"))
async def about(client, message):
     await message.reply_text(f"<b>🎇 My Name : MeG Telegraph Bot \n\n📝 Language : <a href='https://www.python.org/'>Python3</a>\n\n💞 Developer : @StarkXT8\n\n📢 Channel : @MeGBots\n\n🆘 Support : @MeGBotsChat \n\n♻️ Powered By : @Discovery_Mirror_Channel</b>", True)             

@TGraph.on_message(filters.command("more")) 
async def about(client, message):
    await message.reply_text(f"<b>For Moere Join Our Channel 👉🏻 @MeGBots</b>\n\nSee Our Projects List👉🏻 <a href='https://t.me/MeGBots/29'>At Here</a></b>", True)
@TGraph.on_message(filters.video)
async def getvideo(client, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    imgdir = tmp + "/" + str(message.message_id) +".mp4"
    dwn = await message.reply_text("", True)          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("🚅 Starting Upload 🚅")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dan.edit_text(f"😓 Oopes Something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response [0]}")
    shutil.rmtree(tmp,ignore_errors=True)

@TGraph.on_message(filters.photo)
async def getimage(client, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    imgdir = tmp + "/" + str(message.message_id) +".jpg"
    dwn = await message.reply_text("Downloading Please Wait...🤗", True)          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("Starting Upload...🤗")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp,ignore_errors=True)


TGraph.run()
