# davidMAC

This simple repository contains a script for changing the MAC (Media Access Control) Address the hard way.

It uses the `subprocess` module for executing shell commands, `optparse` for handling script arguments (dynamic interface and MAC address) and of course the `re` (regex) module for getting the MAC Address from the interface listing.

## What is the MAC Address

Permanent, physical and unique address - assigned by the manufacturer used to identify devices and transfer devices.

## Why change the MAC address

Simple:

  1. Increase anonymity (hide your identity)
  2. Impersonate other devices (spoofing)
  3. Bypass filters
  4. Regulating specific network connections by filtering MAC address

## Usage

This script is tested for Linux OS systems using the `ip a` command. This is a evolved `ifconfig` command that makes things a little bit
easier. In many docs you will find the usage of the `ifconfig` for checking the network interfaces on the OS.

Run the `mac.py` it on Debian 9 or Kali 2018. Check the `mac-ubuntu.py` for Ubuntu Xenial and Bionic.

`python mac-py -i eth0 -m 11:22:33:44:55:00`

You can also set `+x` priveleges like `sudo chmod +x mac.py` and run it like:

`./mac.py -i eth0 -m 11:22:33:44:55:00`


### Raw Script for 'ifconfig'

```
 ifconfig eth0 down
 ifconfig eth0 hw ether 00:11:22:33:44:55 (this will change the ether prop (MAC address) of the eth0 interface)
 ifconfig eth0 up

```

### Raw script for 'ip a'

```

```

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
