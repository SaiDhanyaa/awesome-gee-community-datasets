
# DEM France (Continental) 5m IGN RGE Alti

## Description:

The RGE ALTI® 5m dataset describes the ground elevation of France with a spatial resolution of 5x5m. It is produced by the National Institute of Geographic and Forest Information (IGN - https://www.ign.fr/).IGN or the National Institute for Geographic and Forest Information, is the State operator for geographic and forest information. The Institute intervenes in support of the evaluation and implementation of public risk prevention and regional planning policies The full dataset description is [available here](https://geoservices.ign.fr/documentation/donnees/alti/rgealti). The RGE ALTI® is updated from surveys obtained by airborne LIDAR or by correlation of aerial images. You can find the [dataset description here](https://geoservices.ign.fr/sites/default/files/2021-07/DC_RGEALTI_2-0.pdf). You can also find the Google Translated version of the [document in English here](https://github.com/microsoft/USBuildingFootprints/files/8786991/DL_RGEALTI_2-0_EN.pdf).

#### Dataset Preprocessing
The dataset was preprocessed by [Guillaume Attard](https://guillaumeattard.com/) from the ASCII files and converted into sub regional datasets. These images were then combined into a single Earth Engine image.

## Citations:

### Publication DOI

NA

### Dataset DOI

Additional information on license and citation guide can be [found here](https://www.etalab.gouv.fr/wp-content/uploads/2018/11/open-licence.pdf)

```
Ministry of xxx—Original data downloaded from http://www.data.gouv.fr/fr/ datasets/xxx/, updated on 14 February 2017.
```

### Published Paper Citations

NA

![rge_alti5](https://user-images.githubusercontent.com/6677629/170712928-9ad828de-85ef-4369-a877-3b328ba0693a.gif)

## Earth Engine Snippet:

### Sample Code

```js
var rge_alti5 = ee.Image("projects/sat-io/open-datasets/IGN_RGE_Alti_5m");
```
**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/IGN-RGE-France-DEM-5m)

### Sample Application

NA

## License

The dataset is licensed under a [Etalab Open License 2.0](https://spdx.org/licenses/etalab-2.0.html). The “Reuser” is free to reuse the “Information”
- to reproduce it, copy it,
- to adapt, modify, extract and transform it, to create "Derived Information", products or services,
- to communicate, distribute, redistribute, publish and transmit it,
- to exploit it for commercial purposes, for example by combining it with other information, or by including it in its own product or application.

## Keywords

digital elevation model, terrain, remote sensing, France

## Date Created

NA

## Changelog

NA

## Provider

National Institute of Geographic and Forest Information (IGN)

## Curated in GEE by
Guillaume Attard and Samapriya Roy