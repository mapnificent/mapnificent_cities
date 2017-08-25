```
---
cityid: example-city
cityname: Example City
# Center of the map when loaded
# Coordinates as lat lng (the leading dash is NOT a minus sign, it's a list item)
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
    url: https://transitfeeds.com/p/verkehrsverbund-berlin-brandenburg/213/latest/download
version: 1
# Zoom level when loaded
zoom: 12
---

(c) [Transit Agency Name](http://transitagency.example.org)
([Terms of Use](http://license.example.org))
```
