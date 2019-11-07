---
cityid: thuringia
cityname: Thuringia
# Center of the map when loaded
# Coordinates as [LNG, LAT] (like GeoJSON, NOT like leaflet)
# (the leading dash is NOT a minus sign, it's a list item)
coordinates:
- 11.32487
- 50.99110
description: ''
# Preferably provide a transitfeeds.com location ID, e.g.
# tf_location_ids:
# - 169-berlin-germany
# Or provide GTFS files like so
gtfs:
  vmt:
    # Transitfeeds.com feed id if available
    # tf_feed_id: verkehrsverbund-berlin-brandenburg/213
    # URL of Feed if tf_location_ids or tf_feed_id are not available
    url: https://www.vmt-thueringen.de/fileadmin/user_upload/Open_Data/VMT_GTFS.zip
    # sha256: 883DAA9CBD57C2B13C9B5597C6C0D29D90C1C544D0C66F06CC8F8DD24E414DA0
version: 1
# Zoom level when loaded
zoom: 10
---

(c) [VMT GmbH](https://www.vmt-thueringen.de) ([CC BY-ND](https://creativecommons.org/licenses/by-nd/2.0/de/))
