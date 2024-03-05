import requests
from bs4 import BeautifulSoup

def scrape_cricket_scores():
    # URL of the Google search page for live cricket scores
    url = 'https://static.cricinfo.com/rss/livescores.xml'
    # Send a GET request to fetch the HTML content of the page
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        # Find the elements containing the live cricket scores
        score_elements = soup.find_all('title')
        print(score_elements)
        #write to html
        with open('livescore.html', 'w') as f:
            f.write(str(soup))
        # print(soup.prettify()) 
        # Extract and print the live cricket scores
        for score_element in score_elements:
            #print(score_elements)
            # Get the text content of the score element
            score_text = score_element.text.strip()
           # print(score_text)

    else:
        print('Failed to fetch the live cricket scores. Status code:', response.status_code)
scrape_cricket_scores()