import os
import csv
import json
import re

def load_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))
    print(f"Loaded {len(data)} records from the CSV file.")
    return data

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    print(f"Directory checked or created: {directory}")

def parse_md_file(md_file_path):
    if not os.path.exists(md_file_path):
        print(f"Markdown file not found: {md_file_path}")
        return {'title': 'File Not Found', 'description': 'Description not available'}
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    title = re.search(r'^#\s*(.*)$', content, re.MULTILINE)
    description = re.search(r'^## Description:\n\n([^#]*)', content, re.MULTILINE | re.DOTALL)
    return {
        'title': title.group(1) if title else 'No Title Found',
        'description': description.group(1).strip() if description else 'No Description Found'
    }

def create_stac_files(directory, metadata, dataset_id):
    catalog_path = os.path.join(directory, f'{dataset_id}-catalog.json')
    collection_path = os.path.join(directory, f'{dataset_id}-collection.json')
    catalog = {
        "stac_version": "1.0.0",
        "id": f"{dataset_id}-catalog",
        "description": f"Catalog for {metadata['title']}",
        "type": "Catalog",
        "links": [{"rel": "self", "href": f"./{dataset_id}-catalog.json"}]
    }
    collection = {
        "stac_version": "1.0.0",
        "id": f"{dataset_id}-collection",
        "title": metadata['title'],
        "description": metadata['description'],
        "license": "CC-BY-4.0",
        "extent": {
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [["2016-01-01T00:00:00Z", None]]}
        },
        "links": [{"rel": "self", "href": f"./{dataset_id}-collection.json"}]
    }
    with open(catalog_path, 'w') as file:
        json.dump(catalog, file, indent=4)
    with open(collection_path, 'w') as file:
        json.dump(collection, file, indent=4)
    print(f"Catalog and Collection JSONs created for {dataset_id}")

def process_datasets(filepath, base_dir):
    data = load_csv(filepath)
    for dataset in data:
        full_md_path = os.path.join(base_dir, dataset['id'] + '.md')
        print(f"Processing: {full_md_path}")
        if os.path.exists(full_md_path):
            metadata = parse_md_file(full_md_path)
            directory = os.path.dirname(full_md_path)
            dataset_id = os.path.basename(dataset['id'])
            create_stac_files(directory, metadata, dataset_id)
        else:
            print(f"Markdown file does not exist: {full_md_path}")

# Define paths
csv_file_path = '/Users/dhanyapriyas/Downloads/INTERNSHIP/awesome-gee-community-datasets/community_datasets.csv'
markdown_files_path = '/Users/dhanyapriyas/Downloads/INTERNSHIP/awesome-gee-community-datasets/docs/md_files'  # Updated path to markdown files

# Process the datasets
process_datasets(csv_file_path, markdown_files_path)

