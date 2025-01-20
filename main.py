import tkinter as tk 
import nltk 
from textblob import TextBlob 
from newspaper import Article 


def summarize():
    url = utext.get("1.0", "end").strip()

    article = Article(url)

    try:
        article.download()
        article.parse()
        article.nlp()
    except Exception as e:
        print(f"Error: {e}")
        return

    # Update title
    title.config(state="normal")
    title.delete('1.0', 'end')
    title.insert('1.0', article.title or "Unknown")
    title.config(state="disabled")

    # Update authors
    author.config(state="normal")
    if article.authors:
        author_names = ', '.join(article.authors)
    else:
        author_names = "Unknown"
    author.delete('1.0', 'end')
    author.insert('1.0', author_names)
    author.config(state="disabled")

    # Update publication date
    publication.config(state="normal")
    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date or "Unknown")
    publication.config(state="disabled")

    # Update summary
    summary.config(state="normal")
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary or "No summary available")
    summary.config(state="disabled")

    # Perform sentiment analysis
    analysis = TextBlob(article.text)
    sentiment.config(state="normal")
    sentiment.delete('1.0', 'end')
    sentiment.insert(
        '1.0',
        f'Polarity: {analysis.polarity}, Sentiment: '
        f'{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'
    )
    sentiment.config(state="disabled")


root = tk.Tk()
root.title(" News Summarizer")
root.geometry("1200x600")


tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()


alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1,width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()


plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1,width=140)
publication.config(state='disabled',bg='#dddddd')
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20,width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

selabel= tk.Label(root, text="Sentiment Analysis")
selabel.pack()
sentiment = tk.Text(root, height=1,width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()
utext = tk.Text(root, height=1,width=140)
utext.pack()

btn= tk.Button(root, text="Summarize",command=summarize)
btn.pack()

root.mainloop()