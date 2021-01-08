import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
from tkinter import *
from tkinter import ttk
from methods import MyTranslator

def summarize():
    #download this first
    #nltk.download('punkt')

    url = utext.get('1.0', "end").strip()
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    #Accessing article.summary for run() use
    global summaryget
    summaryget = article.summary

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    translation.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    translation.config(state='disabled')
    sentiment.config(state='disabled')

def get():

    s = srcLangs.get()
    d = destLangs.get()
    translation.config(state='normal')
    message =summaryget

    translator = MyTranslator()
    text = translator.run(txt= message, src=s, dest=d)

    translation.delete(1.0,END)
    translation.insert(END, text)

#===============GUI LAYOUT====================
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text = "Title")
tlabel.grid(row = 0, column = 0)

title = tk.Text(root, height = 1, width= 70)
title.config(state='disabled', bg ='#dddddd')
title.grid(row = 1, column = 0, padx = 10, pady = 5)


alabel = tk.Label(root, text = "Author")
alabel.grid(row = 0, column = 1)

author = tk.Text(root, height = 1, width= 70)
author.config(state='disabled', bg ='#dddddd')
author.grid(row = 1, column = 1, padx = 10, pady = 5)
#=================================================================
plabel = tk.Label(root, text = "Publishing Date")
plabel.grid(row = 2, column = 0)

publication = tk.Text(root, height = 1, width= 70)
publication.config(state='disabled', bg ='#dddddd')
publication.grid(row = 3, column = 0, padx = 10, pady = 5)

selabel = tk.Label(root, text = "Sentiment Analysis")
selabel.grid(row = 2, column = 1)

sentiment = tk.Text(root, height = 1, width= 70)
sentiment.config(state='disabled', bg ='#dddddd')
sentiment.grid(row = 3, column = 1, padx = 10, pady = 5)
#=================================================================

slabel = tk.Label(root, text = "Summary")
slabel.grid(row = 4, column = 0)


summary = tk.Text(root, height = 20, width= 70)
summary.config(state='disabled', bg ='#dddddd')
summary.grid(row = 5, column = 0, padx = 10, pady = 5)

translabel= tk.Label(root, text = "Tranlated")
translabel.grid(row = 4, column = 1)

translation = tk.Text(root, height = 20, width= 70)
translation.config(state='disabled', bg ='#dddddd')
translation.grid(row = 5, column = 1, padx = 10, pady = 5)
#=================================================================
ulabel = tk.Label(root, text = "URL")
ulabel.grid(row = 6, column = 0, columnspan = 2)

utext = tk.Text(root, height = 1, width= 140)
utext.grid(row = 7, column = 0, columnspan = 2)

btn = tk.Button(root, text = "Summarize", command = summarize)
btn.grid(row = 8, column = 1)

transBtn = tk.Button(root, text = 'Translate', command =get)
transBtn.grid(row = 8, column = 0)

langs =MyTranslator().langs

srcLangs = ttk.Combobox(root,values =langs, width =10)
srcLangs.place(x=140, y=500)
srcLangs.set('english')

destLangs = ttk.Combobox(root,values =langs, width =10)
destLangs.place(x=360, y=500)
destLangs.set('japanese')

root.mainloop()
