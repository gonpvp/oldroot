# BY GONPVP

# IMPORTS
import os
import string
import itertools
import requests
from itertools import product

# GET CONFIG
def getconfig(var):
    
    dirconfig = os.getcwd() + '\\' + 'config.yml'
    
    with open(dirconfig, 'r') as config:
                
        textlign = config.readline().rstrip() 
                        
        while textlign:
            if var.startswith(var):
                print('var : ' + var)
                print('var replace : ' + var.replace('var' + ': ', ''))
                return var.replace('var' + ': ', '')
                    
            textlign = config.readline().rstrip()


# nofiltresearch IMGRU
def filtresearchfromlist(fromfile, name, format):
    dirconfig = os.getcwd() + '\\' + fromfile
    
    dirhtml = os.getcwd() + '\\' + name + '.html'
    os.makedirs(os.path.dirname(dirhtml), exist_ok=True)
    html = open(dirhtml, 'w+', encoding='utf8')

    loopint = 1
    with open(dirconfig, 'r') as list:
                
        textlign = list.readline().rstrip() 
                        
        while textlign:
            html.write('<img alt="'+ str(loopint) + '(return URL): ' + textlign + '" src=https://i.imgur.com/' + textlign + format + '">\n')
            loopint += 1
            textlign = list.readline().rstrip()

    print('Done with a spam of ' + str(loopint) + '(99% of the images do not exist)')
    html.close()       
                    

# filtresearch IMGRU
def filtresearch(link, number, car, name = 'not-name-defined'):

    digits = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    print('Loading ...')  
    loopint = 1    
    fastn = 1
    for i in product(car + digits, repeat=int(number)):
        
        r = requests.get('https://i.imgur.com/' + link.replace('§',''.join(i)))
        fastn =+ 1
        if r.url != 'https://i.imgur.com/removed.png':
            response = link.replace('§',''.join(i))
            print('The image with a search of has been found! : https://i.imgur.com/' + response)
            loopint += 1
    
    print('Done with a spam of ' + str(loopint) + 'and correct image found' + str(loopint) + '(99% of the images contains weird stuff, creepy stuff, pornographic etc take care of yourself!)')
        
# nofiltresearch IMGRU
def nofiltresearch(link, number, car):

    digits = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    print('Loading ...')

    dirhtml = os.getcwd() + '\\' + car + '.html'
    os.makedirs(os.path.dirname(dirhtml), exist_ok=True)
    html = open(dirhtml, 'w+', encoding='utf8')
        
    loopint = 1
    for i in product(car + digits, repeat=int(number)):
        response = link.replace('§',''.join(i))
        html.write('<img alt="'+ str(loopint) + 'Return URL: ' + response + '" src=https://i.imgur.com/' + response + '">\n')
        loopint += 1
    
    print('Done with a spam of ' + str(loopint) + '(99% of the images do not exist)')
    html.close()        

def panel():
    print(r"""
    _      ______          _____  _____ _   _  _____      ____  _      _____  _____   ____   ____ _______ 
    | |    |  ____|   /\   |  __ \|_   _| \ | |/ ____|   / __ \| |    |  __ \|  __ \ / __ \ / __ \__   __|
    | |    | |__     /  \  | |__) | | | |  \| | |  __   | |  | | |    | |  | | |__) | |  | | |  | | | |   
    | |    |  __|   / /\ \ |  _  /  | | | . ` | | |_ |  | |  | | |    | |  | |  _  /| |  | | |  | | | |   
    | |____| |____ / ____ \| | \ \ _| |_| |\  | |__| |  | |__| | |____| |__| | | \ \| |__| | |__| | | |   
    |______|______/_/    \_\_|  \_\_____|_| \_|\_____|   \____/|______|_____/|_|  \_\\____/ \____/  |_|   
    
    """)
    print("Tape help to see all commands and close to close script")
    while True:
        command = input("Command : ")
        if command == 'help':
            print(' ')
            print('Spam search image from imgru link and generate html response:')
            print('- nofiltresearch <link> <car> <name>')
            print('exemple: - nofiltresearch ywDgK§.png 2 name test1')
            print(' ')
            print('Spam search image from list.txt file and generate html response:')
            print('- filtresearchfromlist <from> <name> <format>')
            print('exemple: - filtresearchfromlist filename.txt test1 .png')
            print(' ')
            print('Check image from imgru link is exist (attention it is long because it makes requests of packet and no html responnse):')
            print('- filtresearch <link> <car> <name>')
            print('exemple: - filtresearch ywDgK§.png 2 caracters')
            print(' ')
        elif command.startswith('filtresearchfromlist '):
            searchcommand = command.split(' ')
            filtresearchfromlist(searchcommand[1], searchcommand[2], searchcommand[3])
        elif command.startswith('filtresearch '):
            searchcommand = command.split(' ')
            filtresearch(searchcommand[1], searchcommand[2], searchcommand[3], searchcommand[4])
        elif command.startswith('nofiltresearch '):
            searchcommand = command.split(' ')
            nofiltresearch(searchcommand[1], searchcommand[2], searchcommand[3])
        elif command == 'hide':
            os.system('cls')
            break
        elif command == 'restart' or 'redem' or 'reload':
            os.system('cls')
            os.system('python main.py')
        else:
            print('command not exist')
    
    exit()
    
# LANCH THE SCRIPT
panel()