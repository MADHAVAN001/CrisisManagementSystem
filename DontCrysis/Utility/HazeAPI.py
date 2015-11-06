__author__ = 'Ankur Bansal'
import urllib2
import xml.etree.ElementTree as ET

def webAPI():
    refKey = "781CF461BB6606AD28A78E343E0E4176E16BDF3D971B1D9B"
    url = "http://www.nea.gov.sg/api/WebAPI?dataset=psi_update&keyref=" + refKey

    try:
        content = urllib2.urlopen(url).read()
    except:
        print("Unexpected Error.")

    return content

def checkHaze():
    xmlData = webAPI()

    #Retrieve root element
    root = ET.fromstring(xmlData)
    #Get readings for NPSI_PM25_3HR
    readings = root.findall(".//reading[2]")
    #Delete the NSR reading
    del readings[1]
    finalReadings = []
    for reading in readings:
        finalReadings.append(int(reading.attrib['value']))

    # Order of Readings : North, Central, East, West, South
    # For Mapping : North, North East, East, West, Central
    return finalReadings