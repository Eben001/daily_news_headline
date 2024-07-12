import requests
from bs4 import BeautifulSoup
import asyncio
import os
from notificationapi_python_server_sdk import notificationapi
if asyncio.get_event_loop().is_running():
    import nest_asyncio
    nest_asyncio.apply()


CLIENT_ID = os.environ['client_id']
CLIENT_SECRET = os.environ['client_secret']
EMAIL = os.environ['email']
PHONE_NUMBER = os.environ['phone_number']


async def send_notification(comment):
    notificationapi.init(
        CLIENT_ID,  
         CLIENT_SECRET
    )

    await notificationapi.send({
        "notificationId": "new_comment",
        "user": {
          "id": "ndacekogana@gmail.com",
          "email": "ndacekogana@gmail.com",
          "number":"+2348152758566"    
        },
        "mergeTags": {
          "comment": comment
        }
    })


url = 'https://dailynigerian.com/category/headline/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

news_div = soup.find_all('div', class_='td-block-span6')
news_text = f'NEWS HEADLINE\n'
for i, news in enumerate(news_div, 1):
  try:
    news_title = news.find('h3', class_='entry-title td-module-title').text.strip()
    news_date = news.find('span', class_='td-post-date').text.strip()

  except: 
    continue
  news_text += f"{i}. {news_title} || {news_date}\n"

notification_text = f'{news_text}\nThis messsage was sent automatically. \nPowered by Eben'
print(notification_text)
asyncio.run(send_notification(notification_text))
