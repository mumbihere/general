
import re
import urllib.request
import logging
import sys
from collections import OrderedDict

LOG_FILENAME = 'error.log'

#writes error message into logfile 
def logging(msg):
    import logging
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logging.error(msg)

#reads a webpage and returns all the words on the page    
def read_webpage(url):
    the_page=''
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        the_page = response.read().decode(errors='ignore')
    except urllib.error.HTTPError as e:
         logging(e.code)
         logging(e.read())        
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, the_page.split()) if x]
    return words


#Phase 1: Reads the Catalog file and creates the dictionary Books and list Titles
def ReadCatalog(catalog_file):
    try:
        Books ={}
        Titles = []
        with open(catalog_file,'r',encoding='utf-8') as f_in:
            lines = list(line for line in (l.strip() for l in f_in) if line)

        for book in lines:
            p = (re.compile('(.+),(http:\/\/.+)')).match(book)
            
            try:
                Books[p.group(1)] = [len(Books) ,p.group(2)]
                Titles.append(p.group(1))
            except:
                logging(sys.exc_info()[0])
                logging(sys.exc_info()[1])
        return Books, Titles
    
    except FileNotFoundError:
        print("Catalog file not found")
        return None
    except:
        print('Please provide a valid catalog.txt file')
        logging("Unexpected error:"+str(sys.exc_info()[0]))
        logging("Unexpected error:"+str(sys.exc_info()[1]))
    

    


#Reads a url and returns a dictionary of the count of all unique words
def ReadBook(book_url):
    book_words = {}
    all_words_in_book = read_webpage(book_url)
    unique_words_in_book = list(set(all_words_in_book))
    for word in unique_words_in_book:
        book_words[word]=all_words_in_book.count(word)
    return book_words

#modifys the Words dictionary given the book number and the 
def UpdateWords(book_number, Words_dict,book_words):
    print('Loading words in book '+ str(book_number) +' ....')
    absent_words = list(set(Words_dict.keys()) - set(book_words.keys()))
    for key, value in book_words.items():
        try:    #existing_words
            Words_dict[key].append(value)
        except KeyError:#new_words
            try:
                my_list = [0] * int(book_number)
                my_list.append(value)
                Words_dict[key] = my_list
            except:
                logging(sys.exc_info()[0])
                logging(sys.exc_info()[1])
        except:
            logging(sys.exc_info()[0])
            logging(sys.exc_info()[1])
    for key in absent_words:
        Words_dict[key].append(0)
    return Words_dict




def search(search_word,words,books,titles):
    try:
        word_count = words[search_word]

        for occurence in word_count:
            book_title = titles[word_count.index(occurence)]
            link = books[book_title][1]
            if occurence != 1: plural = 's'
            else: plural='' 
            print('\nThe word '+str(search_word)+' appears '+str(occurence)+' time'+plural+' in '+str(book_title)+' (link:'+str(link)+')')
    except KeyError:
        print('The word '+str(search_word)+' does not appear in any books in the library')


def main():
    #catalog = 'test.pdf'
    #catalog = 'blank.txt'
    #catalog = 'hw4localcatalog.txt'
    catalog = 'hw4simplecatalog.txt'
    word_dict = {}
    ct = ReadCatalog(catalog)

    if ct:
        books,titles = ct
        while(True):
            if len(titles)==0:
                x = input('Empty catalog loaded. \nType \'<terminate>\' to exit.\n')
                if x == '<terminate>':
                    break
            else:
                for title in titles:
                    book = books[title]
                    book_number = book[0]
                    words_in_book = ReadBook(book[1]) #Phase 1
                    word_dict = UpdateWords(book_number, word_dict,words_in_book) #Phase 2

                #Phase 3: Search, terminate, catalog, titles
                while(True):
                    search_term = input('\nSearch term? ').lower()
                    
                    if search_term == '':
                        print('Please enter a valid search term.')
                    elif search_term == '<terminate>':
                        break
                    elif search_term == '<catalog>':
                        for t in titles:
                            print('\n',t,':',books[t])
                    elif search_term == '<titles>':
                        for t in titles:
                            print(t)
                    else :
                        search_term = ''.join(e for e in search_term if e.isalnum())
                        search(search_term,word_dict,books,titles)
                break
         
    


if __name__ == "__main__":
    main()

