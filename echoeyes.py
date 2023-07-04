# host checker Bot CODED by echoeyes

# echoeyes - telegram @echoeyes 

# echoeyes - github @  https://github.com/echoeyesdev 

# imports 
import requests 
import logging 
import sys
import os
import concurrent.futures

# Foreground (text) colors
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

# Background colors
bg_black = '\033[40m'
bg_red = '\033[41m'
bg_green = '\033[42m'
bg_yellow = '\033[43m'
bg_blue = '\033[44m'
bg_magenta = '\033[45m'
bg_cyan = '\033[46m'
bg_white = '\033[47m'

# Text styles
bold = '\033[1m'


def cloudflare(url):
        count = f"{cyan}~"
        httpwebsite = f"https://{url}"
        request = requests.Session()
        request.headers = { # pose as a human browser
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
        try: 
            
            response = request.get(httpwebsite)
            if response.status_code == 200 and response.headers["Server"] == "cloudflare":
                print(count, f"{green}[working] {blue}[{url}]{white}")
            else:
                print(count, f"{red}[N/W][{url}]{white}")
  
                
        except:
            print(count, f"{red}[N/A][{url}]{white}")
     
            
            
def cloudfront(url):
        count = f"{cyan}~"
        httpwebsite = f"https://{url}"
        request = requests.Session()
        request.headers = { # pose as a human browser
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
        try: 
            
            response = request.get(httpwebsite)
            if response.status_code == 200 and response.headers["Server"] == "cloudfront" or response.headers["Server"] == "AmazonS3":
                print(count, f"{green}[working] {blue}[{url}]{white}")
            else:
                print(count, f"{red}[N/W][{url}]{white}")
  
                
        except:
            print(count, f"{red}[N/A][{url}]{white}")
     
            
def nginx(url):
        count = f"{cyan}~"
        httpwebsite = f"https://{url}"
        request = requests.Session()
        request.headers = { # pose as a human browser
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
        try: 
            
            response = request.get(httpwebsite)
            server = response.headers["Server"]
            if response.status_code == 200 and "nginx" in server:
                print(count, f"{green}[working] {blue}[{url}]{white}")
            else:
                print(count, f"{red}[N/W][{url}]{white}")
  
                
        except:
            print(count, f"{red}[N/A][{url}]{white}")
     
            
            
def apache(url):
        count = f"{cyan}~"
        httpwebsite = f"https://{url}"
        request = requests.Session()
        request.headers = { # pose as a human browser
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
        try: 
            
            response = request.get(httpwebsite)
            server = response.headers["Server"]
            if response.status_code == 200 and "Apache" in server:
                print(count, f"{green}[working] {blue}[{url}]{white}")
            else:
                print(count, f"{red}[N/W][{url}]{white}")
  
                
        except:
            print(count, f"{red}[N/A][{url}]{white}")
     
            
            
def haproxy(url):
        count = f"{cyan}~"
        httpwebsite = f"https://{url}"
        request = requests.Session()
        request.headers = { # pose as a human browser
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
        try: 
            
            response = request.get(httpwebsite)
            server = response.headers["Server"]
            if response.status_code == 200 and "HAProxy" in server:
                print(count, f"{green}[working] {blue}[{url}]{white}")
            else:
                print(count, f"{red}[N/W][{url}]{white}")
  
                
        except:
            print(count, f"{red}[N/A][{url}]{white}")
     
            
           
           
            
os.system("clear")

intro = f"""{red} 

            ⚠️THIS TOOL IS FOR HUNTING PURPOSES ONLY                   
            ⚠️MAKE SURE TO USE A SIM CARD WITH NO DATA      
            
            {yellow}Telegram account{white} -> {blue}@echoeyes{white}  
            {yellow}github{white} -> {blue}https://github.com/echoeyesdev{white}                                    
            
            {green}<-----let the Hunt begin ----->{white}
            coded with love by -->{blue}Echoeyes{white}<--
 
{blue}
choose index of the Server

[1] cloudflare 
[2] cloudfront 
[3] Apache
[4] HAProxy
[5] nginx all versions 
{white}
""" 
with open("hosts.txt", "r") as f:
    list_of = f.readlines()
    hosts = [host.strip() for host in list_of]
    
    print(intro)
    
    choice = input("choose the index of the sever: ")
    
    try:
        if choice == "1": 
            print(f"{blue}you selected {green}Cloudflare{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(cloudflare, hosts)
        elif choice == "2":
            print(f"{blue}you selected {green}Cloudfront{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(cloudfront, hosts)
        elif choice == "3":
            print(f"{blue}you selected {green}Apache{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(apache, hosts)
        elif choice == "4":
            print(f"{blue}you selected {green}HAProxy{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(haproxy, hosts)
        elif choice == "5":
            print(f"{blue}you selected {green}Nginx{blue} GOOD LUCK\n")
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(nginx, hosts)
            
        else:
            print("invalid input")
            
    except KeyboardInterrupt:
        sys.exit("this could cause an Error, Try CTRL+C...")
        
        