from tkinter import *
import os
import requests
from bs4 import BeautifulSoup

#GUI interface
root = Tk()
root.title('IMDB scraper with other things')
root.geometry('400x600')

#Variables

#Getting the imdb movie list
def findActorMovieList():
    global myTextbox
    urlHolder = myTextbox.get()
    print('works')
    result = requests.get(urlHolder)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    actorName = soup.find('h1').find('span').string

    global filmNames
    filmNames = []

    filmNames.append(actorName)
    for b_tag in soup.find_all('b'):
        a_tag = b_tag.find('a')
        if a_tag.attrs['href']:
            filmNames.append(a_tag.string)

    for name in filmNames:
        name = Label(root, text=filmNames)
        name.pack()


myLabel = Label(root, text='Enter the website link of the actor/actress')
myLabel.pack()

#textbox
myTextbox = Entry(root, width=30)
myTextbox.pack()
myTextbox.focus_set()

#button
myButton = Button(root, text='Enter', command=findActorMovieList())
myButton.pack()

#myList = Text(root)
#for x in filmNames():
 #   myList.insert(END, x + '\n')
#myList.pack()

root.mainloop()




