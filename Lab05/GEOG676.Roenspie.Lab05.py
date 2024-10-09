## Lab 05: Toolbox

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class BuildingProximity(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "BuildingProximity"
        self.description = "Determine which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False
	self.category = "Building Tools"

    def getParameterInfo(self):
        param0 = arcpy.Parameter( #geodatabase folder -- this is a new folder becuase in code below (in execute), gdb gets created 
            displayName="GDB Folder", 
            name="GDBFolder",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )
        param1 = arcpy.Parameter( #geodatabase
            displayName="GDB Name",
            name="GDBName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param2 = arcpy.Parameter( #garage CSV
            displayName="Garage CSV File",
            name="GarageCSVFile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )        
        param3 = arcpy.Parameter( #garage layer name (that is going to be (?)created as XY event)
            displayName="Garage Layer Name",
            name="GarageLayerName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )        
        param4 = arcpy.Parameter( #campus geodatabase
            displayName="Campus GDB",
            name="CampusGDB",
            datatype="DEType",
            parameterType="Required",
            direction="Input"
        )
        param5 = arcpy.Parameter( #buffer distance
            displayName="Buffer Radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3, param4, param5]
        return params
        

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        folder_path = parameters[0].valueAsText
        gdb_name = parameters[1].valueAsText
        gdb_path = folder_path + '\\' + gdb_name
        arcpy.CreateFileGDB_management(folder_path, gdb_name)

        csv_path = parameters[2].valueAsText
        garage_layer_name = parameters[3].valueAsText
        garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

        input_layer = garages
        arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
        garage_points = gdb_path + '\\' + garage_layer_name

        campus = parameters[4].valueAsText
        bldgs_campus = campus + '\Structures'
        bldgs = gdb_path + '\\' + 'Buildings'

        arcpy.Copy_management(bldgs_campus, bldgs)

        spatial_ref = arcpy.Describe(bldgs).spatialReference
        arcpy.Project_management(garage_points, gdb_path + '\garage_pts_reproj', spatial_ref)

        buffer_dist = int(parameters[5].value)
        garage_buff = arcpy.Buffer_analysis(gdb_path + '\garage_pts_reproj', gdb_path + '\garage_pts_buff', 150)

        arcpy.Intersect_analysis([garage_buff, bldgs], gdb_path + '\garage_bldgs_intersect', 'ALL')

        arcpy.ExportTable_conversion(gdb_path + '\garage_bldgs_intersect.dbf', r'P:\676\DevSource\GEOG_676_iles\Lab_05\nearby_bldgs.csv')

        return

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        folder_path = parameters[0].valueasText
        gdb_name = parameters[1].valueasText
        gdb_path = folder_path + '\\' + gdb_name
        arcpy.CreateFileGDB_management(folder_path, gdb_name)
    

        csv_path = parameters[2].valueasText
        garage_layer_name = parameters[3].valueasText
        garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)


        input_layer = garages
        arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
        garage_points = gdb_path + '\\' + garage_layer_name


        campus = parameters[4].valueasText
        buildings_campus = campus + '\Structures'
        buildings = gdb_path + '\\' + 'Buildings'


        arcpy.Copy_management(buildings_campus, buildings)


        spatial_ref = arcpy.Describe(buildings).spatialReference
        arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_Reprojected', spatial_ref)


        buffer_distance = int(parameters[5].value)
        garageBuffer = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_Reprojected', gdb_path + '\Garage_Points_Buffer', 150)


        arcpy.Intersect_analysis([garageBuffer, buildings], gdb_path + '\Garage_Building_Intersect', 'ALL')


        arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersect.dbf', folder_path, 'BuildingsCloseBy.csv')

        return None

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return