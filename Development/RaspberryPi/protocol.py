
_CONNECT_PI = 0x01
_DISCONNECT_PI = 0x02
_CONNECT_CLIENT = 0x03
_DISCONNECT_CLIENT = 0x04
_SUBSCRIBE = 0x05
_UNSUBSCRIBE = 0x06
_DATA = 0x07
_GET_LAST = 0x08

def code_information(i, mi, ma, mean, num, ped, time):
	assert type(i) is int, 'Id is not an int'
	assert type(mi) is float, 'Min is not an float'
	assert type(ma) is float, 'Max is not an float'
	assert type(mean) is float, 'Mean is not a float'
	assert type(num) is int, 'Number of cars is not an int'
	assert type(ped) is int, 'Estimation of pedestrian number'
	assert type(time) is int, 'Capture time is not an int'

	string = '%d\t%.1f\t%.1f\t%.1f\t%d\t%d\t%d' % (i,mi,ma,mean,num,ped,time)

	return string