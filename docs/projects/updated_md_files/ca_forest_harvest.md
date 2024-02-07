
# Canada Landsat Derived Forest harvest disturbance 1985-2020

## Description:

The annual forest change data included in this product is national in scope (entire forested ecosystem) and represents the wall-to-wall
characterization of harvest in Canada at a 30-m spatial resolution. The information outcomes represent 36 years of harvest change over Canada’s
forests, derived from a single, consistent, spatially explicit data source, derived in a fully automated manner. This demonstrated capacity to
characterize forests at a resolution that captures human impacts is key to establishing a baseline for detailed monitoring of forested ecosystems
from management and science perspectives. Time series of Landsat data were used to characterize national trends in stand replacing forest
disturbances caused by wildfire and harvest for the period 1985–2020 for Canada's 650 Mha forested ecosystems.

Landsat data has a 30 m spatial resolution, so the change information is highly detailed and informative regarding both natural and human driven
changes. These data represent annual stand replacing forest changes. The stand replacing disturbance types labeled are wildfire and harvest, with
lower confidence wildfire and harvest, also shared. The distinction and sharing of lower class membership likelihoods is to indicate to users that
some change events were more difficult to allocate to a change type, but are generally found to be in the correct category. For an overview on the
data, image processing, and time series change detection methods applied, as well as information on independent accuracy assessment of the data, see
(Hermosilla et al. 2016). The data available is Change year for Harvest Events and [can be downloaded here](https://opendata.nfis.org/downloads/forest_change/CA_Forest_Harvest_1985-2020.zip)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

```
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., Campbell, L.B., 2016. Mass data processing of time series Landsat imagery:
pixels to data products for forest monitoring. International Journal of Digital Earth 9(11), 1035-1054.
```

![ca_forest_harvest_small](https://user-images.githubusercontent.com/6677629/215292086-0b98bb65-e49a-479e-9fd4-4422d49e426e.gif)

## Earth Engine Snippet:

### Sample Code
```js
var ca_forest_harvest = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_Forest_Harvest_1985-2020");
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FOREST-HARVEST-1985-2020)

### Sample Application

NA

## License

This work is licensed under and freely available to the public Open Government Licence - Canada.

## Keywords

Forest Harvest, Forest inventory, Land cover, Landsat, Machine learning

## Date Created

2023-01-28

## Changelog

NA

## Provider

Hermosilla et al. 2016

## Curated in GEE by
Samapriya Roy
