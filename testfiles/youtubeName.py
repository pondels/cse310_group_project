# This file Grabs the name of the Youtube Video to be used
# For file naming and organization

# https://www.geeksforgeeks.org/python-obtain-title-views-and-likes-of-youtube-video-using-beautifulsoup/
from bs4 import BeautifulSoup
import requests
  
def removeCrap(data):
    data = data.replace('-', '')
    data = data.replace('!', '')
    data = data.replace('@', '')
    data = data.replace('#', '')
    data = data.replace('$', '')
    data = data.replace('%', '')
    data = data.replace('^', '')
    data = data.replace('&', '')
    data = data.replace('*', '')
    data = data.replace('(', '')
    data = data.replace(')', '')
    data = data.replace('+', '')
    data = data.replace('{', '')
    data = data.replace('[', '')
    data = data.replace('}', '')
    data = data.replace(']', '')
    data = data.replace('\\', '')
    data = data.replace('/', '')
    data = data.replace('"', '')
    data = data.replace("'", '')
    data = data.replace('_', '')
    data = data.replace('=', '')
    data = data.replace(':', '')
    data = data.replace(';', '')
    data = data.replace('.', '')
    data = data.replace(',', '')
    data = data.replace('>', '')
    data = data.replace('<', '')
    data = data.replace('?', '')
    data = data.replace('~', '')
    data = data.replace('`', '')
    return data
# creating function
def scrape_info(url):
      
    # getting the request from url
    r = requests.get(url)
      
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
    # finding meta info for title
    title = s.find("title").text.replace("\n", "")
    title = title.split(" ")
    title.pop()
    title.pop()
    data = ''
    for i in range(len(title)):
        title[i].strip('-')
        if i != " " and i != '' and i != '-':
            data += title[i]
    return data
  
# main function
if __name__ == "__main__":
      
    # URL of the video
    url = input("Enter a Valid Youtube URL: ")
      
    # calling the function
    data = scrape_info(url)
      
    # printing the dictionary
    data = removeCrap(data)
    
    print(data)