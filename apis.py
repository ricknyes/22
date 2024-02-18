from pyrogram import Client, enums
import re, asyncio
from kvsqlite.sync import Client as uu
import random 
from pyrogram.raw import functions
db = uu('dbs/elhakem.ss', 'rshq')

def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None

def check_format(link):
    pattern = r"https?://t\.me/(\w+)/(\d+)"
    match = re.match(pattern, link)
    
    if match:
        username = match.group(1)
        post_id = int(match.group(2))
        return username, post_id
    else:
        return False

async def join_chat(session: str, chat: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    if db.exists(f'issub_{session[:15]}_{chat}'): return 'o'
    try:
        await c.join_chat(chat)
        db.set(f'issub_{session[:15]}_{chat}', True)
    except Exception as e:
        print(e)
        return False
    return True
async def leave_chats(session: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    types = ['ChatType.CHANNEL', 'ChatType.SUPERGROUP', 'ChatType.GROUP']
    
    async for dialog in c.get_dialogs():
        if str(dialog.chat.type) in types:
            id = dialog.chat.id
            try:
                await c.leave_chat(id)
                await asyncio.sleep(2.5)
            except:
                continue
        else:
            continue
    return True
async def leave_chat(session: str, chat: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    try:
        await c.leave_chat(chat)
    except Exception as e:
        print(e)
        return False
    return True

async def send_message(session:str, chat:str, text: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except Exception as e:
        print(e)
        return False
    info = None
    if detect(chat):
        print('ok')
        try:
            try:
                id = await c.join_chat(chat)
            except:
                pass
            try:
                info = await c.get_chat(chat)
            except Exception as e:
                return False
        except Exception as e:
            return False
    else:
        chat = chat.replace('https://t.me/', '').replace('t.me', '').replace('@', '').replace('.', '')
        print(chat)
        try:
            info = await c.get_chat(chat)
            print(info)
        except Exception as e:
            print(e)
            return False
    if info:
        type = None
        allowed = ['bot', 'user', 'group', 'super', 'bot']
        if info.type == enums.ChatType.BOT:
            type = 'bot'
        if info.type == enums.ChatType.PRIVATE:
            type = 'user'
        if info.type == enums.ChatType.GROUP:
            type = 'group'
        if info.type == enums.ChatType.SUPERGROUP:
            type = 'super'
        if type in allowed:
            if type == 'bot':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                except Exception as e:
                    print(e)
                    return False
                await c.stop()
                return True
            if type == 'group':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                except:
                    return False
                try:
                    await c.leave_chat(info.id)
                except:
                    pass
                await c.stop()
                return True
            if type == 'super':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                except:
                    return False
                try:
                    await c.leave_chat(info.id)
                except:
                    pass
                await c.stop()
                return True
            if type == 'user':
                try:
                    await c.send_message(chat_id=info.id, text=text)
                    
                except Exception as e:
                    print(e)
                    return False
                await c.stop()
                return True
        else:
            return False
    else:
        return False

async def vote_one(session, link, time):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    if db.exists(f'isvote_{session[:15]}_{link}'): return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as e:
            print(e)
            return False
        if msg[0].reply_markup:
            await c.join_chat(username)
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            await asyncio.sleep(time)
            result = await msg[0].click(button)
            if result:
                db.set(f'isvote_{session[:15]}_{link}', True)
                return True
            else:
                db.set(f'isvote_{session[:15]}_{link}', True)
                return True
        else:
            return False
    else:
        return False
async def reactions(session, link, like):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.send_reaction(channel, msg_id, like)
        return True
    except Exception as e:
        print(e)
        return False
async def reaction(session, link):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    if db.exists(f'isreact_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.send_reaction(channel, msg_id, random.choice(rs))
        return True
    except Exception as e:
        print(e)
        return False
async def forward(session, link):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.forward_messages('me', channel, [msg_id])
        return True
    except Exception as e:
        print(e)
        return False
async def view(session, link):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    if db.exists(f'isview_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        z = await client.invoke(functions.messages.GetMessagesViews(
                    peer= (await client.resolve_peer(channel)),
                    id=[int(msg_id)],
                    increment=True
        ))
        db.set(f'isview_{session[:15]}_{link}', True)
        return True
    except Exception as e:
        print(e)
        return False
async def poll(session, link, pi):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    if db.exists(f'ispoll_{session[:15]}_{link}'):
        return 'o'
    x = check_format(link)
    if x:
        channel, msg_id = x
    try:
        await client.vote_poll(channel, msg_id, [pi])
        db.set(f'ispoll_{session[:15]}_{link}', True)
        return True
    except Exception as e:
        print(e)
        return False
async def userbot(session, user):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    try:
        await client.send_message(user, "/start")
        return True
    except Exception as e:
        print(e)
        return False
async def linkbot(session, user, text):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    try:
        await client.send_message(user, text)
        return True
    except Exception as e:
        print(e)
        return False
async def linkbot2(session, user, text, channel_force):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    try:
        await client.join_chat(channel_force)
        await client.send_message(user, text)
        await client.leave_chat(channel_force)
        return True
    except Exception as e:
        print(e)
        return False
async def check_chat(session: str, link: str):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471, no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    x = check_format(link)
    if x:
        username, id = x
        try:
            x = await c.get_chat(username)
        except:
            return False
        return True
    else:
        return False
async def send_comment(session, url, text):
    client = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await client.start()
    x = check_format(url)
    if x:
        channel, msg_id = x
    try:
        await client.join_chat(channel)
        await client.send_message(channel, text, reply_to_message_id=msg_id)
        await client.leave_chat(channel)
        return True
    except Exception as e:
        print(e)
        return False
        
async def leave_chats(session):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    types = ['ChatType.CHANNEL', 'ChatType.SUPERGROUP', 'ChatType.GROUP']
    ty = ['ChatType.BOT']
    async for dialog in c.get_dialogs():
        if str(dialog.chat.type) in types:
            id = dialog.chat.id
            try:
                await c.leave_chat(id)
                await asyncio.sleep(2)
            except:
                continue
        else:
            if str(dialog.chat.type) in ty:
                id = dialog.chat.id
                try:
                    await c.block_user(id)
                    await asyncio.sleep(2)
                    print("Done")
                except Exception as e:
                    print(e)
                    continue
            else:
                continue
    return True
async def join_chatp(session, invite_link):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    await c.start()
    print(invite_link)
    try:
        chat = await c.join_chat(invite_link)
        return True
    except Exception as e:
        print('An error occurred:', str(e))
        return False
async def dump_votess(session, link):
    c = Client('::memory::', in_memory=True, api_hash='a0c224dc0c362b07b450f61b8689977b', api_id=20130471,lang_code="ar", no_updates=True, session_string=session)
    try:
        await c.start()
    except:
        return False
    if not db.exists(f'isvote_{session[:15]}_{link}'): return 'o'
    x = check_format(link)
    if x:
        username, id = x
        try:
            await c.join_chat(username)
            msg = await c.get_messages(chat_id=username, message_ids=[int(id)])
        except Exception as e:
            print(e)
            return False
        if msg[0].reply_markup:
            
            button = msg[0].reply_markup.inline_keyboard[0][0].text
            result = await msg[0].click(button)
            if result:
                db.delete(f'isvote_{session[:15]}_{link}')
            else:
                return False
        else:
            return False
    else:
        return False


async def mill(link):
    points = None
    
    async def handle_message(event):
        nonlocal points
        if "تم اضافة" in str(event.message.text):
            x = event.message.text
            start_index = x.find("تم اضافة **") + len("تم اضافة **")
            end_index = x.find("** نقاط", start_index)
            points = int(x[start_index:end_index].strip())
            print(points)
            await client.disconnect()
        else:
            points = False
            await client.disconnect()
    try:
        client = TelegramClient('session', 29848011, 'ab9bd73716cfe9939ea5ff0bd9bad498')
        try:
            await client.connect()
        except:
            await client.disconnect()
            await client.connect()
        
        try:
            await client.send_message('EEObot', f"/start {link}")
            client.add_event_handler(handle_message, events.NewMessage(from_users='EEObot'))
            await client.run_until_disconnected()
        except Exception as e:
            print(e)
            return False
    except Exception as e:
        print(e)
        pass
    return points