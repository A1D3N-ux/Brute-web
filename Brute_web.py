import requests
import pyfiglet
from bs4 import BeautifulSoup
from time import sleep

url = "https://free-proxy-list.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table_text = soup.find_all("textarea")[0].get_text()
rows = table_text.split("\n")
 
for row in rows[1:-1]:
    parts = row.split(":")
    if len(parts) == 2:
        proxy_ip, proxy_port = parts
        print(f'{proxy_ip}: {proxy_port}')
 
 
print('\n')
 
print('------------------------------')
 
print('\n')

        

ascii_banner = pyfiglet.figlet_format("Programmed By A1D3N")
print(ascii_banner)
print(""""
############################
#  Brute Admin/Diretorio   #
############################
""")
def paineladmin():
    
    site = input("Digite a url, exemplo:https://www.exemplo.com.br: ").strip()
    word = open("wordlist.txt")
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }
    proxies = []
    with open('proxys.txt', 'r') as lista_proxys:
        for proxy in lista_proxys:
            proxies.append({
                'http': proxy.strip()
            })
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }
    for proxy in proxies:
            for wor in word:
                sit = site + '/' + wor.strip()
                try:
                    bru = requests.get(sit, proxies=proxy, headers=headers, timeout=10)
                    sleep(3)
                    if bru.status_code == 200:
                        print(f'Diretorio encontrado! {sit} Status: {bru.status_code} | proxy >  {proxy["http"].split(":")[0]}')
                        print('')
                    else:
                        print(sit, bru.status_code, f' | proxy > {proxy["http"].split(":")[0]}')
    
                        print('')
                except Exception as e:
                    print(f"Erro ao acessar {sit} via {proxy['http']}: {str(e)} ")
                    print('')
 
def diretorio():
     
    site = input('Insira o site alvo: ')
    word = input('Insira o caminho da wordlist: ')
    print('')
 
    proxies = []
    with open('proxys.txt', 'r') as lista_proxys:
        for proxy in lista_proxys:
            proxies.append({
                'http': proxy.strip()
            })
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }
 
 
    for proxy in proxies:
        for wor in word:
            sit = site + '/' + wor.strip()
            try:
                bru = requests.get(sit, proxies=proxy, headers=headers, timeout=10)
                sleep(3)
                if bru.status_code == 200:
                    print(f'Diretorio encontrado! {sit} Status: {bru.status_code} | proxy >  {proxy["http"].split(":")[0]}')
                    print('')
                else:
                    print(sit, bru.status_code, f' | proxy > {proxy["http"].split(":")[0]}')
 
                    print('')
            except Exception as e:
                print(f"Erro ao acessar {sit} via {proxy['http']}: {str(e)} ")
                print('')
 

opcao = int(input("Escolha uma opção\n 1 - Painel Admin \n 2 - Brute Diretorio \n "))
if opcao == 1:
    print(""""
                ############################
                #       Painel admin       #
                ############################
                """)
    paineladmin()
elif opcao == 2:
    print(""""
        ############################
        #       Brute Diretorio    #
        ############################
        """)
    diretorio()
elif opcao < 1  or opcao > 2:
    print("opção invalida, tente novamente.")