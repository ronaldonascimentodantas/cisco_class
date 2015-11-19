#THIS IS THE README FILE!

#N9K Scripts

Script: show-simple-inventory_v2.py
This simple python script show the inventory from N9K Devices.
show simple information like interface description and CDP Neighbor information.

Input: python show-simple-inventory_v2.py <IP> <username> <password>

Script: apic_show-mac-address.py is used to show all if a mac-address is inside the fabric
Usage: python apic_show-mac-address.py <hostname> <username> <password> <mac-address>

Examples:

(1) Single mac address inside the fabric
python apic_show-mac-address.py apic admin XXXX 00:44:56:6F:85:AD

(2) Single mac address IS NOT inside the fabric
python apic_show-mac-address.py apic admin XXXX 00:44:56:FF:FF:FF

(3) Group mac address inside the fabric
python apic_show-mac-address.py apic admin XXXX 00:44:56


#APIC Scripts

Script: apic_find-epg.py is used to find a specific EPG inside the Fabric
or find a sub-string EPG inside the fabric

Usage: python apic_find-epg.py <hostname> <username> <password> <epg> [-s]

Examples:

(1) Find a EPG string inside the fabric
python apic_find-epg_v2.py apic admin XXXX App

(2) Find a EPG sub-string inside the fabric
python apic_find-epg_v2.py apic admin XXXX App -s
