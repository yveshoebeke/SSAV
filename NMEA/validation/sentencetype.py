'''
NMEA.validate.sentencetype

author          Yves Hoebeke - yves.hoebeke@gmail.com
internal        Extracts the GPS navigation sentence type designator.
params          GPS navigation sentence.
returns         GPS navigation sentence type designator.
version         0.1 - 20150314
'''

def NMEA_get_sentence_type(s):
        return s[s.find('$')+3:s.find(',')]
