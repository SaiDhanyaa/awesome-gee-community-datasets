
# HydroLAKES v1.0

## Description:

Lakes are key components of biogeochemical and ecological processes, thus knowledge about their distribution, volume and residence time is crucial in understanding their properties and interactions within the Earth system. However, global information is scarce and inconsistent across spatial scales and regions. Here we develop a geo-statistical model to estimate the volume of global lakes with a surface area of at least 10 ha based on the surrounding terrain information.

The HydroLAKES database was designed as a digital map repository to include all lakes with a
surface area of at least 10 ha with a total surface area of 2.67 × 106 km2 (1.8% of global land area), a total shoreline length of 7.2 × 106 km (about four times longer than the world’s ocean coastline) and a total volume of 181.9 × 103 km3 (0.8% of total global non-frozen terrestrial water stocks). HydroLAKES aims to be as comprehensive and consistent as possible at a global scale and contains both freshwater and saline lakes, including the Caspian Sea, as well as human-made reservoirs and regulated lakes.

HydroLAKES is publicly available for download at http://www.hydrosheds.org and is free for scientific, educational, and other uses.

#### Datasets used for creation of HydroLAKES

|Original dataset                                                        |Region                                  |Original format  and resolution                                     |Reference                         |Number of lakes|
|------------------------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------|----------------------------------|---------------|
|Canadian hydrographic dataset (CanVec)                                  |Canada (entire country)                 |Vector; 1:50,000                                                    |Natural Resources Canada (2013)   |863550         |
|Shuttle Radar Topographic Mission (SRTM) Water Body Data (SWBD)         |56° South to 60° North                  |Raster; 1 arc-second (~30 m at the equator); vectorized and smoothed|Slater et al. (2006)              |282571         |
|MODerate resolution Imaging Spectro-radiometer (MODIS) MOD44W water mask|Russia above 60° North                  |Raster; 250 m;  vectorized and smoothed                             |Carroll et al. (2009)             |167435         |
|US National Hydrography Dataset (NHD)                                   |Alaska (entire state)                   |Vector; 1:24:000                                                    |U.S. Geological Survey (2013)     |58496          |
|European Catchments and Rivers Network System (ECRINS)                  |Europe above 60° North and entire Norway|Vector; varying resolutions (~1:250,000)                            |European Environment Agency (2012)|50699          |
|Global Lakes and Wetlands Database (GLWD)                               |World                                   |Vector; 1:1 million                                                 |Lehner and Döll (2004)            |3023           |
|Global Reservoir and Dam database (GRanD)                               |World                                   |Vector; varying resolutions (1:1 million or better)                 |Lehner et al. (2011)              |1133           |
|Other (own mapping)                                                     |World                                   |Vector; varying resolutions (1:1 million or better)                 |n/a                               |781            |
|Total                                                                   |                                        |                                                                    |                                  |1427688        |


#### Attribute table of HydroLAKES polygon and point layers

|Property |Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Hylak_id |Unique lake identifier. Values range from 1 to 1,427,688.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|Lake_name|Name of lake or reservoir. This field is currently only populated for lakes with an area of at least 500 km2; for large reservoirs where a name was available in the GRanD database; and for smaller lakes where a name was available in the GLWD database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|Country  |Country that the lake (or reservoir) is located in. International or transboundary lakes are assigned to the country in which its corresponding lake pour point is located and may be arbitrary for pour points that fall on country boundaries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|Continent|Continent that the lake (or reservoir) is located in. Geographic continent: Africa, Asia, Europe, North America, South America, or Oceania (Australia and Pacific Islands)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|Poly_src |Source of original lake polygon: CanVec; SWBD; MODIS; NHD; ECRINS; GLWD; GRanD; or Other More information on these data sources can be found in Table 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|Lake_type|Indicator for lake type: 1: Lake 2: Reservoir 3: Lake control (i.e. natural lake with regulation structure) Note that the default value for all water bodies is 1, and only those water bodies explicitly identified as other types (mostly based on information from the GRanD database) have other values; hence the type ‘Lake’ also includes all unidentified smaller human-made reservoirs and regulated lakes.                                                                                                                                                                                                                                                                                                          |
|Grand_id |ID of the corresponding reservoir in the GRanD database, or value 0 for no corresponding GRanD record. This field can be used to join additional attributes from the GRanD database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|Lake_area|Lake surface area (i.e. polygon area), in square kilometers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|Shore_len|Length of shoreline (i.e. polygon outline), in kilometers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|Shore_dev|Shoreline development, measured as the ratio between shoreline length and the circumference of a circle with the same area. A lake with the shape of a perfect circle has a shoreline development of 1, while higher values indicate increasing shoreline complexity.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|Vol_total|Total lake or reservoir volume, in million cubic meters (1 mcm = 0.001 km3). For most polygons, this value represents the total lake volume as estimated using the geostatistical modeling approach by Messager et al. (2016). However, where either a reported lake volume (for lakes ≥ 500 km2) or a reported reservoir volume (from GRanD database) existed, the total volume represents this reported value. In cases of regulated lakes, the total volume represents the larger value between reported reservoir and modeled or reported lake volume. Column ‘Vol_src’ provides additional information regarding these distinctions.                                                                                     |
|Vol_res  |Reported reservoir volume, or storage volume of added lake regulation, in million cubic meters (1 mcm = 0.001 km3). 0: no reservoir volume                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|Vol_src  |1:  ‘Vol_total’ is the reported total lake volume from literature 2:  ‘Vol_total’ is the reported total reservoir volume from GRanD or literature 3:  ‘Vol_total’ is the estimated total lake volume using the geostatistical modeling approach by Messager et al. (2016)                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|Depth_avg|Average lake depth, in meters. Average lake depth is defined as the ratio between total lake volume (‘Vol_total’) and lake area (‘Lake_area’).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|Dis_avg  |Average long-term discharge flowing through the lake, in cubic meters per second. This value is derived from modeled runoff and discharge estimates provided by the global hydrological model WaterGAP, downscaled to the 15 arc-second resolution of HydroSHEDS (see section 2.2 for more details) and is extracted at the location of the lake pour point. Note that these model estimates contain considerable uncertainty, in particular for very low flows. -9999: no data as lake pour point is not on HydroSHEDS landmask                                                                                                                                                                                              |
|Res_time |Average residence time of the lake water, in days. The average residence time is calculated as the ratio between total lake volume (‘Vol_total’) and average long-term discharge (‘Dis_avg’). Values below 0.1 are rounded up to 0.1 as shorter residence times seem implausible (and likely indicate model errors). -1: cannot be calculated as ‘Dis_avg’ is 0 -9999: no data as lake pour point is not on HydroSHEDS landmask                                                                                                                                                                                                                                                                                               |
|Elevation|Elevation of lake surface, in meters above sea level. This value was primarily derived from the EarthEnv-DEM90 digital elevation model at 90 m pixel resolution by calculating the majority pixel elevation found within the lake boundaries. To remove some artefacts inherent in this DEM for northern latitudes, all lake values that showed negative elevation for the area north of 60°N were substituted with results using the coarser GTOPO30 DEM of USGS at 1 km pixel resolution, which ensures land surfaces ≥0 in this region. Note that due to the remaining uncertainties in the EarthEnv-DEM90 some small negative values occur along the global ocean coastline south of 60°N which may or may not be correct.|
|Slope_100|Average slope within a 100 meter buffer around the lake polygon, in degrees. This value is derived from the EarthEnv-DEM90 digital elevation model at 90 m pixel resolution. Slopes for each pixel were computed with latitudinal corrections for the distortion in the XY spacing of geographic coordinates by approximating the geodesic distance between cell centers. For 12 lakes located above the northern limit of the EarthEnv-DEM90 digital elevation model (83°N), slopes were computed from the GTOPO30 DEM of USGS at 1 km pixel resolution. -1: slope values were not calculated for the largest lakes (polygon area ≥ 500 km2)                                                                                 |
|Wshd_area|Area of the watershed associated with the lake, in square kilometers. The watershed area is calculated by deriving and measuring the upstream contribution area to the lake pour point using the HydroSHEDS drainage network map at 15 arc-second resolution. -9999: no data as lake pour point is not on HydroSHEDS landmask                                                                                                                                                                                                                                                                                                                                                                                                 |
|Pour_long|Longitude of the lake pour point, in decimal degrees.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|Pour_lat |Latitude of the lake pour point, in decimal degrees.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

```
Messager, Mathis Loïc, Bernhard Lehner, Günther Grill, Irena Nedeva, and Oliver Schmitt. "Estimating the volume and
age of water stored in global lakes using a geo-statistical approach."
Nature communications 7, no. 1 (2016): 1-11.
```

You can read the paper here : https://www.nature.com/articles/ncomms13603?origin=ppub

![hydrolakes](https://user-images.githubusercontent.com/6677629/132138861-cbb35781-a412-4ded-b8f4-f0a5fe56cbbc.gif)


## Earth Engine Snippet:

### Sample Code

```js
var lake_poly = ee.FeatureCollection("projects/sat-io/open-datasets/HydroLakes/lake_poly_v10");
var lake_points = ee.FeatureCollection("projects/sat-io/open-datasets/HydroLakes/lake_points_v10");
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROLAKES)

### Sample Application

NA

## License

The data is licensed under a Creative Commons Attribution 4.0 International License (see section 4). By downloading and using the data the user agrees to the terms and conditions of this license.

## Keywords

water,hydrology, lakes, global lake surface, discharge, depth, volume, area, hydrolakes

## Date Created

2021-09-05

## Changelog

NA

## Provider

Messager, M. L., Lehner, B., Grill, G., Nedeva, I., & Schmitt, O

## Curated in GEE by
Samapriya Roy