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
        self.main = [
        """         _______                        _________
        (       )|\     /|     |\     /|\__   __/
        | () () || )   ( |     ( \   / )   ) (
        | || || || |   | | _____\ (_) /    | |
        | |(_)| |( (   ) )(_____)\   /     | |
        | |   | | \ \_/ /         ) (      | |
        | )   ( |  \   /          | |      | |
        |/     \|   \_/           \_/      )_( 0.2.1a""",
        "                    by newfag               ",
        "1-Todo el Thread",
        "2-Video a video",
        "3-Ver lista",
        "4-Ayuda",
        "5-Salir",
        ]

    def DrawMain(self):
        print (Fore.RED + self.main[0],"\n",Fore.YELLOW + self.main[1],Style.RESET_ALL,"\n")
        for items in self.main[2:7]:
            print (Fore.MAGENTA  + items[0:1], Style.RESET_ALL + items[1::])

    def DrawOption(self):
        self.cls()
        print (Fore.RED + self.main[0],"\n",Fore.YELLOW + self.main[1],Style.RESET_ALL,"\n")

    def post(self, text):
        user_in = str(input(Fore.MAGENTA + text + Style.RESET_ALL))
        return user_in

    def test(self):
        print ("test")

    def quit(self):
        self.cls()
        print ("Get the fuck out!")
        sys.exit()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def error(self):
        input("opcion invalida...")

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
    if option == "n":
        pass
    elif option == "b":
        pass
    elif option.isdigit():
        print (int(option))
    elif option[0] == "/":
        selecvids = option[1::].split(",")
        print (selecvids)
        return selecvids
    elif option == "x":
        return option
    else:
        print ("Error")

def main():
    init()
    user_agents = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"]
    run = True
    x = menu()
    x.cls()
    x.DrawMain()
    option = x.post("\u21B3 Select a choice:")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        x.DrawOption()
        res = x.post("Url del thread \u21B3")
        while run:
            choice = input(": ")
            chop = option_list(choice)
            if chop == "x":
                run = False
        Mvyt = mvyt(res, user_agents)
        print ("Procesando..")
        lista,soup = Mvyt.vids()
        Mvyt.pagination()
        allurls = Mvyt.allurls()
        videos = test(lista)
        x.cls()
        x.DrawOption()
        print ("-Videos activos-")
        cont = 0
        for keys in videos:
            cont += 1
            print (cont, " ", keys, "\n", videos[keys])
        print ("Pagina: ",Mvyt.current_pag.contents[0], "de ",Mvyt.nun_pags)
    elif option == "4":
        pass
    elif option == "5":
        x.quit()
    else:
        x.error

if __name__ == '__main__':
    main()
    #main_pagination("/1,2,4,5")
