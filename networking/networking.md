# Networking

Once in a while, i need to make some changes to my networking configuration.

I use Unifi Equipment within my house, specifically,

1. Unifi APs
1. Unifi USG (will be replaced soon)
1. UnifiOS - Network Application -  (with the replacement of the USG in time, hopefully this will be more integrated into the replacement appliance)

## Network setup

I use multiple Vlans for my home network

1. Normal (trusted devices)
1. NoT (Network of Things)
1. IoT (Internet of Things)

### Normal

Range: 192.168.1.0/24

I use this for my trusted devices, like my work machine, home server and other devices I can have a lot control over.

### NoT

Range: 192.168.37.0/25

This is the network I use for my ESPHome and Tasmota type devices, devices which have built by me and I have some limited control over.

### IoT

Range: 192.168.32.0/26

This is the network I use for "off the shelf devices" like Amazon Alexa devices and my TP-Link Tapo devices. THese are devices over which i have no control and VERY limited trust.

## Basic Flow

### Trusted Network Flow

✅ All Other Networks  
✅ Internet

### NoT Flow

✅ Home Assistant Servers  
❌ All Other Networks
❌ Internet  

### IoT Flow

❌ Home Assistant Servers  
❌ All Other Networks  
✅ Internet  

## Loss of Vlans

On occasion, my Unifi Network Application plays up and I can "loose" my vlans, however the routing device (Unifi USG) is still up. If this happens I need to modify some of my networking options to cater for this.

> Windows

```powershell

```

> Home Assistant OS

```bash
nmcli connection modify "Supervisor enp0s25" +ipv4.routes "192.168.37.0/25 192.168.1.254"
nmcli connection modify "Supervisor enp0s25" +ipv4.routes "192.168.32.0/26 192.168.1.254"
```
