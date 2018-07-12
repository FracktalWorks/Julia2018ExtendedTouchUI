import re
import subprocess

# txt = """
# # interfaces(5) file used by ifup(8) and ifdown(8)

# # Please note that this file is written to be used with dhcpcd
# # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# # Include files from /etc/network/interfaces.d:
# source-directory /etc/network/interfaces.d

# auto lo
# iface lo inet loopback

# iface eth0 inet manual
# address 10.1.1.30
# netmask 255.255.255.0
# gateway 10.1.1.1

# allow-hotplug wlan0
# iface wlan0 inet dhcp
    # wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

# allow-hotplug wlan1
# iface wlan1 inet manual
    # wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
# """

regex = r"iface[\s]+eth0[\s]+inet[\s]+(\w+)[\s]?\n(address[\s]+([\d.]+)[\s]?\nnetmask[\s]+([\d.]+)[\s]?\ngateway[\s]+([\d.]+))?"
reEthGlobal = r"iface[\s]+eth0[\s]+inet[\s]+(\w+)[\s]?\n([a-zA-Z0-9\s.]+\n)?"
reEthAddress = r"address[\s]+([\d.]+)"
reEthNetmask = r"netmask[\s]+([\d.]+)"
reEthGateway = r"gateway[\s]+([\d.]+)"

txt = subprocess.Popen("cat test.txt", stdout=subprocess.PIPE, shell=True).communicate()[0]
# print(txt)

mtEthGlobal = re.search(reEthGlobal, txt)

cbEnabled = False
txtEthAddress = "1"
txtEthNetmask = "2"
txtEthGateway = "3"

if mtEthGlobal:
  sz = len(mtEthGlobal.groups())
  cbStaticEnabled = mtEthGlobal.group(1) == "static"
  
  if sz > 1:
    mtEthAddress = re.search(reEthAddress, mtEthGlobal.group(0))
    if mtEthAddress and len(mtEthAddress.groups()) == 1:
      txtEthAddress = mtEthAddress.group(1)
    mtEthNetmask = re.search(reEthNetmask, mtEthGlobal.group(0))
    if mtEthNetmask and len(mtEthNetmask.groups()) == 1:
      txtEthNetmask = mtEthNetmask.group(1)
    mtEthGateway = re.search(reEthGateway, mtEthGlobal.group(0))
    if mtEthGateway and len(mtEthGateway.groups()) == 1:
      txtEthGateway = mtEthGateway.group(1)
  
  print(cbStaticEnabled)
  print(txtEthAddress)
  print(txtEthNetmask)
  print(txtEthGateway)
  
  op = "iface eth0 inet static\naddress {0}\nnetmask {1}\ngateway {2}\n\n".format(txtEthAddress, txtEthNetmask, txtEthGateway)
  res = re.sub(reEthGlobal, op, txt)
  file = open("test.txt","w") 
  file.write(res) 
  file.close() 
  
  