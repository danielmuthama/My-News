from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, get_articles

@main.route('/')
def index():
    """
    Root page
    """

    #show all the news sources
    all_news = get_news()
    print("Available sources")
    title = "YouNews"
    return render_template('index.html', title = title, all_news = all_news)

@main.route('/source/<id>')
def articles(id):
    """dislays articles from a given source"""

    articles = get_articles(id)
    title = f'{id}'

    return render_template("articles.html", id = id, title = title, articles = articles)
