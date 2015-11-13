#!/usr/bin/env python

import xmltodict
import json
import sys
from device import Device

def show_interface(sw):

    getdata = sw.show('show interface description')

    show_int_description = xmltodict.parse(getdata[1])

    data_result = {}
    data = show_int_description['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']

    #Print the header
    print "%s %s %s" % ( '{:<14}'.format('Interface') , '{:<5}'.format('Speed'), 'description' )

    for each in data:
        interface_speed = " "
        interface_description = " "
        data_result['interface_name'] = each['interface']

        # Geting the interface speed
        try:
            if('speed') in each.keys():
                interface_speed = each['speed']
        except KeyError:
                interface_speed = " "

        # Geting the interface description
        try:
            if('desc') in each.keys():
                interface_description = each['desc']
        except KeyError:
                interface_description = " "

        print "%s %s %s" % ( '{:<14}'.format( data_result['interface_name'] ),'{:<5}'.format( interface_speed ),interface_description )

def show_cdp_neighbors(sw):

    getdata = sw.show('show cdp neighbors')

    show_cdp = xmltodict.parse(getdata[1])
    data = show_cdp['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']

    print "\n\nNeighbors information"
    print "%s %s %s" % ( '{:<14}'.format('Interface') , '{:<40}'.format('Device'), 'Neighbors Interface' )
    for x in range(0, len(data)):
        print "%s %s %s" % ( '{:<14}'.format( data[x]['intf_id'] ) , '{:<40}'.format(data[x]['device_id']) , data[x]['port_id'])

def main():

    args = sys.argv

    if len(args)  == 4:
        switch = Device(ip=args[1], username=args[2], password=args[3])
        
        try:
            switch.open()
            interface = show_interface(switch)
            cdp = show_cdp_neighbors(switch)
        except:
            print "\nshow-simple-inventory.py: Please review your input parameters."
    else:
        print "\nshow-simple-inventory.py: Invalid Key.\nSyntax: show-simple-inventory.py <switch-name> <username> <password>\n"

if __name__ == "__main__":
    main()
