from osgeo import ogr
from osgeo import osr

driver = ogr.GetDriverByName("ESRI Shapefile")

dataSource = driver.Open("/Users/greg/Desktop/kba/kba_ch.shp", 1)
layer = dataSource.GetLayer()

#Prepare a transformation between projections
src_srs = layer.GetSpatialRef()
tgt_srs = osr.SpatialReference()
tgt_srs.ImportFromEPSG(3857)
transform = osr.CoordinateTransformation(src_srs, tgt_srs)

#Add new field
new_field = ogr.FieldDefn("Area", ogr.OFTReal)
new_field.SetPrecision(2)
layer.CreateField(new_field)

#Compute the area for each feature
for feature in layer:
        geom = feature.GetGeometryRef()
        geom2 = geom.Clone()
        geom2.Transform(transform)
        
        area_in_sq_m = geom2.GetArea()
        print('Area in sq m', area_in_sq_m)
        feature.SetField("Area", area_in_sq_m)
        layer.SetFeature(feature)

dataSource.Destroy()