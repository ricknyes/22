import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    import shutil
    import time
    import datetime
except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    pass
w = json.loads(open('config.json', 'r+').read())
token = w['bot_token']
stypes = ['member', 'administrator', 'creator']

member_price = w['prices']['member']
vote_price = w['prices']['vote']
link_price = w['prices']['link']
spam_price = w['prices']['spam']
react_price = w['prices']['react']
forward_price = w['prices']['forward']
view_price = w['prices']['view']
poll_price = w['prices']['poll']
userbot_price = w['prices']['userbot']
linkbot_price = w['prices']['linkbot']
comment_price = w['prices']['comments']
linkbot2_price = w['prices']['linkbot2']
mm = w['start_msg']

db = uu('dbs/elhakem.ss', 'rshq')
print(db)
bk = mk(row_width=1).add(btn('رجوع', callback_data='back'))
bot = TeleBot(token="6825651369:AAF4qwRLeDKGrk1oBDWbdsCuWuQIzdcmISs",num_threads=45,threaded=True,skip_pending=True,parse_mode='html', disable_web_page_preview=True) # توكن بوت الرشق الاساسي هنا
if not db.get('accounts'):
    db.set('accounts', [])
    pass

admin = 6227455684 #الادمن
if not db.get("admins"):
    db.set('admins', [admin, 6024124201])
if not db.get('badguys'):
    db.set('badguys', [])
if not db.get('force'):
    db.set('force', [])

if not db.get('force_ch'):
    db.set('force_ch', [])
    
sudo = w['sudo']
def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
        print(x)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
@bot.message_handler(regexp='^/start$')
def start_message(message):
    user_id = message.from_user.id
    count_ord = db.get('orders') if db.get('orders') else 1
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
    for temp in a:
        db.delete(f'{a}_{user_id}_proccess')
    keys = mk(row_width=2)
    if user_id in db.get("admins") or user_id == sudo:
        keys_ = mk()
        btn01 = btn('الاحصائيات', callback_data='stats')
        btn02 = btn("اذاعة", callback_data='cast')
        btn05, btn06 = btn('حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
        btn09 = btn('معرفة عدد الارقام', callback_data='numbers')
        btna = btn('تفعيل ViP', callback_data='addvip')
        btnl = btn('الغاء ViP', callback_data='lesvip')
        leave = btn('مغادرة كل الحسابات من قناة', callback_data='leave')
        lvall = btn('مغادرة كل القنوات والمجموعات', callback_data='lvall')
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        keys_.add(leave)
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        les = btn('خصم نقاط', callback_data='lespoints')
        btn10 = btn('اضافه نقاط ', callback_data='addpoints')
        btn03 = btn('اضافة ادمن', callback_data='addadmins')
        btn04 = btn('مسح ادمن', callback_data='deladmin')
        btn012 = btn('الادمنية ', callback_data='admins')
        btn013 = btn('سحب اصوات', callback_data='dump_votes')
        btn105 = btn('سبام رسائل (بوتات ، جروبات ، حسابات) ', callback_data='spams')
        btn150 = btn('رشق روابط دعوة اشتراك اجبارى',callback_data='linkbot2')
        btn059 = btn('نسخة احتياطية لقاعدة البيانات', callback_data='zip_all')
        code = btn('انشاء كود هدية', callback_data='gen_code')
        btn19 = btn('سعر التمويل لكل عضو', callback_data='price_join')
        btn20 = btn('نقاط الاشتراك بالقناة', callback_data='coin_join')
        btn21 = btn('اقل حد للتمويل', callback_data='less_tmoil')
        btn22 = btn('اقل حد لتبديل النقاط من بوت المليار', callback_data='less_change')
        btn23 = btn('الغاء تمويل قناة', callback_data='can_tmoil')
        btn24 = btn('احصائيات التمويل', callback_data='stats_tmoil')
        keys_.add(btn03, btn04)
        keys_.add(btn10, btn11)
        keys_.add(btn012, les)
        keys_.add(lvall)   
        keys_.add(btn09)
        keys_.add(btna, btnl)
        keys_.add(btn013)
        keys_.add(btn105,  btn150)
        keys_.add(btn059)
        keys_.add(code)
        keys_.add(btn19, btn20)
        keys_.add(btn21, btn22)
        keys_.add(btn23, btn24)
        bot.reply_to(message, '**• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖**\n\n- يمكنك التحكم في البوت الخاص بك من هنا \n\n===================', reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                try:
                    x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                    if str(x.status) in stypes:
                        pass
                    else:
                        bot.reply_to(message, f'• عليك الاشترك بقناة البوت اولا \n• @{channel}')
                        return
                except:
                    pass
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.send_message(chat_id=int(sudo), text=f'٭ *تم دخول شخص جديد الى البوت الخاص بك 👾*\n\n•_ معلومات العضو الجديد ._\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}\n\n*• عدد الاعضاء الكلي* : {good}', parse_mode="Markdown")
        coin = get(user_id)['coins']
        btn1 = btn(f'رصيدك : {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('معلومات حسابك 🗃', callback_data='account')
        btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='send')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/zzzhs9')
        btn7 = btn('شراء رصيد 💰', callback_data='buy')
        btn9 = btn('استخدام كود💳 ', callback_data='use_code') 
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn7)
        keys.add(btn9)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        
        return bot.reply_to(message, mm, reply_markup=keys)
    do = db.get('force')
    if do is not None:
        for channel in do:
            try:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    pass
                else:
                    bot.reply_to(message, f'• عليك الاشتراك بقناة البوت اولا\n- @{channel}')
                    return
            except:
                pass
    
    coin = get(user_id)['coins']
    btn1 = btn(f'رصيدك : {coin}', callback_data='none')
    btn2 = btn('الخدمات 🛍', callback_data='ps')
    btn3 = btn('معلومات حسابك 🗃', callback_data='account')
    btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
    btn5 = btn('تحويل نقاط ♻️', callback_data='send')
    btn6 = btn('قناة البوت 🩵', url='https://t.me/zzzhs9')
    btn7 = btn('شراء رصيد 💰', callback_data='buy')
    btn9 = btn('استخدام كود💳 ', callback_data='use_code') 
    keys.add(btn1)
    keys.add(btn2)
    keys.add(btn4, btn7)
    keys.add(btn9)
    keys.add(btn3, btn5)
    keys.add(btn6)
    keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))

    return bot.reply_to(message, mm, reply_markup=keys)


@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    join_user = message.from_user.id

    to_user = int(message.text.split("/start ")[1])
    if join_user == to_user:
        start_message(message)
        bot.send_message(join_user,f'لا يمكنك الدخول عبر الرابط الخاص بك ❌')
        return
    if not check_user(join_user):
        someinfo = get(to_user)
        if join_user in someinfo['users']:
            start_message(message)
            return
        else:
            dd = link_price
            someinfo['users'].append(join_user)
            someinfo['coins'] = int(someinfo['coins']) + dd
            info = {'coins': 0, 'id': join_user, 'premium': False, "users": []}
            set_user(join_user, info)
            set_user(to_user, someinfo)
            bot.send_message(to_user,f'• قام {message.from_user.mention} بالدخول الى رابط الدعوة الخاص بك وحصلت علي {dd} نقطة ✨')
            good = 0
            users = db.keys('user_%')
            for ix in users:
                try:
                    d = db.get(ix[0])['id']
                    good+=1
                except: continue
            bot.send_message(chat_id=int(sudo), text=f'٭ *تم دخول شخص جديد الى البوت الخاص بك 👾*\n\n•_ معلومات العضو الجديد ._\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}\n\n*• عدد الاعضاء الكلي* : {good}', parse_mode="Markdown")
            start_message(message)
    else:
        start_message(message)
        return

@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    if cid in db.get('badguys'): return
    do = db.get('force')
    count_ord = db.get('orders') if db.get('orders') else 1
    if do != None:
        for channel in do:
            try:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=cid)
                if str(x.status) in stypes:
                    pass
                else:
                    bot.edit_message_text(text=f'• عليك الاشتراك بقناة البوت اولا قبل استخدامه\n• @{channel}', chat_id=cid, message_id=mid)
                    return
            except:
                pass
    admins = db.get('admins')
    d = db.get('admins')
    a = ['leave', 'member', 'vote', 'spam']
    for temp in a:
        db.delete(f'{a}_{cid}_proccess')
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    d = db.get('admins')
    user_id = call.from_user.id
    if data == 'tmoo_bot':
        price_tmoo_bot = db.get('price_tmoo_bot') if db.exists('price_tmoo_bot') else 5
        text = f'• ارسل عدد الاعضاء الذي تريد تمويلها لبوت التليجرام الخاص بك\n\n• سعر التمويل لكل عضو : {price_tmoo_bot}'
        x = bot.edit_message_text(text=text, chat_id=cid, message_id=mid, reply_markup=bk)
        type = 'tmoo_bot'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'gen_code':
        x = bot.edit_message_text(text='• ارسل الان الكود الذي تريد صنعه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, gen_code_name)
    if data == 'dailygift':
        x = check_dayy(call.from_user.id)
        if x is not None:
            xduration = 59342
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            date_str = target_datetime.strftime('%Y/%m/%d')
            date_str2 = target_datetime.strftime('%I:%M:%S %p')
            yduration = 18120
            result = xduration * (10 ** len(str(yduration))) + yduration
            bot.answer_callback_query(call.id, text=f'طالب بالهدية غدا في: {date_str2}',show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            info = db.get(f'user_{call.from_user.id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{call.from_user.id}", info)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"• تهانيناً، لقد حصلت على هدية يومية بقيمة {daily_gift} 🎁", reply_markup=bk)
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            return
    if data == 'numbers':
        d = len(db.get('accounts'))
        bot.answer_callback_query(call.id, text=f'عدد ارقام البوت : {d}', show_alert=True)
        return
    if data == 'price_join':
        x = bot.edit_message_text(text='ارسل الان عدد النقاط الجديدة', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, price_joinn)
    if data == 'coin_join':
        x = bot.edit_message_text(text='ارسل الان عدد النقاط الجديدة', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, coin_joinn)
    if data == 'less_tmoil':
        x = bot.edit_message_text(text='ارسل الان عدد الحد الادني لطلب تمويل اعضاء', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, less_tmoil)
    if data == 'addpoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد اضافة النقاط له', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    if data == 'send':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تحويل النقاط له.', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, send)
    if data == 'addadmins':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addvip':
        type = 'add'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد تفعيل vip له',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, vipp, type)
    if data == 'lesvip':
        type = 'les'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالة vip منه',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, vipp, type)
    if data == 'deladmin':
        type = 'delete'
        x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'banone':
        if cid in db.get("admins") or cid == sudo:
            type = 'ban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") or cid == sudo:
            type = 'unban'
            x  = bot.edit_message_text(text=f'• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") or cid == sudo:
            x  = bot.edit_message_text(text=f'ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'lespoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تخصم النقاط منه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if call.data.startswith('canceltmoil:'):
        ch = call.data.split(':')[1]
        chats = db.get("force_ch")
        if ch in chats:
            chats.remove(ch)
            db.set("force_ch", chats)
        bot.edit_message_text(text=f"⌁︙تم الغاء تمويل قناة {ch} بنجاح ✅", chat_id=cid, message_id=mid)
    if data == 'can_tmoil':
        x = bot.edit_message_text(text='ارسل الان معرف القناة التي تريد الغاء تمويلها \n⌁︙يجب ان يكون حروف المعرف صغير @gkwosjp مثل  وليس مثل @GKWOSJP', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, can_tmoil)
    if data == 'report':
        report(call)
    if data == 'skip':
        skip(call)
    if data == 'check_join':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                if i in chats_joining:
                    bot.answer_callback_query(call.id, text=f"لقد حصلت علي نقاط من هذه القناة بالفعل ❌",show_alert=True)
                    return
                try:
                    x = bot.get_chat_member(chat_id=i, user_id=user_id)
                except Exception as a:
                    if "bot was kicked" in str(a):
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        ids = db.get(f"id_{i}")
                        bot.send_message(chat_id=int(ids), text=f"*⌁︙لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {i} ❌*", parse_mode="Markdown")
                    elif "chat not found" in str(a):
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(channel)
                        db.set("force_ch", chats_dd)
                        ids = db.get(f"id_{i}")
                        bot.send_message(chat_id=int(ids), text=f"*⌁︙لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {i} ❌*", parse_mode="Markdown")
                if str(x.status) in stypes:
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    bot.answer_callback_query(call.id, text=f"تم اضافة {coin_join} نقاط بنجاح ✅",show_alert=True)
                    typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
                    ftt = typ + 0.1
                    db.set(f"typ_{user_id}", float(ftt))
                    ids = db.get(f"id_{i}")
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    count = db.get(f"count_{i}")
                    countcc = int(count) - 1
                    db.set(f"count_{i}", countcc)
                    joo = db.get(f"user_{user_id}")
                    joo['coins'] = int(joo['coins']) + int(coin_join)
                    db.set(f"user_{user_id}", joo)
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(i)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(i)
                    name = chat_inf.title
                    count = db.get(f"count_{i}")
                    ids = db.get(f"id_{i}")
                    nextch(call)
                    if int(count) <= 0:
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else ""
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) ب {mem} بنجاح ✅", parse_mode="Markdown")
                        iddd = 1540163051
                        bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناة [{name}](https://t.me/{ii}) بنجاح ✅", parse_mode="Markdown")
                    else:
                        ii = i.replace('@', '')
                else:
                    bot.answer_callback_query(call.id, text="اشترك بالقناة اولا ❌",show_alert=True)
    if data == 'join_ch':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                count = db.get(f"count_{i}")
                ids = db.get(f"id_{i}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    try:
                        chat_info = bot.get_chat(i)
                    except Exception as a:
                        if "bot was kicked" in str(a):
                            chats_dd = db.get('force_ch')
                            chats_dd.remove(i)
                            db.set("force_ch", chats_dd)
                            ids = db.get(f"id_{i}")
                            bot.send_message(chat_id=int(ids), text=f"*⌁︙لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {i} ❌*", parse_mode="Markdown")
                        elif "chat not found" in str(a):
                            chats_dd = db.get('force_ch')
                            chats_dd.remove(i)
                            db.set("force_ch", chats_dd)
                            ids = db.get(f"id_{i}")
                            bot.send_message(chat_id=int(ids), text=f"*⌁︙لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {i} ❌*", parse_mode="Markdown")
                    name = chat_info.title
                    ii = i.replace('@', '')
                    mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅", parse_mode="Markdown")
                    iddd = 1540163051
                    bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) ب {mem} بنجاح ✅", parse_mode="Markdown")
                    db.set(f"mem_{i}", 0)
                else:
                    try:
                        chat_info = bot.get_chat(i)
                    except Exception as a:
                        if "bot was kicked" in str(a):
                            chats_dd = db.get('force_ch')
                            chats_dd.remove(i)
                            db.set("force_ch", chats_dd)
                            ids = db.get(f"id_{i}")
                            bot.send_message(chat_id=int(ids), text=f"⌁︙لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {i} ❌")
                        elif "chat not found" in str(a):
                            chats_dd = db.get('force_ch')
                            chats_dd.remove(i)
                            db.set("force_ch", chats_dd)
                            ids = db.get(f"id_{i}")
                            bot.send_message(chat_id=int(ids), text=f"⌁︙لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {i} ❌")
                    name = chat_info.title
                    ii = i.replace('@', '')
                    k = f'''اشترك فالقناة {i}'''
                    keys = mk(
                        [
                            [btn(text='اشتركت ✅', callback_data='check_join')],
                            [btn(text='تبليغ 📛', callback_data='report'), btn(text='تخطي ⚠️', callback_data='skip')],
                            [btn(text='‹ رجوع ↻›', callback_data='collect')]
                        ]
                    )
                    bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                    return
            kk = f"لا يوجد قنوات حالياً 🤍"
            key = mk(
                [
                    [btn(text='‹ رجوع ↻›', callback_data='collect')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key)
            return
    if data == 'stats_tmoil':
        chats = db.get("force_ch")
        ln = len(chats)
        xx = f"⌁︙اليك قائمة بالقنوات التي يتم تمويلها\n⌁︙يتم تمويل : {ln}\n\n"
        for i in chats:
            count = db.get(f"count_{i}")
            xx+= f"القناة ↫ {i} | متبقي : {count}\n"
            bot.edit_message_text(text=xx, chat_id=cid, message_id=mid)
    if data == 'back':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        btn1 = btn(f'رصيدك : {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('معلومات حسابك 🗃', callback_data='account')
        btn4 = btn('تجميع الرصيد ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='send')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/zzzhs9')
        btn7 = btn('شراء رصيد 💰', callback_data='buy')
        btn9 = btn('استخدام كود💳 ', callback_data='use_code') 
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn7)
        keys.add(btn9)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'getinfo':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص الذي تريد معرفة معلوماته', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, get_info)
    if data == 'lvall':
        keys = mk(row_width=2)
        btn2 = btn('تاكيد المغادرة',callback_data='lvallc')
        btn3 = btn('الغاء',callback_data='cancel')
        keys.add(btn2)
        keys.add(btn3)
        bot.edit_message_text(text='هل انت متاكد من مغادرة كل القنوات والمجموعات ؟',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'priv_serv':
        sess = db.get(f"ses_{cid}") if db.exists(f"ses_{cid}") else []
        ses = len(sess)
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem:
            keys = mk(row_width=2)
            btn2 = btn(f'عدد ارقامك : {ses}', callback_data='non')
            btn3 = btn('تسليم ارقام',url='https://t.me/ALISMS7_BOT')
            btn4 = btn('تصويت لايكات مسابقات', callback_data='private_vote')
            btn6 = btn('سبام رسائل (بوتات ، جروبات ، حسابات)', callback_data='spams_private')
            btn5 = btn('تنظيف حساباتك', callback_data='pri_leave_sure')
            btn7 = btn('خروج من قناة', callback_data='pri_leave')
            btn8 = btn('ارسال تفاعلات',callback_data='pri_react')
            btn9 = btn('انضمام لقناة',callback_data='pri_members')
            keys.add(btn2,btn3)
            keys.add(btn4)
            keys.add(btn6)
            keys.add(btn8, btn9)
            keys.add(btn5, btn7)
            keys.add(btn('رجوع ', callback_data='ps'))
            bot.edit_message_text(text='• مرحبا بك في قسم الخدمات الخاصة 👤\n• يمكنك تسليم حسابات في بوت التسليم واستخدامها في جميع خدماتك بشكل خاص ومستقل〽️',reply_markup=keys,chat_id=cid,message_id=mid)
        else:
            keys = mk(row_width=2)
            keys.add(btn('ما هي الخدمات الخاصة ؟', url='https://t.me/zzzhs9/1126'))
            keys.add(btn('رجوع ↪️', callback_data='ps'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'private_vote':
        a = ['leave', 'member', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads']
        for temp in a:
            db.delete(f'{temp}_{cid}_proccess')
        db.set(f'vote_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• حسنا ، ارسل الان عدد التصويتات التي تريدها\n\n• سيتم التصويت باستخدام حساباتك في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
        type = 'private_vote'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'use_code':
        db.set(f'code_{cid}_proccess', True)
        keys = mk(row_width=2)
        keys.add(btn('‹ رجوع ↻›', callback_data='back'))
        x = bot.edit_message_text(text='⌁︙ ارسل الكود الان',reply_markup=keys,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, use_codes)
    if data == 'spams_private':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
        for temp in a:
            db.delete(f'{temp}_{cid}_proccess')
        db.set(f'spam_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد الرسائل التي تريد ارسالها اسبام',chat_id=cid,message_id=mid)
        type = 'msgs_private'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'pri_leave_sure':
        keys = mk(row_width=2)
        btn1 = btn('الغاء ❌', callback_data='priv_serv')
        btn3 = btn('تاكيد ✅',callback_data='pri_leave')
        keys.add(btn3, btn1)
        bot.edit_message_text(text='• هل انت متاكد من مغادرة كل القنوات والمجموعات من حساباتك الخاثة ؟ ',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'pri_leave':
        bot.edit_message_text(text='• تم بدء مغادرة كل القنوات والمجموعات بنجاح ✅',chat_id=cid,message_id=mid)
        acc = db.get(f"ses_{cid}") if db.exists(f"ses_{cid}") else []
        amount = len(acc)
        true = 0
        for amount in acc:
            try:
                true+=1
                o = asyncio.run(pri_leave(amount['s']))  
            except Exception as e:
                print(e)
                continue
        id = call.from_user.id
        bot.send_message(chat_id=id, text=f'• تم بنجاح الخروج من كل القنوات والمجموعات \n• تم الخروج من <code>{true}</code> حساب بنجاح ✅')
    if data == 'pri_react':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'reacts','chtime','send','send_link','code','tmoo', 'ads']
        for temp in a:
            db.delete(f'{temp}_{cid}_proccess')
        xxx = db.get(f'react_{cid}_proccess')
        if xxx != True and xxx == None:
            db.set(f'react_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها \n\n',chat_id=cid,message_id=mid,reply_markup=bk)
            type = 'pri_react'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها \n\n',chat_id=cid,message_id=mid,reply_markup=bk)
    if data == 'ps':
        keys = mk(row_width=2)
        btn2 = btn('الخدمات العادية',callback_data='free')
        btn3 = btn('الخدمات الـ ViP',callback_data='vips')
        btn5 = btn('الخدمات الخاصة',callback_data='priv_serv')
        btn6 = btn('تمويل قناتك او مجموعتك', callback_data='tmoo')
        btn8 = btn('تمويل مستخدمين بوت 🤖', callback_data='tmoo_bot')
        keys.add(btn6)
        keys.add(btn3, btn2)
        keys.add(btn5)
        keys.add(btn8)
        keys.add(btn('رجوع .', callback_data='back'))
        bot.edit_message_text(text='اهلا بيك بقسم الخدمات العادية ',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'free':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        keys = mk(row_width=2)
        btn2 = btn('تصويت لايكات مسابقات',callback_data='votes')
        btn3 = btn('رشق تفاعلات اختياري',callback_data='react')
        btn5 = btn('رشق تفاعلات عشوائي',callback_data='reacts')
        btn6 = btn('رشق توجيهات علي منشور القناة',callback_data='forward')
        btn7 = btn('رشق مشاهدات ',callback_data='view')
        btn8 = btn('رشق استفتاء',callback_data='poll')
        btn9 = btn('رشق روابط دعوة بدون اشتراك اجبارى',callback_data='linkbot')
        keys.add(btn2)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn7, btn8)
        keys.add(btn('رجوع', callback_data='ps'))
        bot.edit_message_text(text='اهلا بيك بقسم الخدمات العادية ',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'pri_members':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
        for temp in a:
            db.delete(f'{temp}_{cid}_proccess')
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        db.set(f'member_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها',chat_id=cid,message_id=mid)
        type = 'pri_members'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'tmoo':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code', 'ads']
        for temp in a:
            db.delete(f'{temp}_{cid}_proccess')
        user_id = call.from_user.id
        joo = db.get(f"user_{user_id}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        xxx = db.get(f'tmoo_{cid}_proccess')
        keys = mk(row_width=3)
        btn1 = btn('تمويل بجميع نقاطك', callback_data='tmoil_with_all')
        btn2 = btn('تمويل 15 عضو', callback_data='tmoil_15')
        keys.add(btn1)
        if mem >= 15:
            keys.add(btn2)
        x = bot.edit_message_text(text=f'• ارسل عدد الاعضاء المراد تمويلهم او يمكنك الاختيار من الازرار 🌐\n\n-ملاحظه كل1عضو={price_join} نقطة\n\n-نقاطك الحاليه : {coin}',chat_id=cid, message_id=mid, parse_mode="Markdown", reply_markup=keys)
        bot.register_next_step_handler(x, tmmo)
        db.set(f'tmoo_{cid}_proccess', True)
    if data == 'tmoil_with_all':
        joo = db.get(f"user_{cid}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        count = int(mem)
        db.delete(f'tmoo_{cid}_proccess')
        if mem >= 15:
            x = bot.edit_message_text(text=f'• لقد اخترت تمويل {count} عضو\n• ارفع البوت المساعد @V42_bot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥',chat_id=cid,message_id=mid)
            bot.register_next_step_handler(x, tmm_count, count)
        else:
            bot.answer_callback_query(call.id, text=f"عذرا ، الحد الادني من التمويل هو 15 عضو",show_alert=True)
    if data == 'tmoil_15':
        joo = db.get(f"user_{cid}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        mem = coin / price_join
        db.delete(f'tmoo_{cid}_proccess')
        if mem >= 15:
            x = bot.edit_message_text(text='• لقد اخترت تمويل 15 عضو\n• ارفع البوت المساعد @V42_bot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة 👥',chat_id=cid,message_id=mid)
            count = 15
            bot.register_next_step_handler(x, tmm_count, count)
        else:
            bot.answer_callback_query(call.id, text=f"عذرا ، نقاطك لا تكفي ❌",show_alert=True)
            
    if data == 'join_10':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط 💲', callback_data='collect')],
                [btn(text='رجوع ➰', callback_data='back')]
            ]
        )
        count = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            try:
                chat_info = bot.get_chat(channel)
                name = chat_info.title
                ii = channel.replace('@', '')
                button = btn(name, url=f"https://t.me/{ii}")
                button2 = btn('ابلاغ', callback_data=f"repotch|{ii}")
                keys.add(button, button2)
                count += 1
                if count == 1:
                    np = "⬜️"
                    mf = 10 * count
                elif count == 2:
                    np = "⬜️⬛️"
                    mf = 10 * count
                elif count == 3:
                    np = "⬜️⬛️🟫"
                    mf = 10 * count
                elif count == 4:
                    np = "⬜️⬛️🟫🟪"
                    mf = 10 * count
                elif count == 5:
                    np = "⬜️⬛️🟫🟪🟥"
                    mf = 10 * count
                elif count == 6:
                    np = "⬜️⬛️🟫🟪🟥🟧"
                    mf = 10 * count
                elif count == 7:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨"
                    mf = 10 * count
                elif count == 8:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦"
                    mf = 10 * count
                elif count == 9:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩"
                    mf = 10 * count
                elif count == 10:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩✔️"
                    mf = 10 * count
                else:
                    np = "⬜️⬛️🟫🟪🟥🟧🟨🟦🟩✔️"
                    mf = 10 * count
            except:
                continue
            all = int(count) * int(coin_join)
            k = f'''⚡️] الاشتراك بالقنوات 10x \n\n{np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
        if count == 0:
            k = f'''• لا يوجد قنوات حاليا ، قم بتجميع النقاط بطريقة مختلفة.'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
        else:
            button1 = btn("تحقق ♻️", callback_data="check10")
            button2 = btn("رجوع ➰", callback_data="collect")
            keys.add(button1,button2)
            all = int(count) * int(coin_join)
            k = f'''⚡️] الاشتراك بالقنوات 10x \n\n{np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
    if data == 'check10':
        bot.answer_callback_query(call.id, text="لحظة من فضلك . . .")
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط ', callback_data='collect')],
                [btn(text='رجوع ➰', callback_data='back')]
            ]
        )
        count = 0
        count1 = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            try:
                x = bot.get_chat_member(chat_id=channel, user_id=user_id)
            except:
                continue
            if str(x.status) in stypes:
                count1 += 1
                count = db.get(f"count_{channel}")
                ids = db.get(f"id_{channel}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(channel)
                    db.set("force_ch", chats_dd)
                    chat_info = bot.get_chat(channel)
                    name = chat_info.title
                    ii = channel.replace('@', '')
                    mem = db.get(f"mem_{channel}") if db.exists(f"mem_{channel}") else ""
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك @{ii} ب {mem} عضو 🚸", parse_mode="Markdown")
                    iddd = 5310577402
                    bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✔️\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                else:
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    ids = db.get(f"id_{channel}")
                    chat_info = bot.get_chat(channel)
                    name = chat_info.title
                    count = db.get(f"count_{channel}")
                    countcc = int(count) - 1
                    db.set(f"count_{channel}", countcc)
                    chats_joining.append(channel)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(channel)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(channel)
                    name = chat_inf.title
                    count = db.get(f"count_{channel}")
                    ids = db.get(f"id_{channel}")
                    ii = channel.replace('@', '')
                    bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✔️\n\n• العدد المتبقي : `{countcc}` 🚸", parse_mode="Markdown")
        if int(count1) == 0:
            kkj = f'''يبدو انك لم تشترك بأي قناة 🗿'''
        else:
            all = int(coin_join) * int(count1)
            kkj = f'''• اشتركت في {count1} قنوات وحصلت علي {all} نقطة ✔️'''
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) + int(all)
            db.set(f"user_{user_id}", joo)
        bot.edit_message_text(text=kkj, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
    if data == 'vips':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        keys = mk(row_width=2)
        btn3 = btn('رشق اعضاء قناة عامة ',callback_data='members')
        btn4 = btn('رشق اعضاء قناة خاصة ',callback_data='membersp')
        btn8 = btn('رشق مستخدمين البوت',callback_data='userbot')
        btn9 = btn('رشق تعليقات',callback_data='comments')
        btn10 = btn('رشق روابط دعوة اشتراك اجبارى',callback_data='linkbot2')
        keys.add(btn3,btn4)
        keys.add(btn8)
        keys.add(btn9)
        keys.add(btn('رجوع', callback_data='ps'))
        bot.edit_message_text(text='• مرحبا بك في قسم المشتركين الـ ViP , يمكن للمشتركين الـ ViP استخدام هذا القسم فقط',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'collect':
        keys = mk(row_width=2)
        btn1 = btn('الهدية اليومية 🎁', callback_data='dailygift')
        btn2 = btn('الاشتراك بالبوتات 🤖', callback_data="join_bots")
        btn3 = btn('رابط الدعوة 🌀',callback_data='share_link')
        btn4 = btn('الاشتراك بالقنوات 📣',callback_data='join_ch')
        btn5 = btn('الاشتراك بالقنوات (تيربو) 📣',callback_data='join_10')
        btn10 = btn('تبديل نقاط تمويل مليار',callback_data='change_point_mill')
        
        keys.add(btn5)
        keys.add(btn2, btn4)
        keys.add(btn3, btn1)
        keys.add(btn10)
        keys.add(btn('رجوع', callback_data='back'))
        bot.edit_message_text(text='• مرحبا بك في قسم تجميع النقاط \n\n• يمكنك تجميع النقاط عبر الازرار التي امامك',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if call.data.startswith('port:'):
        user_id = call.from_user.id
        robot = call.data.split(':')[1]
        text = f'<strong>• ابلاغ جديد علي بوت {robot} 🚫</strong>\n\n- اسمه : {call.from_user.first_name}\n- ايديه : {call.from_user.id}\n- يوزره : @{call.from_user.username}'
        keys = mk()
        btn1 = btn('للدخول الي البوت 🤖', url='https://t.me/' + str(robot.replace('@', '')))
        btn2 = btn('تخطي ⚠️', callback_data=f'skbot:{robot}')
        btn3 = btn('رجوع ↪️', callback_data='collect')
        btn4 = btn('تم الابلاغ', callback_data=f'dnReport')
        keys.add(btn1)
        keys.add(btn2, btn4)
        keys.add(btn3)
        bot.edit_message_reply_markup(chat_id=cid, message_id=mid, reply_markup=keys)
        keys = mk().add(btn('الغاء تمويل البوت', callback_data=f"Xbot:{robot}"))
        bot.send_message(chat_id=sudo, text=text, reply_markup=keys, parse_mode='html')

    if call.data.startswith('Xbot:'):
        user_id = call.from_user.id
        robot = call.data.split(':')[1]
        tmoo_bots = db.get('tmoo_bots') if db.exists('tmoo_bots') else []
        if robot in tmoo_bots:
            tmoo_bots.remove(robot)
            db.set('tmoo_bots', tmoo_bots)
            text = f'- تم الغاء تمويل البوت بنجاح : {robot}'
            bot.edit_message_text(chat_id=cid, text=text, message_id=mid)
        else:
            text = "هذا البوت لا يتم تمويله"
            bot.edit_message_text(chat_id=cid, text=text, message_id=mid)
    if call.data.startswith('skbot:'):
        user_id = call.from_user.id
        link = call.data.split(':')[1]
        bots_joining = db.get(f"bots_{user_id}") if db.exists(f"bots_{user_id}") else []
        bots_joining.append(link)
        db.set(f"bots_{user_id}", bots_joining)
        k = f'''<strong>• رجاء الانتظار ....</strong>'''
        bot.edit_message_text(text=k, chat_id=cid, message_id=mid)
        price_tmoo_bot = db.get('price_tmoo_bot') if db.exists('price_tmoo_bot') else 5
        bots_joining = db.get(f"bots_{user_id}") if db.exists(f"bots_{user_id}") else []
        tmoo_bots = db.get('tmoo_bots') if db.exists('tmoo_bots') else []
        bots_user = [bot for bot in tmoo_bots if bot not in bots_joining]
        if len(bots_user) == 0:
            kk = f"• لا يوجد بوتات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕"
            key = mk(
                [
                    [btn(text='تجميع النقاط ❇️', callback_data='collect')],
                    [btn(text='رجوع ↪️', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
            return
        else:
            robot = bots_user[0]
            text = f'''<strong>• قم بالدخول الي بوت {robot} 🤖</strong>

- ارسل /start داخل الروبوت ثم قم بتحويل رسالة من الروبوت الي هنا لتحصل علي {price_tmoo_bot} نقطة ❇️'''
            keys = mk()
            btn1 = btn('للدخول الي البوت 🤖', url='https://t.me/' + str(robot.replace('@', '')))
            btn2 = btn('تخطي ⚠️', callback_data=f'skbot:{robot}')
            btn3 = btn('رجوع ↪️', callback_data='collect')
            btn4 = btn('ابلاغ 🚫', callback_data=f'port:{robot}')
            keys.add(btn1)
            keys.add(btn2, btn4)
            keys.add(btn3)
            x = bot.edit_message_text(text=text, chat_id=cid, message_id=mid, reply_markup=keys, parse_mode="html")
            bot.register_next_step_handler(x, check_forward_bot, robot)
            
    if call.data.startswith('tm:'):
        link = call.data.split(':')[1]
        amount = int(call.data.split(':')[2])
        price_tmoo_bot = db.get('price_tmoo_bot') if db.exists('price_tmoo_bot') else 5
        acc = db.get(f'user_{cid}')
        pr = amount * price_tmoo_bot
        if int(pr) > acc['coins']:
            bot.answer_callback_query(call.id, text='• رصيدك غير كافي لاتمام عملية التمويل', show_alert=True)
            return
        tmoo_bots = db.get('tmoo_bots') if db.exists('tmoo_bots') else []
        if link in tmoo_bots:
            id = db.get(f'id_{link}')
            count = db.get(f'count_{link}')
            amount += count
            db.set(f'count_{link}', amount)
            text = f'''<strong>• تم بدء تمويل بوتك بنجاح ✅</strong>

- تم خصم {pr} نقطة 
- يتم الان تمويل : {amount} عضو

- البوت الجارِ تمويله {link}
'''
            bot.edit_message_text(chat_id=cid, text=text, message_id=mid, parse_mode='html', reply_markup=bk)
            text = f'''<strong>• تم بدء تمويل بوت بنجاح ✅</strong>

- يتم الان تمويل : {amount} عضو

- البوت الجارِ تمويله {link}'''
            bot.send_message(chat_id=sudo, text= text, parse_mode='html')
            acc = db.get(f'user_{cid}')
            acc['coins'] -= pr
            db.set(f'user_{cid}', acc)
        else:
            db.set(f'id_{link}', cid)
            db.set(f'count_{link}', amount)
            tmoo_bots.append(link)
            db.set('tmoo_bots', tmoo_bots)
            acc = db.get(f'user_{cid}')
            acc['coins'] -= pr
            db.set(f'user_{cid}', acc)
            text = f'''<strong>• تم بدء تمويل بوتك بنجاح ✅</strong>

- تم خصم {pr} نقطة 
- يتم الان تمويل : {amount} عضو

- البوت الجارِ تمويله {link}
'''
            bot.edit_message_text(chat_id=cid, text=text, message_id=mid, parse_mode='html', reply_markup=bk)
            text = f'''<strong>• تم بدء تمويل بوت بنجاح ✅</strong>

- يتم الان تمويل : {amount} عضو

- البوت الجارِ تمويله {link}'''
            bot.send_message(chat_id=sudo, text=text, parse_mode='html')
    if call.data.startswith('report:'):
        ch = call.data.split(':')[1]
        print(ch)
        try:
            chat_info = bot.get_chat(ch)
            name = chat_info.title
        except Exception as a:
            if "bot was kicked" in str(a):
                chats_dd = db.get('force_ch')
                if ch in chats_dd:
                    chats_dd.remove(ch)
                    db.set("force_ch", chats_dd)
                    ids = db.get(f"id_{ch}")
                    bot.send_message(chat_id=int(ids), text=f"*• لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {ch} ❌*", parse_mode="Markdown")
            elif "chat not found" in str(a):
                chats_dd = db.get('force_ch')
                if ch in chats_dd:
                    chats_dd.remove(ch)
                    db.set("force_ch", chats_dd)
                    ids = db.get(f"id_{ch}")
                    bot.send_message(chat_id=int(ids), text=f"*• لقد قمت بازالة البوت من الادمنية وتم الغاء تمويل قناتك {ch} ❌*", parse_mode="Markdown")
        chat_info = bot.get_chat(ch)
        name = chat_info.title
        ii = chat_info.username
        bot.answer_callback_query(call.id, text="تم ارسال بلاغك ⛔")
        keys = mk(row_width=5)
        tar = btn(f'الغاء تمويل قناة {name}', callback_data=f'canceltmoil:{ch}')
        keys.add(tar)
        user_id = call.from_user.id
        bot.send_message(chat_id=int(sudo), text=f"*• بلاغ جديد علي قناة *[{name}](https://t.me/{ii}) \n• الشخص الذي قام بالابلاغ :\n\n• الاسم : [{call.from_user.first_name}](tg://user?id={user_id})\n• المعرف : @{call.from_user.username}\n• الايدي : [{user_id}](tg://user?id={user_id}) ", parse_mode="Markdown", reply_markup=keys)
        return
    if data == 'dnReport':
        bot.answer_callback_query(call.id, '- تم ارسال ابلاغك بالفعل 🚫')
    if data == 'join_bots':
        k = f'''<strong>• رجاء الانتظار ....</strong>'''
        user_id = call.from_user.id
        bot.edit_message_text(text=k, chat_id=cid, message_id=mid)
        price_tmoo_bot = db.get('price_tmoo_bot') if db.exists('price_tmoo_bot') else 5
        join_tmoo_bot = db.get('join_tmoo_bot') if db.exists('join_tmoo_bot') else 5
        bots_joining = db.get(f"bots_{user_id}") if db.exists(f"bots_{user_id}") else []
        tmoo_bots = db.get('tmoo_bots') if db.exists('tmoo_bots') else []
        bots_user = [bot for bot in tmoo_bots if bot not in bots_joining]
        if len(bots_user) == 0:
            kk = f"• لا يوجد بوتات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕"
            key = mk(
                [
                    [btn(text='تجميع النقاط ❇️', callback_data='collect')],
                    [btn(text='رجوع ↪️', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
            return
        else:
            robot = bots_user[0]
            text = f'''<strong>• قم بالدخول الي بوت {robot} 🤖</strong>

- ارسل /start داخل الروبوت ثم قم بتحويل رسالة من الروبوت الي هنا لتحصل علي {join_tmoo_bot} نقطة ❇️'''
            keys = mk()
            btn1 = btn('للدخول الي البوت 🤖', url='https://t.me/' + str(robot.replace('@', '')))
            btn2 = btn('تخطي ⚠️', callback_data=f'skbot:{robot}')
            btn3 = btn('رجوع ↪️', callback_data='collect')
            btn4 = btn('ابلاغ 🚫', callback_data=f'port:{robot}')
            keys.add(btn1)
            keys.add(btn2, btn4)
            keys.add(btn3)
            x = bot.edit_message_text(text=text, chat_id=cid, message_id=mid, reply_markup=keys, parse_mode="html")
            bot.register_next_step_handler(x, check_forward_bot, robot)
    if data == 'change_point_mill':
        keys = mk(row_width=2)
        btn5 = btn('إضغط هنا لتبديل النقاط',callback_data='change_points_mill')
        btn4 = btn('الذهاب إلى بوت تمويل المليار',url='https://t.me/EEObot?start=6227455684')
        btn6 = btn('‹ رجوع ↻›',callback_data='collect')
        keys.add(btn5)
        keys.add(btn4)
        keys.add(btn6)
        bot.edit_message_text(text='⌁︙يمكنك إستبدال نقاط تمويل بدل ↫رصيد\n⌁︙كل 500 نقطة تمويل بدل 250 IQD\n⌁︙كل 1000 نقطة تمويل بدل 500 IQD\n⌁︙اقل عدد نقاط ممكن استبداله ↫ 500 \n⌁︙نستقبل نقاط من بوت تمويل المليار ↫⤈',reply_markup=keys,chat_id=cid,message_id=mid)
    if data == 'change_points_mill':
        x = bot.edit_message_text(text='⌁︙يرجى ارسال رابط تحويل النقاط من بوت المليار',chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, change_points_mill)
    if data == 'zip_all':
        bot.answer_callback_query(call.id, text="انتظر لحظه ...")
        folder_path = f"./dbs"
        zip_file_name = f"database.zip"
        zip_file_nam = f"database"
        try:
            shutil.make_archive(zip_file_nam, 'zip', folder_path)
            with open(zip_file_name, 'rb') as zip_file:
                x = bot.send_document(cid, zip_file)
                bot.pin_chat_message(cid, x.message_id)
            os.remove(zip_file_name)
        except Exception as a:
            print(a)
            bot.answer_callback_query(call.id, text="المجلد غير موجود ❌")
    if data == 'leave':
        if cid in admins:
            db.set(f'leave_{cid}_proccess', True)
            x = bot.edit_message_text(text='ارسل رابط اذا القناة خاصه، اذا عامه ارسل معرفها فقط؟',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'leavs'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'account':
        if not check_user(cid):
            return start_message(call.message)
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        y = trend()
        prem = 'Premium' if info['premium'] == True else 'Free'
        textt = f'''
• [❇️] عدد نقاط حسابك : {coins}
• [🌀] عدد عمليات الاحاله التي قمت بها : {users}
• [👤] نوع اشتراكك داخل البوت : {prem}
• [🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• [❇️] عدد النقاط اللي جمعتها من الهدايا اليومية : {all_gift}
• [📮] عدد الطلبات التي طلبتها : {buys}
• [♻️] عدد التحويلات التي قمت بها : {trans}

{y}'''
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=bk)
        return
    if data == 'setforce':
        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n@first @second',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)
    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
    if data == 'votes':
        db.set(f'vote_{cid}_proccess', True)
        x = bot.edit_message_text(text='• حسنا ، ارسل الان عدد التصويتات التي تريدها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'votes'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'buy':
        keys = mk(row_width=2)
        keys.add(btn('رجوع', callback_data='back'))
        hakem = ''' مرحبا بك في قسم شراء النقاط

• لشراء النقاط تواصل مع المطور : @X_K_L'''
        bot.edit_message_text(text=hakem,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'dump_votes':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'dump_votes_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل الان رابط المنشور الذي تريد سحب المنشورات منه ',reply_markup=bk,chat_id=cid,message_id=mid)
            bot.register_next_step_handler(x, dump_votes)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=f'• حدث خطا ما في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = mk(row_width=2)
        keys.add(btn('رجوع', callback_data='collect'))
        xyz = f'''
<strong>
انسخ الرابط ثم قم بمشاركته مع اصدقائك !!
</strong>
~  كل شخص يقوم بالدخول ستحصل على <strong>{link_price}</strong> نقطه

~ بإمكانك عمل اعلان خاص برابط الدعوة الخاص بك 

🌀 رابط الدعوة : \n<strong>{link}</strong> .

~ مشاركتك للرابط : <strong>{len(get(cid)["users"])} </strong>.

{y}
        '''
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'members':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'member_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها ',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'members'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'membersp':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'memberp_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها ',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'membersp'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'spams':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'spam_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد الرسائل التي تريد ارسالها اسبام',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'msgs'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
        
    if data == 'react':
        db.set(f'react_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التفاعلات التي تريد رشقها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'react'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'reacts':
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التفاعلات التي تريد رشقها بشكل عشوائي',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'reactsrandom'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'forward':
        db.set(f'forward_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد التوجيهات التي تريد رشقها علي منشور القناة ',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'forward'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'view':
        db.set(f'view_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد المشاهدات اللي تريد ترشقها علي منشور القناة',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'view'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'poll':
        db.set(f'poll_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد الاستفتاء الذي تريد رشقه',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'poll'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'userbot':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'userbot_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد المستخدمين الذي تريد ترشقهم للبوت الخاص بك',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'userbot'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'linkbot':
        db.set(f'linkbot_{cid}_proccess', True)
        x = bot.edit_message_text(text='• ارسل الان عدد روابط الدعوة التي تريد رشقها',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'linkbot'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'comments':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'comments_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد التعليقات التي تريد رشقها ',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'comments'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'lvallc':
        bot.edit_message_text(text='• تم بدء مغادرة كل القنوات والمجموعات بنجاح ✅',chat_id=cid,message_id=mid)
        acc = db.get('accounts')
        amount = len(acc)
        true = 0
        for amount in acc:
            print("Done1")
            try:
                true+=1
                o = asyncio.run(leave_chats(amount['s']))  
            except Exception as e:
                print(e)
                continue
            id = call.from_user.id
            bot.send_message(chat_id=id, text=f'• تم بنجاح الخروج من كل القنوات والمجموعات \n• تم الخروج من <code>{true}</code> حساب بنجاح ✅')
    if data == 'cancel':
        bot.edit_message_text(text='<strong>• تم الغاء عملية المغادرة ❌</strong>',chat_id=cid,message_id=mid)
    if data == 'linkbot2':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            db.set(f'linkbot2_{cid}_proccess', True)
            x = bot.edit_message_text(text='• ارسل الان عدد رشق روابط الدعوة التي تريدها',reply_markup=bk,chat_id=cid,message_id=mid)
            type = 'linkbot2'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ViP قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    else:
        return


def get_amount(message, type):
    admins = db.get('admins')
    cid = message.from_user.id
    if type == 'leavs':
        if not db.get(f'leave_{cid}_proccess'): return
        if detect(message.text):
            url = message.text
            acc = db.get('accounts')
            amount = len(acc)
            if len(acc) > 10:
                amount = amount / 2
            true = 0
            for y in acc:
                true+=1
                if true >=amount:
                    break
                try:
                    o = asyncio.run(leave_chats(y['s'], url))
                    
                except Exception as e:
                    
                    continue
            bot.reply_to(message, f'• تم الخروج من <code>{true}</code> حساب ينجاح ✅')
            return
                    
        else:
            url = message.text.replace('https://t.me/', '').replace('@', '')
            acc = db.get('accounts')
            amount = len(acc)
            if len(acc) > 10:
                amount = amount / 2
            true = 0
            for y in acc:
                
                if true >=amount:
                    break
                try:
                    o = asyncio.run(leave_chat(y['s'], url))
                   
                    true+=1
                except Exception as e:
                    
                    continue
            bot.reply_to(message, f'• تم الخروج من <strong>{true}</strong> حساب ✅')
            return
            pass
        
    if type == 'members':
        if not db.get(f'member_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = member_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان معرف قناتك او رابطها')
            bot.register_next_step_handler(x, get_url_mem, amount)
            return
    if type == 'tmoo_bot':
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• الحد الادني لتمويل الاضعاء هو 10.',reply_markup=bk2)
                return
            
            price_tmoo_bot = db.get('price_tmoo_bot') if db.exists('price_tmoo_bot') else 5
            pr = price_tmoo_bot * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  {pr-amount} نقطة')
                return

            load_ = db.get('accounts')
            x = bot.reply_to(message,f'• عدد الاعضاء : {amount}\n\n• ارسل الان معرف او رابط بوتك لتمويله')
            bot.register_next_step_handler(x, tmoo_bot, amount)
            return
    if type == 'membersp':
        if not db.get(f'memberp_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = member_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بالقناة الخاصة')
            bot.register_next_step_handler(x, get_url_memp, amount)
            return
    if type == 'react':
        if not db.get(f'react_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان التفاعل الذي تريد ارساله')
            bot.register_next_step_handler(x, get_react, amount)
            return
    if type == 'forward':
        if not db.get(f'forward_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong>',reply_markup=bk)
                return
            pr = forward_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_forward, amount)
            return
    if type == 'poll':
        if not db.get(f'poll_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong>',reply_markup=bk)
                return
            pr = poll_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_poll, amount)
            return
    if type == 'reactsrandom':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• تم اختيار الكمية <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_reacts_url, amount)
            return
    if type == 'view':
        if not db.get(f'view_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = view_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_view_url, amount)
            return
    if type == 'votes':
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>300</strong>',reply_markup=bk)
                return
            pr = vote_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطة .')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• تم اختيار الكمية {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 300')
            bot.register_next_step_handler(x, get_time_votes, amount)
            return
    
    if type == 'msgs':
        if not db.get(f'spam_{cid}_proccess'): return
        if message.text:
            amount = None
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message,f'• رجاء ارسل عدد فقط ، اعد المحاولة لاحقا',reply_markup=bk)
                return
            load_ = db.get('accounts')
            if amount < 1:
                bot.reply_to(message, f'• رجاء ارسل عدد اكبر من 10', reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'• رجاء ارسل عدد اقل من 300',reply_markup=bk)
                return
            
            if len(load_) < amount:
                bot.reply_to(message,text=f'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            pr = spam_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if acc['coins'] < pr:
                bot.reply_to(message,f'• نقاطك غير كافية لتنفيذ طلبك ، تحتاج الي {pr-amount} نقطه',reply_markup=bk)
                return
            x = bot.reply_to(message,text=f'• الان ارسل يوزر او رابط الحساب اللي تريد تعمل سبام عليه')
            bot.register_next_step_handler(x, get_url_spam, amount)
            return
    if type == 'userbot':
        if not db.get(f'userbot_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = userbot_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط ااو معرف البوت اللي تريد ترشقله مستخدمين')
            bot.register_next_step_handler(x, get_bot_user, amount)
            return
    if type == 'linkbot':
        if not db.get(f'linkbot_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = linkbot_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link_bot, amount)
            return
    if type == 'linkbot2':
        if not db.get(f'linkbot2_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link_bot2, amount)
            return
    if type == 'comments':
        if not db.get(f'comments_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 300:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>300</strong> ..',reply_markup=bk)
                return
            pr = comment_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور اللي تريد التعليق عليه \n\n يجب ان تنسخ منشور القناة من مجموعة المناقشة وليس من القناة نفسها')
            bot.register_next_step_handler(x, get_comments_url, amount)
            return
    if type == 'pri_react':
        if not db.get(f'react_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            load_ = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حساباتك غير كافية',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان التفاعل الذي تريد ارساله\n• او يمكنك الاختيار من بين التفاعلات التالية \n\n👍👎❤🔥🥰👏😁🤔🤯🤬😢🎉🤩🤮💩🙏👌🕊🤡🥱🥴😍🐳❤️‍🔥🌚🌭💯🤣⚡️🍌🏆💔🤨😐🍓🍾💋🖕😈😴🤓👻👨‍💻👀🎃🙈😇😨🤝✍🤗🫡🎅🎄☃️💅🤪🗿🆒💘🙉🦄😘💊🙊😎👾🤷‍♂🤷🤷‍♀😡')
            bot.register_next_step_handler(x, get_pri_react, amount)
    if type == 'pri_members':
        if not db.get(f'member_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            load_ = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حساباتك غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان معرف قناتك او رابطها')
            bot.register_next_step_handler(x, get_url_pri_mem, amount)
            return
    if type == 'private_vote':
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>0</strong>',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>2000</strong>',reply_markup=bk)
                return
            load_ = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حساباتك المسجله لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
            bot.register_next_step_handler(x, get_time_private_vote, amount)
            return
    if type == 'msgs_private':
        if not db.get(f'spam_{cid}_proccess'): return
        if message.text:
            amount = None
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message,'• رجاء ارسل عدد فقط ، اعد المحاولة لاحقا',reply_markup=bk)
                return
            load_ = db.get(f'ses_{message.from_user.id}') if db.exists(f'ses_{message.from_user.id}') else []
            if amount < 1:
                bot.reply_to(message, '• رجاء ارسل عدد اكبر من 1', reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'• رجاء ارسل عدد اقل من 2000',reply_markup=bk)
                return
            if len(load_) < amount:
                bot.reply_to(message,text='• عدد حساباتك لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,text='• الان ارسل يوزر او رابط الحساب اللي تريد تعمل سبام عليه')
            bot.register_next_step_handler(x, get_url_spam_private, amount)
            return
###########
def get_time_votes(message, amount):
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط المنشور')
    bot.register_next_step_handler(x, get_url_votes, amount, time)
def link_bot2(message, amount):
    url = message.text
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل رابط او معرف قناة الاشتراك الاجبارى')
        bot.register_next_step_handler(x, linkbot_chforce, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
def tmoo_bot(message, amount):
    if message.text == "/start":
        start_message(message)
        return
    if '@' in message.text or 'https://t.me/' in message.text or 'http://t.me/' in message.text:
        if 'bot' not in message.text.lower():
            x = bot.reply_to(message, text='• رجاء ارسل معرف او اربط البوت بشكل صحيح', reply_markup=bk2)
            bot.register_next_step_handler(x, tmoo_bot, amount)
            return
        text = f'''• هل انت متاكد من تاكيد عملية التمويل ؟
    
- عدد الاعضاء : {amount}
- البوت : {message.text}

• اختر من الازرار ادناه 📥'''
        robot = message.text.replace('https://t.me/', '@').replace('http://t.me/', '@')
        if "?start=" in robot:
            robot = "@" + str(message.text.split("?start=")[0].split("/")[-1])   
        keys = mk()
        btn1 = btn('تاكيد ✅', callback_data=f'tm:{robot}:{amount}')
        btn2 = btn('الغاء ❌', callback_data='cancel')
        keys.add(btn2, btn1)
        bot.reply_to(message, text, reply_markup=keys)
    else:
        x = bot.reply_to(message, text='• رجاء ارسل معرف او اربط البوت بشكل صحيح', reply_markup=bk2)
        bot.register_next_step_handler(x, tmoo_bot, amount)
        
def dump_votes(message):
    url = message.text
    load_ = db.get('accounts')
    num = len(load_)
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'سحب تصويت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n')
    
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for num in load_:
        try:
            x = asyncio.run(dump_votess(num['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(f"Erorr: {e}")
            continue
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n\n• تم سحب : {false} تصويت\n• لم يتم سحب : {true}',reply_markup=bk)
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ') 
def linkbot_chforce(message, amount, url):
    channel_force = message.text.replace('https://t.me/', '').replace('@', '')
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot2_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}\n• قناة الاشتراك الاجبارى : @{channel_force}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(linkbot2(y['s'], channel, tex, channel_force))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= linkbot2_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*linkbot2_price}',reply_markup=bk)
    return
##################
def get_comments_url(message, amount):
    url = message.text
    admins = db.get('admins')
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل التعليق الذي تريد رشقه')
        bot.register_next_step_handler(x, comment_text, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
def comment_text(message, amount, url):
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 100:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 100 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = comment_price * amount
        load_ = db.get('accounts')
        typerr = 'تعليقات خدمة ViP'
        bot.reply_to(message,text=f'• جارى تنفيذ طلبك بنجاح ✅\n\n• النوع : {typerr}\n• الرابط : {url}\n• الكمية : {amount}')
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true, false = 0, 0
        for y in load_:
            if true >= amount:
                break
            try:
                x = asyncio.run(send_comment(y['s'], url, text))
                true += 1
            except:
                false += 1
                continue
        if true >= 1:
            for ix in range(true):
                acc['coins'] -= comment_price
            db.set(f'user_{message.from_user.id}', acc)
        else:
            pass
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} \n• لم يتم ارسال : {false}\n• تم خصم : {true*comment_price} من رصيدك',reply_markup=bk)
        return
########################
def link_bot(message, amount):
    admins = db.get('admins')
    url = message.text
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة بدون اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(linkbot(y['s'], channel, tex))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= linkbot_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*linkbot_price}',reply_markup=bk)
    return

def get_bot_user(message, amount):
    admins = db.get('admins')
    url = message.text.replace('https://t.me/', '').replace('@', '')
    pr = userbot_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مستخدمين بوت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr} \n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(userbot(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= userbotprice
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*userbot_price}',reply_markup=bk)
    return
    
def get_url_spam(message, amount):
    url = message.text
    admins = db.get('admins')
    if 'https://t.me' in url or '@' in url:
        x = bot.reply_to(message,text=f'• الان ارسل الرسالة اللي تريد ترسلها للحساب')
        bot.register_next_step_handler(x, get_text, amount, url)
        return

def get_text(message, amount, url):
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 1000:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 1000 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = spam_price * amount
        load_ = db.get('accounts')
        typerr = 'رسائل مزعجة خدمة ViP'
        bot.reply_to(message,text=f'• جارى تنفيذ طلبك بنجاح ✅\n\n• النوع : {typerr}\n• الرابط : {url}\n• الكمية : {amount}')
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true, false = 0, 0
        for y in load_:
            if true >= amount:
                break
            try:
                x = asyncio.run(send_message(y['s'], chat=url, text=text))
                true += 1
            except:
                false += 1
                continue
        if true >= 1:
            for ix in range(true):
                acc['coins'] -= spam_price
            db.set(f'user_{message.from_user.id}', acc)
        else:
            pass
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} \n• لم يتم ارسال : {false}\n• تم خصم : {true*spam_price} من رصيدك',reply_markup=bk)
        return

def get_url_memp(message, amount):
    admins = db.get('admins')
    url = message.text
    load = db.get('accounts')
    info = get(message.from_user.id)
    price = member_price * amount
    if price > int(info['coins']):
        bot.reply_to(message,text=f'نقاطك غير كافية لتنفيذ طلبك تحتاج الي <strong> {price - int(info["coins"])} </strong>',reply_markup=bk)
        return
    if len(load) < 1:
        bot.reply_to(message,text='عدد حسابات البوت لا تكفي لتنفيذ طلبك ',reply_markup=bk)
        return
    typerr = 'رشق اعضاء قناة خاصة خدمة ViP'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅\n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
    true, false = 0, 0
    for y in load:
        if true >= amount:
            break
        try:
            x = asyncio.run(join_chatp(y['s'], url))
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            pass
    if true >= 1:
        for ix in range(true):
            info['coins'] -= member_price
        db.set(f'user_{message.from_user.id}', info)
    else:
        pass
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} .\n• لم يتم ارسال : {false}\n• تم خصم : {true*member_price} من رصيدك ',)
    return

def get_url_mem(message, amount):
    admins = db.get('admins')
    url = message.text
    if 'https://t.me' in url or '@' in url:
        if detect(url):
            load = db.get('accounts')
            info = get(message.from_user.id)
            price = member_price * amount
            if price > int(info['coins']):
                bot.reply_to(message,text=f'مامعك نقاط كافية، تحتاج <strong> {price - int(info["coins"])} </strong> نقطة علمود ترسل هذا العدد',reply_markup=bk)
                return
            if len(load) < 1:
                bot.reply_to(message,text='عدد حسابات البوت لا تكفي لتنفيذ طلبك ',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ViP'
            v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅\n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
            true, false = 0, 0
            for y in load:
                if true >= amount:
                    break
                try:
                    x = asyncio.run(join_chat(y['s'], url))
                    if x == 'o':
                        continue
                    if x == True:
                        true += 1
                    else:
                        false += 1
                except Exception as e:
                   pass
            if true >= 1:
                for ix in range(true):
                    info['coins'] -= member_price
                db.set(f'user_{message.from_user.id}', info)
            else:
                pass
            bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} .\n• لم يتم ارسال : {false}\n• تم خصم : {true*member_price} من رصيدك ',)
            return
        else:
            username = url.replace('https://t.me/', '').replace('@', '')
            load = db.get('accounts')
            info = get(message.from_user.id)
            price = member_price * amount
            if price > int(info['coins']):
                bot.reply_to(message,text=f'• نقاطك غير كافية : تحتاج الي <strong> {price - int(info["coins"])} </strong> نقطة',reply_markup=bk)
                return
            if len(load) < 1:
                bot.reply_to(message,text=f'• حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ViP'
            v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅\n\n• النوع : {typerr}\n• اليوزر : @{username}\n• الكمية : {amount}')
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
            true, false = 0, 0
            for y in load:
                if true >= amount:
                    break
                try:
                    x = asyncio.run(join_chat(y['s'], username))
                    if x == 'o':
                        continue
                    if x == True:
                        true += 1
                    else:
                        false += 1
                except Exception as e:
                   
                    continue
            for i in range(true):
                info['coins'] -= member_price
            db.set(f'user_{message.from_user.id}', info)
            addord()
            user_id = message.from_user.id
            buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
            buys+=1
            db.set(f"user_{user_id}_buys", int(buys))
            bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true} \n• لم يتم ارسال : {false}\n• تم خصم : {true*member_price} من رصيدك',)
            return


def checks(link):
    admins = db.get('admins')
    pattern = r"https?://t\.me/(\w+)/(\d+)"
    match = re.match(pattern, link)

    if match:
        username = match.group(1)
        post_id = match.group(2)
        return username, post_id
    else:
        return False

def get_react(message, amount):
    rs = ["👍","🤩","🎉","🔥","❤️","🥰","🥱","🥴","🌚","🍌","💔","🤨","😐","🖕","😈","👎","😁","😢","💩","🤮","🤔","🤯","🤬","💯","😍","🕊","🐳","🤝","👨","🦄","🎃","🤓","👀","👻","🗿","🍾","🍓","⚡️","🏆","🤡","🌭","🆒","🙈","🎅","🎄","☃️","💊"]
    if message.text in rs:
        x = bot.reply_to(message,f'• تم اختيار الكمية {amount}\n• التفاعل : {message.text}\n\n• ارسل الان رابط المنشور لرشق التفاعلات عليه')
        bot.register_next_step_handler(x, get_url_react, amount, message)
    else:
        x = bot.reply_to(message,f'• رجاء ارسل التفاعل بشكل صحيح')
        bot.register_next_step_handler(x, get_react, amount)
        return
def get_url_votes(message, amount, time):
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}\n• الوقت بين التصويت : {time}')
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• عزيزي تبقي {amount} علي اكتمال طلبك ....')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true, false = 0, 0
    nume = int(amount)
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(vote_one(y['s'], url, time))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• عزيزي تبقي {nume} علي اكتمال طلبك ....')
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {true*vote_price}',reply_markup=bk)
    return
    
def get_url_react(message, amount, like):
    admins = db.get('admins')
    url = message.text
    like = like.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات اختياري'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• التفاعل : {like}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(reactions(y['s'], url, like))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {true*react_price}',reply_markup=bk)
    return
def get_reacts_url(message, amount):
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات عشوائي'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(reaction(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لك يتم ارسال : {false} \n• تم خصم : {true*react_price}',reply_markup=bk)
    return
def get_url_forward(message, amount):
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = forward_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'توجيهات'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(forward(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*react_price}',reply_markup=bk)
    return
def get_url_poll(message, amount):
    admins = db.get('admins')
    url = message.text
    x = checks(url)
    if x:
        channel, msg_id = x
    if not checks(url):
        bot.reply_to(message,text='• رجاء ارسل الرابط بشكل صحيح')
        return
    try:
        mm = "• ارسل الان تسلسل الإجابة في الاستفتاء\n\n• يجب ان يتراوح بين 0 : 9\n• علما بان اول اختيار يكون تسلسلة 0"
        x = bot.reply_to(message, mm, parse_mode='HTML')
        bot.register_next_step_handler(x, start_poll, amount, url)
    except Exception as e:
        bot.reply_to(message, "الرسالة ممسوحة أو القناة المجموعة غير صحيحة.")
        print(e)
        return
def start_poll(message, amount, url):
    num = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = poll_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'استفتاء'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(poll(y['s'], url, int(num)))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= poll_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*poll_price}',reply_markup=bk)
    return
    
def get_url_pri_mem(message, amount):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if 'https://t.me' in url or '@' in url:
        if detect(url):
            load = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
            info = get(message.from_user.id)
            price = member_price * amount
            if len(load) < 1:
                bot.reply_to(message,text='عدد حساباتك غير كافية',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ᴠɪᴘ'
            tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
            db.set(f"serv_{message.from_user.id}", True)
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
            
            true, false = 0, 0
            nume = int(amount)
            db.set(f"stop_request_{message.from_user.id}", True)
            v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
            for y in load:
                if true >= amount:
                    break
                stre = db.get(f"stop_request_{message.from_user.id}")
                if stre is False:
                    break
                try:
                    x = asyncio.run(join_chat(y['s'], url, tim))
                    if x == 'o':
                        continue
                    if x == True:
                        true += 1
                        nume -= 1
                    else:
                        false += 1
                except Exception as e:
                   pass
            db.set(f"serv_{message.from_user.id}", False)
            bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*poll_price}',reply_markup=bk)
            
            user_id = message.from_user.id
            code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
            daily_count = code + int(true*member_price)
            db.set(f"po_{user_id}", int(daily_count))
            a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
            for temp in a:
                db.delete(f'{temp}_{message.from_user.id}_proccess')
            return
        else:
            username = url.replace('https://t.me/', '').replace('@', '')
            load = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
            info = get(message.from_user.id)
            price = member_price * amount
            if len(load) < 1:
                bot.reply_to(message,text=f'• حساباتك غير كتفية',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ᴠɪᴘ'
            tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
            db.set(f"serv_{message.from_user.id}", True)
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
            
            true, false = 0, 0
            nume = int(amount)
            db.set(f"stop_request_{message.from_user.id}", True)
            v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
            for y in load:
                if true >= amount:
                    break
                stre = db.get(f"stop_request_{message.from_user.id}")
                if stre is False:
                    break
                try:
                    x = asyncio.run(join_chat(y['s'], username, tim))
                    if x == 'o':
                        continue
                    if x == True:
                        true += 1
                        nume -= 1
                    else:
                        false += 1
                except Exception as e:
                   
                    continue
            db.set(f"serv_{message.from_user.id}", False) 
            db.set(f'user_{message.from_user.id}', info)
            addord()
            user_id = message.from_user.id
            buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
            buys+=1
            db.set(f"user_{user_id}_buys", int(buys))
            bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*poll_price}',reply_markup=bk)
            
            user_id = message.from_user.id
            code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
            daily_count = code + int(true*member_price)
            db.set(f"po_{user_id}", int(daily_count))
            a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
            for temp in a:
                db.delete(f'{temp}_{message.from_user.id}_proccess')
            return

def get_pri_react(message, amount):
    if message.text == "/start":
        start_message(message)
        return
    rs = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "🌚", "🌭", "💯", "🤣", "⚡️", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕","😈", "😴", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃️", "💅", "🤪","🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂️", "🤷", "🤷‍♀️", "😡","❤"]
    if message.text in rs:
        x = bot.reply_to(message,f'• الكمية : {amount}\n• التفاعل : {message.text}\n\n• ارسل الان رابط المنشور لرشق التفاعلات عليه')
        bot.register_next_step_handler(x, get_url_pri_react, amount, message)
    elif message.text == "❤":
        x = bot.reply_to(message,f'• الكمية : {amount}\n• التفاعل : {message.text}\n\n• ارسل الان رابط المنشور لرشق التفاعلات عليه')
        bot.register_next_step_handler(x, get_url_pri_react, amount, message)
    else:
        x = bot.reply_to(message,f'• رجاء ارسل التفاعل بشكل صحيح')
        bot.register_next_step_handler(x, get_pri_react, amount)
        return

def get_url_pri_react(message, amount, like):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    like = like.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
    typerr = 'تفاعلات اختياري'
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    db.set(f"serv_{message.from_user.id}", True)
    true, false = 0, 0
    nume = int(amount)
    db.set(f"stop_request_{message.from_user.id}", True)
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    for y in load_:
        if true >= amount:
            break
        stre = db.get(f"stop_request_{message.from_user.id}")
        if stre is False:
            break
        try:
            x = asyncio.run(reactions(y['s'], url, like))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*poll_price}',reply_markup=bk)
    
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*react_price)
    db.set(f"po_{user_id}", int(daily_count))
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
    for temp in a:
        db.delete(f'{temp}_{message.from_user.id}_proccess')
    return

def get_url_spam_private(message, amount):
    if message.text == "/start":
        start_message(message)
        return
    url = message.text
    admins = db.get('admins')
    if 'https://t.me' in url or '@' in url:
        x = bot.reply_to(message,text=f'• الان ارسل الرسالة اللي تريد ترسلها للحساب')
        bot.register_next_step_handler(x, get_text_private, amount, url)
        return
def get_text_private(message, amount, url):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 1000:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 1000 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = spam_price * amount
        load_ = db.get(f'ses_{message.from_user.id}') if db.exists(f'ses_{message.from_user.id}') else []
        typerr = 'رسائل مزعجة خدمة خاصة'
        tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
        db.set(f"serv_{message.from_user.id}", True)
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true, false = 0, 0
        nume = int(amount)
        db.set(f"stop_request_{message.from_user.id}", True)
        v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
        for y in load_:
            if true >= amount:
                break
            stre = db.get(f"stop_request_{message.from_user.id}")
            if stre is False:
                break
            try:
                x = asyncio.run(send_message(y['s'], url, text))
                true += 1
                nume -= 1
            except Exception as a:
                print(a)
                false += 1
                continue
        db.set(f"serv_{message.from_user.id}", False)
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*poll_price}',reply_markup=bk)
        
        code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
        daily_count = code + int(true*spam_price)
        db.set(f"po_{user_id}", int(daily_count))
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
        for temp in a:
            db.delete(f'{temp}_{message.from_user.id}_proccess')
        return
        
def get_view_url(message, amount):
    admins = db.get('admins')
    url = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = view_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مشاهدات'
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(view(y['s'], url))
           
            if x == 'o':
                continue
            if x == True:
                true += 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= view_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*view_price}',reply_markup=bk)
    return
def get_time_private_vote(message, amount):
    if message.text == "/start":
        start_message(message)
        return
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية : {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط المنشور')
    bot.register_next_step_handler(x, get_url_private_vote, amount, time)
def get_url_private_vote(message, amount, time):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    load_ = db.get(f"ses_{message.from_user.id}") if db.exists(f"ses_{message.from_user.id}") else []
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    db.set(f"serv_{message.from_user.id}", True)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} \n• خدمة خاااصة vip')
    true, false = 0, 0
    nume = int(amount)
    db.set(f"stop_request_{message.from_user.id}", True)
    v = bot.reply_to(message,text=f'• تم بدء طلبك بنجاح ✅ : \n\n• النوع : {typerr}\n• الرابط : {url} \n• الكمية : {amount}')
    for y in load_:
        if true >= amount:
            break
        stre = db.get(f"stop_request_{message.from_user.id}")
        if stre is False:
            break
        try:
            x = asyncio.run(vote_one(y['s'], url, time))
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            xi = 7
        xi = 8
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {true*poll_price}',reply_markup=bk)
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts','chtime','send','send_link','code','tmoo', 'ads', 'story']
    for temp in a:
        db.delete(f'{temp}_{message.from_user.id}_proccess')
    return
def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True

def set_user(id, data):
    db.set(f'user_{id}', data)
    return True

def get(id):
    return db.get(f'user_{id}')

def delete(id):
    return db.delete(f'user_{id}')

def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "•<strong> المستخدمين الاكثر مشاركة لرابط الدعوى :</strong>\n"
    for user in sorted_users[:5]:
        result_string += f"🏅: ({len(user['users'])}) > {user['id']}\n"
    return (result_string)


def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None
def casting(message):
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الي مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الي : {bad} ')
    return
def adminss(message, type):
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return
def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return
def get_info(message):
    id = message.text
    try:
        id = int(id)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    d = db.get(f'user_{id}')
    if not d:
        bot.reply_to(message, f'• هذا العضو غير موجود')
        return
    # {'id': user_id, 'users': [], 'coins': 0, 'paid': False}
    id, coins, users = d['id'], d['coins'], len(d['users'])
    bot.reply_to(message, f'• ايديه : {id}.\n• نقاطه: {coins} نقطة \n• عدد مشاركته لرابط الدعوة{users}')
    return
def send(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح ')
        return
    if not db.exists(f'user_{id}'):
        bot.reply_to(message, f'• هذا العضو غير موجود في البوت ❌')
        return
    if int(message.text) == int(message.from_user.id):
        bot.reply_to(message, f'• عذرا لا يمكنك تحويل نقاط لنفسك ❌')
        return
    x2 = bot.reply_to(message, f'• ارسل الان عدد النقاط التي تريد تحويلها لـ {id}')
    bot.register_next_step_handler(x2, get_amount_send, id)
def get_amount_send(message, id):
    amount = message.text
    try:
        amount = int(message.text)
    except:
        te = bot.reply_to(message, f'• الكمية يجب ان تكون عدد فقط ')
        return
    to_user = db.get(f'user_{id}')
    from_user = db.get(f'user_{message.from_user.id}')
    if amount < 1:
        bot.reply_to(message, f'• لا يمكن تحويل عدد اقل من 1')
        return
    if from_user['coins'] < amount:
        bot.reply_to(message, f'• نقاطك غير كافية لتحويل هذا المبلغ \n• تحتاج الي {amount-from_user["coins"]} نقطة')
        return
    from_user['coins']-=amount
    db.set(f'user_{message.from_user.id}', from_user)
    to_user['coins']+=amount
    db.set(f'user_{id}', to_user)
    try:
        bot.send_message(chat_id=id, text=f"• [👤] تم استلام {amount} من نقاط\n\n- من الشخص : {message.from_user.id}\n- نقاطك القديمة : {to_user['coins']}\n- نقاطك الان : {to_user['coins']+amount}")
    except: pass
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بارسال <strong>{amount}</strong> نقطة\n من <code>{message.from_user.id}</code> ..')
    bot.reply_to(message, f"• [👤] تم ارسال {amount} من نقاط\n\n- الى الشخص : {id}\n- نقاطك القديمة : {from_user['coins']}\n- نقاطك الان : {from_user['coins']-amount}")
    user_id = message.from_user.id
    trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
    count_trans = trans + 1
    db.set(f"user_{user_id}_trans", int(count_trans))
    return
def addpoints(message):
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية')
    bot.register_next_step_handler(x, addpoints_final, id)
def addpoints_final(message, id):
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']+=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
    return
def setfo(message):
    if "@" not in message.text:
        bot.reply_to(message, f'• رجاء ارسل القناة بشكل صحيح')
        return 
    elif message.text == "/start":
        start_message(message)
        return 
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return
def vipp(message, type):
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get(f"user_{id}")
        if d is None:
            bot.reply_to(message, f'• العضو غير موجود في البوت')
            return
        d['premium'] = True
        db.set(f'user_{id}', d)
        db.set(f'private_{id}', True)
        bot.reply_to(message, f'• اصبح العضو {id} من المشتركين الـ ViP')
        return
    if type == 'les':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get(f"user_{id}")
        if d is None:
            bot.reply_to(message, f'• العضو غير موجود في البوت')
            return
        d['premium'] = False
        db.set(f'user_{id}', d)
        bot.reply_to(message, f"تم انهاء الاشتراك الـ ViP للمستخدم {id}")

def skip(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
    chats_dd = db.get('force_ch')
    joo = db.get(f"user_{user_id}")
    coin = joo['coins']
    chats_user = [chat for chat in chats_dd if chat not in chats_joining]
    doo = db.get('force_ch')
    if doo != None:
        for i in chats_user:
            chats_joining.append(i)
            db.set(f"chats_{user_id}", chats_joining)
            nextch(call)
            return
def nextch(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    v = 5
    if v == 5:
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                count = db.get(f"count_{i}")
                ids = db.get(f"id_{i}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    ii = i.replace('@', '')
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅", parse_mode="Markdown")
                    bot.send_message(chat_id=int(sudo), text=f"*تم انتهاء تمويل قناة [{name}](https://t.me/{ii}) بنجاح ✅*", parse_mode="Markdown")
                else: 
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    ii = i.replace('@', '')
                    k = f'''اشترك فالقناة {i}'''
                    keys = mk(
                        [
                            [btn(text='اشتركت ✅', callback_data='check_join')],
                            [btn(text='تبليغ 📛', callback_data='report'), btn(text='تخطي ⚠️', callback_data='skip')],
                            [btn(text='رجوع', callback_data='collect')]
                        ]
                    )
                    bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                    return
            kk = f"لا يوجد قنوات حالياً 🤍"
            key = mk(
                [
                    [btn(text='رجوع', callback_data='collect')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
def tmmo(msg):
    if msg.text == "/start":
        start_message(msg)
        return
    if not db.get(f'tmoo_{msg.from_user.id}_proccess'): return
    user_id = msg.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    coin = int(joo['coins'])
    try:
        count = int(msg.text)
    except:
        bot.reply_to(msg, '• يجب ان يكون عدد فقط')
        return
    hh = db.get("less_tmoil") if db.exists("less_tmoil") else 10
    if count <hh:
        bot.reply_to(msg, f"• اقل حد للطلب هو {hh} ❌")
        return
    all = int(price_join) * int(count)
    joo = db.get(f"user_{user_id}")
    if joo['coins'] < int(all):
        bot.reply_to(msg, "• عفوا ، نقاطك لا تكفي لهذا الطلب ❌")
        return
    x = bot.reply_to(msg, """⚠️ ارفع البوت @V42_bot ادمن في قناتك
ارسل معرف او رابط قناتك :""")
    bot.register_next_step_handler(x, tmm_count, count)
def tmm_count(msg,count):
    if msg.text == "/start":
        start_message(msg)
        return
    if not db.get(f'tmoo_{msg.from_user.id}_proccess'): return
    user_id = msg.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    channel = msg.text.replace('https://t.me/', '@').replace('@', '@')
    channels_force = db.get("force_ch") if db.exists("force_ch") else []
    channel_username = channel.lower().strip()
    try:
        chat_member = bot.get_chat_member(channel_username, bot.get_me().id)
    except:
        bot.reply_to(msg, "⚠️ لا يوجد قناة او مجموعة تحمل هذا المعرف", parse_mode="Markdown")
        return
    if str(chat_member.status) == "administrator":
        if channel_username in channels_force:
            count_befor = db.get(f"count_{channel_username}")
            alll = int(count_befor) + int(count)
            all_coins = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all_coins)
            db.set(f"user_{user_id}", joo)
            all_count = alll
            db.set(f"count_{channel_username}", all_count)
            all_mem = alll
            db.set(f"mem_{channel_username}", all_mem)
            db.set(f"id_{channel_username}", user_id)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            all_coins = int(price_join) * int(count)
            bot.reply_to(msg, f"تم انشاء تمويل ✅\n\n• الكمية : {alll}\n• السعر : {all_coins}\n• القناة : [{name}](https://t.me/{ii})\n\n• تأكد من عدم ازالة البوت من الادمنية\n• تم اضافة التمويل القديم الي الجديد", parse_mode="Markdown")
            bot.send_message(chat_id=int(sudo), text=f"- بدء تمويل قناة جديدة [{name}](https://t.me/{ii}) بـ {alll} عضو 🚸", parse_mode="Markdown")
        else:
            all = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all)
            db.set(f"user_{user_id}", joo)
            all_count = count
            db.set(f"count_{channel_username}", all_count)
            
            all_mem = count
            db.set(f"mem_{channel_username}", all_mem)
            db.set(f"id_{channel_username}", user_id)
            channels_force = db.get("force_ch") if db.exists("force_ch") else []
            channels_force.append(channel_username)
            db.set("force_ch", channels_force)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            bot.reply_to(msg, f"تم انشاء تمويل جديد ✨\n\n🩵] الكمية : {count}\n🌚] السعر : {all}\n💯] القناة : [{name}](https://t.me/{ii})\n\n♻️] تأكد من عدم ازالة البوت من الادمنية", parse_mode="Markdown")
            bot.send_message(chat_id=int(sudo), text=f"- بدء تمويل قناة جديدة [{name}](https://t.me/{ii}) بـ {count} عضو 🚸", parse_mode="Markdown")
    else:
        bot.reply_to(msg, "⚠️ البوت غير مشرف بهذه القناة", parse_mode="Markdown")
        return
def report(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
    
    key = mk(
        [
            [btn(text='تجميع النقاط ❇️', callback_data='invite')],
            [btn(text='رجوع ↪️', callback_data='back')]
        ]
    )
    chats_dd = db.get('force_ch')
    joo = db.get(f"user_{user_id}")
    coin = joo['coins']
    chats_user = [chat for chat in chats_dd if chat not in chats_joining]
    doo = db.get('force_ch')
    if doo != None:
        for i in chats_user:
            count = db.get(f"count_{i}")
            ids = db.get(f"id_{i}")
            
            if int(count) <= 0:
                tm = db.get("tmoil") if db.exists("tmoil") else 0
                tmm = int(tm) + 1
                db.set("tmoil", int(tmm))
                chats_dd = db.get('force_ch')
                chats_dd.remove(i)
                db.set("force_ch", chats_dd)
                chat_info = bot.get_chat(i)
                name = chat_info.title
                ii = i.replace('@', '')
                mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else ""
                bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) ب {mem} بنجاح ✅", parse_mode="Markdown")
                bot.send_message(chat_id=int(sudo), text=f"تم انتهاء تمويل قناة [{name}](https://t.me/{ii}) ب {mem} بنجاح ✅", parse_mode="Markdown")
            else: 
                chat_info = bot.get_chat(i)
                name = chat_info.title
                ii = i.replace('@', '')
                k = f'''اشترك فالقناة {i}'''
                keys = mk(
                    [
                        [btn(text='اشتركت ✅', callback_data='check_join')],
                        [btn(text='تبليغ 📛', callback_data='report'), btn(text='تخطي ⚠️', callback_data='skip')],
                        [btn(text='رجوع', callback_data='collect')]
                    ]
                )
                iddd = 5076382739
                keyss = mk(row_width=5)
                tar = btn(f'الغاء تمويل قناة {name}', callback_data=f'canceltmoil:{i}')
                keyss.add(tar)
                bot.send_message(chat_id=int(iddd), text=f"*• بلاغ جديد علي قناة *[{name}](https://t.me/{ii}) \n• الشخص الذي قام بالابلاغ :\n\n• الاسم : {call.from_user.first_name}\n• المعرف : @{call.from_user.username}\n• الايدي : [{user_id}](tg://user?id={user_id}) ", parse_mode="Markdown", reply_markup=keyss)
                bot.answer_callback_query(call.id, text="تم ارسال بلاغك الي المطور ⛔")
                bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys)
                return
                
                
def check_dayy(user_id):
    users = db.get(f"user_{user_id}_giftt")
    noww = time.time()    
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"user_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            users['timee'] = noww
            db.set(f'user_{user_id}_giftt', users)
            return None
    else:
        users = {}
        users['timee'] = noww
        db.set(f'user_{user_id}_giftt', users)
        return None

def change_points_mill(msg):
    link = msg.text
    try:
        forw = link.split("?start=")[1]
    except:
        bot.reply_to(msg, f"⌁︙رجاءاً أرسل رابط النقاط بصورة صحيحة.")
        return
    if "https://t.me/EEObot?start=" not in str(link):
        bot.reply_to(msg, f"⌁︙رجاءاً أرسل رابط النقاط بصورة صحيحة من بوت المليار.")
        return
    x = asyncio.run(mill(forw))
    if x == False:
        bot.reply_to(msg, f"الرابط⌁︙ غير صحيح او انتهت مدة الرابط !",reply_markup=bk)
        return
    else:
        try:
            points = int(x)
        except:
            bot.reply_to(msg, f"⌁︙رجاءاً أرسل رابط النقاط بصورة صحيحة.")
            return
        hh = db.get("less_change") if db.exists("less_change") else 500
        if points <hh:
            bot.reply_to(msg, f"⌁︙ عذرا ، الحد الادني لتحويل النقاط هو {hh} نقطة من بوت المليار",reply_markup=bk)
            return
        bef = points / 2
        b = db.get(f'user_{msg.from_user.id}')
        b['coins']+=int(bef)
        db.set(f'user_{msg.from_user.id}', b)
        bot.reply_to(msg, f"⌁︙تم بنجاح عملية تحويل {points} نقطة ✅\n\n⌁︙تم اضافة {int(bef)} نقطة الي حسابك بنجاح ✅",reply_markup=bk)

def price_joinn(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير عدد النقاط الي {it}",reply_markup=bk)
        db.set("price_join", it)
    except:
        bot.reply_to(msg, f"ارسل رقم فقط عزيزي",reply_markup=bk)
def coin_joinn(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير عدد النقاط الي {it}",reply_markup=bk)
        db.set("coin_join", it)
    except:
        bot.reply_to(msg, f"ارسل رقم فقط عزيزي",reply_markup=bk)
def less_tmoil(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير عدد النقاط الي {it}",reply_markup=bk)
        db.set("less_tmoil", it)
    except:
        bot.reply_to(msg, f"ارسل رقم فقط عزيزي",reply_markup=bk)
def price_adss(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير سعر الاعلان الي {it}",reply_markup=bk)
        db.set("price_ads", it)
    except:
        bot.reply_to(msg, f"ارسل رقم فقط عزيزي",reply_markup=bk)
def channel_adss(message):
    try:
        it = message.text
        bot.reply_to(message, f"تم تغيير قناة الاعلانات الي {it}",reply_markup=bk)
        db.set("channel_ads", it)
    except:
        bot.reply_to(msg, f"ارسل المعرف بشكل صحيح",reply_markup=bk)
def less_change(message):
    try:
        it = int(message.text)
        bot.reply_to(message, f"تم تغيير عدد النقاط الي {it}",reply_markup=bk)
        db.set("less_change", it)
    except:
        bot.reply_to(msg, f"ارسل رقم فقط عزيزي",reply_markup=bk)

def can_tmoil(message):
    chats = db.get("force_ch")
    if message.text in chats:
        chats.remove(message.text)
        db.set("force_ch", chats)
        bot.reply_to(message, f"⌁︙تم الغاء تمويل قناة {message.text} بنجاح ✅",reply_markup=bk)
    else:
        bot.reply_to(message, f"هذه القناة لا يتم تمويلها",reply_markup=bk)

def gen_code_name(message):
    name_code = message.text
    x = bot.reply_to(message,f'• ارسل الان عدد مستخدمين الكود الخاص بك')
    bot.register_next_step_handler(x, gen_code_num, name_code)
def gen_code_num(message, name_code):
    try:
        num_code = int(message.text)
    except:
        bot.reply_to(message,f'• ارسل رقم فقط')
        return
    x = bot.reply_to(message,f'• ارسل الان عدد النقاط التي تريد وضعها داخل الكود')
    bot.register_next_step_handler(x, gen_code_coin, name_code, num_code)
    
def gen_code_name(message):
    name_code = message.text
    x = bot.reply_to(message,f'⌁︙ارسل الان عدد مستخدمين الكود الخاص بك')
    bot.register_next_step_handler(x, gen_code_num, name_code)
def gen_code_num(message, name_code):
    try:
        num_code = int(message.text)
    except:
        bot.reply_to(message,f'⌁︙ارسل رقم فقط')
        return
    x = bot.reply_to(message,f'⌁︙ارسل الان عدد النقاط التي تريد وضعها داخل الكود')
    bot.register_next_step_handler(x, gen_code_coin, name_code, num_code)

def gen_code_coin(message, name_code, num_code):
    try:
        coin_code = int(message.text)
    except:
        bot.reply_to(message,f'• ارسل رقم فقط')
        return
    db.set(f"coin_code_{name_code}", int(coin_code))
    db.set(f"num_code_{name_code}", int(num_code))
    db.set(f"name_code_{name_code}", str(name_code))
    bot.reply_to(message,f'<strong>• تم انشاء كود هدية جديد 🔥</strong>\n\n• الكود : <code>{name_code}</code>\n• عدد النقاط : {coin_code} \n• عدد المستخدمين : {num_code}')
    
def use_codes(msg):
    if msg.text == "/start":
        start_message(msg)
        return False
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(msg, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    text = msg.text
    if db.exists(f"name_code_{text}"):
        user_code = db.get(f"num_code_{text}")
        used_codes = db.get(f"used_codes_{text}") if db.exists(f"used_codes_{text}") else []
        if msg.from_user.id in used_codes:
            bot.reply_to(msg,f'• لقد استخدمت هذا الكود من قبل ❌')
            return
        if user_code >= 1:
            coin_code = db.get(f"coin_code_{text}")
            join_user = msg.from_user.id
            joo = db.get(f"user_{join_user}")
            joo['coins'] = int(joo['coins']) + int(coin_code)
            db.set(f"user_{msg.from_user.id}", joo)
            bot.reply_to(msg,f'• تم اضافة {coin_code} نقاط الي حسابك ✅')
            user_after = int(user_code) - 1
            db.set(f"num_code_{text}", user_after)
            used_codes.append(msg.from_user.id)
            db.set(f'used_codes_{text}', used_codes)
            start_message(msg)
            user_id = msg.from_user.id
            code = int(db.get(f"cd_{user_id}")) if db.exists(f"cd_{user_id}") else 0
            daily_count = code + 1
            db.set(f"cd_{user_id}", int(daily_count))
            bot.send_message(chat_id=int(sudo), text=f'''🎁- قام العضو : [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) | `{msg.from_user.id}`\n\n✅- بشحن كود الهدية : {msg.text}\n\n☑️- عدد نقاط الكود : {coin_code}\n\n👤- عدد نقاطه الان : {joo['coins']}\n\n🤖- عدد الأشخاص المتبقية : {user_after}''', parse_mode='MarkDown')
        else:
            bot.reply_to(msg,'• انتهت صلاحية هذا الكود ❌')
    else:
        bot.reply_to(msg,f'• لقد ادخلت كود بشكل خطا ❌')

def check_forward_bot(message, robot):
    if message.text == "/start":
        start_message(message)
        return
    user_id = message.from_user.id
    try:
        username = message.forward_from.username
        if str(username.lower()) == str(robot.replace('@', '').lower()):
            bots_joining = db.get(f"bots_{user_id}") if db.exists(f"bots_{user_id}") else []
            price_tmoo_bot = db.get('price_tmoo_bot') if db.exists('price_tmoo_bot') else 5
            join_tmoo_bot = db.get('join_tmoo_bot') if db.exists('join_tmoo_bot') else 5
            bots_joining.append(robot)
            db.set(f"bots_{user_id}", bots_joining)
            count = db.get(f'count_{robot}')
            id = db.get(f'id_{robot}')
            count -= 1
            db.set(f'count_{robot}', count)
            acc = db.get(f'user_{user_id}')
            acc['coins'] += join_tmoo_bot
            db.set(f'user_{user_id}', acc)
            bot.send_message(chat_id=id, text=f'''<strong>• قام عضو بتفعيل البوت الخاص بك ✅</strong>\n\n- العدد المتبقي : {count}''', parse_mode='html')
            keys = mk(row_width=1)
            btn1 = btn('متابعة التجميع 🤖', callback_data="join_bots")
            btn2 = btn('رجوع ↪️', callback_data="back")
            keys.add(btn1, btn2)
            bot.reply_to(message, f'<strong>• تم تفعيل البوت بنجاح ✅</strong>\n\n- تم اضافة : {price_tmoo_bot} نقطة الي حسابك.', reply_markup=keys)
            if count <= 0:
                tmoo_bots = db.get('tmoo_bots') if db.exists('tmoo_bots') else []
                tmoo_bots.remove(robot)
                db.set('tmoo_bots', tmoo_bots)
                bot.send_message(chat_id=id, text=f'''<strong>• تم انتهاء تمويل بوتك {robot} بنجاح ✅</strong>''', parse_mode='html')
                bots = db.get('bots') if db.exists('bots') else 0
                bots += 1
                db.set('bots', bots)

        else:
            x = bot.reply_to(message, f'<strong>• برجاء التحقق من ان الرسالة محولة من بوت {robot} 🤖</strong>\n\n- اعد تحويل الرسالة مره اخرى.')
            bot.register_next_step_handler(x, check_forward_bot, robot)
    except Exception as a:
        print(a)
        x = bot.reply_to(message, f'<strong>• برجاء التحقق من ان الرسالة موجهه من بوت {robot} 🤖</strong>\n\n- اعد الارسال مره اخرى، ارسل /start لتخطي المتابعة')
        bot.register_next_step_handler(x, check_forward_bot, robot)

try:
    bot.infinity_polling()
except:
    pass
