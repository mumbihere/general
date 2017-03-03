import sys
import urllib.request
from bs4 import BeautifulSoup
import re
import csv
#import wikipedia


def preprocess_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content



def extract_content(url,file):
    print('....')
    content = urllib.request.urlopen(url).read().decode('utf8')
    try:
        content = preprocess_page(content) # Now *content* is a string containing a page of search results, ready for processing with BeautifulSoup
        soup = BeautifulSoup(content,"html.parser")
        data = soup.find_all("tr")
        print(len(data))

        for item in data:
            print(item)
            break

    
    except:
        print('Error accessing content of the link.')
        pass
        
def main():
    global soup
    url = 'file:///Users/monicah/Desktop/Spring%202017/Info%20Viz/Tableau%20Exploratory%20Assignment/COUNTY%20ELECTION%20RESULTS%20%E2%80%93%20GOVERNORS%20AND%20SENATORS%20_%20KenyaForum.htm'
    #initial_url = 'http://www.kenyaforum.net/2013/03/12/county-election-results-governors-and-senators/'
    file = open('data/governors.csv', 'w',encoding='utf-8')
    try:
        extract_content(url,file)
        
    except:
        print('Error Encountered')
        pass
    file.close()




if __name__ == "__main__":
    main()
