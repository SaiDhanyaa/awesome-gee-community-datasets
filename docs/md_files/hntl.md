
# Harmonized Global Night Time Lights (1992-2021)

## Description:

In this study, the authors generated an integrated and consistent NTL dataset at the global scale by harmonizing the inter-calibrated NTL observations from the DMSP data and the simulated DMSP-like NTL observations from the VIIRS data. The generated global DMSP NTL time-series data (1992–2018) show consistent temporal trends. This temporally extended DMSP NTL dataset provides valuable support for various studies related to human activities such as electricity consumption and urban extent dynamics. The dataset contains

1. Temporally calibrated DMSP-OLS NTL time series data from 1992-2013; and
2. Converted NTL time series from the VIIRS data (2014-2021)

Spatial resolution: 30 arc-seconds (~1km)

**The authors suggest using pixels with DN values greater than 7.**

You can [read the paper here](https://www.nature.com/articles/s41597-020-0510-y#Sec8)

You can [download the datasets here](https://figshare.com/articles/dataset/Harmonization_of_DMSP_and_VIIRS_nighttime_light_data_from_1992-2018_at_the_global_scale/9828827/5)

## Citations:

### Publication DOI

NA

### Dataset DOI

```
Li, Xuecao; Zhou, Yuyu; zhao, Min; Zhao, Xia (2020): Harmonization of DMSP and VIIRS nighttime
light data from 1992-2020 at the global scale. figshare. Dataset.
https://doi.org/10.6084/m9.figshare.9828827.v5
```

### Published Paper Citations

```
Li, Xuecao, Yuyu Zhou, Min Zhao, and Xia Zhao. "A harmonized global nighttime light dataset 1992–2018." Scientific data 7, no. 1 (2020): 1-9.
```

![NTL](https://user-images.githubusercontent.com/6677629/143602333-14726b3e-7bbe-4b83-a283-7cb11cbf8ecb.gif)


## Earth Engine Snippet:

### Sample Code

```js
var dmsp = ee.ImageCollection("projects/sat-io/open-datasets/Harmonized_NTL/dmsp");
var viirs = ee.ImageCollection("projects/sat-io/open-datasets/Harmonized_NTL/viirs");
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/HARMONIZED-GLOBAL-NTL)

### Sample Application

NA

## License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

## Keywords

DMSP/OLS data, VIIRS, nighttime light, calibration, consistent, global

## Date Created

2023-09-22

## Changelog

* Updated to v7 now included 2021 VIIRS datatset

## Provider

Xuecao Li et al

## Curated in GEE by
Samapriya Roy