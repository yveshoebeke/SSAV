'''
NMEA.validate.checksum

author          Yves Hoebeke - yves.hoebeke@gmail.com
original        Adam Dosh - see: http://doschman.blogspot.com/2013/01/calculating-nmea-sentence-checksums.html
internal        The checksum field consists of a '*' and two hex digits representing an 8 bit exclusive OR of 
                all characters between, but not including, the '$' and '*'.
                Should be run after harvesting the satelite data.
                If checksum validation is not passed the navigation sentence should be discarted.
params          GPS navigation sentence.
returns         True if checksum passes, else False.
version         0.1 - 20150314
'''

def NMEA_verify_checksum(s):
        csum = 0
        cksum = s[len(s) - 2:]
        chksumdata = s[s.find("$")+1:s.find("*")]

        for c in chksumdata:
                csum ^= ord(c)

        if hex(csum) == hex(int(cksum, 16)):
                return True
        else:
                return False

