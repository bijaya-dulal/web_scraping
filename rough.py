import re
def extract_groups(item):
    # Regular expression pattern to extract the desired groups
    pattern = r'(.+?)\s(\d+/\d+)(?:\s&\s(\d+/\d+))?\s\*\sv\s(.+?)\s(\d+/\d+)(?:\s&\s(\d+/\d+))?'

    # Match the pattern against the item
    match = re.match(pattern, item)

    if match:
        # Extract the groups
        group1 = match.group(1)
        score1 = match.group(2)
        extra_score1 = match.group(3)
        group2 = match.group(4)
        score2 = match.group(5)
        extra_score2 = match.group(6)

        # Check if extra scores are present and concatenate if necessary
        if extra_score1:
            score1 += " & " + extra_score1
        if extra_score2:
            score2 += " & " + extra_score2

        return group1, score1, group2, score2
    else:
        return None

# Example list of items
items = [
    "New Zealand 179/10 & 196/10 * v Australia 383/10 & 164/10",
    "New South Wales 242/4 * v South Australia 287/10",
    "Tasmania 240/10 & 307/10 v Victoria 144 & 106/10 *",
    "Western Australia 32 & 310/10 * v Queensland 170/10",
    "Vidarbha 170/10 v Madhya Pradesh 47/1 *",
    "Mumbai 45/2 * v Tamil Nadu 146/10",
    "Kuwait 65/1 * v Tanzania",
    "Italy v Vanuatu 25/2 *",
    "Bahrain 33/1 * v Bermuda",
    "Hong Kong Cricket Club Women 77/4 * v Diasqua Little Sai Wan CC Women",
    "Craigengower Cricket Club Women 146/1 * v Lantau Cricket Club Women",
    "Jaffna v Galle",
    "Kandy v Dambulla",
    "Hong Kong Cricket Club v Diasqua Little Sai Wan Cricket Club",
    "Pakistan Association of Hong Kong v United Services Recreation Club",
    "Namibia v Netherlands",
    "United Arab Emirates v Scotland",
    "Mountaineers v Durham",
    "Mid West Rhinos v Southern Rocks",
    "Karachi Kings v Multan Sultans",
    "Delhi Capitals Women v Gujarat Giants Women",
    "Mashonaland Eagles v Matabeleland Tuskers"
]

# Extract groups for each item
for item in items:
    groups = extract_groups(item)
    if groups:
        print("Group 1:", groups[0])
        print("Score 1:", groups[1])
        print("Group 2:", groups[2])
        print("Score 2:", groups[3])
        print()
    else:
        print("No match found for:", item)
