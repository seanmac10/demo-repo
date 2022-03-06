import arcpy

srcraster = r"C:\temp\src\m_3811754_ne_11_1_20170704.tif"
arcpy.management.AddRastersToMosaicDataset(r"C:\temp\mosaic\Default.gdb\test_mos", 
                                           "Raster Dataset", 
                                           srcraster, 
                                           "UPDATE_CELL_SIZES", 
                                           "UPDATE_BOUNDARY", 
                                           "UPDATE_OVERVIEWS", 
                                           None, 0, 1500, 
                                           'PROJCS["NAD_1983_UTM_Zone_11N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-117.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]];-5120900 -9998100 450445547.391054;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision', 
                                           '', 
                                           "SUBFOLDERS", 
                                           "ALLOW_DUPLICATES", 
                                           "BUILD_PYRAMIDS", 
                                           "CALCULATE_STATISTICS", 
                                           "NO_THUMBNAILS", '', 
                                           "NO_FORCE_SPATIAL_REFERENCE", 
                                           "ESTIMATE_STATISTICS", None, 
                                           "USE_PIXEL_CACHE", 
                                           r"C:\Users\Terra\AppData\Local\ESRI\rasterproxies\test_mos")


#Add a comment
#another comment
