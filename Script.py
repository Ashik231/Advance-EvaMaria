import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """𝘏𝘦𝘭𝘰 {},
𝘔𝘺 𝘖𝘧𝘧𝘪𝘤𝘪𝘢𝘭 𝘕𝘢𝘮𝘦 𝘪𝘴 <a href=https://t.me/{}>{}</a>, 𝘐 𝘊𝘢𝘯 𝘎𝘪𝘷𝘦 𝘠𝘰𝘶 𝘔𝘰𝘷𝘪𝘦𝘴, 𝘢𝘯𝘥 𝘐𝘢𝘮 𝘖𝘧𝘧𝘪𝘤𝘪𝘢𝘭𝘺 𝘔𝘢𝘥𝘦 𝘧𝘰𝘳 <a href=https://t.me/team_ngc_group>𝘛𝘩𝘪𝘴 𝘎𝘳𝘰𝘶𝘱♡</a></b>...

⇚𝘠𝘰𝘶 𝘊𝘢𝘯 𝘈𝘥𝘥 𝘮𝘦 𝘖𝘯 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱, 𝘐𝘵𝘴 𝘕𝘰𝘵 𝘢 𝘗𝘳𝘰𝘣𝘭𝘦𝘮, 𝘢𝘥𝘥 𝘮𝘦 𝘢𝘴 𝘈𝘥𝘮𝘪𝘯 𝘢𝘯𝘥 𝘐 𝘸𝘪𝘭𝘭 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴⇛"""
    HELP_TXT = """𝘏𝘦𝘺 {}
𝘏𝘦𝘳𝘦 𝘪𝘴 𝘮𝘺 𝘏𝘦𝘭𝘱 𝘊𝘰𝘮𝘮𝘢𝘯𝘥𝘴"""
    ABOUT_TXT = """<b>● 𝘍𝘢𝘮𝘪𝘭𝘺 𝘕𝘢𝘮𝘦: 𝘕𝘎𝘊 𝘐𝘮𝘋𝘣 𝘉𝘰𝘵𝘴</b>
<b>● 𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳: <a href=https://t.me/Unavailable4allTime>𝘈𝘴𝘩𝘪𝘬 𝘔𝘩𝘥</a></b>
<b>● 𝘓𝘪𝘣𝘳𝘢𝘳𝘺: 𝘗𝘺𝘳𝘰𝘨𝘳𝘢𝘮</b>
<b>● 𝘓𝘢𝘯𝘨𝘶𝘢𝘨𝘦: 𝘗𝘺𝘵𝘩𝘰𝘯 3</b>
<b>● 𝘋𝘢𝘵𝘢 𝘉𝘢𝘴𝘦: 𝘔𝘢𝘯𝘨𝘰 𝘋𝘉</b>
<b>● 𝘏𝘰𝘴𝘵 𝘚𝘦𝘳𝘷𝘦𝘳: 🚀
<b>● 𝘝𝘦𝘳𝘴𝘪𝘰𝘯: ᴜᒪᴛʀᴀ</b>
<b>● 𝘔𝘢𝘪𝘯 𝘎𝘳𝘰𝘶𝘱: <a href=https://t.me/team_ngc_group>𝘕𝘦𝘸𝘎𝘦𝘯 𝘊𝘪𝘯𝘦𝘮𝘢𝘢𝘻𝘻𝘻™📌</a></b>
<b>● 𝘕𝘦𝘸 𝘔𝘰𝘷𝘪𝘦𝘴: <a href=https://t.me/TeamNGC>𝘕𝘦𝘸 𝘔𝘰𝘷𝘪𝘦𝘴📂</a></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Unavailable4allTime)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
