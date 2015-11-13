#!/usr/bin/env python

import xmltodict
import json
import sys
from device import Device

def show_cdp(sw, interface):

    command = 'show cdp neighbor interface ' + interface
    #print "%s" % ( command )
    
    getdata = sw.show(command)
    result  = xmltodict.parse(getdata[1])
    print json.dumps( result, indent=2 )

def main():

    args = sys.argv

    if len(args)  == 5:
        switch = Device(ip=args[1], username=args[2], password=args[3])
        interface_name = args[4]   # Get the interface name
        
        try:
            switch.open()
            cdp = show_cdp(switch, interface_name)
        except:
            print "\nshow-cdp-inventory-interface.py: Please review your input parameters."
    else:
        print "\nshow-cdp-inventory-interface.py: Invalid Key.\nSyntax: show-cdp-inventory-interface.py <switch-name> <username> <password> <interface_name>\n"

if __name__ == "__main__":
    main()
