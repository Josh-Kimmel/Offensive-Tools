#!/bin/python
import netifaces
import random
import sys

def genRandomFileName():
    usableCharacters = "012345679ABCDEF"

    randomFileName = ""
    for i in range(32):
        randomFileName += random.choice(usableCharacters)

    return(randomFileName)

def printUrls(webPath):
    addresses = []
    for iface in netifaces.interfaces():
        if(iface != "lo"):
            addresses.append(netifaces.ifaddresses(iface))

    for addr in addresses[0]:
        ip = addresses[0][addr][0]["addr"]
        print("http://" + ip + "/" + webPath)

def readFile(inFilePath):
    try:
        with open(inFilePath, "rb") as inFile:
            return inFile.read()
        
    except FileNotFoundError:
        print("Error reading " + inFilePath + ": File not found. Please try again.")
        exit
    except PermissionError:
        print("Error reading " + inFilePath + ": Insufficient permissions. Please try again.")
        exit
    except:
        print("Error reading " + inFilePath + ": Unkown error. Please try again.")
        exit

def writeFile(inFilePath, outFileName):
    outFilePath = "/var/www/html/" + outFileName
    
    try:
        with open(outFilePath, "wb") as outFile:
            outFile.write(readFile(inFilePath))
    
    except PermissionError:
        print("Error writing " + outFilePath + ": Insufficient permissions. Please try again.")
        exit
    except:
        print("Error writing " + outFilePath + ": Unkown error. Please try again.")
        exit



if(len(sys.argv) == 1):
    print("\nError: No arguments provided. Please provide file to be posted as argument.")
    print("Example: ./" + sys.argv[0] +" [Input file path]\n")
    exit

else:
    inFilePath = sys.argv[1][0]
    outFileName = genRandomFileName()
    writeFile(inFilePath, outFileName)

    print("\n\nYour file is hosted at these links:")
    printUrls(outFileName)
    print("\n\n")
