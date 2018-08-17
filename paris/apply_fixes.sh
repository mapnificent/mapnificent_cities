#!/bin/bash

set -ex

pushd data

unzip stif-822.zip -d stif-822

pushd stif-822

# Switch columns trip_headsign and trip_short_name
# The headsign in stif-822 contains the trip_id which DOES NOT "identifies the trip's destination"
# Converter creates unique trip-route for every trip, which results in no frequencies.
sed -i.bak s/,trip_headsign,trip_short_name,/,trip_short_name,trip_headsign,/g trips.txt
zip ../stif-822.zip *.txt

popd

rm -rf stif-822

popd
