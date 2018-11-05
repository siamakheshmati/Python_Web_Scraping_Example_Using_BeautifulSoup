import BeautifulSoup
import re
from urllib import urlopen


def main():
    webpage=urlopen('http://www.latimes.com/local/rss2.0.xml').read()
    TitlepatternFinder=re.compile('<title>(.*)</title>')
    LinkpatternFinder=re.compile('<link rel.*href=(.*)>')
     
     
    titles=re.findall(TitlepatternFinder,webpage)
    links=re.findall(LinkpatternFinder,webpage)
   
    listIterator=[]
    listIterator[:]=range(1,26)
                        
    for i in listIterator:
        try:
           print titles[i]
           print links[i]
           print '\n'
        except:    
            print '\n'
    
if __name__=='__main__': main()