## COMBO DATA

### COUNTY

xsv select '!WKT' USBB_05302019_county_fcc_mlab_2014_2017.csv | \
  xsv stats | \
  xsv select type | \
  tail -n +2 | \
  sed 's/.*/"&"/' | \
  sed 's/Unicode/String/g' | \
  sed 's/Float/Real/g' | \
  tr '\n' , > USBB_05302019_county_fcc_mlab_2014_2017.csvt

  echo '"WKT"' >> USBB_05302019_county_fcc_mlab_2014_2017.csvt

ogr2ogr -f GeoJSON /dev/stdout -oo KEEP_GEOM_COLUMNS=no USBB_05302019_county_fcc_mlab_2014_2017.csv | tippecanoe -o usbb_county.mbtiles -f -l usbb_county /dev/stdin -z6 --simplification=10 --detect-shared-borders --coalesce-densest-as-needed

### TRACT

xsv select '!WKT' USBB_05302019_ct_mlab_fcc_2014_2017.csv | \
  xsv stats | \
  xsv select type | \
  tail -n +2 | \
  sed 's/.*/"&"/' | \
  sed 's/Unicode/String/g' | \
  sed 's/Float/Real/g' | \
  tr '\n' , > USBB_05302019_ct_mlab_fcc_2014_2017.csvt

  echo '"WKT"' >> USBB_05302019_ct_mlab_fcc_2014_2017.csvt

ogr2ogr -f GeoJSON /dev/stdout -oo KEEP_GEOM_COLUMNS=no USBB_05302019_ct_mlab_fcc_2014_2017.csv | tippecanoe -o usbb_tract.mbtiles -f -l usbb_tract /dev/stdin -z6 --simplification=10 --detect-shared-borders --coalesce-densest-as-needed

### ZCTA

xsv select '!WKT' USBB_05282019_zcta_fcc_mlab_2014_2018.csv | \
  xsv stats | \
  xsv select type | \
  tail -n +2 | \
  sed 's/.*/"&"/' | \
  sed 's/Unicode/String/g' | \
  sed 's/Float/Real/g' | \
  tr '\n' , > USBB_05282019_zcta_fcc_mlab_2014_2018.csvt

  echo '"WKT"' >> USBB_05282019_zcta_fcc_mlab_2014_2018.csvt

ogr2ogr -f GeoJSON /dev/stdout -oo KEEP_GEOM_COLUMNS=no USBB_05282019_zcta_fcc_mlab_2014_2018.csv | tippecanoe -o usbb_zcta.mbtiles -f -l usbb_zcta /dev/stdin -z6 --simplification=10 --detect-shared-borders --coalesce-densest-as-needed

### STATE HOUSE

xsv select '!WKT' USBB_05282019_state_house_fcc_mlab_2014_2018.csv | \
  xsv stats | \
  xsv select type | \
  tail -n +2 | \
  sed 's/.*/"&"/' | \
  sed 's/Unicode/String/g' | \
  sed 's/Float/Real/g' | \
  tr '\n' , > USBB_05282019_state_house_fcc_mlab_2014_2018.csvt

  echo '"WKT"' >> USBB_05282019_state_house_fcc_mlab_2014_2018.csvt

ogr2ogr -f GeoJSON /dev/stdout -oo KEEP_GEOM_COLUMNS=no USBB_05282019_state_house_fcc_mlab_2014_2018.csv | tippecanoe -o usbb_state_house.mbtiles -f -l usbb_state_house /dev/stdin -z6 --simplification=10 --detect-shared-borders --coalesce-densest-as-needed

### STATE SENATE

xsv select '!WKT' USBB_06062019_state_senate_fcc_mlab_2014_2018.csv | \
  xsv stats | \
  xsv select type | \
  tail -n +2 | \
  sed 's/.*/"&"/' | \
  sed 's/Unicode/String/g' | \
  sed 's/Float/Real/g' | \
  tr '\n' , > USBB_06062019_state_senate_fcc_mlab_2014_2018.csvt

  echo '"WKT"' >> USBB_06062019_state_senate_fcc_mlab_2014_2018.csvt

ogr2ogr -f GeoJSON /dev/stdout -oo KEEP_GEOM_COLUMNS=no USBB_05282019_state_senate_fcc_mlab_2014_2018.csv | tippecanoe -o usbb_state_senate.mbtiles -f -l usbb_state_senate /dev/stdin -z6 --simplification=10 --detect-shared-borders --coalesce-densest-as-needed

## UPLOADING to MAPBOX

mapbox upload --name 'MLab and FCC County' newamerica.usbb_county mbtiles/usbb_county.mbtiles
