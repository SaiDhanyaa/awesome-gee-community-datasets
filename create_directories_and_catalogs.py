import os
import csv
import json

def load_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_stac_catalog(directory, dataset):
    stac_catalog = {
        "stac_version": "1.0.0",
        "id": dataset['id'].split('/')[-1],  # Use the last part of the ID as the catalog ID
        "description": f"STAC catalog for {dataset['id'].split('/')[-1]}",
        "type": "Collection",
        "license": "CC-BY-4.0",
        "links": [],
        "extent": {
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [["2016-01-01T00:00:00Z", None]]}
        }
    }
    with open(os.path.join(directory, 'catalog.json'), 'w') as file:
        json.dump(stac_catalog, file, indent=4)
    print(f"STAC catalog created at {directory}")

def process_datasets(filepath, base_dir):
    data = load_csv(filepath)
    for dataset in data:
        path_segments = dataset['id'].split('/')
        if len(path_segments) > 1:
            category_dir = os.path.join(base_dir, *path_segments)  # Build full directory path
            ensure_dir(category_dir)
            generate_stac_catalog(category_dir, dataset)

base_directory_path = '/Users/dhanyapriyas/Downloads/INTERNSHIP/awesome-gee-community-datasets'  # Base directory for the datasets
csv_file_path = os.path.join(base_directory_path, 'community_datasets.csv')  # Full path to the CSV file

process_datasets(csv_file_path, base_directory_path)
