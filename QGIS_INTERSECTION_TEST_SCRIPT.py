"""
This script is a failed attempt to find intersections between multipart polygons
and multipart lines.

run multipart to singlepart algorithm and attempts to find the intersection.

However, my multipart lines and polygons are not actually split up.

This is good example on how to run a processing algorithm.

05-07-20
""" 

import os

#run processing algorithms in standalone script
import processing
from processing.core.Processing import Processing

def run_processing_alg():
    """
    runs processing algorithm multipart_to_singleparts on current vector layer.
    
    """
    Processing.initialize()
    
    params = {
        'INPUT': iface.activeLayer(),
        'OUTPUT': os.path.join(r'C:\path\multi_to_single.shp')
        }
        
    feedback = QgsProcessingFeedback()
    
    #run multipart to single part to split multi objects into single objects
    res = processing.run('native:multiparttosingleparts',params, feedback=feedback)
    
    print(res['OUTPUT'])

run_processing_alg()
#indication list
#lines list
indication = []
lines = []

#iterate through each layer separate lines and indication
for layer in QgsProject.instance().mapLayers().values():
    
    if 'lines' in layer.name():
        lines.append(layer)
    else:
        indication.append(layer)

print(lines)
print("-----")
print(indication)

intersection_dict = {}
count = 0

for line_layer in lines:
    
    line_features = line_layer.getFeatures()
    for indication_layer in indication:
        indication_features = indication_layer.getFeatures()
        
        for line_feature in line_features:
        
            for indication_feature in indication_features:
            
                print(count,indication_feature.geometry(),line_feature.geometry)
                
                if indication_feature.geometry().intersects(line_feature.geometry()):
                
                    if line_feature in intersection_dict:
                    
                        intersection_dict[line_feature.geometry()] += 1
                    else:
                        intersection_dict[line_feature.geometry()] = 1
                    
                    count+=1
                print(count)

        
            
        
        