# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="EpB4i1nhcYGC4NcouTjf.TZjEI917pMDTTp1BY9K5+W.oCEZfjyRT+DdHRBpUrjffvCGoa6iJpmFiwVSApq0I74=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EpblCz73hrX3hUpoZinb.Fg2xAK8+c6My92znQ5+akW.qGkHLORfc68TpHk9vzfMtZbCA06MPadGC+gSVW+b32I=")
ki.loginResult()

ag = LINETCR.LINE()
ag.login(token="Ep3VVe1Mz0oVsf2b9PM8.tSL6Ni+BpiVGFpzQ9Gu22a.iX2bLYPIjcAWZhnc1yDJr52i+Dtw+kZ9Z8pdep3Yaqc=")
ag.loginResult()

print "╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ Login Success WIB\n║╚════════════════════════\n╚═════════════════════════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
   🅲🅾🅼🅼🅰🅽🅳

➧   Help  
➧   Myhelp
➧   Me
➧   Myname: 
➧   Mybio: 
➧   Mybio
➧   Mypict
➧   Mycover
➧   Mycopy @
➧   Mybackup
➧   Getgrup image
➧   Speed Response
➧   Getmid @
➧   Getprofile @
➧   Getcontact @
➧   Getinfo @
➧   Getname @
➧   Getbio @
➧   Getpict @
➧   Getcover @
➧   Mention
➧   Lurk on/off
➧   Lurkers
➧   Mimic on/off
➧   Micadd @
➧   Micdel @
➧   Link on/off
➧   Url/Gurl
➧   Cancel
➧   Gcreator
➧   Hai @
➧   Kick @
➧   Ulti @
➧   Sentil @
➧   Dj @
➧   Cancel
➧   Gname: 
➧   Gbroadcast: 
➧   Cbroadcast: 
➧   Infogrup
➧   Gruplist
➧   Link bokep
➧   Friendlist
➧   Blocklist
➧   Ban @
➧   Unban @
➧   Clearban
➧   Banlist
➧   Contactban
➧   Midban
➧   Midban
➧   Nuke
➧   Expert crash
➧   Talkban
➧   Takol
➧   Takel
➧   Talklist
➧   Sp
➧   Sp all
➧   Dsp
➧   Sp set

    ℬℽ : W⃟   I⃟   B⃟   
"""

myhelp ="""
     🆂🅴🆃🆃🅸🅽🅶🆂

➧   Contact on/off
➧   Autojoin on/off
➧   Autoleave on/off
➧   Autoadd on/off
➧   Sleep on/off
➧   Read on/off
➧   Simi on/off
➧   Sensi on/off
➧   Autocrash on/off
➧   Crashpc on/off
➧   Crashtag on/off
➧   Crashkick on/off
➧   Pc on/off
➧   Dm on/off
➧   Pergi on/off
➧   Welcome on/off
➧   Protect on/off
➧   High on/off
➧   Qr on/off
➧   Invit on/off
➧   Cancel on/off
➧   Talkban on/off
➧   Apakah
➧   Checkdate
➧   Cekig
➧   Kapan
➧   Lirik
➧   Music
➧   Profileig
➧   Quote
➧   Time
➧   Runtime
➧   say-id
➧   say-en
➧   say-jp
➧   say-ko
➧   Youtube

   ℬℽ : W⃟   I⃟   B⃟   
"""

mulai = time.time()

mid = cl.getProfile().mid
kimid = ki.getProfile().mid
agmid = ag.getProfile().mid
Bots=[mid,kimid,agmid]
admin=["u4a361586c55ac4ef218a0a9b78b2f1b3","u4fd239a77c16d1ea7853cd801f6c379d"]
owner=["u4a361586c55ac4ef218a0a9b78b2f1b3"]
Creator=["u4a361586c55ac4ef218a0a9b78b2f1b3"]
staff=["u4a361586c55ac4ef218a0a9b78b2f1b3","u4fd239a77c16d1ea7853cd801f6c379d"]

wait = {
    "likeOn":False,
    "alwayRead":False,
    "detect":False,
    "kickMention":False,
    "steal":False,
    "talkban":{},
    'pap':{},
    'invite':{},
    "spam":{},
    "blacklist":{},
    "talkblacklist":{},
    "talkwblacklist":False,
    "talkdblacklist":False,
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":10},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Thnx for add me",
    "lang":"JP",
    "comment":"",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "respondpc":False,    
    "crashpc":False, 
    "crashTag":False, 
    "crashKick":False, 
    "autoCrash":False, 
    "Wc":True,
    "Lv":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect": False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
} 

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke"]

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "•\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)        
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
                
#-----------------------------------------------
#        if op.type == 19:
#            try:
#                if op.param3 in mid:
#                    if op.param2 in kimid:
#                        G = ki.getGroup(op.param1)
#                        G.preventJoinByTicket = False
#                        ki.updateGroup(G)
#                        Ticket = ki.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ag.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G.preventJoinByTicket = True
#                        cl.updateGroup(G)
#                    else:
#                        G = ki.getGroup(op.param1)




#                        ki.kickoutFromGroup(op.param1,[op.param2])
#                        G.preventJoinByTicket = False
#                        ki.updateGroup(G)
#                        Ticket = ki.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ag.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G.preventJoinByTicket = True
#                        cl.updateGroup(G)
#                        ki.updateGroup(G)
#                        wait["blacklist"][op.param2] = True



#                elif op.param3 in kimid:
#                    if op.param2 in agmid:
#                        G = ag.getGroup(op.param1)
#                        G.preventJoinByTicket = False
#                        ag.updateGroup(G)
#                        Ticket = ag.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ag.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G.preventJoinByTicket = True
#                        ag.updateGroup(G)
#                    else:
#                        G = ag.getGroup(op.param1)

#                        ag.kickoutFromGroup(op.param1,[op.param2])
#                        G.preventJoinByTicket = False
#                        ag.updateGroup(G)
#                       Ticket = ag.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        ag.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G.preventJoinByTicket = True
#                        ki.updateGroup(G)   
#-----------------------------------------------       

        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
           else: 
              pass
              
        if op.type == 19:
           if op.param3 in admin:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,admin)
           else:
               pass
               
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ag.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ag.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
               
                if kimid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ag.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
               
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ag.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if agmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ag.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ag.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ag.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ag.updateGroup(G)
                    Ticket = ag.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
	
        if op.type == 5:
            if wait["autoAdd"] == True: 
                cl.findAndAddContactsByMid(op.param1)
                xname = cl.getContact(op.param1).displayName
                cl.sendText(op.param1, "Halo " + xname + " ,terimakasih telah menambahkan saya sebagai teman :3")
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message            
            if msg.text in ["Crash","crash"]:
              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash","Kamu asu ngecrash terus!")
              ket = random.choice(dia)
              cl.sendText(msg.to,ket)
              cl.kickoutFromGroup(msg.to,[msg.from_])
              cl.sendText(msg.to,"Mampus Lu Kekick 😂")                            
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[SimiSimi] " + data['result']['response'].encode('utf-8'))
                                
            if wait["respondpc"] == True:
                if msg.toType == 0:                	
                    cl.sendChatChecked(msg.from_,msg.id)
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Halo 「" + cName + "」\nMohon Maaf  Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Nanti, Terimakasih."]
                    agler = "" + random.choice(balas)                    
                    cl.sendText(msg.from_,agler) ## "Halo", displayName + "\n\nMohon Maaf Riko Sedang Sibuk, Ini Adalah Pesan Otomatis, Jika Ada Yang Penting Mohon Hubungi Riko Nanti, Terimakasih.")                                        

            if wait["crashpc"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                    cl.sendText(msg.from_,"「Dont Chat Me!! 」")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "',"}                	
                    cl.sendMessage(msg)  
                    
            if 'MENTION' in msg.contentMetadata.keys() != {'mid': mid}:
                 if wait["detect"] == True:
                    xname = cl.getContact(msg.from_).displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    balas = "@"+xname+ " What ?","@"+xname+ " Dont Tag Me!! Im Busy 😒","@"+xname+ " Sokap lu ngetag ngetag","@"+xname+ " Im just newbie","@"+xname+ " Jangan Suka Tag gua.","@"+xname+ " Kenapa ngetag? Kangen? Pc ae","@"+xname+ " Gausah ngetag ngetag","@"+xname+ " Ada apa?","@"+xname+ " Ada perlu apa?","@"+xname+ " ┌П┐(◣_◢)┌П┐"
                    msg.text = random.choice(balas)
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                    cl.sendMessage(msg)
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["crashTag"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Hadeeeh",cName + "┌П┐(◣_◢)┌П┐"]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "',"}                	
                                  cl.sendMessage(msg)                                       
                                  break                                              
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["[Auto Respon] Dont Tag Me!! Im Busy ",cName + " Ngapain Ngetag?, ",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja ", cName + " Kenapa Tag saya? ","┌П┐(◣_◢)┌П┐ " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?",cName + " ┌П┐(◣_◢)┌П┐"]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "',"}                	
                                  cl.sendMessage(msg)                                                                                      
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             cl.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 cl.inviteIntoGroup(msg.to,[target])
                                 cl.sendText(msg.to,"Telah Menginvite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      cl.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                    
            if msg.contentType == 1:
                cl.sendText(msg.to,"Foto apa itu ?")
            if msg.contentType == 12:
                cl.sendText(msg.to,"Link apaan itu?")
            if msg.contentType == 14:
                cl.sendText(msg.to,"Filenya auto download")
                               
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    
            if wait["autoCrash"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)      
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "',"}                	
                    cl.sendMessage(msg)                    
                    
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmsg + datetime.today().strftime('%H:%M:%S'))
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Creator}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'myhelp':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,myhelp + datetime.today().strftime('%H:%M:%S'))
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': Creator}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,myhelp)            
            elif "Mybot" == msg.text:
            	cl.sendText(msg.to,"This Is My Bot")
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': agmid}
                cl.sendMessage(msg) 
                msg.contentType = 13
#==============================================================================#              
            elif "Tagmid " in msg.text:
                    mid_ = msg.text.replace("Tagmid ","")
		    for eue in mid_:
			    xname = cl.getContact(eue).displayName
			    xlen = str(len(xname)+1)
			    msg.contentType = 0
			    msg.text = "@"+xname+ ""
			    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid_)+'}]}','EMTVER':'4'}
			    cl.sendMessage(msg)
#==============================================================================#              
            elif msg.text in ["Speed","Sp","speed","sp"]:
              if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "「Please wait..」")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))
                
            elif msg.text in ["Sp all"]:
              if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "「Please wait..」")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))
                ki.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))
                ag.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))

            elif msg.text in ["Dsp",".Sp",".Speed",".speed"]:
               if msg.from_ in owner or admin or staff:            	
                cl.sendText(msg.to, "「 Debug Speed 」\n☼Type: speed\n☼Testing....")
                start = time.time()
                for i in range(3000):
                    1+1 
                elsp = time.time() - start
                cl.sendText(msg.to, "「 Debug Speed」\nType: speed\nTime taken: %s" % (elsp))   

            elif msg.text in ["Sp set"]:
               if msg.from_ in owner or admin or staff:            	
                cl.sendText(msg.to, "「 Debug Speed 」\n☼Type: Speed Setting\n☼Testing....")
                cl.sendText(msg.to, "=====「Speed Setting」=====")
                start = time.time()
                start2 = time.time()
                start3 = time.time()
                start4 = time.time()             
                start5 = time.time()             
                start6 = time.time()             
                start7 = time.time()    
                start8 = time.time()             
                start9 = time.time()             
                start10 = time.time()                         
                for i in range(3000):
                    1+1
                elsp = time.time() - start          
                elsp2 = time.time() - start2
                elsp3 = time.time() - start3
                elsp4 = time.time() - start4
                elsp5 = time.time() - start5
                elsp6 = time.time() - start6
                elsp7 = time.time() - start7
                elsp8 = time.time() - start8
                elsp9 = time.time() - start9
                elsp10 = time.time() - start10    
                cl.sendText(msg.to, "「 Debug Speed」\nType: Contact\nTime taken: %s" % (elsp))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: AutoJoin\nTime taken: %s" % (elsp2))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: AutoCancel\nTime taken: %s" % (elsp3))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: LeaveRoom\nTime taken: %s" % (elsp4))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: Timeline\nTime taken: %s" % (elsp5))                
                cl.sendText(msg.to, "「 Debug Speed」\nType: AutoAdd\nTime taken: %s" % (elsp6))                
                cl.sendText(msg.to, "「 Debug Speed」\nType: Protect\nTime taken: %s" % (elsp7))    
                cl.sendText(msg.to, "「 Debug Speed」\nType: Linkprotect\nTime taken: %s" % (elsp8))        
                cl.sendText(msg.to, "「 Debug Speed」\nType: Inviteprotect\nTime taken: %s" % (elsp9))      
                cl.sendText(msg.to, "「 Debug Speed」\nType: Cancelprotect\nTime taken: %s" % (elsp10))     
                                                              

#----------------------------------------------------------
            elif msg.text in ["Respon","respon"]:
                cl.sendText(msg.to,"Hadir booos WIB")
                ki.sendText(msg.to,"Hadir booos WIB")
                ag.sendText(msg.to,"Hadir booos WIB")
                cl.sendText(msg.to,"WIB - BOT")
#==============================================================================#                                                                                  
            elif 'Xpertcrash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ",'"}
                cl.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
                cl.sendMessage(msg)                                                   
            elif msg.text.lower() == '...':
               if msg.from_ in owner or admin or staff:           	
                msg.contentType = 13
                msg.contentMetadata = {'mid': "',"}
                cl.sendText(msg.to,"Sepi ea ┌П┐(◣_◢)┌П┐")
                cl.sendMessage(msg)
            elif msg.text in ["404"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
            elif msg.text.lower() == 'me':
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    xname = cl.getProfile().displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    msg.text = "@"+xname+ ""
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                    cl.sendMessage(msg)
            elif msg.text.lower() == 'Hai @':
                _name = msg.text.replace("Hai @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': "',"}
                            cl.sendMessage(g.mid,msg.to + str(msg))
                            cl.sendText(g.mid, "Hallo")
                            cl.sendText(g.mid, "Error ya 😅 ??")
                            print " Spammed crash Wkwkwk!"                            
#========================== B O T ``C O M M A N D =============================#
#==============================================================================#
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"contact already on")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ❎ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Contact」\nType: Contact\nStatus: Contact ❎ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"contact already off")
            elif msg.text.lower() == 'high on':
               if msg.from_ in owner or admin or staff:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection High Already ON")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection High Already ON")
            elif msg.text.lower() == 'protect on':
               if msg.from_ in owner or admin or staff:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection already on")                                               
            elif msg.text.lower() == 'qr on':
               if msg.from_ in owner or admin or staff:            	
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect qr ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect qr ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'invit on':
               if msg.from_ in owner or admin or staff:            	
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'cancel on':
               if msg.from_ in owner or admin or staff:            	
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'autojoin on':   
               if msg.from_ in owner or admin or staff:             
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
            elif msg.text.lower() == 'autojoin off':
               if msg.from_ in owner or admin or staff:            	
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join」\nType: Auto join\nStatus: Auto join ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
            elif msg.text.lower() == 'high off':
               if msg.from_ in owner or admin or staff:            	
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection High Already OFF")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection High」\nType: Protection High\nStatus: Protect high ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection High Already OFF")                        
            elif msg.text.lower() == 'protect off':
               if msg.from_ in owner or admin or staff:            	
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection」\nType: Protection\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'qr off':
               if msg.from_ in owner or admin or staff:            	
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Qr」\nType: Protection Qr\nStatus: Protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'invit off': 
               if msg.from_ in owner or admin or staff:           	
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protection Invite」\nType: Protection Invite\nStatus: Protect invite ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'cancel off':
               if msg.from_ in owner or admin or staff:            	
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protection」\nType: Cancel Protection\nStatus: Cancel protect ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
            elif "Grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'autoleave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave」\nType: Auto leave\nStatus: Auto leave ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Share」\nType: Share\nStatus: Share ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Share already off")
 #==============================================================================#                                   
            elif msg.text.lower() == 'set':   
               if msg.from_ in owner or staff:
                md = ""
                if wait["autoJoin"] == True: md+="Auto join  ✔\n"
                else: md +="Auto join ☞ ✖\n"  
                if wait["autoCancel"]["on"] == True:md+="Auto cancel ☞" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "Group cancel  ✖\n"
                if wait["leaveRoom"] == True: md+="Auto leave  ✔\n"
                else: md+="Auto leave  ✖\n"
                if wait["contact"] == True: md+="Contact  ✔\n"
                else: md+="Contact  ✖\n"
                if wait["timeline"] == True: md+="Share  ✔\n"
                else:md+="Share  ✖\n"
                if wait["alwayRead"] == True: md+="Auto read  ✔\n"
                else: md +="Auto read  ✖\n"
                if wait["crashpc"] == True: md+="Auto crash pc  ✔\n"
                else: md +="Auto crash pc  ✖\n"
                if wait["crashTag"] == True: md+="Tag crash  ✔\n"
                else: md +="Tag crash  ✖\n"
                if wait["crashKick"] == True: md+="Auto crash kick ✔\n"
                else: md +="Auto crash kick  ✖\n"
                if wait["autoCrash"] == True: md+="Auto crash  ✔\n"
                else: md +="Auto crash  ✖\n"
                if wait["respondpc"] == True: md+="Auto respond  ✔\n"
                else: md +="Auto respond pc  ✖\n"
                if wait["detect"] == True: md+="Respond tag  ✔\n"
                else: md +="Respond tag  ✖\n"
                if wait["kickMention"] == True: md+="Mention kick  ✔\n"
                else: md +="Mention kick ✖\n"
                if wait["protect"] == True: md+="Protect  ✔\n"
                else:md+="Protect  ✖\n"
                if wait["protect"] == True: md+="High  ✔\n"
                else:md+="High  ✖\n"
                if wait["linkprotect"] == True: md+="Link protect  ✔\n"
                else:md+="Link protect  ✖\n"
                if wait["inviteprotect"] == True: md+="Invitation protect  ✔\n"
                else:md+="Invitation protect  ✖\n"
                if wait["cancelprotect"] == True: md+="Cancel protect  ✔\n"
                else:md+="Cancel protect  ✖"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)      
 #==============================================================================#              
            elif cms(msg.text,["Bot creator","Bot Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u4a361586c55ac4ef218a0a9b78b2f1b3"}
                cl.sendMessage(msg)
            elif cms(msg.text,["staff","Staff"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': staff}
                cl.sendMessage(msg)       
            elif cms(msg.text,["admin","Admin"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                cl.sendMessage(msg)       
#==============================================================================#         
            elif msg.text.lower() == 'autoadd on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ✔ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add」\nType: Auto add\nStatus: Auto add ❌ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Actived")
                    else:
                        cl.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Jam")
#==============================================================================#
#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                cl.sendText(msg.to,"Send Contact 😎")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Simi on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simi off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","R on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"「 Auto Read」\nType: All\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Read off","R off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"「 Auto Read」\nType: All\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["C on","Autocrash on"]:
                wait["autoCrash"] = True
                cl.sendText(msg.to,"「 Auto Crash」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["C off","Autocrash off"]:
                wait["autoCrash"] = False
                cl.sendText(msg.to,"「 Auto Crash」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Pc on","Responpc on"]:
                wait["respondpc"] = True
                cl.sendText(msg.to,"「 Auto Respon Pc」\nType: Respon Pc\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Pc off","Responpc off"]:
                wait["respondpc"] = False
                cl.sendText(msg.to,"「 Auto Respon Pc」\nType: Respon Pc\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Cpc on","Crashpc on"]:
                wait["crashpc"] = True
                cl.sendText(msg.to,"「 Auto Respon Pc」\nType: Respon Pc\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Cpc off","Crashpc off"]:
                wait["crashpc"] = False
                cl.sendText(msg.to,"「 Auto Respon Pc + Crash」\nType: Respon Pc\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Ct on","Crashtag on"]:
                wait["crashTag"] = True
                cl.sendText(msg.to,"「 Mention Crash」\nType: Respon Pc\nStatus: On tSuccess\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Ct off","Crashtag off"]:
                wait["crashTag"] = False
                cl.sendText(msg.to,"「 Mention Crash」\nType: Respon Pc\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Ck on","Crashkick on"]:
                wait["crashKick"] = True
                cl.sendText(msg.to,"Kick Crash Set to ON")
                
            elif msg.text in ["Ck off","Crashkick off"]:
                wait["crashKick"] = False
                cl.sendText(msg.to,"Kick Crash Set to OFF")      
                
            elif msg.text in ["Sleep on","Detect mention on","Dm on","Tag on","Respon on","Modeoff on"]:
                if wait["detect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,)
                else:
                    wait["detect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                        
            elif msg.text in ["Sleep off","Detect mention off","Dm off","Tag off","Respon off","Modeoff off"]:
                if wait["detect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["detect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
            
            elif msg.text in ["Sensi on","S on","Kick mention on","Km on","Responkick on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"「 Kick Mention」\nType: Respon Group\nStatus: On Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif msg.text in ["Sensi off","S off","Kick mention off","Km off","Responkick off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"「 Kick Mention」\nType: Respon Group\nStatus: Off Success\n\n"+ datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.text in ["Welcome on","welcome on","Wc on","wc on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ yg joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
            elif msg.text in ["Welcome off","welcome off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ yg joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already oғғ")
                            
            elif msg.text in ["Pergi on","pergi on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ yg leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","pergi off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"noтιғ yg leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif msg.text in ["BUBAR","bubar","bubar tolol"]:
            	   cat = ["http://dl.profile.line-cdn.net/0m002af1d3725161d09deb2597257acb237065e3003073"]
                   meow = random.choice(cat)
                   cl.sendImageWithURL(msg.to,meow)
#==============================================================================#
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif msg.text in ["Gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
               
            elif msg.text in ["Spam gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
#============================ooo==================================================#
            elif "Salam1" in msg.text:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
            elif "Salam2" in msg.text:
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
                if msg.from_ in admin:
    				if msg.toType == 2:
    					if msg.toType == 2:
    						print "ok"
    						_name = msg.text.replace("Salam3","")
    						gs = cl.getGroup(msg.to)
    						gs = cl.getGroup(msg.to)
    						gs = cl.getGroup(msg.to)
    						gs = cl.getGroup(msg.to)
    						cl.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
    						cl.sendText(msg.to,"maaf kalo gak sopan")
    						targets = []
    						for g in gs.members:
    							if _name in g.displayName:
    								targets.append(g.mid)
    						if targets == []:
    							cl.sendText(msg.to,"Not found.")
    						else:
    							for target in targets:
    								try:
    									klist=[kr,kr1,kr2,kr3]
    									kicker=random.choice(klist)
    									kicker.kickoutFromGroup(msg.to,[target])
    									print (msg.to,[g.mid])
    								except:
    									cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                        cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                        cl.sendText(msg.to,"Nah salamnya jawab sendiri jadinya")
#==============================================================================#
            elif "Cleanse" in msg.text:
                if msg.from_ in owner or admin:    	
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"Grup Cleanse")
#-----------------------------------------------------
                                
            elif "Ratakan" in msg.text:
                if msg.from_ in owner or admin or staff:            	
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"Grup Dibersihkan")
#-----------------------------------------------------------
            
            elif "Kickall" in msg.text:
				OWN = "u4a361586c55ac4ef218a0a9b78b2f1b3"
				if msg.from_ in OWN:
					pass
				else:
					nk0 = msg.text.replace("Fuck","")
					nk1 = nk0.lstrip()
					nk2 = nk1.replace("@","")
					nk3 = nk2.rstrip()
					_name = nk3
					gs = cl.getGroup(msg.to)
					targets = []
					for h in gs.members:
						if _name in h.displayName:
							targets.append(h.mid)
					if targets == []:
						sendMessage(msg.to,"PEMBERSIHAN!!")
						pass
					else:
						for target in targets:
							try:
								if msg.from_ not in target:
									cl.kickoutFromGroup(msg.to, [target])							   
							except:
									cl.kickoutFromGroup(msg.to, [target])							   
									pass
            elif "Mayhem" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n' abort' to abort♪")
                    cl.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[cl]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   cl.sendText(msg.to,"Mayhem done")
            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Success ea 😅")
            
            elif ("Ulti " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Success ea 😅")
            
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.from_ in owner:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada undangan")
                        else:
                            cl.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'ourl':
                if msg.from_ in owner:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 URL Group」\nType: Url\nStatus: Url open success")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'curl':
                if msg.from_ in owner:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 URL Group」\nType: Url\nStatus: Url close success")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in owner:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"「 LINK Group」\nType: Link group\nStatus: line://ti/g/" + gurl)
                    
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                    
            elif "Gcreator" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.from_ in owner:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(X)
            
            elif msg.text.lower() == 'infogrup':        
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in ["Quote","quote","quotes","Quotes"]:
                quote = ['Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut\n\nQuote By WIB.','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL.\n\nQuote By WIB.','Buang mantan di TPA']
                psn = random.choice(quote)
                cl.sendText(msg.to,psn)
#==============================================================================#
            elif msg.text == "Link bokep":
                    cl.sendText(msg.to,"nekopoi.host")
                    cl.sendText(msg.to,"sexvideobokep.com")
                    cl.sendText(msg.to,"memek.com")
                    cl.sendText(msg.to,"pornktube.com")
                    cl.sendText(msg.to,"faketaxi.com")
                    cl.sendText(msg.to,"videojorok.com")
                    cl.sendText(msg.to,"watchmygf.mobi")
                    cl.sendText(msg.to,"xnxx.com")
                    cl.sendText(msg.to,"pornhd.com")
                    cl.sendText(msg.to,"xvideos.com")
                    cl.sendText(msg.to,"vidz7.com")
                    cl.sendText(msg.to,"m.xhamster.com")
                    cl.sendText(msg.to,"xxmovies.pro")
                    cl.sendText(msg.to,"youporn.com")
                    cl.sendText(msg.to,"pornhub.com")
                    cl.sendText(msg.to,"anyporn.com")
                    cl.sendText(msg.to,"hdsexdino.com")
                    cl.sendText(msg.to,"rubyourdick.com")
                    cl.sendText(msg.to,"anybunny.mobi")
                    cl.sendText(msg.to,"cliphunter.com")
                    cl.sendText(msg.to,"sexloving.net")
                    cl.sendText(msg.to,"free.goshow.tv")
                    cl.sendText(msg.to,"eporner.com")
                    cl.sendText(msg.to,"Pornhd.josex.net")
                    cl.sendText(msg.to,"m.hqporner.com")
                    cl.sendText(msg.to,"m.spankbang.com")
                    cl.sendText(msg.to,"m.4tube.com")
                    cl.sendText(msg.to,"brazzers.com")
#==============================================================================#
            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═══════List Friend═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Friend═══════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═══════List Member═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Member═══════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═══════List FriendMid═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═══════List FriendMid═══════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═══════List Blocked═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Blocked═══════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═══════List Grup═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═══════List Grup═══════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═══════List GrupMid═══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═══════List GrupMid═══════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (cl.getGroup(i).name +" ? ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
                         
            elif "Auto add" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.findAndAddContactsByMids(mi_d)
                cl.sendText(msg.to,"Success Add all")
                    
            elif "@bye" in msg.text:
                if msg.from_ in owner or admin or staff:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------------------------------------                            
            elif "mention" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Dor","Ats","Tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error              
#==============================================================================#
            elif "Ngh" in msg.text:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  ag.acceptGroupInvitationByTicket(msg.to,Ti)                  
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
#-------------------------------------------------------------    
#-----------------------------------------------------------
            elif msg.text in ["@"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					ag.leaveGroup(msg.to)
                except:
                     pass 
#-----------------------------------------------------------

            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
                        
            elif "slurker on" == msg.text.lower():
               if msg.from_ in staff:            	
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "slurker off" == msg.text.lower():
               if msg.from_ in staff:            	
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "slurkers" == msg.text.lower():
                 if msg.from_ in staff:           	
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
                        
            elif "Sider on" == msg.text.lower():
               if msg.toType == 2:         	
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "Sider off" == msg.text.lower():
               if msg.toType == 2:   	
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "Siders" == msg.text.lower():
                if msg.toType == 2:	
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")                        
                        
            elif "Gbroadcast: " in msg.text:  	
                bc = msg.text.replace("Gbroadcast: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text: 	
                bc = msg.text.replace("Cbroadcast: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i, bc)
            
            elif "Spam change: " in msg.text:            	
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
                    
            elif "Tag:10 @" in msg.text:
                _name = msg.text.replace("Tag:10 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        
            elif "Tag:15 @" in msg.text:
                _name = msg.text.replace("Tag:15 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
            
            elif "Tag @" in msg.text:
                _name = msg.text.replace("Tag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                        
            elif "Tag:25 @" in msg.text:
                _name = msg.text.replace("Tag:25 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                        
            elif "Tag:30 @" in msg.text:
                _name = msg.text.replace("Tag:30 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                        
            elif "Tag:35 @" in msg.text:
                _name = msg.text.replace("Tag:35 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                        
            elif "Tag:40 @" in msg.text:
                _name = msg.text.replace("Tag:40 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                        
            elif "Tag:45 @" in msg.text:
                _name = msg.text.replace("Tag:45 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
                        
            elif "Tag:50 @" in msg.text:
                _name = msg.text.replace("Tag:50 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["pap"])
#==============================================================================#
            elif msg.text.lower() == 'mymid':
                cl.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change ◑")          
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio👉" + string + "👈")
            elif msg.text in ["Myname"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif "Mycopy @" in msg.text:	
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:    	
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#==============================================================================#
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
                
            elif "playstore " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("playstore ","")
                    cl.sendText(msg.to,"Sedang Mencari boss...")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"Ketemu boss ^")
                    
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
                    
            elif 'video ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('video ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
                        
            elif "Cekig " in msg.text:
                    try:
                        instagram = msg.text.replace("Cekig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                        cl.sendImageWithURL(msg.to, profileIG)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendImageWithURL(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                        
            elif "idline: " in msg.text:
                msgg = msg.text.replace('idline: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text.lower() == 'time':
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bulan = blan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
                
            elif "google:" in msg.text:
                    a = msg.text.replace("google:","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "https://www.google.co.jp/search?q=" + b)                
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#==============================================================================#                             
            elif "Restart" in msg.text:
            	if msg.from_ in owner or admin or staff:
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        cl.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please waiting...")
                        restart_program()
                        pass                   
                
            elif msg.text.lower() == 'runtime':
               if msg.from_ in owner or admin or staff:
                cl.sendText(msg.to,"「Please wait..」\nType  :Loading...\nStatus : Loading...")
                eltime = time.time() - mulai
                van = "「 Runtime」\nType: Runtime\nStatus: вoт нaѕ вeen acтιve "+waktu(eltime)
                cl.sendText(msg.to,van)     

            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass               
#==============================================================================#
#==============================================================================#           
            elif "Ban @" in msg.text:
               if msg.from_ in owner or admin or staff:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
               if msg.from_ in owner or admin or staff:            	
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                cl.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:      
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.Istrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:        
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    cl.sendText(msg.to,_name + " Not In Blacklist")
                                    
            elif msg.text in ["Clear"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="════════List Blacklist════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n════════List Blacklist════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "════════List Blacklist════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n════════List Blacklist════════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#----------------------------------------------
            elif msg.text.lower() in dangerMessage:
                try:
                    if msg.toType == 2:
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                        cl.sendText(msg.from_,"Hati Hati Kalo Ngomong (｀・ω・´)")
                except:
                    pass
#========================================
            elif msg.text in ["creator"]:   
               if msg.toType == 2:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                jawab = ("Bot Creator by WIB","My Creator is Handsome","My Creator is Cool")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')     
#-----------------------[staff add section]------------------------
            elif "staff add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ag.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Staff add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ag.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "staff remove @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)                
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ag.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Staff remove @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ag.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"              
#==============================================================================#
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ag.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------   
            elif "Dj" in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                                    try:
                                        cl.kickoutFromGroup(msg.to,[target])
                                        cl.inviteIntoGroup(msg.to,[target])
                                        cl.cancelGroupInvitation(msg.to,[target])
                                    except:
                                        cl.sendText(msg.to, "ѕυcceѕѕ")
#-----------------------------------------------------------   
            elif ("Sentil " in msg.text):
                if msg.from_ in owner or admin or staff:            	
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")    
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Sp respon"]:
                if msg.from_ in owner or staff:

                    cl.sendText(msg.to, "=====「Speed Response」=====")
                    
                    cl.sendText(msg.to, "「Response Protect」")
                    start = time.time()
                    for i in range(3000):
                        1+1
                    elsp = time.time() - start
                    cl.sendText(msg.to,"「%sseconds」" % (elsp))     
                    print "[Command]Speed Response Protect"                    
 
                    cl.sendText(msg.to, "「Response Invite」")                    
                    start2 = time.time()
                    for i in range(3000):
                        1+1
                    elsp2 = time.time() - start2
                    cl.sendText(msg.to,"「%sseconds」" % (elsp2))     
                    print "[Command]Speed Response Invite"                  
                    
                    cl.sendText(msg.to, "「Response Cancel」")                    
                    start3 = time.time()
                    for i in range(3000):
                        1+1
                    elsp3 = time.time() - start3
                    cl.sendText(msg.to,"「%sseconds」" % (elsp3))       
                    print "[Command]Speed Response Cancel"                
                    
                    cl.sendText(msg.to, "「Response Kick」")                    
                    start4 = time.time()
                    for i in range(3000):
                        1+1
                    elsp4 = time.time() - start4
                    cl.sendText(msg.to,"「%sseconds」" % (elsp4))       
                    print "[Command]Speed Response Kick"        
                    
                    cl.sendText(msg.to, "「Response Qr」")                    
                    start5 = time.time()
                    for i in range(3000):
                        1+1
                    elsp5 = time.time() - start5
                    cl.sendText(msg.to,"「%sseconds」" % (elsp5))    
                    print "[Command]Speed Response Qr"       

                    cl.sendText(msg.to, "=====「Response Done! 」=====")
                    print "[Command]Speed all executed"
                else:
                    cl.sendText(msg.to,"Command Speed Done!")                   
     #-------------------------------------------------
            elif "youtube:" in msg.text.lower():
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                           #cl.sendVideoWithURL(msg.to, song[4])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))  
#----------------------NUKE----------------------------------
            elif "Nuke" in msg.text:
                if msg.from_ in admin:
                    print "Nuke ok"
                    _name = msg.text.replace("Nuke","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ag.getGroup(msg.to)                    
                    start = time.time()
                    ki.sendText(msg.to, "Nuke Speed")
                    elapsed_time = time.time() - start
                    ag.sendText(msg.to, "%sseconds" % (elapsed_time))
                    cl.sendText(msg.to, "Nuke Start")
                    ki.sendText(msg.to, "Nuke Proses")
                    ag.sendText(msg.to,"􀜁􀇔􏿿 See You Bitch!")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,ag]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Nuke Finish")
                                ag.sendText(msg,to,"Nuke Succes")                       
#==============================================#

            elif 'talkban ' in msg.text.lower():
                spl = msg.text.lower().replace('talkban ','')
                if spl == 'on':
                    if wait['talkban'] == True:
                        msgs="Talkban already Not For chat"
                    else:
                        msgs="Talkban set to Not For chat"
                        wait['talkban']=True
                    cl.sendText(msg.to, msgs)
                elif spl == 'off':
                    if wait['talkban'] == False:
                        msgs="Talkban already Allow For chat"
                    else:
                        msgs="Talkban set to Allow For chat"
                        wait['talkban']=False
                    cl.sendText(msg.to, msgs)
#-----------------------------------------------
            elif "Takol" in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           wait["talkblacklist"][target] = True
                           group = cl.getContact(target)
                           cl.sendText(msg.to,group.displayName + " Succes Add to Talkban")
                       except:
                           cl.sendText(msg.to,"Error")
#---------------------------------------------------
            elif "Takel" in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           del wait["talkblacklist"][target]
                           group = cl.getContact(target)
                           cl.sendText(msg.to,group.displayName + " Delete From Talkban")
                       except:
                           cl.sendText(msg.to,group.displayName + " Not In Talkban")
#-----------------------------------------------
            elif msg.text in ["Talklist"]:
                displayfreand = ki.getContacts(wait["talkblacklist"])
                cl.sendText(msg.to, "Please wait...")
                num=1
                msgs="「User Talkban List」"
                for ids in displayfreand:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「Total %i Talkban List」 " % len(wait["talkblacklist"])
                cl.sendText(msg.to, msgs)
#-------------------------------------------------
            if wait["talkban"] == True:
             if msg.from_ in wait["talkblacklist"]:
                try:
                    cl.sendText(msg.to,cl.getContact(msg.from_).displayName + " Ngomong wae kentod")
                    cl.kickoutFromGroup(msg.to,[msg.from_])
                except:
                    try:
                        cl.sendText(msg.to,cl.getContact(msg.from_) .displayName + " ")
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        cl.sendText(msg.to,cl.getContact(msg.from_).displayName + " ")
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                        cl.kickoutFromGroup(msg.to,[msg.from_])     
#-----------------------------------------------
        if op.type == 17:
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
	        if wait["protect"] == True:
		    if wait["blacklist"][op.param2] == True:
		       try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    ki.updateGroup(G)
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		       except:
			    pass
			    try:
			        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			        G = random.choice(KAC).getGroup(op.param1)
			        G.preventJoinByTicket = True
			        random.choice(KAC).updateGroup(G)
			        random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			    except:
			        pass
		    elif op.param2 not in admin + Bots:
		        random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	        else:
		    pass      
		
        if op.type == 19:
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
		    elif wait["protect"] == True:
		        wait ["blacklist"][op.param2] = True
		        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		    else:
		        cl.sendText(op.param1,"")
	        else:
		        cl.sendText(op.param1,"")

        if op.type == 11:
           if op.param2 not in Bots:
              G = cl.getGroup(op.param1)
              if G.preventJoinByTicket == False:
                 Ticket = cl.reissueGroupTicket(op.param1)
                 ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                 ki.kickoutFromGroup(op.param1,[op.param2])
                 ki.leaveGroup(op.param1)
              else:
                 G.preventJoinByTicket = False
                 cl.updateGroup(G)
                 Ticket = cl.reissueGroupTicket(op.param1)
                 ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                 ki.kickoutFromGroup(op.param1,[op.param2])
                 ki.leaveGroup(op.param1)
                 G.preventJoinByTicket = True
                 cl.updateGroup(G)
                 cl.sendContact(op.param1,op.param2)

        if op.type == 11:
            if op.param2 not in Bots:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = True
              invsend = 0
              Ticket = cl.reissueGroupTicket(op.param1)
              ki.acceptGroupInvitationByTicket(op.param1, Ticket)
              time.sleep(0.01)
              ki.kickoutFromGroup(op.param1,[op.param2])
              ki.leaveGroup(op.param1)
              satpam.updateGroup(G)
              x = Message(to=op.param1, from_=None, text=None, contentType=13)
              x.contentMetadata={'mid':op.param2}
              ki.sendMessage(x)         

        if op.type == 13:
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
		    elif wait["inviteprotect"] == True:
		        wait ["blacklist"][op.param2] = True
		        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		    else:
		        cl.sendText(op.param1,"")
	        else:
		    cl.sendText(op.param1,"")
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
		    elif wait["inviteprotect"] == True:
		        wait ["blacklist"][op.param2] = True
		        cl.cancelGroupInvitation(op.param1,[op.param3])
		    else:
		        cl.sendText(op.param1,"")
	        else:
		        cl.sendText(op.param1,"")
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
		    elif wait["cancelprotect"] == True:
		        wait ["blacklist"][op.param2] = True
		        cl.cancelGroupInvitation(op.param1,[op.param3])
		    else:
		        cl.sendText(op.param1,"")
	        else:
		       cl.sendText(op.param1,"")
		
        if op.type == 11:
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
		    elif wait["linkprotect"] == True:
		        wait ["blacklist"][op.param2] = True
		        G = ki.getGroup(op.param1)
		        G.preventJoinByTicket = True
		        ki.updateGroup(G)
		        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		    else:
		        cl.sendText(op.param1,"")
	        else:
		        cl.sendText(op.param1,"")

        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               G = cl.getGroup(op.param1)
               h = cl.getContact(op.param2)
               cl.sendText(op.param1, "╔═════════════" + "\n║" + cl.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Datang Di Indomaret Selamat Berbelanja 😊 \n╚═════════════")
               cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1, "╔═════════════" + "\n║" + cl.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Jalan Kakak Terima Kasih Telah Berbelanja Di Indomaret 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            cl.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    cl.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)   

        if op.type == 19:
            if op.param2 not in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass            
                
        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("·",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                                           
#---------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like"
#---------------------------------------------------------------
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
