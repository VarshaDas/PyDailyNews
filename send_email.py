from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

COUNTRY_CODE = 'in'
CATEGORY = 'business'

def send_email(headlines):
    # Set your SendGrid API key
    sendgrid_api_key = ''

    subject = f'Top Headlines on {CATEGORY.capitalize()}'

    # Create the HTML content for the email body
    html_body = "<h2>Top Headlines</h2>"
    for index, article in enumerate(headlines):
        title = article['title']
        description = article['description']
        url = article['url']
        source = article['source']

        # Create a hyperlink for the description
        description_html = f'<a href="{url}">{description}</a>'
        html_body += f"<p><strong>{index + 1}. {title}</strong><br>{description_html}<br>Source: {source}</p>"

    message = Mail(
        from_email='',
        to_emails='',
        subject=subject,
        html_content=html_body
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Email sent with {len(headlines)} top headlines")
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(f"Failed to send email: {e}")
