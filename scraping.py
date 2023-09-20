import requests
from bs4 import BeautifulSoup

def get_subscriber_count(channel_url):
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming subscriber count is contained within a <span> element with a specific class
    subscriber_count_element = soup.find('span', {'class': 'yt-subscription-button-subscriber-count-branded-horizontal'})
    
    if subscriber_count_element:
        subscriber_count = subscriber_count_element.text.strip()
        return subscriber_count
    else:
        return None

# Replace 'CHANNEL_URL' with the actual URL of the channel you're interested in
channel_url = 'https://www.youtube.com/channel/UCEEkKXpAkSwcMaIHnGi3Niw'
subscriber_count = get_subscriber_count(channel_url)

if subscriber_count is not None:
    print(f"The channel has {subscriber_count} subscribers.")
else:
    print("Subscriber count not found.")
