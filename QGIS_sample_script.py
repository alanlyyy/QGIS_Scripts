from qgis.PyQt.QtGui import QColor

#load layer if it doesn't exist
if qgis.utils.iface.activeLayer() == NULL:
    v_layer = iface.addVectorLayer(r'C:\Users\Alan\Desktop\QGIS Work\qgis_sample_data\shapefiles\airports.shp','airports','ogr')
    
#get layer name
print(v_layer.name())

#get number of features
v_layer.featureCount()

#feature object
my_features = v_layer.getFeatures()

#print all features and attributes
for feature in my_features:
    print(feature.attributes())

#print field names
for field in v_layer.fields():
    print(field.name())

#print each attribute found in the feature with Field Name 'NAME'
for feature in v_layer.getFeatures():
    print(feature.attribute('NAME'))

#calaculate total elevation
temp =[feature.attribute('ELEV') for feature in v_layer.getFeatures()]
running_total = 0
for item in temp:
    if item == NULL:
        pass
    else:
        running_total += item
print(running_total)

#add alaska raster layer
#r_layer = iface.addRasterLayer(r"C:\Users\Alan\Desktop\QGIS Work\qgis_sample_data\raster\SR_50M_alaska_nad.tif",'hillshade')

#get raster layer name
print(r_layer.name())

#get width and height of the raster
print(r_layer.width(), r_layer.height())

#get raster color band max
print(r_layer.dataProvider().bandStatistics(1).maximumValue)

#create a symbol yello diamond in the layer
symbol = QgsMarkerSymbol.createSimple({
'name': 'diamond', 'size': '5', 
'color':'#ffff00'})
v_layer.renderer().setSymbol(symbol)
v_layer.triggerRepaint()


#rule based rendering using filter expressions
rules = [['Civil','USE LIKE \'%Civil%\'','green'],
    ['Other','USE NOT LIKE \'%Civil%\'','red']
        ]
#get the current symbol object        
symbol = QgsMarkerSymbol.defaultSymbol(v_layer.geometryType())

#load the expression from rules
renderer = QgsRuleBasedRenderer(symbol)
root_rule = renderer.rootRule()


for label,expression, color_name in rules:
    
    #make a parent rule for each expression found in list "rules:"
    rule = root_rule.children()[0].clone()
    
    #execute filter using the rule
    rule.setFilterExpression(expression)
    
    #set color of symbol
    rule.symbol().setColor(QColor(color_name))
    
    #append new rule to symbol layer
    root_rule.appendChild(rule)

#remove child rules
root_rule.removeChildAt(0)

#display modified data from rules
v_layer.setRenderer(renderer)
v_layer.triggerRepaint()

