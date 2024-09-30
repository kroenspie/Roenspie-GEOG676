# create a gdb 
import arcpy

arcpy.env.workspace = r'C:\Users\Roenspie\Desktop\GEOG676\Lab04\codes_env'
folder_path = r'C:\Users\Roenspie\Desktop\GEOG676\Lab04'
gdb_name = 'Roenspie_Lab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)


#Create Feature Data Points 
csv_path = r'C:\Users\Roenspie\Desktop\GEOG676\Lab04\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X' , 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# open campus gdb, copy building feature to our gdb
campus = r'C:\Users\Roenspie\Desktop\GEOG676\Lab04\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Reprojection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_Reprojected', spatial_ref)

# Buffer
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_Reprojected', gdb_path + '\Garage_Points_buffered', 150)

#Run an Intersect
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Buildings_Intersection', 'ALL')

arcpy.TabletoTable_conversion(gdb_path + '\Garage_Buildings_Intersection.dbf' , r'C:\Users\Roenspie\Desktop\GEOG676\Lab04' , 'nearbybuildings.csv')
