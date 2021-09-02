# Troubleshooting wifi problems

## Resources
### Commands to try running
* list hardware `lshw`, should find the following under `*pci:1`
```
           *-network
                description: Wireless interface
                product: QCA6174 802.11ac Wireless Network Adapter
                vendor: Qualcomm Atheros
                physical id: 0
                bus info: pci@0000:6b:00.0
                logical name: wlp107s0
                version: 32
                serial: 98:22:ef:d0:23:b7
                width: 64 bits
                clock: 33MHz
                capabilities: bus_master cap_list ethernet physical wireless
                configuration: broadcast=yes driver=ath10k_pci driverversion=4.15.0-66-generic firmware=WLAN.RM.4.4.1-00079-QCARMSWPZ-1 ip=192.168.1.107 latency=0 link=yes multicast=yes wireless=IEEE 802.11
                resources: irq:143 memory:6e200000-6e3fffff
```
* restart wifi radio
```
nmcli radio wifi off
nmcli radio wifi on
```
[source](https://askubuntu.com/questions/271387/how-to-restart-wifi-connection)
* replacing wifi card
  * [lenovo hardware maintainence manual](https://download.lenovo.com/consumer/mobiles_pub/yoga920-13ikb_yoga920-13ikbglass_hmm_201709.pdf)
  * [forum on replacing with intel 8265](https://forums.lenovo.com/t5/Lenovo-Yoga-Series-Notebooks/Yoga-920-13IKB-replacing-Qualcomm-Aetheros-with-Intel-AC-8265/td-p/3987716/page/2)

## Log


### 5-Nov-2019
* Restarted computer (Ubuntu -> Ubuntu), wifi card didn't appear on reboot in Ubuntu
* Rebooted, still didn't appear
* opened bottom of computer, removed wifi card and then put it back in. On reboot, it appeared and is working currently

### 14-Dec-2019
* Wifi working fine an hour or so earlier, brought computer out of sleep and while the WiFi select a network option is available, no networks show up
* Running lshw gives the folllowing output:
```
   *-generic DISABLED
		description: Wireless interface
		product: Illegal Vendor ID
		vendor: Illegal Vendor ID
		physical id: 0
		bus info: pci@0000:6b:00.0
		logical name: wlp107s0
		version: ff
		serial: 98:22:ef:d0:23:b7
		width: 32 bits
		clock: 66MHz
		capabilities: bus_master vga_palette cap_list ethernet physical wireless
		configuration: broadcast=yes driver=ath10k_pci driverversion=4.15.0-70-generic firmware=WLAN.RM.4.4.1-00079-QCARMSWPZ-1 latency=255 link=no maxlatency=255 mingnt=255 multicast=yes wireless=IEEE 802.11
		resources: irq:134 memory:6e200000-6e3fffff
```
* Running `nmcli off/on` didn't change anything.
* rebooting corrected the issue
