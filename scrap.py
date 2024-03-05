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
        
        # Find the elements containing the live cricket scores
        score_elements = soup.find_all('title')
        
        # Create an HTML table to store the cricket scores
        html_table = '<table border="1">'
        html_table += '<tr><th>Match</th></tr>'

        # Extract and print the live cricket scores
        for score_element in score_elements:
            score_text = score_element.text.strip()
            html_table += f'<tr><td>{score_text}</td></tr>'
        
        html_table += '</table>'

        # Write the HTML table to a file
        with open('livescore.html', 'w') as f:
            f.write(html_table)

    else:
        print('Failed to fetch the live cricket scores. Status code:', response.status_code)

scrape_cricket_scores()
