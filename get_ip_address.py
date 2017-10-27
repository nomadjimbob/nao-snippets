# Originally code by Alexandre M
# https://community.ald.softbankrobotics.com/en/forum/getting-ip-address-robot-python-5583


import socket
import fcntl
import struct

def get_ip_address(strInterfaceName):
	try:
		sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
		strInterfaceName = strInterfaceName[:15];
		packedInterfaceName = struct.pack('256s', strInterfaceName);
		ret = fcntl.ioctl(sock.fileno(), 0x8915, packedInterfaceName);

		ret = ret[20:24];
		return socket.inet_ntoa( ret );
	except:
		return '';

return get_ip_address('wlan0');	# could also be eth0, eth1
