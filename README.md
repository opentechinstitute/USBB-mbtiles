# USBB-mbtiles

Overall Steps:

1. Run the SQL query that joins the Spatial Data, FCC data and M-Lab data
    1. Note: Main differences here are about the spatial data (zcta, county, census tract, senate house, state senate)
2. Export the JSON via GCS
3. Convert the JSON to CSV ('rewrite_export_combined.py')
4. Re-code the CSV schema to know what the data types are (xsv commands in '/notes/ogr_commands.md')
5. Run ogr2ogr > tippecanoe command to create mbtiles (ogr2ogr commands in 'notes/ogr_commands.md')
6. Upload mbtiles to Mapbox using python library (Mapbox command in 'notes/ogr_commands.md')


