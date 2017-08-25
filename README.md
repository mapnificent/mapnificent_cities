# Mapnificent cities

This repo contains data and meta data about all cities in [Mapnificent.net](http://www.mapnificent.net/). Metadata is stored in MarkDown files in the YAML Front matter and data is stored as Protocol Buffers in a `.bin` file.

## How to add a city.

In order to add a transit system to Mapnificent, [GTFS data](https://developers.google.com/transit/gtfs/) for that transit system needs to be available without charge under a license that allows its use with Mapnificent.

If the city is not yet in Mapnificent and please open an issue or – preferably – a pull request.

The issue will have a template that you need to fill out. The template is identical to the Markdown meta data and also reproduced below.

If you can, please create a pull request where the markdown file is already named correctly: `<cityid>/<cityid>.md`. This will make adding this city more convenient and thus faster.

You can use the following template:

```
---
cityid: example-city
cityname: Example City
# Center of the map when loaded
# Coordinates as [LNG, LAT] (like GeoJSON, NOT like leaflet)
# (the leading dash is NOT a minus sign, it's a list item)
coordinates:
- 13.369545
- 52.525592
description: ''
# Preferably provide a transitfeeds.com location ID, e.g.
tf_location_ids:
- 169-berlin-germany
# Or provide GTFS files like so
gtfs:
  example_feed_name:
    # Transitfeeds.com feed id if available
    tf_feed_id: verkehrsverbund-berlin-brandenburg/213
    # URL of Feed if tf_location_ids or tf_feed_id are not available
    url: https://transitfeeds.com/p/verkehrsverbund-berlin-brandenburg/213/latest/download
version: 1
# Zoom level when loaded
zoom: 12
---

(c) [Transit Agency Name](http://transitagency.example.org)
([Terms of Use](http://license.example.org))
```
