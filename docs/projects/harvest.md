
# NASA Harvest Layers

## Description:

This page includes studies and geospatial layers made available as a result of publications from the NASA Harvest group members and made available in Google Earth Engine. This will be updated as newer and updated studies get published.

## Rapid Response Crop Maps in Data Sparse Regions

We present a method for rapid mapping of croplands in regions where little to no ground data is available. We present results for this method in Togo, where we delivered a high-resolution (10 m) cropland map in under 10 days to facilitate rapid response to the COVID-19 pandemic by the Togolese government. This demonstrated a successful transition of machine learning applications research to operational rapid response in a real humanitarian crisis. All maps, data, and code are publicly available to enable future
research and operational systems in data-sparse regions. [Read the paper here](https://arxiv.org/pdf/2006.16866.pdf)

## Annual and in-season mapping of cropland at field scale with sparse labels

Previously, we developed a method for binary classification of cropland that learns from sparse local labels and abundant global labels using a multi-headed LSTM and timeseries multispectral satellite inputs over one year. In this work, we present a new method that uses an autoregressive LSTM to classify cropland during the growing season (i.e., partially-observed time series). We used these methods to produce publicly-available 10m-resolution cropland maps in Kenya for the 2019-2020 and 2020-2021 growing seasons. These are the highest-resolution and most recent cropland maps publicly available for Kenya. These methods and associated maps are critical for scientific studies and decision-making at the intersection of food security and climate change. [Read the paper here](https://www.climatechange.ai/papers/neurips2020/29/paper.pdf)


![kenya_binary_probability](https://user-images.githubusercontent.com/6677629/116005494-cdd2fc80-a5cc-11eb-8d2d-eec240680174.gif)

## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

```
Hannah Kerner, Gabriel Tseng, Inbal Becker-Reshef, Catherine Nakalembe,Brian Barker, Blake Munshell,
Madhava Paliyam, and Mehdi Hosseini. 2020.Rapid Response Crop Maps in Data Sparse Regions.
KDD ’20: ACMSIGKDDConference on Knowledge Discovery and Data Mining Workshops, August22–27, 2020, San Diego, CA.
```

![togo_binary_probability](https://user-images.githubusercontent.com/6677629/116005416-6a48cf00-a5cc-11eb-8938-2fd5e3e907f8.gif)

## Earth Engine Snippet:

### Sample Code

```js
var togo_cropland_binary = ee.Image("projects/sat-io/open-datasets/nasa-harvest/togo_cropland_binary");
var togo_cropland_probability = ee.Image("projects/sat-io/open-datasets/nasa-harvest/togo_cropland_probability");
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/NASA-HARVEST-CROPLAND
)


```js
var kenya_cropland_binary = ee.Image("projects/sat-io/open-datasets/nasa-harvest/kenya_cropland_binary");
var kenya_cropland_probability = ee.Image("projects/sat-io/open-datasets/nasa-harvest/kenya_2019_cropland_probability");
var busia_cropland_probability = ee.Image("projects/sat-io/open-datasets/nasa-harvest/busia_cropland_probability");
var busia_cropland_binary = ee.Image("projects/sat-io/open-datasets/nasa-harvest/busia_cropland_binary");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/NASA-HARVEST-CROPLAND)

### Sample Application

NA

## License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

## Keywords

agriculture, Africa, Togo, crops, crop classification, food security, satellite data, Earth observation, GIS

## Date Created

2021-04-25

## Changelog

NA

## Provider

NA

## Curated in GEE by
Samapriya Roy