
import socket
import struct



_PROTOCOL1 = 0b01010101
_PROTOCOL2 = 0b00110011


def code_1_information(speed):
	assert type(speed) is float, 'The argument given is not a float'

	mess = bytearray([_PROTOCOL1])+struct.pack('f', speed)

	return mess

def code_2_information(num, speeds):
	assert type(num) is int, 'The num argument is not a int'

	mess = bytearray([_PROTOCOL2]) + struct.pack('i', num)
	for s in speeds:
		mess = mess + struct.pack('f', s)

	return mess

def decode(mess):
	assert type(mess) is bytearray, 'The message is not a bytearray'
	if mess[0] == _PROTOCOL1:
		return _decode1(mess[1:])
	elif mess[0] == _PROTOCOL2:
		return _decode2(mess[1:])
	else:
		return None

def _decode1(info):
	rec = struct.unpack('f', info)[0]//.1/10
	return rec

def _decode2(info):
	num = struct.unpack('i', info[:4])
	speeds = []
	for i in range(len(info[4:])/4):
		s = struct.unpack('f', info[4+i*4:8+i*4])[0]//.1/10
		speeds.append(s)

	return num[0], speeds
