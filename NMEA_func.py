#import re
def NMEA_verify_checksum(s):
	csum = 0
	cksum = s[len(s) - 2:]
	#chksumdata = re.sub("(\n|\r\n)","", s[s.find("$")+1:s.find("*")])
	chksumdata = s[s.find("$")+1:s.find("*")]

	for c in chksumdata:
	        csum ^= ord(c)ß

	if hex(csum) == hex(int(cksum, 16)):
	        return True
	else:
	        return False

def NMEA_get_sentence_type(s):
	return s[s.find('$')+3:s.find(',')]

def NMEA_validate_data(s,t,m=True):
	result = False
	if(t == 'GGA'):
		if(s[6] == 1 || s[6] == 2):
			if(s[7] > 2):
				result = True
	elif(t == 'RMC'):
		#etc....
	'''	
	RMC: status = 'A' & mode = 'A' | 'D'
	VTG: mode = 'A' | 'D'
	GGA: Fix quality=1 | 2 & Number of satelites being tracked > 2
	GSA: Auto select = 2 | 3
	GSV: Number of satelites in view > 2
	'''
	return result

def NMEA_get_lat_long(s,t):
	sentence_pos = {'GGA':{'lat':2,'latNS':3,'long':4,'longEW':5},
					'RMC':{'lat':3,'latNS':4,'long':5,'longEW':6}}
	e = s.split(',')
	longlat_tup = e[sentence_pos[t]['lat']]+e[sentence_pos[t]['latNS']],e[sentence_pos[t]['long']]+e[sentence_pos[t]['longEW']]
	return longlat_tup






	msgtype = sentence[3:6]
	print "Message type: " + msgtype
	print "Message elements:"
	print "-----------------"
	print "Time: " + elements[1]
	print "Lat: " + elements[2] + elements[3]
	print "Long: " + elements[4] + elements[5]
	print "Quality: " + elements[6]
	print "No. of Satelites: " + elements[7]
	print "Altitude: " + elements[9] + elements[10]
	print "-----------------"

