# -*- coding: utf-8 -*-
#Vipro_Bot
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
from time import sleep
from datetime import datetime
from os.path import join,dirname
from io import BytesIO
from multiprocessing import Queue
from urllib import urlopen, urlretrieve, urlencode
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile,shutil,subprocess
import json,sys,atexit,datetime,base64,hmac
import getopt
import unicodedata
import shlex
import signal
import traceback
import os

ts = LINETCR.LINE()
ts.login(token='EtB3rGfhPeUNzzbmsc71.zo0JzCuk2kQRySUtQ4hjCq.HUqf7I+amXgYtizInmIO4cMi6alYV6LgaFTVDkmI9ew=')
ts.loginResult()
print "Trisan"

cl = LINETCR.LINE()
#cl.login()
cl.login(token='EtpIVY4rimbdpBqdvhd7.szOnB/55dwLUlMmlaLEXXW.rIF7bX+ij4wphDs4x05v1gDHvFZCetgTBYG5EPT/oD4=')
cl.loginResult()
print "Cl-Login Success\n"
ki = LINETCR.LINE()
#ki.login(qr=True)
ki.login(token='Et0u9i7zije4n6FJ21e0.b8Fj7vmq9zZ3sLz9FZk34a.gsapKvM1EFuuDSuwpvbkNxapU2D1PjC19U7v1dhep28=')
ki.loginResult()
print "Ki-Login Success\n"
kk = LINETCR.LINE()
kk.login(token='EtRq9k9xA5I3ZB45jQV5.PIeuqmNaypFJgMa6WfY4nq.40UmLi54b3Xu2VhqaK+X+2cov9tRXsB8opDB/OM5pkI=')
kk.loginResult()
print "Kk-Login Success\n"
kc = LINETCR.LINE()
kc.login(token='EtLZCrXelgk6Bwuhuh4f.F+uO1UpBrBXbmqKjbMEGJW.M6c2ud8wruyOCxgGOSiR3g1DYnLvprFKIbDRi4T5ojQ=')
kc.loginResult()
print "Kc-Login Success\n"
kr = LINETCR.LINE()
#kr.login(qr=True)
kr.login(token='Etkje3qQpelPaYYxICu6.v8+cdchVDwdlqGHtE2CPTG.fyVBDB50MU2ca/tZ1Y6k2gSVnDKTIHtwaxaCvRXlvOE=')
kr.loginResult()
print "Kr-Login Success\n"
vipro = LINETCR.LINE() #(isi dengan akun utama fungsinya biar akun utama di kick langsung di invite bot)
#vipro.login(qr=True)
vipro.login(token='EtpIVY4rimbdpBqdvhd7.szOnB/55dwLUlMmlaLEXXW.rIF7bX+ij4wphDs4x05v1gDHvFZCetgTBYG5EPT/oD4=')
vipro.loginResult()
print "Vipro-Login Success\n"
km = LINETCR.LINE() #(bot ini di luar grup fungsinya jadi algojo kaya kicker siri)
#km.login(qr=True)
km.login(token='EtV8yV2k2sowCdXGcx3c.L3LRW8OQKHdtzMetz1ChFa.FkvETGX6c7bYy6iQ7zck0PJS3LBzZQPhArrgTphBuBQ=')
km.loginResult()

km2 = LINETCR.LINE()
km2.login(token='Etd1WUlFBf3fYfXBRiPa.pWQ+JY2qAlrsqSsLyf/n2G.w3LfUqPa1iIewE/xdHzX9Hpjpa3ttNfNpWUBjASUSv8=')
km2.loginResult()

km3 = LINETCR.LINE()
km3.login(token='EtF6RNEcY3RWZ7AysYR2.7TBaF/bX8c45GigifN+BuG.hiGZ59ChZAUUkVfxYxzDEeoo2kv6sWZ7nhmVMbIxynw=')
km3.loginResult()

km4 = LINETCR.LINE()
km4.login(token='EtcybeWbzUZes3VjKfF4.RfmT/6ttsVBIQKDq7odxza.IM0WLWCymnulMUr/sODewzrcMOtpEYDmqvRq2zjaVIc=')
km4.loginResult()

km5 = LINETCR.LINE()
km5.login(token='EtClq117Is4yCrMUZv25.p3X+duHCDBsTsBZaOBCBHq.e4NmOxIdYq5mYy4nnDY9eUAffOF4RetzAtqHrCYQcUE=')
km5.loginResult()
print "\n\n=====[Sukses All Login]====="
reload(sys)
sys.setdefaultencoding('utf-8')
mulai = time.time()
album = None
image_path = 'tmp/tmp.jpg'

selfMessage ="""
╔═════════════════════════
║     ☆☞ S E L F ☜☆
╠═════════════════════════
➣〘Hi〙
➣〘Me〙
➣〘Mid @〙
➣〘SearchID: (ID LINE)〙
➣〘Checkdate (DD/MM/YY)〙
➣〘Kalender〙
➣〘Steal contact〙
➣〘Pp @〙
➣〘Cover @〙
➣〘Auto like〙
➣〘Scbc Text〙
➣〘Cbc Text〙
➣〘Gbc Text〙
➣〘Bio @〙
➣〘Info @〙
➣〘Name @〙
➣〘Profile @〙
➣〘Contact @〙
➣〘Getvid @〙
➣〘Friendlist〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""
botMessage ="""
╔═════════════════════════
║         ☆☞ B O T ☜☆
╠═════════════════════════
➣〘@bye (Usir Bot Utama)〙
➣〘Bye bot (Usir Semua Bot)〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""

mediaMessage ="""
╔═════════════════════════
║        ☆☞ M E D I A ☜☆
╠═════════════════════════
➣〘Gift〙
➣〘Giftbycontact〙
➣〘Google (Text)〙
➣〘Playstore NamaApp〙
➣〘Fancytext Text〙
➣〘Apakah Text (Kerang Ajaib)〙
➣〘Kapan Text (Kerang Ajaib)〙
➣〘Hari Text (Kerang Ajaib)〙
➣〘Berapa Text (Kerang Ajaib)〙
➣〘Berapakah Text〙
➣〘Youtube Judul Video〙
➣〘Youtubevideo Judul Video〙
➣〘Youtubesearch Judul Video〙
➣〘Image NamaGambar〙
➣〘Say Text〙
➣〘Say-en Text〙
➣〘Say-jp Text〙
➣〘Tr-id Text (Translate En Ke ID〙
➣〘Tr-en Text (Translate ID Ke En〙
➣〘Tr-th Text (Translate ID Ke Th〙
➣〘Id@en Text (Translate ID Ke En〙
➣〘Id@th Text (Translate ID Ke TH〙
➣〘En@id Text (Translate En Ke ID〙
NEW
• Musik text
• Xvideos Text
• IG Username
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""
groupMessage ="""
╔═════════════════════════
║        ☆☞ G R O U P ☜☆
╠═════════════════════════
➣〘Welcome〙
➣〘Say:welcome〙
➣〘Invite creator〙
➣〘Gn: (NamaGroup)〙
➣〘Gcreator〙
➣〘Ginfo〙
➣〘Gurl〙
➣〘List group〙
➣〘Pict group: (NamaGroup)〙
➣〘Spam: (Text)〙
➣〘Kick: (Mid)〙
➣〘Invite: (Mid)〙
➣〘Invite〙
➣〘Memlist〙
➣〘Getgroup image〙
➣〘Urlgroup Image〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""
vip="uba553877e995e2bd476d1d78469dc8d2"
OA="uef0a3654b9795742b58cdb3621d22c53"
setMessage ="""
╔═════════════════════════
║           ☆☞ S E T ☜☆
╠═════════════════════════
➣〘Notif on/off〙
➣〘Url on/off〙
➣〘Alwaysread on/off〙
➣〘Sider on/off〙
➣〘Contact on/off〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""
creatorMessage ="""
╔═════════════════════════
║      ☆☞ C R E A T O R ☜☆
╠═════════════════════════
➣〘Admin add @〙
➣〘Admin remove @〙
➣〘Crash〙
➣〘Bc: (Text)〙
➣〘Nk: @〙
➣〘Ulti @〙
➣〘Join group: (NamaGroup〙
➣〘Leave group: (NamaGroup〙
➣〘Leave all group〙
➣〘Bot restart〙
➣〘Turn off〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""

adminMessage ="""
╔═════════════════════════
║         ☆☞ A D M I N ☜☆
╠═════════════════════════
➣〘Admin list〙
➣〘Ban〙
➣〘Unban〙
➣〘Ban @〙
➣〘Unban @〙
➣〘Ban list〙
➣〘Set member: (Jumlah)〙
➣〘Ban group: (NamaGroup〙
➣〘Del ban: (NamaGroup〙
➣〘List ban〙
➣〘Kill ban〙
➣〘Glist〙
➣〘Glistmid〙
➣〘Details group: (Gid)〙
➣〘Cancel invite: (Gid)〙
➣〘Invitemeto: (Gid))
➣〘Removechat〙
➣〘Join on/off〙
➣〘Joincancel on/off〙
➣〘Respon on/off〙
➣〘Responkick on/off〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""

helpMessage ="""
╔••••••••PUBLIC••••••••••
║      |sᴇʟғᴛʙᴏᴛ|
╠════════════════════════
➣〘Help protect〙
➣〘Help self〙
➣〘Help bot〙
➣〘Help group〙
➣〘Help set〙
➣〘Help media〙
➣〘Help admin〙
➣〘Help creator〙
➣〘Owner〙
➣〘Status〙
╠|||||||||||||||||||||||||
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""

protectMessage ="""
╔═════════════════════════
║       ☆☞ P R O T E C T ☜☆
╠═════════════════════════
➣〘Allprotect on/off〙
➣〘Autocancel on/off〙
➣〘Qr on/off〙
➣〘Autokick on/off〙
➣〘Ghost on/off〙
➣〘Invitepro on/off〙
╠═════════════════════════
║ https://line.me/R/ti/p/%40nda9374k
╚═════════════════════════
"""
KAC=[ts,cl,ki,kc,kk,kr,km,km2,km3,km4,km5]
ts1 = ts.getProfile().mid
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kr.getProfile().mid
Emid = km.getProfile().mid
Fmid = vipro.getProfile().mid
Gmid = km2.getProfile().mid
Hmid = km3.getProfile().mid
Imid = km4.getProfile().mid
Pmid = km5.getProfile().mid
Bots=[ts1,mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Pmid,'u499a0d6fee790d696e2e630b0257b1c7','u07c7c9ed5310f59cf74a567d7f32b7e0','u3f7c7f0d485c75b4ad49bcc0a1b71b85','u7ff528d6e3db45bc413109090667a08f','u57cfc20c21ef7560cb4208537b6729b6','u97796bc3ca2a9210d36661136757077c','u3f0abf8f2d9068b45242c4a5605f8dda','ueed6c07fe071f02e39808188167fdb52','uac532dfba4d34af6e2aa4750ece0d764','u64ed2365c50ad8aaab62cb93ab81c971']
Creator=["uba553877e995e2bd476d1d78469dc8d2"]
admin=["uba553877e995e2bd476d1d78469dc8d2"]
wait = {
    "LeaveRoom":True,
    "AutoJoin":False,
    "AutoJoin1":True,
    "AutoJoinCancel":True,
    "memberscancel":10,
    "Members":1,
    "Members1":1,
    "AutoCancel":{},
    "AutoCancelon":False,  
    "joinkick":False,
    "AutoKick":{},
    "AutoKickon":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':True,
    'Leave':{},    
    'detectMention':False,
    'kickMention':False,      
    'timeline':False,
    "Timeline":False,
    "comment":"Auto Like ©By : TSpublic\nContact Me : https://line.me/R/ti/p/%40nda9374k",
    "comment2":"Auto Like ©By : TSpublic\nContact Me : 👉 https://line.me/R/ti/p/%40nda9374k",
    "commentOn":False,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^) Undang Ke group iya",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":{},
    "Qron":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":True,
    "inviteprotect":True,   
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{},
    "userAgent": [
        "Mozzila/5.0 (X11: U:Linux i586: de: rv:5.0) Gecko/20100101 firefox/5.0"
        ],
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
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
{
    "type": "location",
    "title": "my location",
    "address": "〒150-0002 東京都渋谷区渋谷２丁目２１−１",
    "latitude": 35.65910807942215,
    "longitude": 139.70372892916203
}
setTime = {}
setTime = wait2['setTime']
mulai = time.time()
counter = 0

dns = {
    'google_a': '2001:4860:4860::8888',
    'google_b': '2001:4860:4860::8844',
    'he_net': '2001:470:20::2',
    'lax_he_net': '2001:470:0:9d::2'
}

config = {
    'dns': dns['google_b'],
    'infile': '',
    'outfile': '',
    'querytype': 'aaaa',
    'cname': False,
    'threadnum': 10
}
res = {
    'num':{},
    'us':{},
    'au':{},
}

fastbinary = None
mulai = time.time()
contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

hosts = []
done_num = 0
thread_lock = threading.Lock()
running = True

def crackClients(clients, usersMac, SSID, passphraseQ):
    clientHandshakes = []
    for client in clients:
        handshake = []
        for message in clients[client]:
            if message['message'] == 1:
                handshake = [message]
            elif len(handshake) == 1:
                handshake.append(message)
                clientHandshakes.append(handshake)
                break
            else:
                handshake = []
    for clientHandshake in clientHandshakes:
        if clientHandshake[0]['AP'] == usersMac:
            cracked = crack(SSID, clientHandshake[0]['client'], clientHandshake[0]['AP'], clientHandshake[0]['Anonce'], clientHandshake[1]['Snonce'], clientHandshake[1]['mic'], clientHandshake[1]['data'], passphraseQ)
            if cracked != False:
                return cracked
    return False

if __name__ == "__main__":
    from sys import argv, exit
    import getopt
    try:                  
        opts, args = getopt.getopt(argv[1:], "r:m:s:d:")
    except getopt.GetoptError:          
        print "bad args"
        exit(2)
    for opt, arg in opts:
        if opt == '-r':
            readFile = arg
        if opt == '-m':
            usersMac = arg.replace(":", "").decode('hex')
        if opt == '-s':
            SSID = arg
        if opt == '-d':
            try:
                f = open(arg, 'r')
                passphraseQ = Queue()
                for passphrase in f.read().split('\n'):
                    passphraseQ.put(passphrase)
                f.close()
            except IOError:
                print "Error reading dictionary"
                exit(2)

def speedReg(self, log):
    log['CMD'] = log['CMD'] - (self.motorType()[1])
    X = log['CMD']
    Y = log['Knots']
    X = np.array(X).reshape(-1, 1)
    Y = np.array(Y).reshape(-1, 1)
    reg = linear_model.LinearRegression()
    reg.fit(Y, X)
    self.rValue = round(reg.score(Y, X), 3)
    self.speedSlope = round(reg.coef_[0], 1)
    self.speedIntercept = int(self.motorType()[1])
#================#
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def __init__(self, *args, **kwargs):
        source_address = kwargs.pop('source_address', None)
        context = kwargs.pop('context', None)
        timeout = kwargs.pop('timeout', 1)
        HTTPConnection.__init__(self, *args, **kwargs)
        self.source_address = source_address
        self._context = context
        self.timeout = timeout
        
def connect(self):
        """Connect to the host and port specified in __init__."""
        try:
            self.sock = socket.create_connection(
                (self.host, self.port),
                self.timeout,
                self.source_address
            )
        except (AttributeError, TypeError):
            self.sock = create_connection(
                (self.host, self.port),
                self.timeout,
                self.source_address
            )

def data(self):
        if not self._data:
            self.pre_allocate()
        return self._data

def dict(self):
        """Return dictionary of result data"""

        return {
            'download': self.download,
            'upload': self.upload,
            'ping': self.ping,
            'server': self.server,
            'timestamp': self.timestamp,
            'bytes_sent': self.bytes_sent,
            'bytes_received': self.bytes_received,
            'share': self._share,
            'client': self.client,
        }

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

def call(self, name, *params):
        """RPC IPC Call to a Go function, return results or raise error."""
        msg = {"id": next(self._id), "params": tuple(params), "method": name}
        data = bytes(json.dumps(msg, separators=(",", ":")), "utf-8")
        self.socket.sendall(data)

        while True:
            try:
                json_response = json.loads(self.socket.recv(8192))
                if not json_response:
                    break
            except Exception:
                sleep(0.1, msg)
            else:
                break
#========#
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.cl.sendMessage(0, msg)

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def RECEIVE_MESSAGE(op):
    try:
        msg = op.message
        if msg.toType == 0:
            cl.log("[%s]"%(msg._from)+msg.text)
        else:
            cl.log("[%s]"%(msg.to)+msg.text)
        if msg.contentType == 0:
            #Save message to dict
            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
    except Exception as e:
        print(e)

def NOTIFIED_DESTROY_MESSAGE(op):
    try:
        at = op.param1
        msg_id = op.param2
        if msg_id in msg_dict:
            if msg_dict[msg_id]["from"] not in bl:
                cl.sendMessage(at,"SentMessage cancelled.\n\n[Sender]\n %s\n[SentAt]\n %s\n[Detail]\n %s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])),msg_dict[msg_id]["text"]))
            del msg_dict[msg_id]
        else:
            cl.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
    except Exception as e:
        print(e)
#=====================#
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
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

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def cmd(string, commands):
    tex = [" ","Sp","Kuy","|","@"]
    for texX in tex:
        for command in command:
            if string ==texX + command:
                return True
    return False

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False    

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

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
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
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error            

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "◈ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error 

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
           sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
           if wait["autoAdd"] == True:
              cl.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                cl.sendText(op.param1,str(wait["message"]))

        if op.type == 55:
            try:
               group_id = op.param1
               user_id=op.param2
               subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
            except Exception as e:
             print e

        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nSini join chat. . .\n(-__-)   ")
                                    else:
                                        random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nSalam kenal iya. . .\nChat Napa hehe (-__-)   ")
                                else:
                                    random.choice(KAC).sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nHalalin ni   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      
        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)

        if op.type == 19: #Member Ke Kick
          if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in Creator:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        #------SEPERTI SIRI------#
        if op.type == 11:
            if op.param2 not in Bots:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                km.kickoutFromGroup(op.param1,[op.param2])
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                km.sendMetadata={'mid':op.param2}
                km.leaveGroup(op.param1)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                wait["blacklist"][op.param2] = True
                print "kicker"

        if op.type == 19:
            if op.param3 in Amid: #Akun Utama Ke Kick
                G = random.choice(KAC).getGroup(op.param1)
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.0)
                G.preventJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                ki.updateGroup(G)
                wait["blacklist"][op.param2] = True

        if op.type == 19:
          try:
            if op.param3 in mid: #Akun Utama Ke Kick
              G = cl.getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              vipro.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.0)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              ki.updateGroup(G)
              wait["blacklist"][op.param2] = True
          except:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            random.cboice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Creator:
		    kr.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Cmid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in mid:
		    kr.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Amid:
		    kr.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Bmid:
		    kr.acceptGroupInvitation(op.param1)
            if op.param3 in Gmid:
                if op.param2 in Cmid:
                    km2.acceptGroupInvitation(op.param1)
            if op.param3 in Hmid:
                if op.param2 in Amid:
                    km3.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Amid:
                    km4.acceptGroupInvitation(op.param1)
            if op.param3 in Pmid:
                if op.param2 in Gmid:
                    km5.acceptGroupInvitation(op.param1)
            if op.param3 in ts1:
                if op.param2 in Dmid:
                    ts.acceptGroupInvitation(op.param1)
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Maaf " + cl.getContact(op.param2).displayName + "\nMember Kurang Dari 20 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':vip}
                        cl.sendMessage(c)                        
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			Ti = cl.reissueGroupTicket(op.param1)
		        cl.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")

	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			kr.acceptGroupInvitationByTicket(op.param1,Ti)
			km2.acceptGroupInvitationByTicket(op.param1,Ti)
			km3.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"][op.param1] == True:
		    if op.param3 in admin:
			pass
		    else:
                        random.choice(KAC).cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			random.choice(KAC).cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass

        if op.type == 19:
		if wait["AutoKick"][op.param1] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass
		
                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True
                
                    X = km.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km.updateGroup(X)
                    Ti = km.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True    
                
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        vipro.kickoutFromGroup(op.param1,[op.param2])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True

                    X = vipro.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    vipro.updateGroup(X)
                    Ti = vipro.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        km2.kickoutFromGroup(op.param1,[op.param2])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True

                    X = km2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km2.updateGroup(X)
                    Ti = km2.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        km3.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True

                    X = km3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km3.updateGroup(X)
                    Ti = km3.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kr.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        km4.kickoutFromGroup(op.param1,[op.param2])
                        km2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True

                    X = km4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km4.updateGroup(X)
                    Ti = km4.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = km3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    km3.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if Pmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        km5.kickoutFromGroup(op.param1,[op.param2])
                        km3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
                            if op.param2 in Bots:
                                pass
                            else:
                                wait["blacklist"][op.param2] = True

                    X = km5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    km5.updateGroup(X)
                    Ti = km5.reissueGroupTicket(op.param1)
                    ts.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    km2.acceptGroupInvitationByTicket(op.param1,Ti)
                    km3.acceptGroupInvitationByTicket(op.param1,Ti)
                    km4.acceptGroupInvitationByTicket(op.param1,Ti)
                    km5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = km3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    km3.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
#=============#
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 11:
            if wait["Qr"][op.param1] == True:
                if op.param2 not in Bots:
                  if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).updateGroup(G)
            
            
        if op.type == 17:
          if wait["joinkick"] == True:
            if op.param2 in Bots:
                return
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            print "MEMBER JOIN KICK TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
              if op.param2 in Bots:
                return
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP"

        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in admin:
           if op.param2 in Bots:
               pass
          else:
            try:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              km.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.1)
              km.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              km.sendMessage(c)
              km.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(x)
              wait["blacklist"][op.param2] = True
            except:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              km.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.1)
              km.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              km.sendMessage(c)
              km.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(x)
              wait["blacklist"][op.param2] = True

        if op.type == 26:
            msg = op.message
            text = msg.text

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
#Deteksi URL Post for Py2
        if op.type == 26:
            msg = op.message
            text = msg.text

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break                                  
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break 
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Tag Mulu Lo Anjirr!","Dia Lagi Off", cName + " Kenapa Tag? Kangen?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  break                                  
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break   

            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            random.choice(KAC).sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            random.choice(KAC).sendText(msg.to,"Ditambahkan")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        random.choice(KAC).sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        random.choice(KAC).sendText(msg.to,"Tidak Ada Black List")

                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text is None:
                return

            elif msg.text in ["OA"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "udb6d0dd8ba9587582ec5bdd51b5e468c"}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"ADD OA KAMI IYA!!\tQoutes Prontal16+")

            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': vip}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"それは私の所有者です (^_^)")

            elif msg.text in ["Admin","admin"]:
                msg.contentType = 13
                admin1 = "uba553877e995e2bd476d1d78469dc8d2"
                admin2 = "uba553877e995e2bd476d1d78469dc8d2"
                admin3 = "uba553877e995e2bd476d1d78469dc8d2"
                msg.contentMetadata = {'mid': vip}
                random.choice(KAC).sendMessage(msg)
                #msg.contentMetadata = {'mid': admin1}
                #random.choice(KAC).sendMessage(msg)
                #msg.contentMetadata = {'mid': admin2}
                #random.choice(KAC).sendMessage(msg)
                #msg.contentMetadata = {'mid': admin3}
                #random.choice(KAC).sendMessage(msg)                
		random.choice(KAC).sendText(msg.to,"それは私たちの管理者です (^_^)")	
		
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"管理者の追加")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                cl.sendText(msg.to,"Command Denied.")
                cl.sendText(msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"管理者が削除しました")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                cl.sendText(msg.to,"Command Denied.")
                cl.sendText(msg.to,"Creator Permission Required.")
                
            elif msg.text in ["Admin list","admin list","List admin"]:
              if admin == []:
                  cl.sendText(msg.to,"The Admin List Is Empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════════════════\n║        ☆☞ ADMIN ☜☆\n╠═════════════════════════\n"
                  for mi_d in admin:
                      mc += "╠••> " +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc + "╚═════════════════════════")
                  print "[Command]Admin List executed"
                 
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"それは誰がこのグループを作りましたか")

            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    text = msg.text
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)
            
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

            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     groups = ki.getGroup(msg.to)                     
                     groups = kk.getGroup(msg.to)                     
                     groups = kc.getGroup(msg.to)                     
                     groups = kr.getGroup(msg.to)                     
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             random.choice(KAC).sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 ki.findAndAddContactsByMid(target)                                 
                                 kk.findAndAddContactsByMid(target)                                 
                                 kc.findAndAddContactsByMid(target)                                 
                                 kr.findAndAddContactsByMid(target)                                 
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
            elif msg.text in ["Key creator","help creator","Help creator"]:
                cl.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
                cl.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Help self"]:
                cl.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                cl.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                cl.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                cl.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                cl.sendText(msg.to,adminMessage)    
                
            elif msg.text in ["Key protect","help protect","Help protect"]:
                cl.sendText(msg.to,protectMessage)                 
                
            elif msg.text in ["Lg"]:
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Owner")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        random.choice(KAC).sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        random.choice(KAC).sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Vipro")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		gid = ki.getGroupIdsJoined()
		gid = kk.getGroupIdsJoined()
		gid = kc.getGroupIdsJoined()
		gid = kr.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
                            h = ki.getGroup(i).name
                            h = kk.getGroup(i).name
                            h = kc.getGroup(i).name
                            h = kr.getGroup(i).name
		            if h == ng:
		                random.choice(KAC).inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Khusus Owner")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            cl.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    kr.leaveGroup(i)
			    cl.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"Khusus Owner")
 
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!\n Silahkan Undang Kembali")
		        cl.leaveGroup(i)
			kk.leaveGroup(i)
			kc.leaveGroup(i)
			kr.leaveGroup(i)
			km.leaveGroup(i)
			km2.leaveGroup(i)
			km3.leaveGroup(i)
			km4.leaveGroup(i)
			km5.leaveGroup(i)
			vipro.lwaveGroup(i)
		    cl.sendText(msg.to,"Success Leave All Group")
		else:
		    cl.sendText(msg.to,"Khusus Owner")
		   
            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"すでにURLがオンです")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"URLはオフです")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")

            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"すでに自動参加")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"自動参加はすでに無効になっています")
		else:
		    cl.sendText(msg.to,"Khusus Admin")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"自動参加キャンセルはオンです")
		else:
		    cl.sendText(msg.to,"Khusus Owner")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"自動参加キャンセルはすでに無効になっています")
		else:
		    cl.sendText(msg.to,"Khusus Owner")		    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus Admin")	
		    
		    
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    cl.sendText(msg.to,"Khusus Admin")			  
 
            elif msg.text in ["Leave on"]:
		if msg.from_ in admin:
                    wait["Leave"] = True
                    cl.sendText(msg.to,"既にオンのままにする")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Leave off"]:
                if msg.from_ in admin:
                    wait["Leave"] = False
                    cl.sendText(msg.to,"既にオンのままにする")
                else:
                    cl.sendText(msg.to,"Khusus Admin")
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"][msg.to] = True
                wait["AutoCancelon"] = True
                cl.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    cl.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"][msg.to] = False
                wait["AutoCancelon"] = False
                cl.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    cl.sendText(msg.to,"Khusus Admin")	

	    elif msg.text in ["Joinkick on"]:
	     if msg.from_ in admin:	        
                wait["joinkick"] = True
                wait["Sambutan"] = False
                cl.sendText(msg.to,"参加キックはオンです")
	     else:
		    cl.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Joinkick off"]:
	     if msg.from_ in admin:	        
                wait["joinkick"] = False
                cl.sendText(msg.to,"既にキックに参加する")
	     else:
		    cl.sendText(msg.to,"Khusus Admin")	

		    
	    elif msg.text in ["Invitepro on","Inviteprotect on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                cl.sendText(msg.to,"招待保護がオンです")
	     else:
		    cl.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Invitepro off","Inviteprotect off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                cl.sendText(msg.to,"招待保護はオフです")
	     else:
		    cl.sendText(msg.to,"Khusus Admin")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"][msg.to] = True
	        wait["Qron"] = True
	    	cl.sendText(msg.to,"QR Protectがオンです")
		print wait["Qr"]	    	
	     else:
		    cl.sendText(msg.to,"Khusus Admin")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"][msg.to] = False
	    	wait["Qron"] = False
	    	cl.sendText(msg.to,"Qr Protectがオフです")
		print wait["Qr"]	    	
	     else:
		    cl.sendText(msg.to,"Khusus Admin")	    	
                        
	    elif msg.text in ["Autokick on"]:
	     if msg.from_ in admin:	        
                wait["AutoKick"][msg.to] = True
                wait["AutoKickon"] = True
                cl.sendText(msg.to,"自動キックがオンです")
		print wait["AutoKick"]
	     else:
		    cl.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Autokick off"]:
	     if msg.from_ in admin:	        
                wait["AutoKick"][msg.to] = False
                wait["AutoKickon"] = False
                cl.sendText(msg.to,"オートキックはすでに無効になっています")
		print wait["AutoKick"]
	     else:
		    cl.sendText(msg.to,"Khusus Admin")	


	    elif msg.text in ["Ghost on"]:
	     if msg.from_ in admin:	        
                wait["Ghost"] = True
                cl.sendText(msg.to,"ゴーストはオンです")
	     else:
		    cl.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Ghost off"]:
	     if msg.from_ in admin:	        
                wait["Ghost"] = False
                cl.sendText(msg.to,"ゴーストはすでに無効になっています")
	     else:
		    cl.sendText(msg.to,"Khusus Admin")	     

            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"][msg.to] = True
                    wait["AutoCancelon"] = True
                    wait["inviteprotect"] = True 
                    wait["joinkick"] = True 
                    wait["AutoKick"][msg.to] = True
                    wait["AutoKickon"] = True
                    wait["Qr"][msg.to] = True
                    wait["Qron"] = True
                    wait["Ghost"] = True     
                    cl.sendText(msg.to,"すべての保護はすべてオンです")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["Qr"]
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"][msg.to] = False
                    wait["AutoCancelon"] = False
                    wait["inviteprotect"] = False  
                    wait["joinkick"] = False
                    wait["AutoKick"][msg.to] = False
                    wait["AutoKickon"] = False
                    wait["Qr"][msg.to] = False
                    wait["Qron"] = False
                    wait["Ghost"] = False 
                    cl.sendText(msg.to,"すべての保護はすでに無効になっています")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["Qr"]
#		else:                    
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"連絡先はオンです")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"常に読み取りオンです")
                
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"常に読み取りオンです")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"常に読み取りは既に無効になっています")                

            elif msg.text in ["Notif on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"挨拶でアンロックヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"既にオンヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"グリーティングオンディスエーブル(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"既にオフになっています(p′︵‵。)")
                        
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"レディ・オン・チェック・サイダー")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "サイダーをオフにする")
                else:
                    cl.sendText(msg.to, "No Set")                         

            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠➩✔️ Notif : On\n"
		else:md+="╠➩× Sambutan : Off\n"
		if wait["joinkick"] == True: md+="╠➩✔️ Join Kick : On\n"
		else:md+="╠➩× Join Kick : Off\n"		
		if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                else: md +="╠➩× Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                else: md +="╠➩× Auto Join Cancel : Off\n"                
		if wait["Leave"] == True: md+="╠➩✔️ Leave : On\n"
                else: md +="╠➩× Leave : Off\n"                
		if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
		else: md+="╠➩× Info Contact : Off\n"
                if wait["AutoCancelon"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                else: md+= "╠➩× Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                else: md+= "╠➩× Invite Protect : Off\n"                
		if wait["Qron"] == True: md+="╠➩✔️ Qr Protect : On\n"
		else:md+="╠➩× Qr Protect : Off\n"
		if wait["AutoKickon"] == True: md+="╠➩✔️ Auto Kick : On\n"
		else:md+="╠➩× Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="╠➩✔️ Ghost : On\n"
		else:md+="╠➩× Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="╠➩✔️ Always Read : On\n"
		else:md+="╠➩× Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠➩✔️ Auto Respon : On\n"
		else:md+="╠➩× Auto Respon : Off\n"		
		if wait["kickMention"] == True: md+="╠➩✔️ Auto Respon Kick : On\n"
		else:md+="╠➩× Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠➩✔️ Auto Sider : On\n"
		else:md+="╠➩× Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠➩✔️ Simisimi : On\n"
		else:md+="╠➩× Simisimi: Off\n"		
                cl.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")

            elif msg.text in ["Gift","gift"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    cl.sendMessage(msg)

            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                kr.sendMessage(msg)

            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
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
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '3578933'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Tagall","Tag all"]:
                if msg.from_ in admin:
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
                      
            elif msg.text in ["Sepi"]:
                if msg.from_ in Creator:
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Selingkuhan"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)          
#-----CCTV----------
            elif msg.text in ["Lurking","lurking"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "========HAI KANG NYIMAK========%s\n\nKamu tercyduk muehehehe👻👻👻👻\n[%s]" %(wait2['readMember'][msg.to],setTime[msg.to]))
                        print("ReadPoint Set...")
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        cl.sendText(msg.to, "Kami telah memperbarui poin baca secara otomatis.")
                    else:
#                        cl.sendText(msg.to, "Kami telah memperbarui poin baca secara otomatis.")
                        print("ReadPoint Set...")
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
#-----------------------------------------------
            elif ".kickall" in msg.text:
                    try:
                        km2.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass

            elif "!kickall" in msg.text:
                    try:
                        km3.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass

            elif "Fuck " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki.kickoutFromGroup(msg.to,[target])
                   except:
                      pass

	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ki.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["memberscancel"] = int(jml)
		    cl.sendText(msg.to, "メンバーの最小数が設定されています : "+jml)

	    elif "Add all" in msg.text:
                if msg.from_ in admin:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"成功すべてを追加")

            elif text.lower() == 'Unsend':
                if msg.from_ in admin:
                    cl.unsendMessage(msg_id)

            elif msg.text in ["Invite"]:
                wait["invite"] = True
                cl.sendText(msg.to,"連絡先を送信")
                
            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                cl.sendText(msg.to,"Share Post Kamu Yang Mau Di Like!")                

            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                cl.sendText(msg.to,"Send Contact")

            elif ("Gn: " in msg.text):
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn: ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		kicker = [ki,kk,kc,kr,km,vipro,km2,km3,km4,km5]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                ki.findAndAddContactsByMid(midd)
                kk.findAndAddContactsByMid(midd)
                kc.findAndAddContactsByMid(midd)
                kr.findAndAddContactsByMid(midd)
                km.findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "uba553877e995e2bd476d1d78469dc8d2"
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"[BROADCAST]\n\n"+bc+"\n\nContact Me : line.me/ti/p/~mtrisan")
		    cl.sendText(msg.to,"Success BC BosQ")
		else:
		    cl.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["!Kuy","Siri:join"]:
		if msg.from_ in admin:
		    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    km2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    km3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    km4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    km5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")

            elif msg.text in ["Ghost join"]:
		if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    km.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    km.updateGroup(G)
		else:
		    cl.sendText(msg.to,"Sape lu!")		    

            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=200)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["!byeall"]:
              if wait["Leave"] == True:		    
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                    kr.leaveGroup(msg.to)
                    km2.leaveGroup(msg.to)
                    km3.leaveGroup(msg.to)
                    km4.leaveGroup(msg.to)
                    km5.leaveGroup(msg.to)
                    vipro.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"レヴェンヤまだまだ")

            elif msg.text in ["@bye","@Bye"]:
              if wait["Leave"] == True:	
		    cl.leaveGroup(msg.to)
		    wait["Leave"] = False
              else:
		          cl.sendText(msg.to,"Bilang Dulu Sama Admin Ku")		    
		    

            elif msg.text in ["!on"]:
		cl.sendText(msg.to,"?????????????!!")
                ki.sendText(msg.to,"On  \(ˆ▿ˆ)/")
                kk.sendText(msg.to,"On  \(ˆ▿ˆ)/")
                kc.sendText(msg.to,"On  \(ˆ▿ˆ)/")
                kr.sendText(msg.to,"On  \(ˆ▿ˆ)/")

            elif msg.text in ["Sp test"]:
                start = time.time()
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "Kecepatan mengirim pesan: %sms" % (elapsed_time))

            elif msg.text in ["Sp","sp"]:
                sp = int(round(time.time() *1000))
                cl.sendText(msg.to,"my speed : %sms" % (sp - op.createdTime))

            elif "Nk: " in msg.text:
		if msg.from_ in Creator:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                kr.kickoutFromGroup(msg.to,[target])
                                kr.leaveGroup(msg.to)
                                ki.sendText(msg.to,"Succes BosQ")
                                kk.sendText(msg.to,"Pakyu~")
			    else:
			        cl.sendText(msg.to,"Admin Detected")
		else:
		    cl.sendText(msg.to,"Lu sape!")
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes BosQ")
                                except:
                                    ki.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"===[Blacklist User]===\n"+mc)

            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kk.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes BosQ")
                            except:
                                ki.sendText(msg.to,"Succes BosQ")

            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    cl.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kk.sendText(msg.to,"Fuck You")
                            kc.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        ki.sendText(msg.to,"Sampai jumpaa~")
                        kc.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[kk,kc]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    

            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "Vipro,'"}
                cl.sendMessage(msg)

            elif "Copy @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Copy @","")
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
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e

            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Done (^_^)")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif "Musik " in msg.text:
                #if msg.from_ in admin:
                            try:
                                judul = msg.text.replace("Musik ","")
                                params = {"judul": judul}
                                r = requests.get("http://farzain.xyz/api/joox.php?id="+urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendText(msg.to, str(hasil))
                                cl.sendText(msg.to, "Downloading...")
                                cl.sendText(msg.to, "「 Result MP3 」")
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                cl.sendText(msg.to, "Success Download...")
                            except Exception as error:
                                pass

            elif 'Lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('Lirik ','')
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

            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"

            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hFR-rB8h-GX0QCzWZMOZmKixOFxBnJR81aG9eSTUNREhtOVYqJWgFSWYDR05vOwp7K2sCGTELRUVo"]
                                pilih = random.choice(link)
                                cl.sendImageWithURL(msg.to,pilih)

            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    random.choice(KAC).sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = cl.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      cl.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = cl.getAllContactIds()
                  for manusia in orang:
                    cl.sendText(manusia, (broadcasttxt))

            elif 'Ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("Ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    Vipro = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, Vipro)
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))

            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	

            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        cl.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        cl.sendText(msg.to, "Could not find it")                    

            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
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

            elif "Say:welcome" in msg.text:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace("Say:welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-------------------#
            #elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    #beb = "Hi Sayang 😘 " +cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    #cl.sendText(msg.to,beb)
            elif "Playstore " in msg.text.lower():
                tob = msg.text.lower().replace("Playstore ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Tuh Linknya Kak (^_^)")

            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass

            elif "bio " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        kc.updateProfile(profile)
                        kr.updateProfile(profile)
                        km.updateProfile(profile)
                        vipro.updateProfile(profile)
                        km2.updateProfile(profile)
                        km3.updateProfile(profile)
                        cl.sendText(msg.to,"All Done")

            elif "/vipro" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/vipro","Vipro")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")

            elif "Sorry " in msg.text:
              if msg.from_ in Creator:
                ulti0 = msg.text.replace("Sorry ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        km.kickoutFromGroup(msg.to,[target])
                                        km.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        km.sendText(msg.t,"Ter ELIMINASI....")
                                        km.sendText(msg.to,"Disuruh Boskuh....!!!")
                                        km.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)

            elif msg.text.lower() in ["Mymid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)

            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin","Pikir Aja Sendiri","Meneketehe"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "Berapa " in msg.text:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Berapakah " in msg.text:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                cl.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                cl.sendText(msg.to,"Simisimi Di Nonaktifkan")

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
 
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'

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
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)

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
                cl.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)

            elif msg.text in [".me"]:
                cl.sendText(msg.to,"mek")

            elif msg.text in ["Spam"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Aku belum mandi")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Tak tun tuang")
                kc.sendText(msg.to,"Tapi masih cantik juga")
                kr.sendText(msg.to,"Tak tun tuang")
                cl.sendText(msg.to,"Tak tun tuang")
                ki.sendText(msg.to,"apalagi kalau sudah mandi")
                kk.sendText(msg.to,"Tak tun tuang")
                kc.sendText(msg.to,"Pasti cantik sekali")
                kr.sendText(msg.to,"yiha")
                cl.sendText(msg.to,"Kalau orang lain melihatku")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Badak aku taba bana")
                kc.sendText(msg.to,"Tak tun tuang")
                kr.sendText(msg.to,"Tak tuntuang")
                cl.sendText(msg.to,"Tapi kalau langsuang diidu")
                ki.sendText(msg.to,"Tak tun tuang")
                kk.sendText(msg.to,"Atagfirullah baunya")
                kc.sendText(msg.to,"Males lanjutin ah")
                kr.sendText(msg.to,"Sepi bat")
                cl.sendText(msg.to,"Iya sepi udah udah")
                ki.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                kk.sendText(msg.to,"Nah")
                kc.sendText(msg.to,"Mending gua makan dulu")
                kr.sendText(msg.to,"Siyap")
                cl.sendText(msg.to,"Okeh")
                ki.sendText(msg.to,"Katanya owner kita Jomblo ya")
                kk.sendText(msg.to,"Iya emang")
                kc.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                kr.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
 
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

            elif "Group image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)

            elif "Profile" in msg.text:
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

            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))

            elif "Bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)

            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin:
                     eltime = time.time() - mulai
                     van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                     cl.sendText(msg.to,van)

            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")

            elif msg.text in ["Kalender","Time","Waktu"]:
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
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)

            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)

            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)

            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        kr.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")

            elif "Xvideos " in msg.text:
                    a = msg.text.replace("Xvideos ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Searching ....\n" "Type:Search Xvideos\nStatus: Processing")
                    cl.sendText(msg.to, "{ Xvideos search page }\n\nTitle: "+b+"\nSource : Xvideos\nhttp://xvideos.com/?k=" +b)

            elif "IG " in msg.text:
                    a = msg.text.replace("IG ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Searching.....\n" "Type: Search Instagram")
                    cl.sendText(msg.to, "Title: "+b+"\ninstagram:Follow Me And Me Follow You\nhttps://www.instagram.com/"+b)

            elif "/joingc: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("/joingc: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Maaf Bos Ane Tidak Ada Di Group itu")

            elif msg.text in ["Glist"]:
                cl.sendText(msg.to, "Tunggu Sebentar. . .")
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                kr.sendText(msg.to, msgs)

            elif "Google " in msg.text:
                    a = msg.text.replace("Google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Sedang Mencari...")
                    cl.sendText(msg.to, "https://www.google.com/" + b)

            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))

            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")

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

            elif msg.text in ["Kapten acc invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  
#--------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#------------------------
        if op.type == 59:
            print op

    except Exception as error:
        print error

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["01","10","19","55","10","20","25","30","40","50","60","70","80","90","100","00"]:
        return False
    else:
        return True

def autolike():
    for zx in range(0,200):
      hasil = cl.activity(limit=200)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐KrazyBoy⭐👈\n\n™By ")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,200):
        hasil = cl.activity(limit=200)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ^૦Ո૯ ƿɿ૯८૯ ら૯ՆԲც૦੮^\nStatus Boss udah Kami Like\nOwner Kami :\Trisan")
                    ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"KrazyBoy")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, count=50)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)