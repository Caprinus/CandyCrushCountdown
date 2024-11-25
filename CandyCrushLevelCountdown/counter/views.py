from bs4 import BeautifulSoup
from lxml import etree
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


def get_content():
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://candycrush.fandom.com/wiki/Template:TOTALLEVELSR').text
    return html_content



def counter(request):

    html_content = get_content()
    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup)
    webtext = etree.HTML(str(soup))
    #print(webtext)
    levels = webtext.xpath('/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/p')[0].text
    
    print(levels)
    maxlevel=int(levels)
    print(maxlevel)

    return render(request, 'index.html', {'nivelMaximo': maxlevel})
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
  
 
 #/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/p