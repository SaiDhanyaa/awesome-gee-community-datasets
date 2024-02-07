
#==========================================================================================================================
# 1. To identify all unique dataset types present in the catalog, we will extract the 'type' field from each dataset entry
#==========================================================================================================================

### Importing the Required Libraries
import json

# Use raw string notation to avoid escape sequence errors
file_path = r'C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\community_datasets.json'

# Load the JSON file
with open(file_path, 'r',encoding='utf-8') as file:
    data = json.load(file)


# To identify all unique dataset types present in the catalog, we will extract the 'type' field from each dataset entry
# and then use a set to find all unique values.

# Extract 'type' from each dataset
dataset_types = set(dataset['type'] for dataset in data)

# Convert the set to a list to sort and view it more easily
unique_dataset_types = sorted(list(dataset_types))

print("The unique data types available are:", unique_dataset_types)


#==========================================================================================================================
### 2. Counting the Occurrence of Each Metadata Header
#==========================================================================================================================

# To identify common metadata headers across all datasets, we'll analyze all the dataset entries
# and track which headers are present and how frequently they appear.

# Initialize a dictionary to count the occurrence of each header
header_occurrences = {}

# Loop through each dataset in the data
for dataset in data:
    for key in dataset.keys():
        # If the key is already in our dictionary, increment its count
        if key in header_occurrences:
            header_occurrences[key] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            header_occurrences[key] = 1

# Sort headers by occurrence to see the most common ones and any optional ones
sorted_headers = sorted(header_occurrences.items(), key=lambda x: x[1], reverse=True)

print("The sorted headers available are:", sorted_headers)


#==========================================================================================================================
# 3. To identify all unique TAGS  present in the catalog, we will extract the 'TAGS' field from each dataset entry
#==========================================================================================================================
# Extract 'TAGS' from each dataset
dataset_tags = set(dataset['tags'] for dataset in data)

# Convert the set to a list to sort and view it more easily
unique_dataset_tags = sorted(list(dataset_tags))

print("The unique data tags available are:", unique_dataset_tags.count)


#==========================================================================================================================
# 4. To identify all unique liscense  present in the catalog, we will extract the 'liscense' field from each dataset entry
#==========================================================================================================================
# Extract 'liscense' from each dataset
dataset_license = set(dataset['license'] for dataset in data)

# Convert the set to a list to sort and view it more easily
unique_dataset_license = sorted(list(dataset_license))

print("The unique data license available are:", unique_dataset_license)



#==========================================================================================================================
# 5.Documenting Metadata Headers for each dataset in the community_datasets.json file.
#==========================================================================================================================

import json
import pandas as pd

# Load the JSON file
file_path = r'C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\community_datasets.json'

# Load the JSON file
with open(file_path, 'r',encoding='utf-8') as file:
    json_data = json.load(file)


# Extract and organize data for CSV
csv_data = []
for dataset in json_data:
    csv_data.append({
        'Title': dataset.get('title', ''),
        'Sample Code': dataset.get('sample_code', ''),
        'Type': dataset.get('type', ''),
        'ID': dataset.get('id', ''),
        'Provider': dataset.get('provider', ''),
        'Tags': dataset.get('tags', ''),
        'License': dataset.get('license', '')
    })

# Convert to DataFrame
df = pd.DataFrame(csv_data)

# Save the organized data to a CSV file
output_csv_path = r'C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\New_organized_datasets.csv'
df.to_csv(output_csv_path, index=False)
##the newly created oragnised datasests csv filee is created...

#==========================================================================================================================
#IM going to scrap the details form md file to create new template md file
#==========================================================================================================================
import pandas as pd
import os

# Define the path to your CSV file and the directory containing MD files
csv_file = 'datasets.csv'  # Replace with the actual CSV file path
md_directory = 'md_files'  # Replace with the directory containing MD files

# Read data from the CSV file
df = pd.read_csv(csv_file)

# Loop through the MD files in the directory
for md_file in os.listdir(md_directory):
    if md_file.endswith('.md'):
        # Extract dataset title or unique identifier from the MD file name
        dataset_identifier = md_file[:-3]  # Remove the .md extension to get the identifier

        # Check if the dataset identifier exists in the CSV data
        if dataset_identifier in df['title'].values:
            # Extract dataset information from the CSV
            dataset_info = df[df['title'] == dataset_identifier].iloc[0]

            # Read the content of the MD file
            with open(os.path.join(md_directory, md_file), 'r') as f:
                md_content = f.read()

            # Update the MD content with data from the CSV
            md_content = md_content.replace('[Insert Title Here]', dataset_info['title'])
            md_content = md_content.replace('[Insert Description Here]', dataset_info['description'])
            # Repeat this for other sections

            # Write the updated content back to the MD file
            with open(os.path.join(md_directory, md_file), 'w') as f:
                f.write(md_content)

            print(f"Updated {md_file} with data from CSV.")
        else:
            print(f"Dataset {dataset_identifier} not found in CSV.")

print("Automation complete.")



#==========================================================================================================================
#==========================================================================================================================
#==========================================================================================================================
#==========================================================================================================================
#==========================================================================================================================
#==========================================================================================================================
def extract_content(old_md_content):
    # Dictionary to store extracted content
    extracted_content = {
        "description": "N/A",  # Default values if not found
        "earth_engine_snippet": "N/A",
        "usage": "N/A",
        "sample_code": "N/A",
        "sample_application_url": "N/A",
        "citations": "N/A",
        "license": "N/A",
        "changelog": "N/A",
        "keywords": "N/A",
        "date_created": "N/A"
    }

    # Regular expressions to extract sections
    # Adjust these patterns to fit the structure of your old .md files
    patterns = {
        "description": r"## Description\s+(.*?)\s+(##|$)",
        "earth_engine_snippet": r"## Earth Engine Snippet\s+```javascript\s+(.*?)\s+```\s+(##|$)",
        "usage": r"### Usage\s+(.*?)\s+(###|$)",
        "sample_code": r"### Sample Code\s+```javascript\s+(.*?)\s+```\s+(###|$)",
        "sample_application_url": r"### Sample Application\s+\[(.*?)\]\((.*?)\)",
        "citations": r"## Citations\s+(.*?)\s+(##|$)",
        "license": r"## License\s+(.*?)\s+(##|$)",
        "changelog": r"## Changelog\s+(.*?)\s+(##|$)",
        "keywords": r"## Keywords\s+(.*?)\s+(##|$)",
        "date_created": r"## Date Created\s+(.*?)\s+(##|$)"
    }

    # Iterate over each pattern and extract content
    for key, pattern in patterns.items():
        match = re.search(pattern, old_md_content, re.DOTALL)
        if match:
            # Special handling for Sample Application URL to extract the URL only
            if key == "sample_application_url":
                extracted_content[key] = match.group(2).strip()  # URL is the second group in the regex
            else:
                extracted_content[key] = match.group(1).strip()

    return extracted_content









