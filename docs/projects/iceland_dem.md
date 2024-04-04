
# ÍslandsDEM v1.0 10m

## Description:

Since 2015, elevation data from the Arctic (north of 60°N, including Iceland) started to be openly available through the ArcticDEM project, led by the Polar Geospatial Center, University of Minnesota (https://www.pgc.umn.edu/data/arcticdem/).

This data consists of a large amount of Digital Elevation Models (DEMs) repeatedly acquired (multitemporal), typically from 2012-present, and the oldest data reaching back to 2008. The DEMs are derived from satellite sub-meter stereo imagery, particularly from WorldView 1-3 and GeoEye-1. The processing of the DEMs was done using SETSM, an open-source digital photogrammetric software, in the Bluewaters supercomputer (University of Ilinois). Each DEM has 2x2m resolution and a footprint of ~18x100km.

In a collaborative effort between the National Land Survey of Iceland, the Icelandic Meteorological Office and the Polar Geospatial Center, we developed methods to handle and process a large amount of data available for Iceland. The methods developed consisted of

* Spatial adjustment of all the available DEMs, for homogeneity and consistency in the location of each individual DEM.

* Robust mosaicking into one single DEM of Iceland, by taking advantage of the multi-temporal coverage of DEMs. Each pixel of the mosaic corresponds to a median elevation value from the possible elevations available from the ArcticDEM. More details on the dataset [available here](https://gatt.lmi.is/geonetwork/srv/eng/catalog.search#/metadata/e6712430-a63c-4ae5-9158-c89d16da6361). This DEM is resampled for 10x10m resolution.

## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

NA

![iceland_dem](https://user-images.githubusercontent.com/6677629/168207259-0ecfd923-91be-43ae-8747-7064e48b09d0.gif)

## Earth Engine Snippet:

### Sample Code

```js
var DEM_10m_isn93 = ee.Image("projects/ee-landmaelingar/assets/IslandsDEMv1_10m_isn93")
```

Projection used: EPSG 3057 (ISN93/Lambert 1993)

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/ICELAND-DEM-10m)

### Sample Application

NA

## License

The datasets are distributed under a Attribution 4.0 International (CC BY 4.0) license.

## Keywords

Elevation, DEM, ArticDEM, Iceland, Geophysical

## Date Created

2022-03-29

## Changelog

NA

## Provider

National Land Survey of Iceland & PGC

## Curated in GEE by
National Land Survey of Iceland