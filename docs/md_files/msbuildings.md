
# Global ML Building Footprints

## Description:

Bing Maps is releasing open building footprints around the world. We have detected 777M buildings from Bing Maps imagery between 2014 and 2021 including Maxar and Airbus imagery. For the sake of completeness datasets from earlier releases were included in this dataset and included. You can find the Github repo and more information about the [methodology here](https://github.com/microsoft/GlobalMLBuildingFootprints). Datasets are zipped and available as GeoJSON and GeoJSONL files from different regions. Additional information on preprocessing and some more context is available on the [blog here](https://medium.com/@samapriyaroy/microsoft-building-footprints-in-gee-revisiting-scale-accessibility-eee5e97c17a3)

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

#### Data preprocessing

The MSBuildings dataset that I have ingested into Google Earth Engine includes earlier releases apart from the 777 Million Global building footprints from Microsoft and in its final state stands at 1 Billion+ footprint (1,069,059,359). There are some interesting performance behaviors across Ingest. 

* While some datasets are released as GeoJSON some are released as Large GeoJSON format (GeoJSONL) and while the zipped sizes are large enough to limit the type of hardware the unzipped extracts are massive vector files. Hence the need to sort and split datasets.
* Ingest times are not necessarily linear across file sizes, seems a complex geometry can take longer to ingest though this is not a consistent enough generalization. 
* Extremely large datasets were split into smaller subsets and ingested. 
* Once the ingestion was completed sub-parts in a folder could be merged, flattened, and exported with varying degrees of success.




## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

NA

## Earth Engine Snippet:
![msbuildings_small](https://user-images.githubusercontent.com/6677629/171283064-28f4b19d-2356-4b42-aa90-5f6781a8695d.gif)
### Sample Code

All datasets are in the format

```js
var country  = ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/{country_name}');
```

for a list of all countries and assets use this

```js
var ee_folder = ee.data.listAssets("projects/sat-io/open-datasets/MSBuildings");
```

Here are some example setups for two countries

```js
var australia = ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/Australia');
var chile = ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/Chile')
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GLOBAL-ML-BUILDINGS)

### Sample Application

NA

## License

The datasets are released under the [Open Data Commons Open Database License](https://spdx.org/licenses/ODbL-1.0.html).

## Keywords

building footprint, machine learning, remote sensing, global

## Date Created

2022-05-30

## Changelog

NA

## Provider

Microsoft

## Curated in GEE by
Samapriya Roy