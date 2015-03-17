def NMEA_verify_checksum(s):
        csum = 0
        cksum = s[len(s) - 2:]
        #chksumdata = re.sub("(\n|\r\n)","", s[s.find("$")+1:s.find("*")])
        chksumdata = s[s.find("$")+1:s.find("*")]

        for c in chksumdata:
                csum ^= ord(c)

        if hex(csum) == hex(int(cksum, 16)):
                return True
        else:
                return False

