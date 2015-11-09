from bs4 import BeautifulSoup
from random import choice
from urllib.request import Request, urlopen, FancyURLopener
from urllib.parse import urlencode
import urllib.request
from colorama import Fore, Back, Style, init
import os,sys
import time
import pafy

class mvyt(object):
    def __init__(self, url, user_agents):
        self.pag = None
        self.url = url
        self.user_agent = choice(user_agents)
        self.data = []
        self.nun_pags = 0
        self.current_pag = 0
        self.user_in = None
        self.coin = True
        self.all_urls = []

    def pagination(self):
        dat,soup = self.vids()
        current_pag = soup.find_all('div', id='scrollpages')
        nun_pags = soup.find_all('a',class_= 'last')
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
        soup = BeautifulSoup(self.nave(), "html.parser")
        div_em = soup.find_all('div', class_ = 'youtube_lite')
        for items in div_em:
            a = items.find('a')
            link = ('https://www.youtube.com/watch?v=' + a['data-youtube'])
            self.data.append(link)
        return self.data,soup

    def current_pag(self):
        pass

    def allurls(self):
        return self.all_urls

    def user(self):
        return self.user_agent

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
        -u Insert Url: "-u http://www.dsadasd.com"
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


def test(lista):
    videos = {}
    for items in lista:
        try:
            video = pafy.new(items)
            titulo = video.title
            videos[titulo] = items
        except:
            pass
    return videos

def option_list(option):
    selecvids = []
    cont_options = 0
    if option.isdigit():
        print (int(option))
        return option
    elif option[0:2] == "-d":
        selecvids = option[2::].split(",")
        for items in selecvids:
            if ":" in items:
                x = items.split(":")
                start = int(x[0])
                stop = int(x[1])
                del selecvids[cont_options]
                for i in range(int(x[0]),int(x[1]) + 1):
                    selecvids.append(str(i))
            cont_options +=1
        selecvids = list(set(selecvids))
        return selecvids
    else:
        print ("Error")

def main():
    init()
    user_agents = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"]
    run = True
    p = menu()
    p.cls()
    p.DrawMain()
    url = None
    while run:
        option = p.pronpt("-h for help \n:")
        if option == "-x":
            print ("Exit")
            sys.exit()
        elif option == "-h":
            p.cls()
            p.DrawMain()
            p.Draw_help()
        elif option[0:2] == "-u":
            print ("url")

        else:
            p.cls()
            p.DrawMain()
            op = option_list(option)
            if op:
                print (op)




if __name__ == '__main__':
    main()
