import json
import re
from datetime import datetime
from typing import Dict, Any

def parse_markdown(md_content: str) -> Dict[str, Any]:
    """
    Parse the markdown content to extract necessary fields.
    
    Args:
    md_content (str): The content of the Markdown file.
    
    Returns:
    Dict[str, Any]: Parsed content organized in a dictionary.
    """
    parsed_data = {}

    # Extract title
    title_match = re.search(r'#\s+(.+)', md_content)
    parsed_data['title'] = title_match.group(1) if title_match else 'No Title'

    # Extract description
    description_match = re.search(r'## Description:\n\n(.+?)(?=\n##|\Z)', md_content, re.DOTALL)
    parsed_data['description'] = description_match.group(1).strip() if description_match else 'No Description'

    # Extract keywords
    keywords_match = re.search(r'## Keywords\n\n(.+?)(?=\n##|\Z)', md_content, re.DOTALL)
    parsed_data['keywords'] = [kw.strip() for kw in keywords_match.group(1).split(',')] if keywords_match else []

    # Extract date created
    date_created_match = re.search(r'## Date Created\n\n(.+?)(?=\n##|\Z)', md_content)
    parsed_data['date_created'] = date_created_match.group(1).strip() if date_created_match else datetime.now().strftime('%Y-%m-%d')

    # Extract provider
    provider_match = re.search(r'## Provider\n\n(.+?)(?=\n##|\Z)', md_content)
    parsed_data['provider'] = provider_match.group(1).strip() if provider_match else 'Unknown Provider'

    return parsed_data

def generate_stac_json(parsed_data: Dict[str, Any], template: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate the STAC JSON file from the parsed markdown data and template JSON.
    
    Args:
    parsed_data (Dict[str, Any]): Parsed content from the Markdown file.
    template (Dict[str, Any]): Template JSON.
    
    Returns:
    Dict[str, Any]: Generated STAC JSON.
    """
    stac_json = template.copy()
    
    # Update fields with extracted content
    stac_json['description'] = parsed_data.get('description', template['description'])
    stac_json['title'] = parsed_data.get('title', template['title'])
    stac_json['keywords'] = parsed_data.get('keywords', template['keywords'])
    
    # Update provider information
    if 'provider' in parsed_data:
        stac_json['providers'][0]['name'] = parsed_data['provider']
    
    # Update creation date
    if 'date_created' in parsed_data:
        date_created = datetime.strptime(parsed_data['date_created'], '%Y-%m-%d')
        stac_json['extent']['temporal']['interval'][0][0] = date_created.isoformat() + 'Z'
    
    # Specific updates for Carbon Mapper
    stac_json['id'] = 'CarbonMapper/Methane_Emissions'
    stac_json['gee:type'] = 'image_collection'
    stac_json['gee:terms_of_use'] = "Carbon Mapper data is provided for non-commercial purposes subject to the Modified Creative Commons Attribution ShareAlike 4.0 International Public License. All third-party use of the data is subject to the CC license at all times. The license details include terms for non-commercial use and share alike clauses. You can read the modified terms [here](https://carbonmapper.org/wp-content/uploads/2021/12/Carbon-Mapper-Modified-Creative-Commons-License-21-11-09.pdf)."
    stac_json['links'] = [
        {
            "href": "https://data.cyverse.org/dav-anon/iplant/home/dhanilu007/awesome-gee-community-datasets/catalog/projects/sat-io/open-datasets/carbon-mapper/carbon_mapper_stac.json",
            "rel": "self",
            "type": "application/json"
        },
        {
            "href": "https://data.cyverse.org/dav-anon/iplant/home/dhanilu007/awesome-gee-community-datasets/catalog/projects/sat-io/open-datasets/catalog.json",
            "rel": "root",
            "type": "application/json"
        },
        {
            "href": "https://data.cyverse.org/dav-anon/iplant/home/dhanilu007/awesome-gee-community-datasets/catalog/projects/sat-io/open-datasets/carbon-mapper/catalog.json",
            "rel": "parent",
            "type": "application/json"
        },
        {
            "code": "JavaScript",
            "href": "https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/CARBON-MAPPER-METHANE-EMISSIONS",
            "rel": "related",
            "title": "Run the example for Carbon Mapper Methane Emissions in the Earth Engine Code Editor",
            "type": "text/html"
        },
        {
            "href": "https://carbonmapper.org/our-mission/faq/",
            "rel": "license",
            "type": "text/html"
        }
    ]
    stac_json['sci:citation'] = "Please refer to the dataset's citations provided in the description section for appropriate use."
    stac_json['sci:doi'] = "NA"
    stac_json['platform'] = ["Airborne"]
    stac_json['instruments'] = ["AVIRIS-NG", "GAO"]

    return stac_json

def main(md_file_path: str, output_json_path: str):
    # Load the ASTER template JSON
    with open('aster_template.json', 'r') as file:
        template = json.load(file)
        
    # Read the markdown file content
    with open(md_file_path, 'r') as file:
        md_content = file.read()

    # Parse the markdown content
    parsed_data = parse_markdown(md_content)
    
    # Generate the STAC JSON file
    stac_json = generate_stac_json(parsed_data, template)
    
    # Save the generated JSON to a file
    with open(output_json_path, 'w') as json_file:
        json.dump(stac_json, json_file, indent=2)
    
    print(f'STAC JSON file generated successfully at {output_json_path}.')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_stac_json.py <input_md_file_path> <output_json_file_path>")
    else:
        main(sys.argv[1], sys.argv[2])
