import re

def clean_data(data):
    # Split the data based on " v " (for versus)
    parts = data.split(' v ')
    if len(parts) != 2:
        #print("Invalid data format:", data)
        return None
    
    # Extract group 1 and score 1
    match1 = re.match(r'(.+?)\s(\d+/\d+)', parts[0])
    if match1:
        group1 = match1.group(1)
        score1 = match1.group(2)
    else:
        #print("No match found for group 1:", parts[0])
        return None
    
    # Extract group 2 and score 2
    match2 = re.match(r'(.+?)\s(\d+/\d+)', parts[1])
    if match2:
        group2 = match2.group(1)
        score2 = match2.group(2)
    else:
        #print("No match found for group 2:", parts[1])
        return None
    
    return (group1, score1, group2, score2)

