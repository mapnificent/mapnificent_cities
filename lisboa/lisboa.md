---
cityid: lisboa
cityname: Lisboa
# Center of the map when loaded
# Coordinates as [LNG, LAT] (like GeoJSON, NOT like leaflet)
# (the leading dash is NOT a minus sign, it's a list item)
coordinates:
- -9.139444
- 38.713889
description: 'Lisboa and suburban connections'
# Information was submitted to transitfeeds.com,
# ( https://github.com/TransitFeeds/TransitFeeds-Public/issues/created_by/adavidzh )
# but is not yet online
# tf_location_ids:
# - 169-berlin-germany
# Or provide GTFS files like so
gtfs:
  carris:
    # Transitfeeds.com feed id if available
    # tf_feed_id: verkehrsverbund-berlin-brandenburg/213
    # URL of Feed if tf_location_ids or tf_feed_id are not available
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/1/gtfs_1.zip
  rodoviaria_de_lisboa:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/61/gtfs_61.zip
  soflusa:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/14/gtfs_14.zip
  transtejo:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/4/gtfs_4.zip
  fertagus:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/13/gtfs_13.zip
  cp:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/3/gtfs_3.zip
  metro_lisboa:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/2/gtfs_2.zip
  tst:
    url: http://www.transporlis.pt/Portals/0/OpenData/gtfs/zip/11/gtfs_11.zip
    
version: 1
# Zoom level when loaded
zoom: 11
---

(c) [CARRIS](http://carris.pt)
(c) [TST](http://www.tsuldotejo.pt/)
(c) [RL](http://www.rodoviariadelisboa.pt/)
(c) [ML](http://www.metrolisboa.pt/)
(c) [CP](https://www.cp.pt/)
(c) [Fertagus](https://www.fertagus.pt/)
(c) [Transtejo e Soflusa](http://www.transtejo.pt/)
([Terms of Use](http://opendefinition.org/licenses/cc-zero/))
