#!/usr/bin/python
from NMEA.validation import checksum
from NMEA.validation import sentencetype
from NMEA.validation import satdata

s = '$GPGGA,155722.000,4103.9752,N,07332.0105,W,1,7,1.55,84.5,M,-34.3,M,,*50'
s = '$GPVTG,2.29,T,,M,0.02,N,0.04,K,A*32'
s = '$GPGSA,A,3,02,06,05,25,09,10,29,,,,,,2.33,1.55,1.74*06'
s = '$GPGSV,3,3,11,12,20,228,19,09,17,042,44,26,17,170,19*4D'
s = '$GPRMC,155721.000,A,4103.9752,N,07332.0104,W,0.02,2.29,061214,,,A*7D'

print "Sentence to process: ",s

if(checksum.NMEA_verify_checksum(s) == True):
	print 'checksum is good.'
else:
	print 'checksum failed.'

t = sentencetype.NMEA_get_sentence_type(s)
print "Message type: ",t

d = satdata.NMEA_validate_data(s,t,m=True)
print d
