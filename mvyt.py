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

class mvyt(object):
    def __init__(self, user_agents):
        self.pag = None
        self.url = None
        self.user_agent = choice(user_agents)
        self.data = []
        self.nun_pags = 0
        self.current_pag = 0
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
        all_urls = []
        if dat:
            for i in range (1,int(self.nun_pags)+1):
                self.pag_url = self.url + '/' + str(i)
                self.all_urls.append(self.pag_url)
                #print (self.pag_url)
        else:
            print("error paginacion")

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
        self.url = url

    def current_pag(self):
        pass

    def allurls(self):
        return self.all_urls

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

def ytdl(lista):
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
    cont = 0
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for videos in lista:
            cont +=1
            try:
                info_dict = ydl.extract_info(videos, download=False)
                video_title = info_dict.get('title', None)
                print ("[",cont,"]",video_title)
                print (videos)
            except youtube_dl.utils.DownloadError:
                cont -=1
                print ("[ X ] video elminado")
                print (videos)
        #ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
################################################################################

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


def main():
    run = True
    url = False
    p = menu()
    selecvids = []
    user_agents = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"]
    Mvyt = mvyt(user_agents)
    init()
    while run:
        if url:
            try:
                Mvyt.set_url(url)
                yulist = Mvyt.vids()
                ytdl(yulist)
                option = p.pronpt("-h for help \n:")
                if option == "-x":
                    print ("Exit")
                    sys.exit()
                elif option == "-h":
                    p.cls()
                    p.DrawMain()
                    p.Draw_help()
                elif option[0:2] == "-d":
                    if option[3].isdigit():
                        print (option)
                        selecvids.append(option)
                    if option[3] == "-":
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
                        print (selecvids)
                    else:
                        print ("Error")

            except ValueError:
                print (url, "es incorrecto")
                url = None
                time.sleep(1)

        else:
            p.cls()
            p.DrawMain()
            print ('Insert Url: "http://www.example.com"\n "-x" to Exit  ')
            url = p.pronpt(":")
            if url == "-x":
                sys.exit()

if __name__ == '__main__':
    main()
