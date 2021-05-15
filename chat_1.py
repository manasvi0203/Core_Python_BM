import datetime
import webbrowser
import os
import random

helloIntent = ["hello", "heyy", "good morning", "hi", "hi there"]
byeIntent  = ["bye","see you there", "bbye", "see you"]

while True:
    msg = input("Enter your message: ")
    msg = msg.lower()

    if msg in helloIntent:
        print("Hi there")
    elif msg in byeIntent:
        print("See you again")
        break
    elif "date" in msg:
        print(datetime.date.today())
    elif "time" in msg:
        time = datetime.datetime.now()
        print(time.hour, time.minute, time.second, sep=":")
    elif "google" in msg:
        if msg == "google":
            query = input("What do you want to search: ")
        else:
            query = msg[7:]
        path = "https://www.google.com/search?q="+query
        webbrowser.open(path)
    # youtube video search
    elif "song" in msg:
        os.chdir(r"D:\Songs")
        print(os.listdir())
        os.system(random.choice(os.listdir()))
    # video songs
    # game
    elif "word" in msg:
        os.system()
    else:
        print("I don't understand")

