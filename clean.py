import re

# Regular expression pattern to match the country name and score
pattern = r'(.+)\s(\d+/\d+)'

def clean_data(data_list):
    print("i have called")
    for data in data_list:
        match = re.match(pattern, data)
        if match:
            country = match.group(1)
            score = match.group(2)
            print("Country:", country)
            print("Score:", score)
        else:
            print(data,"yet to begin")
        print()  # Add a newline between each data entry

# Example list of data entries
data_list = ["New Zealand 179/10", "Australia 383/10", "India 240/7"]

# Call the clean_data function with the list of data
#clean_data(data_list)
