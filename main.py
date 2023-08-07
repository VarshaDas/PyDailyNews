from news_api import get_top_headlines, filter_articles
from send_email import send_email

if __name__ == "__main__":
    page_size = 20  # Change this to the desired page size
    page_number = 1  # Start from the first page

    articles = get_top_headlines(page_size=page_size, page=page_number)
    if articles:
        filtered_articles = filter_articles(articles)
        send_email(filtered_articles)
