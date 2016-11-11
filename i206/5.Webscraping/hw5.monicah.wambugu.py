import sys
import urllib.request
from bs4 import BeautifulSoup
import re

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code
'''
Citations
http://stackoverflow.com/questions/4981977/how-to-handle-response-encoding-from-urllib-request-urlopen
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

'''
soup=''

def extract_content(url,file):
    print('....')
    global soup
    content = urllib.request.urlopen(url).read().decode('utf8')
    try:
        content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup
        soup = BeautifulSoup(content,"html.parser")
        data = soup.find_all("li",{"class":"regular-search-result"})
    except:
        print('There was an error accessing the url. Please try again');
        pass
    try:
        if len(data)!=10:
            print('Warning!!Returned results are not 10!!!')
            print(len(data))
        for i in data:
            name = (i.contents[0].find("a",{"class":"biz-name js-analytics-click"}).text)
            reviews_text = (i.contents[0].find("span",{"class":"review-count rating-qualifier"}).text)
            reviews = re.match('(\d+)[\w\s]+', reviews_text).group(1)
            restraunt_entry = str(name)+','+str(reviews)+'\n'
            file.write(restraunt_entry)


    except:
        print('Error accessing content of the link.')
        pass
        
def main():
    global soup
    #url = 'file:///Users/monicah/Desktop/206-Distributed%20Computing/Assignments/HW5/Restaurants%20San%20Francisco,%20CA.htm'
    initial_url = 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&sortby=rating&start=0'
    file = open('restaurants.monicah.wambugu.txt', 'w',encoding='utf-8')
    try:
        extract_content(initial_url,file)
        next_pages = soup.find_all("a",{"class":"available-number pagination-links_anchor"})       
        for p in next_pages:
            params = p.get("href")
            url = 'https://www.yelp.com%s'%params
            extract_content(url,file)
            
        file.close()
    except:
        print('Error Encountered!!!')
        pass
if __name__ == "__main__":
    main()
