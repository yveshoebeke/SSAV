def NMEA_get_sentence_type(s):
        return s[s.find('$')+3:s.find(',')]
