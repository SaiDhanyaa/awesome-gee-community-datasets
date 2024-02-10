
# Continental-scale land cover mapping at 10 m resolution over Europe

## Description:

A land cover classification for Europe at 10 m resolution produced with a machine learning workflow driven by Sentinel optical and radar satellite imagery. The classification model was trained on land cover reference data form the LUCAS (Land Use/Cover Area frame Survey) dataset. The map represents conditions in 2018. You can read the [preprint here](https://arxiv.org/abs/2104.10922)

**The pixel values, their definitions and suggested hex color codes include:**

|Category|Land Cover Class        |Hex Code|
|:------:|:----------------------:|:------:|
|0       |not mapped              | #000000|
|1       |Artificial land         | #CC0303|
|2       |Cropland                | #CDB400|
|3       |Woodland                | #235123|
|4       |Shrubland               | #B76124|
|5       |Grassland               | #92AF1F|
|6       |Bare land               | #F7E174|
|7       |Water/permanent snow/ice| #2019A4|
|8       |Wetland                 | #AEC3D6|

## Citations:

### Publication DOI

NA

### Dataset DOI

```
Venter, Zander S., & Sydenham, Markus A.K. (2020). ELC10: European 10 m resolution land cover map 2018
(Version 01) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.4407051
```

### Published Paper Citations

```
Venter, Zander S., and Markus AK Sydenham. "Continental-scale land cover mapping at 10 m resolution
over Europe (ELC10)." arXiv preprint arXiv:2104.10922 (2021).
```


![elc10](https://user-images.githubusercontent.com/6677629/116647370-0150b680-a940-11eb-823f-b3c9a6bf9804.gif)

## Earth Engine Snippet:

### Sample Code

```js
var elc10= ee.ImageCollection("projects/sat-io/open-datasets/NINA/ELC10")
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/EUROPE-10m-LULC)

### Sample Application

NA
## License

Creative Commons Attribution-Share Alike 4.0 International License


## Keywords

land use, europe, land cover, remote sensing, copernicus, sentinel, satellite

## Date Created

2021-04-29

## Changelog

NA

## Provider

Venter, Zander S., & Sydenham, Markus A.K.

## Curated in GEE by
Samapriya Roy