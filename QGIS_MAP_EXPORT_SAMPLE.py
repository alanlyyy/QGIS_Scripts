from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QSize

#qgis.utils.iface == iface

#configure output image
width = 800
height = 600
dpi = 92
img = QImage(QSize(width, height) , QImage.Format_RGB32)
img.setDotsPerMeterX(dpi / 25.4 * 1000)
img.setDotsPerMeterY(dpi / 25.4 * 1000)

#get the map layers and extent 
layers = QgsProject.instance().mapLayers().values()
layer_objects = []

for item in layers:
    layer_objects.append(item)
    
extent = iface.mapCanvas().extent()


#configure map settings for export
mapSettings = QgsMapSettings()
mapSettings.setExtent(extent)
mapSettings.setOutputDpi(dpi)
mapSettings.setOutputSize(QSize(width,height))
mapSettings.setLayers(layer_objects)

mapSettings.setFlags(QgsMapSettings.Antialiasing |
QgsMapSettings.UseAdvancedEffects | QgsMapSettings.ForceVectorOutput |
QgsMapSettings.DrawLabeling)

#configure and run painter (draw the image)
p = QPainter()
p.begin(img)
mapRenderer = QgsMapRendererCustomPainterJob(mapSettings, p)
mapRenderer.start()
mapRenderer.waitForFinished()
p.end()

#save results
img.save(r'C:\Users\Alan\Documents\QGIS_scripts\custom_export.png',"png")
