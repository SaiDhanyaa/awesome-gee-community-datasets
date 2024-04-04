import json
import os
import re

# Define the path to your markdown files
markdown_dir = r'C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\docs\projects\updated_md_files'
print(updated_md_files)
# Function to extract structured metadata from markdown content
def extract_metadata(md_content):
    metadata = {
        'title': re.search(r'^# (.+)', md_content).group(1).strip(),
        'description': re.search(r'^## Description:\s*\n\n(.+)', md_content, re.DOTALL).group(1).strip().split('\n\n')[0],
        'earth_engine_snippet': re.search(r'^## Earth Engine Snippet:\s*\n\n```js\n([^`]+)\n```', md_content, re.DOTALL).group(1).strip(),
        'citation': re.search(r'## Citations:\s*\n\nNA|(?<=\[hyperlink\]\().+?(?=\))', md_content),
        'license': re.search(r'^## License\s*\n\n(.+)', md_content).group(1).strip(),
        'changelog': re.search(r'^## Changelog\s*\n\n(.+)', md_content).group(1).strip() if '## Changelog' in md_content else 'NA',
        'keywords': re.search(r'^## Keywords\s*\n\n(.+)', md_content).group(1).strip().split(', '),
        'date_created': re.search(r'^## Date Created\s*\n\n(.+)', md_content).group(1).strip() if '## Date Created' in md_content else 'NA',
        'provider': re.search(r'^## Provider\s*\n\n(.+)', md_content).group(1).strip(),
        'curated_by': re.search(r'^## Curated in GEE by\s*\n\n(.+)', md_content).group(1).strip()
    }
    return metadata

# Initialize an empty list to hold all dataset metadata
all_datasets = []

# Iterate over markdown files and extract metadata
for md_filename in os.listdir(markdown_dir):
    if md_filename.endswith('.md'):
        with open(os.path.join(markdown_dir, md_filename), 'r') as md_file:
            md_content = md_file.read()
            dataset_metadata = extract_metadata(md_content)
            all_datasets.append(dataset_metadata)
            print(dataset_metadata)

# Define the path for the new JSON file
new_json_file_path = r'C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\new_community_datasets.json'

# Write the collected dataset metadata to a new JSON file
with open(new_json_file_path, 'w', encoding='utf-8') as jf:
    json.dump(all_datasets, jf, indent=4)
