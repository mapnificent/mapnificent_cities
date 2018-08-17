#!/bin/bash

set -ex

DF=mountain-metropolitan-transit-374

pushd data

unzip $DF.zip -d $DF

pushd $DF

# Replace tabs in stops.txt with commas
sed -i.bak "s/	/,/g" stops.txt
sed -i.bak "s/stop_code,/stop_id,/" stops.txt
zip ../$DF.zip *.txt

popd

rm -rf $DF

popd
