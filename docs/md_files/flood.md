
# Global large flood events : Dartmouth Flood Observatory (1985-2016)

## Description:

#### Abstract

The information presented highlights large flood events from 1985 to 2016 identified by the Dartmouth Flood Observatory. For more [information visit](https://floodobservatory.colorado.edu/Archives/index.html) . For mapping purposes, some types of flood events have been merged into one, under the "MAINCAUSEF" attribute. Please refer to the "MAINCAUSE" attribute for original data.

#### Data Quality
Each entry in the table and related "area affected" map outline represents a discrete flood event. However, repeated flooding in some regions is a complex phenomenon and may require a compromise between aggregating and dividing such events. The listing is comprehensive and global in scope. Deaths and damage estimates for tropical storms are totals from all causes, but tropical storms without significant river flooding are not included.
Supplemental Information

The information presented in the Dartmouth Flood Observatory Archive is derived from news, governmental, instrumental, and remote sensing sources. The archive is ""active"" because current events are added immediately.

## Citations:

### Publication DOI

NA

### Dataset DOI

NA

### Published Paper Citations

```
G.R.Brakenridge (2017). Global Active Archive of Large Flood Events.
Dartmouth Flood Observatory, University of Colorado.
```

Retrieved from https://floodobservatory.colorado.edu/Archives/index.html

![flood_events](https://user-images.githubusercontent.com/6677629/116651458-dfa7fd00-a948-11eb-9764-c93c8aa42771.gif)

## Earth Engine Snippet:

### Sample Code

```js
var flood_events = ee.FeatureCollection("projects/sat-io/open-datasets/events/large_flood_events_1985-2016")
```

**Link for sample code:** [Sample code](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/GLOBAL-LARGE-FLOOD-EVENTS)

### Sample Application

NA

## License

Unless otherwise specified, no restriction applies.

Source http://ihp-wins.unesco.org/layers/geonode:types_flood_events1

For additional information, visit: floodobservatory.colorado.edu/Archives/index.html

## Keywords

flood events, flood type, flood cause, Dartmouth Flood Observatory, Intergovernmental Hydrologic Programme

## Date Created

2021-04-29

## Changelog

NA

## Provider

NA

## Curated in GEE by
Samapriya Roy