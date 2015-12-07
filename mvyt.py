from __future__ import unicode_literals
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, FancyURLopener
from urllib.parse import urlencode
from colorama import Fore, Back, Style, init
from random import choice
import urllib.request
import os,sys
import time
import youtube_dl
import readline

class menu(object):
    def __init__(self):
        self.user_in = None
        self.tittle = [
        """         _______                        _________
        (       )|\     /|     |\     /|\__   __/
        | () () || )   ( |     ( \   / )   ) (
        | || || || |   | | _____\ (_) /    | |
        | |(_)| |( (   ) )(_____)\   /     | |
        | |   | | \ \_/ /         ) (      | |
        | )   ( |  \   /          | |      | |
        |/     \|   \_/           \_/      )_( 0.5a""",
        "                    by newfag               ",
        ]
        self.help = """
        -d Download options: "-d 1,2,3,4,8" or "-d 1:4,8"
        -x For exit
        """
    def Draw_help(self):
        print (self.help[0::])

    def DrawMain(self):
        print (Fore.RED + self.tittle[0],"\n",Fore.YELLOW + self.tittle[1],Style.RESET_ALL,"\n")

    def pronpt(self, text):
        self.user_in = str(input(Fore.MAGENTA + text + Style.RESET_ALL))
        return self.user_in

    def msg(text):
        print (Fore.MAGENTA + text + Style.RESET_ALL)

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

class mvyt(object):
    def __init__(self, user_agents):
        self.pag = None
        self.url = None
        self.user_agent = choice(user_agents)
        self.data = []
        self.nun_pags = None
        self.current_pag = None
        self.soup = None

    def pagination(self):
        current_pag = self.soup.find_all('div', id='scrollpages')
        nun_pags = self.soup.find_all('a',class_= 'last')
        for items in current_pag:
            self.current_pag = items.find('em')
        for items in nun_pags:
            self.nun_pags = items.contents[0]
        self.current_pag = str(self.current_pag.contents[0])

    def nave (self):
        pag = urlopen(Request(self.url, headers={'User-Agent': self.user_agent}))
        self.read_pag = pag.read()
        pag.close()
        return self.read_pag

    def vids (self):
        pagvdis = []
        self.soup = BeautifulSoup(self.nave(), "html.parser")
        div_em = self.soup.find_all('div', class_ = 'youtube_lite')
        for items in div_em:
            a = items.find('a')
            link = ('https://www.youtube.com/watch?v=' + a['data-youtube'])
            self.data.append(link)
            pagvdis.append(link)
        return self.data,pagvdis

    def set_url(self, url):
        try:
            self.url = url
            self.vids()
            self.data = []
            return True
        except:
            self.data = []
            return  False

    def get_cpag(self):
        return self.current_pag

    def get_npags(self):
        return self.nun_pags

    def user(self):
        return self.user_agent

################## Youtube_DL ##################################################
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        #print(msg)
        pass

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def ytdl(lista,ydl_opts):
    cont = 0
    vid_list ={}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for videos in lista:
            cont +=1
            try:
                info_dict = ydl.extract_info(videos, download=False)
                video_title = info_dict.get('title', None)
                vid_list[cont] = [video_title,videos]
            except youtube_dl.utils.DownloadError:
                cont -=1
        return vid_list

def ytdldown(lista, ydl_opts):
    #path?
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for link in lista:
            try:
                #ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
            except youtube_dl.utils.DownloadError:
                print ("[Error] ",link)
################################################################################

def clean_list(ytlist, select_vids):
    a = []
    for i in select_vids:
        dd = ytlist[int(i)]
        a.append(dd)
    return a

def dlist(option):
    selecvids = []
    try:
        if option[3].isdigit():
            selecvids.append(option[3])
            return selecvids
        elif option[3] == "-":
            selecvids = option[4::].split(",")
            cont_options = 0
            for items in selecvids:
                if ":" in items:
                    x = items.split(":")
                    del selecvids[cont_options]
                    for i in range(int(x[0]),int(x[1]) + 1):
                        selecvids.append(str(i))
                cont_options +=1
            selecvids = list(set(selecvids))
            return selecvids
    except:
        return False

def main(ydl_opts, user_agents):
    Mvyt = mvyt(user_agents)
    p = menu()
    init()
    run = True
    url = False
    cpag = False
    newpag = None
    pag_vids = []
    ytlist = []
    dd_list = []
    option = ""
    while run:
        if url:
            if not pag_vids:
                pag_vids = Mvyt.vids()[1]
            if not ytlist:
                print ("Loading....")
                ytlist = ytdl(pag_vids,ydl_opts)
                for items in ytlist:
                    print (items, "-" ,ytlist[items][0])
                print (Mvyt.get_cpag(),"de", Mvyt.get_npags())
            if newpag and option[0:2] in ["-n","-b"]:
                p.cls()
                p.DrawMain()
                Mvyt.set_url(newpag)
                Mvyt.pagination()
                pag_vids = Mvyt.vids()[1]
                print (newpag, "\nLoading....")
                ytlist = ytdl(pag_vids,ydl_opts)
                for items in ytlist:
                    print (items, "-" ,ytlist[items][0])
                print (Mvyt.get_cpag(),"de", Mvyt.get_npags())
            elif option[0:2] == "-d":
                p.cls()
                p.DrawMain()
            option = p.pronpt("-h for help \n:")
            if option[0:2] == "-h":
                p.cls()
                p.DrawMain()
                p.Draw_help()
            elif option[0:2] == "-d":
                selecvids = dlist(option)
                print (selecvids)
                if selecvids:
                    dd_list.append(clean_list(ytlist,selecvids))
                else:
                    print ("sintax error")
            elif option[0:2] == "-l":
                if dd_list:
                    for items in dd_list:
                        print (items)
            elif option[0:3] == "-dl":

                pass

            elif option[0:2] == "-n":
                cpag = Mvyt.get_cpag()
                npags = Mvyt.get_npags()
                if cpag < npags:
                    cpag = int(cpag) + 1
                    newpag = url + "/" + str(cpag)
            elif option[0:2] == "-b":
                cpag = int(Mvyt.get_cpag())
                if cpag > 1:
                    cpag -=1
                    newpag = url + "/" + str(cpag)
            elif option[0:2] == "-x":
                print ("Exit")
                sys.exit()
            else:
                print ("cool story")
        else:
            while True:
                p.cls()
                p.DrawMain()
                print ('Insert Url: "http://www.example.com"\n "-x" para salir')
                url = p.pronpt(":")
                if url == "-x":
                    sys.exit()
                test = Mvyt.set_url(url)
                if test:
                    Mvyt.set_url(url)
                    Mvyt.pagination()
                    break
                else:
                    print ("url error")
                    time.sleep(1)

if __name__ == '__main__':
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    user_agents = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0"]
    main(ydl_opts, user_agents)
