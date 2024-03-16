import re

def clean_data(items):
    # Regular expression pattern to extract the desired groups
    pattern = r'(.+)\s(\d+/\d+)\s\*\sv\s(.+)\s(\d+/\d+)'

    extracted_groups = []
    
    for content in items:
        # Match the pattern against the content
        match = re.match(pattern, content)

        if match:
            # Extract the groups
            group1 = match.group(1)
            score1 = match.group(2)
            group2 = match.group(3)
            score2 = match.group(4)

            # Append the extracted groups to the list
            extracted_groups.append((group1, score1, group2, score2))
        else:
            # Append None for items with no match
            extracted_groups.append(None)
    
    return extracted_groups