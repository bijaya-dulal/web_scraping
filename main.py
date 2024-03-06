import numpy as np
from scrap import *
from browser_open import open_html_in_browser

scrape_cricket_scores()
# Call the function with the path to your HTML file
open_html_in_browser('cricket_scores.html')