from gensim.summarization.summarizer import summarize
from bs4 import BeautifulSoup
import requests
import gensim


def get_only_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    title = ' '.join(soup.title.stripped_strings)
    return title, text


text = get_only_text(url)


print(summarize(repr(text), word_count=100))
