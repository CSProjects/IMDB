import requests
from bs4 import BeautifulSoup
from tkinter import *
import os
from pandastable import Table
import pandas as pd
from tqdm import tqdm
from PIL import ImageTk, Image
from tkinter import filedialog
import glob


#GUI interface
root = Tk()
root.title('IMDB scraper with other things')
root.geometry('500x600')

filmNames = []
#filmYear = []

files = glob.glob(r'C:/Users/PuTung/Desktop/PyCharm projects/IMDB/profileImage/*.jpg')
for f in files:
    os.remove(f)

def urllookup():
    result = requests.get(myTextbox.get())
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    #Do i want the actor's name?
    """actorName = soup.find('h1').find('span').string
    filmNames.append(actorName)"""

    #Actor's image
    actorImage = soup.find('img', id='name-poster')
    imgUrl = actorImage['src']

    #function for downloading the image
    def download(url, pathname):
        # if path doesn't exist, make that path dir
        if not os.path.isdir(pathname):
            os.makedirs(pathname)
        # download the body of response by chunk, not immediately
        response = requests.get(url, stream=True)
        # get the total file size
        file_size = int(response.headers.get("Content-Length", 0))
        # get the file name
        filename = os.path.join(pathname, url.split("/")[-1])
        # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
        progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B",
                        unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            for data in progress:
                # write data read to the file
                f.write(data)
                # update the progress bar manually
                progress.update(len(data))
    #download and show image
    download(imgUrl, 'profileImage')
    open_img()

    firstCategory = soup.find_all('div', class_='filmo-category-section')
    #for finding the film name and year
    for fullList in firstCategory:
        for b_tag in fullList.find_all('b'):
            a_tag = b_tag.find('a')
            if a_tag.attrs['href']:
                filmNames.append(a_tag.string)
        #problematic with empty years
        """for span_tag in fullList.find_all('span', class_='year_column'):
            if span_tag.string > '1000':
                filmYear.append("In progress.")
            else:
                filmYear.append(span_tag.string)"""


    """myMovieList = Text(root)
    for x in filmNames:
       myMovieList.insert(END, x + '\n')
    myMovieList.pack()
    print(len(filmNames))"""

    """myYearList = Text(root)
    for x in filmYear:
        myYearList.insert(END, x)
    myYearList.pack()
    print(len(filmYear))"""



    #panda table
    pdTable = pd.DataFrame({'Movie': filmNames})


    #table in tkinter
    frame = Frame(root)
    frame.pack(fill='both', expand=True)
    pt = Table(frame, dataframe=pdTable)
    pt.show()




myLabel = Label(root, text='Enter the website link of the actor/actress')
myLabel.pack()

#textbox
myTextbox = Entry(root, width=30)
myTextbox.pack()
myTextbox.focus_set()

#button
myButton = Button(root, text='Enter', command=urllookup)
myButton.pack()

def open_img2():
    path = openfileName()
    print(path)
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(root, image = img)
    panel.image = img
    panel.pack()

def open_img():
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    picName = str(os.listdir('profileImage'))
    ''.join(picName)
    print(picName)
    print('works')
    img = ImageTk.PhotoImage(Image.open(picName))
    canvas.create_image(20, 20, anchor=NW, image=img)



def openfileName():
    fileName = filedialog.askopenfilename(title='open')
    return fileName




root.mainloop()
