
# Mapbiomas Annual land cover and use maps

## Description:

The Brazilian Annual Land Use and Land Cover Mapping Project is an initiative that involves a collaborative network of biomes, land use, remote sensing, GIS and computer science experts that rely on Google Earth Engine platform and its cloud processing and automated classifiers capabilities to generate Brazil’s annual land use and land cover time series. MapBiomas Project - is a multi-institutional initiative to generate annual land cover and use maps using automatic classification processes applied to satellite images. The complete description of the project can be [found here](http://mapbiomas.org).

Other regions such as Pan Amazonia, Indonesia, Bolivia , Peru and others were spun out of the work in Mapbiomas Brazil and as such these are also included in the current release

Scale: 30 m to 10m
Data Type: Multiple raster datasets and types

## Citations:

### Publication DOI

```
Souza at. al. (2020) - Reconstructing Three Decades of Land Use and Land Cover Changes in Brazilian Biomes with Landsat Archive and Earth Engine -
Remote Sensing, Volume 12, Issue 17, 10.3390/rs12172735 doi: 10.3390/rs12172735 https://doi.org/10.3390 /rs12172735
```

### Dataset DOI

```
"Project MapBiomas - Collection [version] of [region] Land Cover & Use Map Series, accessed on [date] through the link: [LINK]"
```

### Published Paper Citations

NA

## Earth Engine Snippet:
![MapBiomas](https://user-images.githubusercontent.com/6677629/81698669-5300e800-9434-11ea-9c5f-e8bf9588e737.gif)

### Sample Code


```js
//From collection 8
assets: {
    integration: 'projects/mapbiomas-workspace/public/collection8/mapbiomas_collection80_integration_v1',
    transitions: 'projects/mapbiomas-workspace/public/collection8/mapbiomas_collection80_transitions_v1',
    vectors: [
        'projects/mapbiomas-workspace/AUXILIAR/areas-protegidas',
        'projects/mapbiomas-workspace/AUXILIAR/municipios-2016',
        'projects/mapbiomas-workspace/AUXILIAR/estados-2017',
        'projects/mapbiomas-workspace/AUXILIAR/biomas-2019',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-1',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-2',
    ]
},
```

**Add repo link:** https://code.earthengine.google.com/?accept_repo=users/mapbiomas/user-toolkit

**Extra Info:** [GitHub Tutorial](https://github.com/mapbiomas-brazil/user-toolkit)

### Sample Application

NA

## License

All these datasets are shared under Creative Commons Attribution-Share Alike 4.0 International License

## Keywords

 Mapbiomas, Land Use, Land Cover

## Date Created

2023-10-14

## Changelog

* Catalog links updated to v8 and other regions were added
* Catalog links updated to v6 additional dataset links were added.

## Provider

Company's/Agency

## Curated in GEE by
[MapBiomas](https://mapbiomas.org/)