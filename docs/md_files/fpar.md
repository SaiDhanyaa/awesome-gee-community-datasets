
# Sensor-Independent MODIS & VIIRS LAI/FPAR CDR 2000 to 2022

## Description:

This geospatial dataset encompasses crucial biophysical parameters, namely Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR), indispensable for characterizing terrestrial ecosystems. The dataset addresses the limitations observed in existing global LAI/FPAR products, including challenges related to spatial-temporal coherence and accuracy.

Drawing from a range of long-term global LAI/FPAR products, including MODIS&VIIRS, this dataset facilitates a comprehensive analysis of vegetation dynamics and their interplay with climate change. Developed as a Sensor-Independent (SI) LAI/FPAR Climate Data Record (CDR), this dataset is derived from Terra-MODIS, Aqua-MODIS, and VIIRS LAI/FPAR standard products.

Encompassing a substantial temporal scope spanning from 2000 to 2022, the SI LAI/FPAR CDR provides valuable insights at various spatial resolutions: 500 meters, 5 kilometers, and 0.05 degrees. Its temporal granularity includes 8-day intervals and bimonthly frequency. To facilitate diverse analyses and applications, this dataset is accessible in both sinusoidal and WGS1984 projections. It represents a comprehensive and refined resource for studying terrestrial ecosystems and their response to climate dynamics.

## Citations:

### Publication DOI

NA

### Dataset DOI

You can read the [paper here](https://essd.copernicus.org/articles/16/15/2024/)

```
Pu, J., Roy, S., Knyazikhin, Y., & Myneni, R. (2023). Sensor-Independent LAI/FPAR CDR [Data set]. In Sensor-independent LAI/
FPAR CDR: reconstructing a global sensor-independent climate data record of MODIS and VIIRS LAI/FPAR from 2000 to 2022 (Vol.
16, Number 1, pp. 15–34). Zenodo. https://doi.org/10.5281/zenodo.8076540
```

### Published Paper Citations

NA

![lai_fpar](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/28942045-9429-41a9-8836-9f398bac50ec)

## Earth Engine Snippet:

### Sample Code

```js
var wgs_500m_8d = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_500m_8d");
var wgs_5km_8d = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_5km_8d");
var wgs_005degree_8d = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_005degree_8d");
var wgs_500m_bimonthly = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_500m_bimonthly");
var wgs_5km_bimonthly = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_5km_bimonthly");
var wgs_005degree_bimonthly = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_005degree_bimonthly");
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LAI-FPAR-2000-2022)

### Sample Application

NA

## License

The dataset is under a Creative Commons Attribution 4.0 International.

## Keywords

Sensor-Independent, Leaf Area Index (LAI), Fraction of Photosynthetically Active Radiation (FPAR), Climate Dataset Record (CDR)

## Date Created

2023-06-09

## Changelog

NA

## Provider

Jiabin et al

## Curated in GEE by
Samapriya Roy