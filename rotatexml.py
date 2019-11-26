import imutils
import cv2
import os
import re

winkelliste = [0,90,180,270]

def bilddrehen(pathzubild, name):
    image = cv2.imread(pathzubild)
    for winkel in winkelliste:
        rotated = imutils.rotate_bound(image, winkel)
        cv2.waitKey(0)
        cv2.imwrite('neu/'+name[:-4] + '-' + str(winkel) + '.JPG', rotated)
        print('Bild',name,'um',winkel,'° gedrehet')

def xmldrehen(pathzuxml, xmlname):
    alt = open(pathzuxml, "r").readlines()
    for winkel in winkelliste:
        neuxmlname = xmlname[:-4] + '-' + str(winkel) + '.xml'
        print('XMLdatei ' + xmlname + ' um ' + str(winkel) + '° gedreht')
        neu = open('neu/'+neuxmlname, 'w')
        # Winkel 0 (fertig)
        if winkel == 0:
            for zeile in alt:
                if '<folder>' in zeile:
                    pass
                elif '<path>' in zeile:
                    pass
                elif '<filename>' in zeile:
                    altfilenametag = xmlname[:-4] + '.JPG'
                    neufilenametag = neuxmlname[:-4] + '.JPG'
                    zeile = zeile.replace(altfilenametag, neufilenametag)
                    neu.write(zeile)
                else:
                    neu.write(zeile)
        # Winkel 90
        elif winkel == 90:
            # scan
            x0 = []
            y0 = []
            for zeile in alt:
                if '<xmin>' in zeile or '<xmax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    x0.append(i)
                if '<ymin>' in zeile or '<ymax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    y0.append(i)
                if '<height>' in zeile:
                    w = int(re.search(r'\d+', zeile).group())
            # schreiben
            yn = 0
            xn = 0
            for zeile in alt:
                if '<folder>' in zeile:
                    pass
                elif '<path>' in zeile:
                    pass
                elif '<filename>' in zeile:
                    altfilenametag = xmlname[:-4] + '.JPG'
                    neufilenametag = neuxmlname[:-4] + '.JPG'
                    zeile = zeile.replace(altfilenametag, neufilenametag)
                    neu.write(zeile)
                elif '<width>' in zeile:
                    zeile = zeile.replace('width','height')
                    neu.write(zeile)
                elif '<height>' in zeile:
                    zeile = zeile.replace('height','width')
                    neu.write(zeile)
                elif '<ymin>' in zeile or '<ymax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    zeile = zeile.replace(str(i), str(x0[yn]))
                    yn += 1
                    neu.write(zeile)
                elif '<xmin>' in zeile or '<xmax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    zeile = zeile.replace(str(i), str((w - y0[xn])))
                    xn += 1
                    neu.write(zeile)
                else:
                    neu.write(zeile)
        # Winkel 180
        elif winkel == 180:
            # scan
            x0 = []
            y0 = []
            for zeile in alt:
                if '<xmin>' in zeile or '<xmax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    x0.append(i)
                if '<ymin>' in zeile or '<ymax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    y0.append(i)
                if '<height>' in zeile:
                    h = int(re.search(r'\d+', zeile).group())
                if '<width>' in zeile:
                    w = int(re.search(r'\d+', zeile).group())
            # schreiben
            yn = 0
            xn = 0
            for zeile in alt:
                if '<folder>' in zeile:
                    pass
                elif '<path>' in zeile:
                    pass
                elif '<filename>' in zeile:
                    altfilenametag = xmlname[:-4] + '.JPG'
                    neufilenametag = neuxmlname[:-4] + '.JPG'
                    zeile = zeile.replace(altfilenametag, neufilenametag)
                    neu.write(zeile)
                elif '<ymin>' in zeile or '<ymax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    zeile = zeile.replace(str(i), str((h-y0[yn])))
                    yn += 1
                    neu.write(zeile)
                elif '<xmin>' in zeile or '<xmax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    zeile = zeile.replace(str(i), str((w - x0[xn])))
                    xn += 1
                    neu.write(zeile)
                else:
                    neu.write(zeile)
        # Winkel 270
        elif winkel == 270:
            # scan
            x0 = []
            y0 = []
            for zeile in alt:
                if '<xmin>' in zeile or '<xmax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    x0.append(i)
                if '<ymin>' in zeile or '<ymax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    y0.append(i)
                if '<width>' in zeile:
                    h = int(re.search(r'\d+', zeile).group())
            # schreiben
            yn = 0
            xn = 0
            for zeile in alt:
                if '<folder>' in zeile:
                    pass
                elif '<path>' in zeile:
                    pass
                elif '<filename>' in zeile:
                    altfilenametag = xmlname[:-4] + '.JPG'
                    neufilenametag = neuxmlname[:-4] + '.JPG'
                    zeile = zeile.replace(altfilenametag, neufilenametag)
                    neu.write(zeile)
                elif '<ymin>' in zeile or '<ymax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    zeile = zeile.replace(str(i), str((h - x0[yn])))
                    yn += 1
                    neu.write(zeile)
                elif '<xmin>' in zeile or '<xmax>' in zeile:
                    i = int(re.search(r'\d+', zeile).group())
                    zeile = zeile.replace(str(i), str(y0[xn]))
                    xn += 1
                    neu.write(zeile)
                else:
                    neu.write(zeile)
        else:
            print('Unerwarteter Winkel: ' +  str(winkel))

def bildspiegeln(pathzubild, name):
    image = cv2.imread(pathzubild)
    rotated = cv2.flip(image, flipCode=1)
    cv2.waitKey(0)
    cv2.imwrite('neu/' + name[:-4] + '-' + 'gespiegelt' + '.JPG', rotated)
    print('Bild', name, ' gespiegelt')


def xmlspiegeln(pathzuxml, xmlname):
    alt = open(pathzuxml, "r").readlines()
    neuxmlname = xmlname[:-4] + '-' + 'gespiegelt' + '.xml'
    print('XMLdatei ' + xmlname + ' gespiegelt')
    neu = open('neu/'+neuxmlname, 'w')
    # scan
    x0 = []
    y0 = []
    for zeile in alt:
        if '<xmin>' in zeile or '<xmax>' in zeile:
            i = int(re.search(r'\d+', zeile).group())
            x0.append(i)
        if '<ymin>' in zeile or '<ymax>' in zeile:
            i = int(re.search(r'\d+', zeile).group())
            y0.append(i)
        if '<width>' in zeile:
            if '-270' in xmlname:
                pass
            else:
                w = int(re.search(r'\d+', zeile).group())
        if '<height>' in zeile:
            if '-270' in xmlname:
                w = int(re.search(r'\d+', zeile).group())
            else:
                pass
    # schreiben
    yn = 0
    xn = 0
    for zeile in alt:
        if '<folder>' in zeile:
            pass
        elif '<path>' in zeile:
            pass
        elif '<filename>' in zeile:
            altfilenametag = xmlname[:-4] + '.JPG'
            neufilenametag = neuxmlname[:-4] + '.JPG'
            zeile = zeile.replace(altfilenametag, neufilenametag)
            neu.write(zeile)
        elif '<ymin>' in zeile or '<ymax>' in zeile:
            i = int(re.search(r'\d+', zeile).group())
            zeile = zeile.replace(str(i), str((y0[yn])))
            yn += 1
            neu.write(zeile)
        elif '<xmin>' in zeile or '<xmax>' in zeile:
            i = int(re.search(r'\d+', zeile).group())
            zeile = zeile.replace(str(i), str((w - x0[xn])))
            xn += 1
            neu.write(zeile)
        else:
            neu.write(zeile)

# Bilder und XMLDateien drehen
for file in os.listdir("images/"):
    if file.endswith('.JPG'):
        bilddrehen('images/'+file, file)
    if file.endswith('.xml'):
        xmldrehen('images/'+file, file)

# Bilder und XMLDateien spiegeln
for file in os.listdir("neu/"):
    if file.endswith('.JPG'):
        bildspiegeln('neu/'+file, file)
    if file.endswith('.xml'):
        xmlspiegeln('neu/'+file, file)