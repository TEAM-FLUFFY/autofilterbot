class script(object):
    START_TXT = """đˇđ´đ {},
đŧđ đŊđ°đŧđ´ đ¸đ <a href=https://t.me/{}>{}</a>, đ¸ đ˛đ°đŊ đŋđđžđđ¸đŗ đŧđžđđ¸đ´đ , đšđđđ đ°đŗđŗ đŧđ´ đđž đđžđđ đļđđžđđŋ đ°đŊđŗ đŧđ°đēđ´ đŧđ´ đ°đŗđŧđ¸đŊ.. đđˇđ´đŊ đđ´đ´ đŧđ đŋđžđđ´đđ..  âĄâĄ"""
    HELP_TXT = """đˇđ´đ {}
đˇđ´đđ´ đ¸đ đđˇđ´ đˇđ´đģđŋ đĩđžđ đŧđ đ˛đžđŧđŧđ°đŊđŗđ."""
    ABOUT_TXT = """âŽ đŧđ đŊđ°đŧđ´: {}
ââââââ°đĩđ đđ§đđâąâââąâÛĒÛĒ
ââ­ââââââââââââââââŖ 
ââŖâĒŧ đđ đđŧđđ - <a href="https://t.me/{}"> {} </a>
ââŖâĒŧ âšī¸âēī¸âī¸1 - <a href="https://t.me/Hacker_A10"> đĩđ ęĢęĒáĨ´đŦęĢđŗ </a>
ââŖâĒŧ đ´đŗđ¸đđ¸đŊđļ - <a href="https://t.me/TEAM_KERALA"> đŦđĨđĸđđđŦ đđđđ áĩáĩáļ  </a>
ââŖâĒŧ âšī¸âēī¸âī¸2 - <a href="https://t.me/pushpa_Reju"> áĩáĩđģđđđđđđŊđđđ </a>
ââŖâĒŧ đ˛đđ´đ°đđ´đ - <a href="https://t.me/TEAM_KERALA"> đŦđĨđĸđđđŦ đđđđ áĩáĩáļ  </a>
ââŖâĒŧ đđ˛đĢđģđĒđģđģđ - đŋđđđžđļđđ°đŧ
ââŖâĒŧ đđĒđˇđ°đžđĒđ°đŽ - đŋđđđˇđžđŊ đš
ââŖâĒŧ đđĒđŊđĒ đđĒđŧđŽ - đŧđžđŊđļđž đŗđą
ââŖâĒŧ đđ¸đŊ đŧđŽđģđŋđŽđģ -  đˇđ´đđžđēđ
ââŖâĒŧ đđžđ˛đĩđ­ đĸđŊđĒđŊđžđŧ - v1.0.1 [ đąđ´đđ° ]
ââ°ââââââââââââââââŖ âââââââââââââââââââââąâÛĒÛĒ"""
    SOURCE_TXT = """<b>Donation</b>


<b>âââââââââá Payment Methods áâââââââââ

âŽ đđŧđŧđ´đšđ˛đŖđŽđ
âŽ đŖđŽđđđē
âŽ đŖđĩđŧđģđ˛đŖđ˛
âŽ đŖđŽđđŖđŽđš

_đđ¨đ§đ­đđđ­ đđ đđ¨đĢ đđ§đ¨đ° đđđ¨đŽđ­ đđĄđ đđđ˛đĻđđ§đ­ đđ§đđ¨_
ââââââââââââá <a href=https://t.me/Aadhi011><b>ęĒęĒáĻęĢáģ</b></a> áââââââââââââ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and áŠááŠá­ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. áŠááŠá­ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>đ˛ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đŽđđ: 
đŖ. /dice - Roll The Dice 
đ¤. /Throw đđ /Dart - đŗđ đŦđēđđž Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
 
<b>Commands and Usage:</b>
âž /filter - <code>add a filter in chat</code>
âž /filters - <code>list all the filters of a chat</code>
âž /del - <code>delete a specific filter in chat</code>
âž /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- áŠááŠá­ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. áŠááŠá­ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text</code>

<b>Alert buttons:</b>
<code>Button Text</code>"""
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
âž /connect  - <code>connect a particular chat to your PM</code>
âž /disconnect  - <code>disconnect from a chat</code>
âž /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of áŠááŠá­

<b>Commands and Usage:</b>
âž /id - <code>get id of a specifed user.</code>
âž /info  - <code>get information about a user.</code>
âž /imdb  - <code>get the film information from IMDb source.</code>
âž /search  - <code>get the film information from various sources.</code>
âž /roll  - <code>get the dice roll play fun gameplays.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
âĸ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
âĸ /purge - delete all messages from the replied to message, to the current message.


<b>NOTE:</b>
This module only works for my Oá¯áEáâĄ

<b>Commands and Usage:</b>
âž /logs - <code>to get the rescent errors</code>
âž /stats - <code>to get status of files in db.</code>
âž /delete - <code>to delete a specific file from db.</code>
âž /users - <code>to get list of my users and ids.</code>
âž /chats - <code>to get list of the my chats and ids </code>
âž /leave  - <code>to leave from a chat.</code>
âž /disable  -  <code>do disable a chat.</code>
âž /ban  - <code>to ban a user.</code>
âž /unban  - <code>to unban a user.</code>
âž /roll  - <code>to roll a only admins.</code>
âž /channel - <code>to get list of total connected channels</code>
âž /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """đŊđđđŧđ: <code>{}</code>
đđđđ¸đ đđđŧâđ: <code>{}</code>
đđđđ¸đ ââđ¸đđ: <code>{}</code>
đđđŧđģ đđđâđ¸đžđŧ: <code>{}</code> đŧđđą
đŊâđŧđŧ đđđâđ¸đžđŧ: <code>{}</code> đŧđđą"""
    LOG_TEXT_G = """#đđđ°đđĢđ¨đŽđŠ
 đžâđđâ âēâē {}(<code>{}</code>)
 đđđđ¸đ đđŧđđšđŧâđ âēâē <code>{}</code>đ¸đģđģđŧđģ đšđ âēâē {}
"""
    LOG_TEXT_P = """#đđđ°đđŦđđĢ
 đđģ âēâē <code>{}</code>
 âđ¸đđŧ âēâē {}
"""
