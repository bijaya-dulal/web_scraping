import os

def open_html_in_browser(html_file_path):
    # Get the absolute path of the HTML file
    abs_path = os.path.abspath(html_file_path)
    
    # Check if the file exists
    if os.path.exists(abs_path):
        # Open the HTML file in the default web browser
        os.system(f'xdg-open "{abs_path}"')  # For Linux
    else:
        print(f"File '{html_file_path}' does not exist.")
