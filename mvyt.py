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
        |/     \|   \_/           \_/      )_( 0.3a""",
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
        self.user_in = None
        self.coin = True
        self.all_urls = [] #hsahdj
        self.soup = None


    def pagination(self):
        current_pag = self.soup.find_all('div', id='scrollpages')
        nun_pags = self.soup.find_all('a',class_= 'last')
        for items in current_pag:
            self.current_pag = items.find('em')
        for items in nun_pags:
            self.nun_pags = items.contents[0]
        self.current_pag = self.current_pag.contents[0]


    def nave (self):
        pag = urlopen(Request(self.url, headers={'User-Agent': self.user_agent}))
        self.read_pag = pag.read()
        pag.close()
        return self.read_pag

    def vids (self):
        #self.url = link
        self.soup = BeautifulSoup(self.nave(), "html.parser")
        div_em = self.soup.find_all('div', class_ = 'youtube_lite')
        for items in div_em:
            a = items.find('a')
            link = ('https://www.youtube.com/watch?v=' + a['data-youtube'])
            self.data.append(link)
        return self.data

    def set_url(self, url):
        #Yolo
        try:
            self.url = url
            self.vids()
            self.data = []
            return True
        except:
            error = "url error"
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
    vid_list = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for videos in lista:
            cont +=1
            try:
                info_dict = ydl.extract_info(videos, download=False)
                video_title = info_dict.get('title', None)
                #print ("[",cont,"]",video_title)
                #print (videos)
                vid_list.append(videos)
            except youtube_dl.utils.DownloadError:
                cont -=1
                #print ("[ X ] video elminado")
                #print (videos)
        #ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
        return vid_list
################################################################################


def clean_list(ddlist, vdlist, select_vids):
    if len(ddlist) > 1: 
        for i in select_vids:
            dd = vdlist[int(i)-1]
            ddlist.append(dd)
        return ddlist

def dlist(option):
    selecvids = []
    try:
        if option[3].isdigit():
            selecvids.append(option)
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

def main(ydl_opts):
    run = True
    url = False
    cpag = False
    newpag = None
    option = None
    p = menu()
    dd_list = []
    user_agents = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0"]
    Mvyt = mvyt(user_agents)
    init()
    while run:
        if url:
            if newpag and option[0:2] == "-n":
                Mvyt.set_url(newpag)
                Mvyt.pagination()
            else:
                Mvyt.pagination()

            print (cpag,"of", Mvyt.get_npags())
            option = p.pronpt("-h for help \n:")
            if option[0:2] == "-x":
                print ("Exit")
                sys.exit()
            elif option[0:2] == "-h":
                p.cls()
                p.DrawMain()
                p.Draw_help()
            elif option[0:2] == "-d":
                selecvids = dlist(option)
                if selecvids:
                    yulist = Mvyt.vids()
                    mylist = ytdl(yulist, ydl_opts)
                    dd_list = clean_list(dd_list,mylist,selecvids)
                    dd_list = ytdl(dd_list)
                else:
                    print ("sintax error")
                    dd_list = []

            elif option[0:2] == "-l":
                if dd_list:
                    for items in dd_list:
                        print (items)

            elif option[0:2] == "-n":
                cpag = Mvyt.get_cpag()
                npags = Mvyt.get_npags()
                if cpag < npags:
                    cpag = int(cpag) + 1
                    newpag = url + "/" + str(cpag)

            elif option[0:2] == "-b":
                cpag = int(Mvyt.get_cpag())
                cpag -=1
                newpag = url + "/" + str(cpag)

            else:
                print ("Not in options")
        else:
            while True:
                p.cls()
                p.DrawMain()
                print ('Insert Url: "http://www.example.com"\n "-x" to Exit  ')
                url = p.pronpt(":")
                if url == "-x":
                    sys.exit()
                test = Mvyt.set_url(url)
                if test:
                    Mvyt.set_url(url)
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

    main(ydl_opts)
