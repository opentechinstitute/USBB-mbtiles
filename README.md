# USBB-mbtiles

Overall Steps:

1. Run the SQL query that joins the Spatial Data, FCC data and M-Lab data
    1. Note: Main differences here are about the spatial data (zcta, county, census tract, senate house, state senate)
2. Export the JSON via GCS
3. Convert the JSON to CSV ('rewrite_export_combined.py')
4. Re-code the CSV schema to know what the data types are (xsv commands in '/notes/ogr_commands.md')
5. Run ogr2ogr > tippecanoe command to create mbtiles (ogr2ogr commands in 'notes/ogr_commands.md')
6. Upload mbtiles to Mapbox using python library (Mapbox command in 'notes/ogr_commands.md')

If you need to fix something, e.g. missing data..

1. Get the data you need
2. Export JSON
3. Convert JSON to CSV
4. Re-code the CSV schema to know what the data types are (xsv commands in '/notes/ogr_commands.md')
5. Run ogr2ogr > tippecanoe command to create mbtiles (ogr2ogr commands in 'notes/ogr_commands.md')
6. Join the mbtiles to the original mbtiles
7. Upload replacement mbtiles to Mapbox.


