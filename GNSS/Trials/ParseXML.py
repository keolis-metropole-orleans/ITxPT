import xml.etree.ElementTree as ET


def parseXML(xmlfile):
    xmlfile = "test.xml"

    tree = ET.parse(xmlfile)
    root = tree.getroot()


    #permet de faire un print du fichier xml
    #ET.dump(tree)

    # Création de notre dico
    dico = {"Latitude": [], "Longitude": [], "Altitude": "", "SpeedOverGround": "", "Time": "", "Date": ""}


    # Récupération de la latitude
    for elem in root.findall("./GNSSLocation/Latitude/Degree"):
        dico["Latitude"].append(elem.text)

    for elem in root.findall("./GNSSLocation/Latitude/Direction"):
        dico["Latitude"].append(elem.text)


    # Récupération de la longitude
    for elem in root.findall("./GNSSLocation/Longitude/Degree"):
        dico["Longitude"].append(elem.text)

    for elem in root.findall("./GNSSLocation/Longitude/Direction"):
        dico["Longitude"].append(elem.text)


    # Récupération de l'altitude
    for elem in root.findall("./GNSSLocation/Altitude"):
        dico["Altitude"] = elem.text
        

    # Récupération de la speed
    for elem in root.findall("./GNSSLocation/SpeedOverGround"):
        dico["SpeedOverGround"] = elem.text


    # Récupération du time
    for elem in root.findall("./GNSSLocation/Time"):
        dico["Time"] = elem.text


    # Récupération de la date
    for elem in root.findall("./GNSSLocation/Date"):
        dico["Date"] = elem.text


    return dico