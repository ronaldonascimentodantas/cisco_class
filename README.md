THIS IS THE README FILE!

This simple python script show the inventory from N9K Devices.
show simple information like interface description and CDP Neighbor information.

Input:

python show-simple-inventory_v2.py n9k username password

Output example:

Interface      Speed      description
mgmt0                      
Ethernet1/1    10G        Basic Interface Description
Ethernet1/2    10G        Basic Interface Description
Ethernet1/3    10G         
Ethernet1/4    10G         
Ethernet1/5    10G         
Ethernet1/6    10G         
Ethernet1/7    10G         
Ethernet1/8    10G         
Ethernet1/9    10G         
Ethernet1/10   10G         
Ethernet1/11   10G         
Ethernet1/12   10G         
Ethernet1/13   10G         
Ethernet1/14   10G         
Ethernet1/15   10G         
Ethernet1/16   10G         
Ethernet1/17   10G         
Ethernet1/18   10G         
Ethernet1/19   10G         
Ethernet1/20   10G         
Ethernet1/21   10G         
Ethernet1/22   10G         
Ethernet1/23   10G         
Ethernet1/24   10G         
Ethernet1/25   10G         
Ethernet1/26   10G         
Ethernet1/27   10G         
Ethernet1/28   10G         
Ethernet1/29   10G         
Ethernet1/30   10G         
Ethernet1/31   10G         
Ethernet1/32   10G         
Ethernet1/33   10G         
Ethernet1/34   10G         
Ethernet1/35   10G         
Ethernet1/36   10G         
Ethernet1/37   10G         
Ethernet1/38   10G         
Ethernet1/39   10G         
Ethernet1/40   10G         
Ethernet1/41   10G         
Ethernet1/42   10G         
Ethernet1/43   10G         
Ethernet1/44   10G         
Ethernet1/45   10G         
Ethernet1/46   10G         
Ethernet1/47   10G         
Ethernet1/48   10G         
Ethernet2/1    40G         
Ethernet2/2    40G         
Ethernet2/3    40G         
Ethernet2/4    40G         
Ethernet2/5    40G         
Ethernet2/6    40G         
Ethernet2/7    40G         
Ethernet2/8    40G         
Ethernet2/9    40G         
Ethernet2/10   40G         
Ethernet2/11   40G         
Ethernet2/12   40G         
port-channel10            Test_Port_Channel
loopback0                  
loopback1                  
loopback2                 Lo2 - Interface created by NX-API Developer Sandbox


Neighbors information
Interface      Device                                   Neighbors Interface
mgmt0          Switch                                   GigabitEthernet1/4
Ethernet1/1    N9k3.apoaci.com(XXXXXXXXXXX)             Ethernet1/2
Ethernet1/2    n9k4.apoaci.com(XXXXXXXXXXX)             Ethernet1/2
Ethernet1/3    N9K5.apoaci.com(XXXXXXXXXXX)             Ethernet1/2
Ethernet1/47   n9k1.sjc.pcisco.com(XXXXXXXXXXX)         Ethernet1/47

