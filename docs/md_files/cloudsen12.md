
# CloudSEN12 - Global dataset for semantic understanding of cloud and cloud shadow in Sentinel-2

## Description:

CloudSEN12 is a large dataset for cloud semantic understanding that consists of 9880 regions of interest (ROIs) that consists of 49,400 image patches (IP) that are evenly spread throughout all continents except Antarctica. Each IP covers 5090 x 5090 meters and contains data from Sentinel-2 levels 1C and 2A, hand-crafted annotations of thick and thin clouds and cloud shadows, Sentinel-1 Synthetic Aperture Radar (SAR), digital elevation model, surface water occurrence, land cover classes, and cloud mask results from six cutting-edge cloud detection algorithms. Each ROI has five 5090x5090 meters image patches (IPs) collected on different dates that match one of the following cloud cover groups:

- clear (0%)

- low-cloudy (1% - 25%)

- almost clear (25% - 45%)

- mid-cloudy (45% - 65%)

- cloudy (65% >)

 The dataset is available [here](https://shorturl.at/cgjtz). For more details [check out the website](https://cloudsen12.github.io/) and you can read the preprint of the [paper here](https://eartharxiv.org/repository/view/3615/)

## Citations:

### Publication DOI

NA

### Dataset DOI

```
Aybar, C. et al. CloudSEN12 - a global dataset for semantic understanding of cloud and cloud shadow in Sentinel-2.
Science Data Bank https://doi.org/10.57760/sciencedb.06669 (2022).
```

### Published Paper Citations

```
Aybar, C., Ysuhuaylas, L., Loja, J. et al. CloudSEN12, a global dataset for semantic understanding of cloud and cloud shadow in Sentinel-2.Sci Data 9, 782 (2022). https://doi.org/10.1038/s41597-022-01878-2
```

<center>
<img src=https://user-images.githubusercontent.com/16768318/190843651-c8182d07-a49e-4524-be16-2eb38fe9cdc8.png>
</center>

## Earth Engine Snippet:

### Sample Code
#### Hand-crafted labels - high-quality

```js
var cs12_high = ee.ImageCollection("projects/sat-io/open-datasets/cloudsen12/high");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/CloudSEN12-HIGH-QUALITY)

#### Hand-crafted labels - scribble

```js
var cs12_scribble = ee.ImageCollection("projects/sat-io/open-datasets/cloudsen12/scribble");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/CloudSEN12-SCRIBBLE-QUALITY)


#### Hand-crafted labels - nolabel

```js
var cs12_nolabel = ee.ImageCollection("projects/sat-io/open-datasets/cloudsen12/nolabel");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/CloudSEN12-NO-LABEL)


#### IPs footprint

```
var cs12_geom = ee.ImageCollection("projects/sat-io/open-datasets/cloudsen12/footprint");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/CloudSEN12-FOOTPRINT)


### Sample Application

NA

## License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

## Keywords

cloud, deep learning, Sentinel-2, Sentinel-1, U-Net

## Date Created

2022-09-18

## Changelog

NA

## Provider

NA

## Curated in GEE by
Samapriya Roy
