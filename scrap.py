import requests
from bs4 import BeautifulSoup
import re

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
        
        # Extract country and score from each match
        countries = []
        scores = []
        for score_element in score_elements:
            score_text = score_element.text.strip()
            
            # Use regular expression to extract country and score
            match = re.match(r'(.*) v (.*)', score_text)
            if match:
                country = match.group(1).strip()
                score = match.group(2).strip()
                countries.append(country)
                scores.append(score)

        # Generate HTML table
        html_table = '<table border="1">'
        html_table += '<tr><th>Country1</th><th>Country2</th></tr>'
        for i in range(len(countries)):
            html_table += f'<tr><td>{countries[i]}</td><td>{scores[i]}</td></tr>'
        html_table += '</table>'

        # Write HTML table to file
        with open('cricket_scores.html', 'w') as f:
            f.write(html_table)

        print("HTML table generated successfully.")
    else:
        print('Failed to fetch the live cricket scores. Status code:', response.status_code)

scrape_cricket_scores()