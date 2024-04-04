import pandas as pd
import json
import os

# Load the CSV file
data = pd.read_csv('/mnt/data/New_organized_datasets.csv')

# Define the base URL and directory for saving the catalog
base_url = "https://data.cyverse.org/dav-anon/iplant/home/tswetnam/gee-community-catalog/stac/"
save_directory = "./stac_catalog/"
os.makedirs(save_directory, exist_ok=True)


root_catalog = {
    "type": "Catalog",
    "stac_version": "1.0.0",
    "id": "gee-community-catalog",
    "description": "A list of publicly available Google Earth Engine (GEE) assets curated in the Awesome GEE Community Catalog",
    "links": [
        {
            "rel": "self",
            "href": base_url + "catalog.json",
            "type": "application/json"
        }
    ],
    "title": "GEE Community Catalog"
}

# Save the root catalog
with open(os.path.join(save_directory, "catalog.json"), 'w') as f:
    json.dump(root_catalog, f, indent=4)



for index, row in data.iterrows():
    # Simplified handling for collection ID
    collection_id = row['Type'].lower().replace(" ", "_")
    collection_directory = os.path.join(save_directory, collection_id)
    os.makedirs(collection_directory, exist_ok=True)
    
    # Check if collection exists; if not, create it
    collection_path = os.path.join(collection_directory, "collection.json")
    if not os.path.exists(collection_path):
        collection = {
            "type": "Collection",
            "stac_version": "1.0.0",
            "id": collection_id,
            "description": f"Collection for {row['Type']}",
            "links": [
                {"rel": "root", "href": base_url + "catalog.json", "type": "application/json"},
                {"rel": "self", "href": base_url + f"{collection_id}/collection.json", "type": "application/json"}
            ],
            "title": row['Type']
        }
        
        # Update root catalog with new collection
        root_catalog['links'].append({
            "rel": "child",
            "href": collection['links'][1]['href'],
            "type": "application/json"
        })
        
        with open(collection_path, 'w') as f:
            json.dump(collection, f, indent=4)

    # Create item for each dataset
    item_id = f"item_{index}"
    item = {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": item_id,
        "properties": {
            "datetime": row.get('start_datetime', None),
            "end_datetime": row.get('end_datetime', None)
        },
        "geometry": json.loads(row.get('geometry', '{}')),
        "links": [
            {"rel": "parent", "href": base_url + f"{collection_id}/collection.json", "type": "application/json"}
        ],
        "assets": {
            "data": {"href": row['Sample Code'], "title": "Dataset Link"}
        }
    }
    
    item_path = os.path.join(collection_directory, f"{item_id}.json")
    with open(item_path, 'w') as f:
        json.dump(item, f, indent=4)

# Save the updated root catalog with all collections
with open(os.path.join(save_directory, "catalog.json"), 'w') as f:
    json.dump(root_catalog, f, indent=4)
