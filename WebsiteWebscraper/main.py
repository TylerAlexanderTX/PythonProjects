from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from bs4 import BeautifulSoup
import pandas
import requests

app=Flask(__name__)

@app.route('/')
def home():
    base_url = "https://arstechnica.com/"
    request = requests.get(base_url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = request.content
    soup = BeautifulSoup(c, "html.parser")
    features = soup.find_all("li", {"class":"split-feature"})
    #print(features)
    ars = "<div><h1>Headlines - "+ base_url +"</h1><b>"
    for feature in features:
        link = feature.find_all('a')[0].get('href')
        text = feature.find_all('h2')[0].text
        ars = ars + "<h3><a href=" + link + ">"+ text +"</a></h3><b>"

    ars = ars + "</div>"

    base_url2 = "https://old.reddit.com"
    request = requests.get(base_url2, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = request.content
    soup = BeautifulSoup(c, "html.parser")
    posts = soup.find_all("div", {"class": "thing"})[:11]
    reddit = "<b><div class=\"container\"><h1>Reddit Top 10</h1><b>"
    for post in posts:
        sponsored = post.find("span", {"class":"sponsored-indicator"})
        if not sponsored:
            title = post.find("p", {"class":"title"}).text
            link = post.find_all('a', class_='comments')[0].get('href')
            reddit = reddit + "<h4><a href=" + link + ">" + title + "</a></h4><b>"
        
    reddit = reddit + "</div><b>"
            
    return render_template("home.html", ars = ars, reddit = reddit)

if __name__ == "__main__":
    app.run(debug=True)