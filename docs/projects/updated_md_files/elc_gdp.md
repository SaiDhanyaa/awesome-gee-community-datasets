
# Global Electric Consumption revised GDP

## Description:

In this study, we employed a series of methods, such as a particle swarm optimization-back propagation (PSO-BP) algorithm, to unify the scales of DMSP/OLS and NPP/VIIRS images and obtain continuous 1 km × 1 km gridded nighttime light data during 1992–2019. Subsequently, from a revised real growth perspective, we employed a top-down method to calculate global 1 km × 1 km gridded revised real GDP and electricity consumption during 1992–2019 based on our calibrated nighttime light data.

Gridded population and nighttime light data are the most popular proxy tools, and have been adopted extensively because of their strong correlation with economic output and electricity use. Finally the authors note that although nighttime light data as a single indicator may ignore factors such as value added or reduced by forestry or desertification, it is still an effective proxy for calibrating economic growth.You can [read the paper here](https://www.nature.com/articles/s41597-022-01322-5)

**Disclaimer:** Whole or parts of the dataset description were provided by the author(s) or their works.

## Citations:

### Publication DOI

Required

[hyperlink]()

### Dataset DOI

```
Chen, Jiandong; Gao, Ming (2021): Global 1 km × 1 km gridded revised real gross domestic product and electricity consumption during 1992-2019 based
on calibrated nighttime light data. figshare. Dataset. https://doi.org/10.6084/m9.figshare.17004523.v1
```
#### Dataset units

* GDP: Millions of 2017 US dollars
* Electricity consumption: Kilowatt hours


### Published Paper Citations

```
Chen, J., Gao, M., Cheng, S., Hou, W., Song, M., Liu, X., & Liu, Y. (2022). Global 1 km× 1 km gridded revised real gross domestic product and
electricity consumption during 1992–2019 based on calibrated nighttime light data. Scientific Data, 9(1), 1-14. https://doi.org/10.1038/
s41597-022-01322-5
```

![gridded_elc](https://user-images.githubusercontent.com/6677629/193526866-f5c333b1-921d-4258-ab89-fe5a1ea584aa.gif)


## Earth Engine Snippet:

### Sample Code

**1. GRIDDED Electricity Consumption:**

```js
var global_ec = ee.ImageCollection("projects/sat-io/open-datasets/GRIDDED_EC");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GRIDDED-ELECTRICITY-CONSUMPTION)

![gridded_gdp](https://user-images.githubusercontent.com/6677629/193526833-9714b5e5-80b1-4665-8a86-0fe448d315be.gif)

**2. GRIDDED GDP based on Electricity Consumption:**

```js
var global_elc_gdp = ee.ImageCollection("projects/sat-io/open-datasets/GRIDDED_EC-GDP");
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GRIDDED-ELECTRICITY-CONSUMPTION-GDP)


### Sample Application

NA
## License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.


## Keywords

GDP, Electricity Consumption, Night Lights

## Date Created

Use the one given updated date

## Changelog

2022-09-27

## Provider

NA

## Curated in GEE by
Samapriya Roy
