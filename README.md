# Awesome GEE Community Datasets

This repository contains a curated set of geospatial datasets prepared for integration with Google Earth Engine (GEE) using the SpatioTemporal Asset Catalog (STAC) specification. The datasets are organized, processed, and documented to facilitate easy access, use, and sharing within the GEE community.

## Table of Contents
- [Overview](#overview)
- [What is STAC?](#what-is-stac)
- [Project Structure](#project-structure)
- [Creating Markdown Files](#creating-markdown-files)
- [Template Creation for Markdown Files](#template-creation-for-markdown-files)
- [Directory and Catalog Creation](#directory-and-catalog-creation)
- [Dataset Processing](#dataset-processing)
- [STAC JSON Generation](#stac-json-generation)
- [STAC Validation](#stac-validation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project is aimed at creating a structured, accessible, and standardized catalog of geospatial datasets that are compatible with Google Earth Engine. The datasets are organized using the STAC format, making them easily discoverable and usable in various geospatial analyses.

## What is STAC?
The SpatioTemporal Asset Catalog (STAC) is an emerging standard for indexing and discovering geospatial data. Developed to support cloud-native geospatial data, STAC provides a unified and flexible structure for describing geospatial assets. According to [Gillan Science](https://www.gillanscience.com/cloud-native-geospatial/stac/), STAC simplifies the process of making geospatial data accessible, interoperable, and ready for analysis in various platforms, particularly in cloud environments.

### Key Benefits of STAC:
- **Interoperability**: STAC's standardized structure ensures that data from different sources can be easily combined and used together.
- **Flexibility**: The modular design allows users to describe data ranging from simple imagery to complex spatio-temporal datasets.
- **Cloud-Native**: STAC is designed with cloud storage and processing in mind, making it ideal for modern geospatial workflows.
- **Discoverability**: By using STAC, datasets become more discoverable by a wide range of users and applications.

This project leverages the STAC format to organize datasets, ensuring that they are easily accessible for analysis in GEE and other geospatial platforms.

## Project Structure
The repository is organized into the following key components:

- `docs/`: Documentation related to dataset preparation, STAC creation, and usage guidelines.
- `scripts/`: Python scripts for processing datasets, generating STAC JSON files, and creating directory structures.
- `stac_catalog/`: The directory containing the final STAC Catalog, including Collections and Items in JSON format.
- `community_datasets.json`: The original dataset metadata file that served as the basis for STAC catalog generation.

## Creating Markdown Files
The initial step in the STAC catalog preparation involved creating markdown (.md) files for each dataset. These files contain structured metadata, including descriptions, spatial and temporal extents, dataset links, and other relevant information.

### Steps:
1. **Metadata Extraction**: Extract metadata from existing datasets, ensuring all necessary fields are included.
2. **Markdown Formatting**: Organize the metadata into markdown files with consistent headers and sections.

## Template Creation for Markdown Files
To standardize the metadata across multiple datasets, a template for the markdown files was created. This template ensures that all datasets follow the same structure and format, making it easier to manage and process them.

### Steps:
1. **Template Design**: Define the sections and fields required in the markdown files (e.g., title, description, spatial extent, temporal extent, links).
2. **Implementation**: Apply the template to all datasets, ensuring consistency across the markdown files.

## Directory and Catalog Creation
With the markdown files prepared, the next step was to create the necessary directories and catalogs for the STAC structure. This involved organizing the datasets into Collections and Items within the directory structure.

### Steps:
1. **Directory Structure**: Create directories that reflect the hierarchy of the STAC Catalog, including sub-directories for each Collection.
2. **Catalog Files**: Generate empty catalog files (`catalog.json`) for each directory to be filled with relevant metadata.

**Script Used**: [create_directories_and_catalogs.py](./scripts/create_directories_and_catalogs.py)

## Dataset Processing
The datasets were then processed to extract relevant information and prepare them for inclusion in the STAC Catalog. This step involved cleaning the data, extracting spatial and temporal extents, and ensuring compatibility with the STAC format.

### Steps:
1. **Data Cleaning**: Clean and preprocess the datasets to ensure they are ready for analysis.
2. **Extent Extraction**: Extract the spatial and temporal extents of each dataset for inclusion in the STAC metadata.

**Script Used**: [process_datasets.py](./scripts/process_datasets.py)

## STAC JSON Generation
The final step was to generate the STAC-compliant JSON files using a template JSON as a reference. Each dataset's metadata was mapped to the appropriate STAC fields, and the JSON files were created for each Collection and Item.

### Steps:
1. **Template Application**: Use the template JSON file to ensure consistency in the STAC fields across all datasets.
2. **JSON Generation**: Generate the STAC JSON files for each dataset, ensuring they include all required metadata.

**Script Used**: [generate_stac_json.py](./scripts/generate_stac_json.py)

**Template JSON Used**: [aster_template.json](./scripts/aster_template.json)

## STAC Validation
The STAC Catalog was validated using the Radiant Earth STAC Browser to ensure compliance with STAC specifications. This step was crucial in confirming that the catalog is correctly structured and fully compatible with STAC standards.

### Steps:
1. **Validation Process**: Load the generated STAC Catalog into the Radiant Earth STAC Browser.
2. **Review and Adjustments**: Review the catalog for any errors or inconsistencies. Make adjustments as needed to ensure full compliance.

**Status**: Version-1 of the catalog has been successfully validated.

## Usage
To access and use the STAC catalog:

1. **Navigate to the STAC Catalog**: Browse through the `stac_catalog/` directory to explore the available datasets.
2. **Load into GEE**: Use the provided STAC JSON files to load datasets into Google Earth Engine or other compatible platforms.

## Contributing
Contributions to this project are welcome! Please follow the standard fork-and-pull workflow:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
