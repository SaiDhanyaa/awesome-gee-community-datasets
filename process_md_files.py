#===========================================================================================================================
#
#===========================================================================================================================


#===========================================================================================================================
# Step-1. Importing Necessary Libraries
#===========================================================================================================================
import os     # to work with file paths and directories.
import re     # for regular expression operations, which help find specific text patterns in our .md files.


#===========================================================================================================================
# Step-2. Define the Path to our old .md Files
#===========================================================================================================================
directory_path = r"C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\docs\projects"


#===========================================================================================================================
# Step-3. Create a New Template
#===========================================================================================================================
new_template = """
# Title

Required

The name of the dataset

## Description:

Required

Background information about the dataset and its history

## Citations:

### Publication DOI

Required

[hyperlink]()

### Dataset DOI

Optional


[hyperlink]()

### Published Paper Citations

Required

[hyperlink]()

Insert Github GIF Link

## Earth Engine Snippet:

### Sample Code

Required

`Block Code`

**Link for sample code:** [Sample code]()

### Sample Application

Optional
[hyperlink]()

## License

Required

## Keywords

Required

## Date Created

Use the one given updated date

## Changelog

Optional

## Provider

Company's/Agency

## Curated in GEE by
Samapriya Roy
"""

#===========================================================================================================================
# Step 4: Extract Content from Old `.md` Files
#===========================================================================================================================
#Create a function that reads the old `.md` content and extracts parts of it.
def extract_content(old_md_content):
    extracted_content = {
        "title": "N/A",
        "description": "N/A",
        "earth_engine_snippet": "N/A",
        "usage": "Optional section not found",
        "sample_code": "N/A",
        "sample_application": "Optional section not found",
        "citations": "N/A",
        "license": "N/A",
        "keywords": "N/A",
        "created_provided": "N/A",
        "curated_by": "N/A"
    }
    
    # Define regular expressions for each section based on the old Markdown structure
    patterns = {
        "title": r"^# (.+)",
        "description": r"\n\n(.+?)\n\n####",
        "earth_engine_snippet": r"```js\n([\s\S]+?)\n```",
        "usage": r"#### Usage\n\n(.+)",
        "sample_code": r"Sample code: (https?:\/\/[\S]+)",
        "sample_application": r"#### Sample Application\n\n(.+)",
        "citations": r"#### Citation\n\n(.+)",
        "license": r"#### License\n\n(.+)",
        "keywords": r"Keywords: (.+)",
        "created_provided": r"Created & provided by: (.+)",
        "curated_by": r"Curated by: (.+)"
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, old_md_content, re.MULTILINE)
        if match:
            extracted_content[key] = match.group(1).strip()
        else:
            # If the section is not found, use the default value set in the dictionary
            continue
    
    return extracted_content



#===========================================================================================================================
# Step-5: Iterate Over Old .md Files and Create New Ones
#===========================================================================================================================
# Assuming the extract_content function is defined as per the previous step

# Directory path where the old .md files are located
directory_path = r"C:\Users\Saidhanya\INTERNSHIP\awesome-gee-community-datasets\docs\projects"

# New directory to save the updated .md files
# This path adds a subdirectory 'updated_md_files' to the original directory
new_directory_path = os.path.join(directory_path, "updated_md_files")
os.makedirs(new_directory_path, exist_ok=True)  # Creates the directory if it doesn't exist

# Loop through all the .md files in the original directory
for filename in os.listdir(directory_path):
    if filename.endswith(".md"):
        # Construct the full path to the current .md file
        old_file_path = os.path.join(directory_path, filename)
        
        # Read the old Markdown file content
        with open(old_file_path, 'r', encoding='utf-8') as file:
            old_md_content = file.read()

        # Use the extract_content function to get the content for the new template
        content = extract_content(old_md_content)

        # Populate the new Markdown template with the extracted content
        new_md_content = new_template.format(**content)  # **content unpacks the dictionary into the format function

        # Define the path for the new .md file within the new directory
        new_file_path = os.path.join(new_directory_path, filename)

        # Write the new Markdown content to the file
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(new_md_content)

        print(f"New file created: {new_file_path}")
