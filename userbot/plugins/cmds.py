import asyncio
from userbot.utils import admin_cmd

@borg.on ( admin_cmd ( pattern="cmds" ,
                       outgoing=True ) )
async def install ( event ) :
    if event.fwd_from :
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell (
        cmd , stdout=asyncio.subprocess.PIPE , stderr=asyncio.subprocess.PIPE
    )
    stdout , stderr = await process.communicate ()
    o = stdout.decode ()
    _o = o.split ( "\n" )
    o = "\n".join ( _o )
    OUTPUT = f"List of Plugins:**\n`{o}`\n\n**TIP: If you want to know the commands for a plugin, do:- \n " \
             f".help <plugin name> **without the < > brackets.**\n__All plugins might not work directly.\n Visit " \
             f"@Dark_cobra_support_group for assistance... "
    await event.edit ( OUTPUT )




@userbot.event
async def on_message ( message ) :
    if message.content.startswith ( '!!!invite' ) :
        msg = "link: https://t.me/vTelegraphBot?client_id=1283371034&scope=bot" \
              "&permissions=8> "
        await client.send_message ( message.channel , msg )
