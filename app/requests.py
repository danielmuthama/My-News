import urllib.request, json
from .models import New
from .models import Article

#get API key
api_key = None

#get URL 
base_url = None
article_url = None

def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']

def get_news():
    """
    Gets the JSON response to our URL request
    """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None 

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    processes the results list and transforms them to a list of objects
    """
    news_results = []
    for item in news_list:
        id = item.get("id")
        name = item.get("name")
        description = item.get("description")
        url = item.get("url")
        category = item.get("category")
        language = item.get("language")
        country = item.get("country")
    
        news_object = New(id, name, description, url, category, language, country)
        news_results.append(news_object)

    return news_results

def get_articles(id):
    """
    Gets the JSON response to our URL request
    """
    get_article_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None 

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(articles_list):
    
    article_results = []

    for article in articles_list:
        title = article.get('title')
        urlImage = article.get('urlToImage')
        author = article.get('author')
        url =  article.get('url')
        date_x = article.get('publishedAt')
        date = slice_date(date_x)
    
        if urlImage:
            article_object = Article(title, urlImage, author, url, date)
            article_results.append(article_object)

    return article_results

def slice_date(pass_date):
    YYYY = pass_date[0:4]
    MM = pass_date[5:7]
    DD = pass_date[8:10]
    time = pass_date[11:19]
    new_date = f'{time} EAT, {DD}/{MM}/{YYYY}'
    return new_date