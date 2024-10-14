## TAMU GIS Programming- GitHub Portfolio (Roenspie-GEOG676)

# Project Goal

Building a master well database, particularly in industries like oil and gas, presents several challenges, including but not limited to, fragmented data and inconsistent data, lack of standardization among data and presentation of data, the sheer volume of readily availbale data and, of course, determining data accuracy and verification. 
The goal of the project presented below is the creation of a tool which can be used within ArcGIS pro to help address all of the challenges listed above. This tool will 1) Import all data points of well locations, 2) calculate the inverse of all data to write a master well location trending position, 3) build a check to determine if the coordinates are NAD83 versus NAD27, 4) and allow the user to select well location off of aerial imagery as well and 5) finally determine confidence in well location and attribute data.

# Creation and Implementation of Tool

1. The first step to creating any master database will be to read data from all existing databases. Using our software, all relevant data sources can be imported and be read, sorted through and ultimately organized in a manner to allow for ease of use. An example of this first crucial step in the funcationality of this tool can be located here: https://github.com/kroenspie/Roenspie-GEOG676/tree/main/Lab03

2. The tool will then proceed into a verification process. Here the well coordinates pulled in step 1 will be checked for accruacy by examining inverse coordinates of well locations. An example of this tool can be lcoated here: https://github.com/kroenspie/Roenspie-GEOG676/tree/main/Lab02

3. Once data has been standardized and checked for accuracy, the tool developed will then export the data into a geodatabase which can be further used for the purpose and manipulation of the project. An example of this tool can be located here: https://github.com/kroenspie/Roenspie-GEOG676/tree/main/Lab04

4. Once the geodatabse has been created, a series of operations can be applied to the data in order to retrieve desired results. Examples of these sort of operations include creating buffers, selecting data by specific attributes, utilizing points and locations of intersect to include or discinclude data, etc. And example of a buffer analysis tool being utilized can be located here: https://github.com/kroenspie/Roenspie-GEOG676/tree/main/Lab05

5. In order to create confidence in well location and other included data, it might be beneficial to include color gradients in final map imagery. This can be useful in quickly determining size, age, depth, ownership, or other important attributes at a glance. The can be easily manipulated to the client's needs. An example of this tool in action can be located here: https://github.com/kroenspie/Roenspie-GEOG676/tree/main/Lab06

6. As with any georeferenceing, it will be crucial to be able to incooprerate and compare spatial data with aerial imagery. An example of this tool use can be located here: https://github.com/kroenspie/Roenspie-GEOG676/tree/main/Lab07


# Project Planning Discussion

Several important factors must be considered in the actualization of this project.

a. Return of Investment: this leading industry is filled with a robust amount of information. Those who can process it the quickest with the most accuracy stand to claim the most benefits. It is important to streamline as much of this process as possible without loosing the integrity of the data. Investment in a tool with the capabilities mentioned above will set the client a shoulder above their competitors and give them the winning edge.  

b. Software requirements : the tool itself will be deployed as both a python code as well as an ArcGIS toolbox so clients will have the flexibility to utilize as they see fit.

c. Information/Data Requirements: the tool built will be able to access and utilize non-uniform data from multiple sources including USGS, USGWD, NWIS and SDR.

d. Workflow monitoring and reporting : the client will be given a direct line of communication with company personnel to ensure the proper implementation and success of the tool and project. Weekly data counts and refreshes will be monitored for error as well as overall accuracy. The final reports will be delievered in shapefiles, mapbooks, as well as excels to track and maintain data throughout the entirety of the project. All data obtained and maintained throughout the course of the project will be owned entirely by the client during the course of the contracted agreement. 
