
def top10_catalog():
    import requests
    from bs4 import BeautifulSoup
    BASE_URL = "http://www.gutenberg.org"
    url = BASE_URL+ "/browse/scores/top"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.findAll("ol")
    f = open('top10','w',encoding="utf-8")
    print('Top 10 eBooks\' catalog\n')
    for link in links:
        while(True):
            top_list = link.findAll("li")
            x = 0
            for x in range(10):
                title = str(top_list[x].text)
                url_link = BASE_URL+str(top_list[x].findAll("a")[0].get("href"))+'\n'
                string = title+ ','+url_link
                f.write(str(string))
                print(string)
            break
        break
    f.close()

top10_catalog()
