# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:19:40 2016

@author: Eric
"""

from planetary_obj import planetary_obj
import xml.etree.ElementTree as ET, urllib.request, gzip, io
url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))

class Planet(planetary_obj):
    def __init__(self):
        planetary_obj.init(self)
        
    def __str__(self):
        out = "";
        for i in self.data:
            out += (i + ":");
            out += str(self.data[i]);
            out += " ";
        return out;
    # builds a planet object. should only be used after OEC finds a planet
    def buildPlanetFromXML(planet):
        i = 0
        planetBuilder = Planet.Builder("tempName")
        for child in planet.findall(".//name"):
            if child.tag == "name":
                if i == 0:
                    planetBuilder = Planet.Builder(child.text)
                elif i == 1:
                    planetBuilder.addValList("otherNames", child.text)
                else:
                    planetBuilder.addToValList("otherNames", child.text)
                i += 1
            else:
                planetBuilder.addToValList("otherNames", child.text)
                # Pick out the other fields necessary
        planetBuilder.addVal("semimajoraxis", planet.findtext("semimajoraxis"))
        planetBuilder.addVal("separation", planet.findtext("separation"))
        planetBuilder.addVal("eccentricity", planet.findtext("eccentricity"))
        planetBuilder.addVal("periastron", planet.findtext("periastron"))
        planetBuilder.addVal("longitude", planet.findtext("longitude"))
        planetBuilder.addVal("meananomaly", planet.findtext("meananomaly"))
        planetBuilder.addVal("ascendingnode", planet.findtext("ascendingnode"))
        planetBuilder.addVal("inclination", planet.findtext("inclination"))
        planetBuilder.addVal("impactparameter", planet.findtext("impactparameter"))
        planetBuilder.addVal("period", planet.findtext("period"))
        planetBuilder.addVal("transittime", planet.findtext("transittime"))
        planetBuilder.addVal("periastrontime", planet.findtext("periastrontime"))
        planetBuilder.addVal("maximumrvtime", planet.findtext("maximumrvtime"))
        planetBuilder.addVal("mass", planet.findtext("mass"))
        planetBuilder.addVal("radius", planet.findtext("radius"))
        planetBuilder.addVal("temperature", planet.findtext("temperature"))
        planetBuilder.addVal("age", planet.findtext("age"))
        planetBuilder.addVal("spectraltype", planet.findtext("spectraltype"))
        planetBuilder.addVal("magB", planet.findtext("magB"))
        planetBuilder.addVal("magV", planet.findtext("magV"))
        planetBuilder.addVal("magR", planet.findtext("magR"))
        planetBuilder.addVal("magI", planet.findtext("magI"))
        planetBuilder.addVal("magJ", planet.findtext("magJ"))
        planetBuilder.addVal("magH", planet.findtext("magH"))
        planetBuilder.addVal("magK", planet.findtext("magK"))
        planetBuilder.addVal("magH", planet.findtext("magH"))
        planetBuilder.addVal("discoverymethod", planet.findtext("discoverymethod"))
        planetBuilder.addVal("istransiting", planet.findtext("istransiting"))
        planetBuilder.addVal("description", planet.findtext("description"))
        planetBuilder.addVal("discoveryyear", planet.findtext("discoveryyear"))
        planetBuilder.addVal("lastupdate", planet.findtext("lastupdate"))
        planetBuilder.addVal("spinorbitalignment", planet.findtext("spinorbitalignment"))
        return planetBuilder.compile()

def buildPlanetFromXMLa():
    b = 1
    for planet in oec.findall(".//planet"):
        planetBuilder = Planet.Builder("tempName")
        i = 0
        for child in planet.findall(".//name"):
            if child.tag == "name":
                if i == 0:
                    planetBuilder = Planet.Builder(child.text)
                elif i == 1:
                    planetBuilder.addValList("otherNames", child.text)
                else:
                    planetBuilder.addToValList("otherNames", child.text)
                i += 1
            else:
                planetBuilder.addToValList("otherNames", child.text)

        # Pick out the other fields necessary
        planetBuilder.addVal("semimajoraxis", planet.findtext("semimajoraxis"))
        planetBuilder.addVal("separation", planet.findtext("separation"))
        planetBuilder.addVal("eccentricity", planet.findtext("eccentricity"))
        planetBuilder.addVal("periastron", planet.findtext("periastron"))
        planetBuilder.addVal("longitude", planet.findtext("longitude"))
        planetBuilder.addVal("meananomaly", planet.findtext("meananomaly"))
        planetBuilder.addVal("ascendingnode", planet.findtext("ascendingnode"))
        planetBuilder.addVal("inclination", planet.findtext("inclination"))
        planetBuilder.addVal("impactparameter", planet.findtext("impactparameter"))
        planetBuilder.addVal("period", planet.findtext("period"))
        planetBuilder.addVal("transittime", planet.findtext("transittime"))
        planetBuilder.addVal("periastrontime", planet.findtext("periastrontime"))
        planetBuilder.addVal("maximumrvtime", planet.findtext("maximumrvtime"))
        planetBuilder.addVal("mass", planet.findtext("mass"))
        planetBuilder.addVal("radius", planet.findtext("radius"))
        planetBuilder.addVal("temperature", planet.findtext("temperature"))
        planetBuilder.addVal("age", planet.findtext("age"))
        planetBuilder.addVal("spectraltype", planet.findtext("spectraltype"))
        planetBuilder.addVal("magB", planet.findtext("magB"))
        planetBuilder.addVal("magV", planet.findtext("magV"))
        planetBuilder.addVal("magR", planet.findtext("magR"))
        planetBuilder.addVal("magI", planet.findtext("magI"))
        planetBuilder.addVal("magJ", planet.findtext("magJ"))
        planetBuilder.addVal("magH", planet.findtext("magH"))
        planetBuilder.addVal("magK", planet.findtext("magK"))
        planetBuilder.addVal("magH", planet.findtext("magH"))
        planetBuilder.addVal("discoverymethod", planet.findtext("discoverymethod"))
        planetBuilder.addVal("istransiting", planet.findtext("istransiting"))
        planetBuilder.addVal("description", planet.findtext("description"))
        planetBuilder.addVal("discoveryyear", planet.findtext("discoveryyear"))
        planetBuilder.addVal("lastupdate", planet.findtext("lastupdate"))
        planetBuilder.addVal("spinorbitalignment", planet.findtext("spinorbitalignment"))



        planet = planetBuilder.compile()

        '''
        for child in planet:
            planetBuilder = Planet.Builder(planet.findtext("name"))
            planetBuilder.addVal(child.tag, child.attrib)
        '''
        planet = planetBuilder.compile()
        if b == 1:
            print(planet)
            b += 1
    '''
    # Find all circumbinary planets
    for planet in oec.findall(".//binary/planet"):
        print(planet.findtext("name"))
    # Output distance to planetary system (in pc, if known) and number of planets in system
    for system in oec.findall(".//system"):
        print(system.findtext("distance"), len(system.findall(".//planet")))
    '''
