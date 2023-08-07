import requests
from datetime import datetime, timedelta

NEWS_API_KEY = ''
COUNTRY_CODE = 'in'
CATEGORY = 'technology'


def get_top_headlines(page_size=20, page=1):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': NEWS_API_KEY,
        'country': COUNTRY_CODE,
        'category': CATEGORY,
        'pageSize': page_size,
        'page': page
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('articles', [])
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []


def filter_articles(articles):
    current_date = datetime.now()

    # Subtract one day from the current date
    one_day_ago = current_date - timedelta(days=1)

    # Convert the result back to string format '%Y-%m-%d'
    one_day_ago_str = one_day_ago.strftime('%Y-%m-%d')
    filtered_articles = []

    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        source = article.get('source', {}).get('name', '')
        url = article.get('url', '')
        published_at = article.get('publishedAt', '')[:10]

        if title and description and source and url and published_at == one_day_ago_str:
            filtered_articles.append({
                'title': title,
                'description': description,
                'source': source,
                'url': url
            })

    return filtered_articles
