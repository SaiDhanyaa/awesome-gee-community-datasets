
# Soil Organic Carbon Stocks & Trends South Africa

## Description:

Soil organic carbon (SOC) stocks (kg C m-2) are predicted over natural areas (excluding water, urban, and cultivated) of South Africa using a machine learning workflow driven by optical satellite data and other ancillary climatic, morphometric and biological covariates. The temporal scope covers 1984-2019. The spatial scope covers 0-30cm topsoil in South Africa natural land area (84% of the country). See methodology in [linked publication for details](https://www.sciencedirect.com/science/article/pii/S0048969721004526)

#### Dataset Details

Data are provided here at 30m spatial resolution in GeoTIFF files. There is a dataset for the long-term average SOC and trend in SOC. Each dataset is split into four files (suffix *_1, *_2 etc.) covering separate regions of South Africa for ease of download. The raster files are:

* "SOC_mean_30m..." - average of annual SOC predictions between 1984 and 2019. Values are expressed in kg C m-2
* "SOC_trend_30m..." - long-term trend in SOC derived from the Sens slope (M) across annual SOC values between 1984 and 2019. Pixel values (Y) are expressed as a percentage change over the 35 years relative to the long-term mean (X). Y = M / X * 100 * 35 years

*NB-All files are scaled by *100 and converted to floating data point to save space. To back-convert to original values, simply divide the raster values by 100.**

## Citations:

### Publication DOI

NA

### Dataset DOI

```
Venter, Zander S, Hawkins, Heidi-Jayne, Cramer, Michael D, & Mills, Anthony J. (2020). Soil organic
carbon stocks and trends (1984-2019) predicted at 30m spatial resolution for topsoil in natural areas
of South Africa (Version 01) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4384692
```

### Published Paper Citations

```
Venter, Zander S., Heidi-Jayne Hawkins, Michael D. Cramer, and Anthony J. Mills. "Mapping soil organic
carbon stocks and trends with satellite-driven high resolution maps over South Africa." Science of The
Total Environment 771 (2021): 145384.
```

![soc30](https://user-images.githubusercontent.com/6677629/116645849-4d016100-a93c-11eb-9d27-aa6556648674.gif)

## Earth Engine Snippet:

### Sample Code

```js
var SOC30_mean = ee.ImageCollection("projects/sat-io/open-datasets/NINA/SOC30_SA_mean");
var SOC30_trend = ee.ImageCollection("projects/sat-io/open-datasets/NINA/SOC30_SA_trend");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/SOIL-ORGANIC-CARBON-SA)

### Sample Application

NA

## License

Creative Commons Attribution-Share Alike 4.0 International License

## Keywords

carbon stocks, land degradation, natural climate solutions, remote sensing, soil mapping, spatial prediction, soil carbon, carbon sequestration

## Date Created

2021-04-29

## Changelog

NA

## Provider

Venter, Zander S, Hawkins, Heidi-Jayne, Cramer, Michael D, & Mills, Anthony J

## Curated in GEE by
Samapriya Roy