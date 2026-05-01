from bs4 import BeautifulSoup
import urllib
#import Selenium

def instagram():
    list_ = []
    result_list = []
    html =  urllib.urlopen(instagram_url).read()
    soup = BeautifulSoup(html,'html.parser')
    likes =  soup.find_all('body')
    string = str(likes)
    for i in range(0,len(string)):
        if string[i:i+10] == '"caption":':
            jackpot =  string[i+10:i+500]
            list_.append(jackpot)
    for i in range(0, len(list_)):
        number = ''
        print list_[i]
        """for j in range(0,len(list_[i])):
            if list_[i][j] in '0123456789':
                number = number + list_[i][j]
        result_list.append(int(number))"""

    return result_list

instagram_url = 'https://www.instagram.com/luisdelcastillo.official/'

instagram()
