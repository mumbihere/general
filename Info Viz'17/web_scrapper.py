import sys
import urllib.request
from bs4 import BeautifulSoup
import re
#import wikipedia


def preprocess_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#def extract_wiki_yob(name):
import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

def extract_content(url,file):
    print('....')
    content = urllib.request.urlopen(url).read().decode('utf8')
    try:
        content = preprocess_page(content) # Now *content* is a string containing a page of search results, ready for processing with BeautifulSoup
        soup = BeautifulSoup(content,"html.parser")
        data = soup.find_all("li")
        for item in data:
            try:
                data_item = item.p
                if len(data_item)>0:
                    
                    m = re.match(r"Governor (.+) County –(.+)",data_item.string)
                    county = str(m.group(1))
                    governor = str(m.group(2))
                    file.write(county+','+governor+'\n')
                    

            except:
                pass
    

    except:
        print('Error accessing content of the link.')
        pass
        
def main():
    global soup
    url = 'file:///Users/monicah/Desktop/Spring%202017/Info%20Viz/Tableau%20Exploratory%20Assignment/Updated%20List%20of%20Governors%20in%20Kenya%20-%20ZaKenya.htm'
    #initial_url = 'http://www.zakenya.com/politics/updated-list-of-governors-in-kenya.html'
    file = open('data/governors.csv', 'w',encoding='utf-8')
    try:
        extract_content(url,file)
        
    except:
        print('Error Encountered')
        pass
    file.close()




if __name__ == "__main__":
    main()
