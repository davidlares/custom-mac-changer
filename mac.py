#!/usr/bin/python

import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    # message
    print("[+] Changing MAC address for %s to %s" % (interface, new_mac))
    # sequential script
    subprocess.call(["ip","link","set",interface,"down"])
    subprocess.call(["ip","link","set",interface,"address",new_mac])
    subprocess.call(["ip","link","set",interface,"up"])

def get_args():
    # parsing args configuration
    parser = optparse.OptionParser() # instance
    # options
    parser.add_option("-i","--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    # parsing arguments
    (opts, args) = parser.parse_args()
    if not opts.interface:
        # raising errors
        parser.error("[-] Please specify an interface. Use --help for more info")
    elif not opts.new_mac:
        # raising errors
        parser.error("[-] Please specify an new_mac. Use --help for more info")
    sreturn opts

def current_mac(interface):
    eval = subprocess.check_output(["ip","a","show","dev", interface])
    # extracting MAC with regex
    mac_obj = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", eval)
    if mac_obj:
        return mac_obj.group(0)
    else:
        print('[-] Could not read MAC Address.')

if __name__ == "__main__":
    # initial state
    opts = get_args()
    current_mac = current_mac(opts.interface)
    print("Current MAC> %s" % str(current_mac))
    change_mac(opts.interface,opts.new_mac)
    print("Current MAC> %s" % str(current_mac))
    # checking the MAC set
    if current_mac == opts.new_mac:
        print("[+] MAC address was successfully changed to %s" % current_mac)
    else:
        print("[-] MAC address did not get changed")
