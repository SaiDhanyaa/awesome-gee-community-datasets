
# Mississippi River Basin Floodplain Land Use Change (1941-2000)

## Description:

A comprehensive dataset quantifying floodplain land use change along the 3.3 million km2 Mississippi River Basin (MRB) covering 60 years (1941–2000) at 250-m resolution.

## Citations:

### Publication DOI

NA

### Dataset DOI

```
Rajib, A., Zheng, Q., Golden, H.E, Wu, Q., Lane, C.R., Christensen, J.R., Morrison, R.R., Annis, A., & Nardi, F.  (2021). The changing face of
floodplains in the Mississippi River Basin detected by a 60-year land use change dataset. _Scientific Data_, 8, 271.
https://doi.org/10.1038/s41597-021-01048-w
```

### Published Paper Citations

NA

![](https://i.imgur.com/xf26OdK.png)

## Earth Engine Snippet:

### Sample Code

```js

var MRB_boundary = ee.FeatureCollection('users/giswqs/MRB/MRB_Boundary');
var floodplain = ee.Image('users/giswqs/MRB/USGS_Floodplain');
var img_1950 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1950');
var img_1960 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1960');
var img_1970 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1970');
var img_1980 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1980');
var img_1990 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1990');
var img_2000 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_2000');

```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/e982f11b610438862eb908e22c2cc088)

### Sample Application

Earth Engine App: https://giswqs.users.earthengine.app/view/mrb-floodplain


## License

This dataset is shared under a Creative Commons Attribution-Share Alike 4.0 International License

## Keywords

land use, floodplain, Mississippi River Basin, hydrology, river basin, ecysostems

## Date Created

October 2021

## Changelog

NA

## Provider

Rajib et al 2021

## Curated in GEE by
Qiusheng Wu