
# Emergency Observation Data for the 2024 Sea of Japan Earthquake

## Description:

The 2024 Sea of Japan earthquake occurred on January 1, 2024, after 4:00 PM (Japan time), resulting in significant damage,
including building collapses, landslides, and fires at various locations. In response to requests from domestic disaster
prevention agencies, JAXA conducted emergency observations using ALOS-2 from the night of the disaster. The released data
includes Level 2.1 (GeoTIFF) and archive data, facilitating interference analysis and change detection to contribute to
disaster reduction and prevention. Notably, this publicly released data is intended for non-commercial purposes, including
government and local authority use, as well as research by universities.

#### Dataset preprocessing
Additional metadata was added to the images in the collection. Field names such as system:time_start and system:time_end were added to make the collection filterable in Google Earth Engine. Custom code was written for ingest into Google Earth Engine and a no data value of 0 was used for masking.


## Citations:

### Publication DOI

NA
### Dataset DOI

URL: https://www.eorc.jaxa.jp/ALOS/jp/dataset/alos_open_and_free_j.htm#Noto2024

For citation details, please refer to the above URL

### Published Paper Citations
NA

![jp_eq_2024](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/4e60eb7a-8fe1-411e-9e91-0ab988fe9936)

## Earth Engine Snippet:

### Sample Code

```js
var notoPeninsula = ee.ImageCollection("projects/sat-io/open-datasets/disaster/japan-earthquake-2024_ALOS");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/SEA-OF-JAPAN-EQ-2024)

### Sample Application

NA

## License

This publicly released data is intended for non-commercial purposes, including government and local authority use, as well as
research by universities.

Please note the terms of use: https://global.jaxa.jp/policy.html

 - CC-BY-NC-4.0
 - CC-BY-NC-SA-4.0

## Keywords

 Emergency Data, ALOS, JAPAN, Earthquake

## Date Created

2024-01-06

## Changelog

NA

## Provider

Japan Aerospace Exploration Agency (JAXA)

## Curated in GEE by
Samapriya Roy and Keiko Nomura