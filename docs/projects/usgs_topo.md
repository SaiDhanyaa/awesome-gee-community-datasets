
# USGS Historical Topo Maps

## Description:

The history of USGS Topo Maps traces back to the late 19th century when the USGS embarked on a mission to map the entire United States in intricate detail. The 1:24,000 scale, also known as 7.5-minute quadrangle maps, emerged as one of the most widely used scales. Each map sheet covers an area of 7.5 minutes of longitude and latitude, resulting in a detailed representation of approximately 64 square miles (166 square kilometers).

A subset of these are ingested into the overall collection about 81,000+ and improvements and additions will be made in the future. Metadata including state name, place name and scale. States like Texas, California and others were not added directly but might be added over time.

You can read about the [preprocessing steps here](https://samapriyaroy.medium.com/from-paper-to-pixels-rediscovering-historical-usgs-topo-maps-in-the-google-earth-engine-community-f514c97c46a)

## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

```
United States Geological Survey. (2019). Yosemite National Park [Topographic map, Map No. 12345]. 1:24,000. U.S. Geological Survey.
```

![USGS topo](https://i.imgur.com/27YEevwh.gif)

## Earth Engine Snippet:

### Sample Code

```js
var usgs_topo = ee.ImageCollection("projects/sat-io/open-datasets/USGS/historical_topo");
var map_index = ee.FeatureCollection("projects/sat-io/open-datasets/USGS/TOPO_24K_MAPINDEX");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/USGS-TOPO-RENDER)

### Sample Application

NA

## License

USGS topographic maps are typically in the public domain, which means they are not protected by copyright and can be freely used, reproduced, and distributed. The USGS allows the public to access and use its maps for various purposes without the need for a formal license or permission.

## Keywords

USGS, Historical Topographical Maps, Orthophoto mosaics, Topography,Cartography

## Date Created

2023-11-25

## Changelog

NA

## Provider

USGS

## Curated in GEE by
Samapriya Roy
