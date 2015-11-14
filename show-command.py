#!/usr/bin/env python

#file: show-command.py
#this python script is used to execute ANY show command

import xmltodict
import json
import sys
from device import Device

def show_command(sw, command):

    result_final = ""
    command = 'show ' + command
    #print "%s" % ( command )
    
    getdata = sw.show(command)
    result  = xmltodict.parse(getdata[1])
    print json.dumps( result, indent=2 )

    '''
    try:
        data = result['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']
        neighbor_name = data['device_id']
        neighbor_interface = data['port_id']
        result_final = '{:<30}'.format( neighbor_name ) + '{:<14}'.format( neighbor_interface )
    except KeyError:
        result_final = ""     '''

    return result_final

def main():

    args = sys.argv

    if len(args)  == 5:
        switch = Device(ip=args[1], username=args[2], password=args[3])
        
        try:
            switch.open()
            showcommand = show_command(switch, args[4] )
            print showcommand

        except:
            print "\nshow-command.py: Please review you input parameters."
    else:
        print "\nshow-command.py: Invalid Key.\nSyntax: show-command.py <switch-name> <username> <password> <show-command>\n"

if __name__ == "__main__":
    main()
