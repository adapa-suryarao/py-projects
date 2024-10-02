from tkinter import *
from urllib.request import urlopen
import io
import requests
import webbrowser
from PIL import Image, ImageTk
import pyttsx3  # Import pyttsx3 for text-to-speech
import threading  # Import threading to run speak() in parallel

class news_app():

    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=9a92ff3899e846e886a8340709353e2f').json()

        # Initialize the pyttsx3 engine
        self.engine = pyttsx3.init()
        
        # Load the GUI and display the first news item
        self.load_gui()
        self.load_news(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('666x666')
        self.root.title('News Application')
        self.root.config(background='black')
        self.root.resizable(450, 450)

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def load_news(self, index):
        self.clear()

        try:
            img_url = (self.data['articles'][index]['urlToImage'])
            raw_img = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_img)).resize((700, 450))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((700, 450))
            photo = ImageTk.PhotoImage(im)

        Label(self.root, image=photo).pack()

        title = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', font='lucida 22 bold', wraplength=560)
        title.pack()

        description = self.data['articles'][index]['description']
        dec = Label(self.root, text=description, bg='black', fg='white', font='lucida 12', wraplength=750)
        dec.pack(anchor='center')

        # Start a new thread to speak the description in parallel with displaying the news
        threading.Thread(target=self.speak, args=(description,)).start()

        frame = Frame(self.root, bg='grey')
        frame.pack(fill=BOTH, anchor='s', side='bottom')

        if index != 0:
            but1 = Button(frame, text='Prev', command=lambda: self.load_news(index - 1))
            but1.pack(fill=BOTH)

        Button(frame, text='Read More', command=lambda: self.open_url(self.data['articles'][index]['url'])).pack(fill=BOTH)

        if index != len(self.data['articles']) - 1:
            but2 = Button(frame, text='Next', command=lambda: self.load_news(index + 1))
            but2.pack(fill=BOTH)

        self.root.mainloop()

    def speak(self, text):
        """This function will use pyttsx3 to speak out the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def open_url(self, url):
        webbrowser.open(url)

# Create the news app object and run it
obj = news_app()