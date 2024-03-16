import requests
from bs4 import BeautifulSoup
import re
from clean import clean_data

def scrape_cricket_scores():
    print("here")
    # URL of the Google search page for live cricket scores
    url = 'https://static.cricinfo.com/rss/livescores.xml'
    # Send a GET request to fetch the HTML content of the page
    response = requests.get(url)
   
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the elements containing the live cricket scores
        score_elements = soup.find_all('title',)
        pub_date_tag = soup.find('pubdate')
        pub_date = pub_date_tag.text.strip()
        # Extract country and score from each match
 
       
        for score_element in score_elements:
            score_text = score_element.text.strip()
            print(score_text)
            filtered_data = clean_data(score_text)
            
      
        print(filtered_data)   
    
        # # Generate HTML table
        # html_table = '<!DOCTYPE html>\n<html>\n<head>\n<title>Cricket Scores</title>\n<link rel="stylesheet" type="text/css" href="design.css">\n</head>\n<body>\n'
        # html_table += '<h1>Live Cricket Scores</h1>\n<table border="1">'
        # html_table += f'<h3>Updated on: {pub_date}</h3>\n<table border="1">'
        # html_table += '<tr><th>Country 1</th><th> VS </th><th>Country 2</th></tr>'
        # for i in range(len(countries1)):
        #     html_table += f'<tr><td>{countries1[i]}</td><td> VS </td><td>{countries2[i]}</td></tr>'
        # html_table += '</table>\n</body>\n</html>'

        # # Write HTML table to file
        # with open('cricket_scores.html', 'w') as f:clear
        #     f.write(html_table)

        
    else:
        print('Failed to fetch the live cricket scores. Status code:', response.status_code)


scrape_cricket_scores()