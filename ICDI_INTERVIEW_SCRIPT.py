
# Step 1: Import Necessary Libraries
import requests
import re
import requests
import json
from scipy import datasets

# Step 2: Define GitHub Repository Information

github_username = "samapriya"
repository_name = "awesome-gee-community-datasets"
api_base_url = f"https://api.github.com/repos/samapriya/awesome-gee-community-datasets/contents/docs/projects"
#api_base_url = r'C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\docs\projects'

# Step 3: Retrieve .md Files
# We'll send a GET request to the GitHub API to retrieve a list of .md files in the specified directory
response = requests.get(api_base_url)

# Check if the response status code is 200 (success)
if response.status_code == 200:
    # Parse the JSON response to get the list of files
    content_data = response.json()

    # Filter out .md Files .The GitHub API response will contain information about the contents of the directory.
    # We need to filter it to select only the .md files and save that in a dictionary"md_files"
    md_files = [item for item in content_data if item["name"].endswith(".md")]

    # List .md File Names . We can now list the names of the .md files we've retrieved.
    for md_file in md_files:
        print(md_file["name"])

else:
    print(f"Failed to retrieve the content. Status code: {response.status_code}")

# Step 4: Now we are going to Read and Summarize Headers in Each .md File
''' 
# md_file is a dictionary containing information about the .md file, including its name and a download URL.
# We use the requests.get function to make an HTTP GET request to the file_url,which is the download URL of the current .md file. 
# This request fetches the content of the .md file from the internet.
# The response from the HTTP request is stored in the response variable.
'''

for md_file in md_files:
    file_url = md_file["download_url"]
    response = requests.get(file_url)

    # Check if the response status code is 200 (success)
    '''
    * We check if the response status code is 200, which means the content retrieval was successful. 
    * If the status code is not 200, we print an error message and move on to the next .md file.
    * If the response is successful, we proceed to process the content of the .md file. The content is stored in the md_content variable.
    * we initialize an empty dictionary called headers to store the headers we find in the .md file. This dictionary will organize the headers by their levels.
    * The header_matches variable uses a regular expression (re.findall) to search for lines in the md_content that start with one or more # symbols (hash symbols), 
      followed by some text. This regex pattern captures both the level of the header (number of # symbols) and the header text.
    * We iterate through the header_matches list, and for each match, we determine the header level by counting the number of # symbols (the length of the level string).
    * We add the header to the appropriate level in the headers dictionary. If the level is not already a key in the dictionary, 
    * we create an entry for that level and initialize it as an empty list. We then append the header text to that list.
    '''
    if response.status_code == 200:
        # Read the content of the .md file
        md_content = response.text

        # Initialize variables to store the headers--create a dictionary and store the headers in it
        headers = {}

        # Use regular expressions to find and summarize headers
        header_matches = re.findall(r'^(#+)\s(.+)', md_content, re.MULTILINE)
        for level, header_text in header_matches:
            # Count the number of '#' characters to determine the header level
            # if #- 1st level header
            # ##- 2nd level header and so on
            header_level = len(level)

            # Store the header in the headers dictionary
            if header_level not in headers:
                headers[header_level] = []
            headers[header_level].append(header_text)

        # Report the name of the file and its headers
        '''
        * First, we print the name of the .md file using the md_file['name'] attribute, which contains the file's name.
        * Next, we iterate through the headers dictionary, which now contains headers organized by their levels.
        * For each header level, we print the level number (e.g., "Level 1 Headers:"). This indicates the level of the headers we are about to list.
        * Finally, we print each header within that level, indicating the header text using the - symbol.
        * We use a print() statement after each .md file's headers to create a clear separation and make the output easier to read.
        '''
        print(f"File Name: '{md_file['name']}'")
        for level, header_list in headers.items():
            print(f"Level {level} Headers:")
            for header in header_list:
                print(f" - {header}")
        print()
    else:
        print(f"Failed to retrieve the content of '{md_file['name']}'. Status code: {response.status_code}")


################
