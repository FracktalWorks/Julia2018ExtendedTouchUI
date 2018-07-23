import re

txt = """
interface eth0
static ip_address=192.168.1.35/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8 8.8.4.4

# A sample configuration for dhcpcd.
# See dhcpcd.conf(5) for details.

# Allow users of this group to interact with dhcpcd via the control socket.
#controlgroup wheel

# Inform the DHCP server of our hostname for DDNS.
hostname

# Use the hardware address of the interface for the Client ID.
clientid
# or
# Use the same DUID + IAID as set in DHCPv6 for DHCPv4 ClientID as per RFC4361.
#duid

# Persist interface configuration when dhcpcd exits.
persistent

# Rapid commit support.
# Safe to enable by default because it requires the equivalent option set
# on the server to actually work.
option rapid_commit

# A list of options to request from the DHCP server.
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
# Most distributions have NTP support.
option ntp_servers
# Respect the network MTU.
# Some interface drivers reset when changing the MTU so disabled by default.
#option interface_mtu

# A ServerID is required by RFC2131.
require dhcp_server_identifier

# Generate Stable Private IPv6 Addresses instead of hardware based ones
slaac private

# A hook script is provided to lookup the hostname if not set by the DHCP
# server, but it should not be run by default.
nohook lookup-hostname
"""

reEthGlobal = r"interface\s+eth0\s?(static\s+[a-z0-9./_=\s]+\n)*"
reEthAddress = r"static\s+ip_address=([\d.]+)(/[\d]{1,2})?"
reEthGateway = r"static\s+routers=([\d.]+)(/[\d]{1,2})?"

mtEthGlobal = re.search(reEthGlobal, txt)

cbStaticEnabled = False
txtEthAddress = "1"
txtEthGateway = "3"

if mtEthGlobal:
  sz = len(mtEthGlobal.groups())
  cbStaticEnabled = (sz == 1)
  
  if sz == 1:
    mtEthAddress = re.search(reEthAddress, mtEthGlobal.group(0))
    if mtEthAddress and len(mtEthAddress.groups()) == 2:
      txtEthAddress = mtEthAddress.group(1)
    mtEthGateway = re.search(reEthGateway, mtEthGlobal.group(0))
    if mtEthGateway and len(mtEthGateway.groups()) == 2:
      txtEthGateway = mtEthGateway.group(1)
  
  print(cbStaticEnabled)
  print(txtEthAddress)
  print(txtEthGateway)
  
  op = """
  interface eth0
  static ip_address={0}/24
  static routers={1}
  static domain_name_servers=8.8.8.8 8.8.4.4
  """.format(txtEthAddress, txtEthGateway)

  res = re.sub(reEthGlobal, op, txt)
  # print(res)