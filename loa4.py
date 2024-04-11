import xml.etree.ElementTree as ET
import json
import sys

def printValueAlias(e, valueAlias, defaulted, nodefault):
    try: 
        # print(e.attrib["value"])
        # print(e.attrib["default"])
        e.attrib["default"]
        defaulted.write(valueAlias)
        defaulted.write("\n")
        defaulted.write(e.attrib["default"])
        defaulted.write("\n")
    except:
        # print(e.attrib["value"])
        nodefault.write(valueAlias)
        nodefault.write("\n")

soup = ET.parse("/c/x3d-code/www.web3d.org/specifications/X3dUnifiedObjectModel-4.0.xml").getroot()


enums = soup.iter("enumeration")

defaulted = open("./results/loa4defaulted.txt", "w")
nodefault = open("./results/loa4nodefault.txt", "w")
for e in enums:
    try:
        if e.attrib["loa"] == "4":
            printValueAlias(e, e.attrib["value"], defaulted, nodefault)
            try:
                for alias in e.attrib["alias"].split(','):
                    printValueAlias(e, alias, defaulted, nodefault)
            except KeyError:
                pass
    except KeyError:
        pass
    except:
        raise
defaulted.close()
nodefault.close()

defaulted = open("./results/loa4defaulted.txt", "r")
nodefault = open("./results/loa4nodefault.txt", "r")
for f in [ defaulted, nodefault ]:

    line = f.readline()[:-1]
    while line:
        enums = soup.iter("enumeration")
        for e in enums:
            try:
                if e.attrib["loa"] == "4":
                    if e.attrib["value"] == line:
                        try:
                            e.attrib["default"]
                            print(e.attrib["value"], "|", line, "=", e.attrib["default"])
                        except:
                            print(e.attrib["value"], "|", line)
            except KeyError:
                pass
            except:
                raise
        line = f.readline()[:-1]
defaulted.close()
nodefault.close()
