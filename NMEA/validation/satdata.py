'''
NMEA.validate.satdata

author          Yves Hoebeke - yves.hoebeke@gmail.com
internal        Checks aspects of the data elements and determines if this data is to be considered.
                Acceptable values are as follows:
                        RMC:    Status = 'A' (active), Mode = 'A'|'D' (A=autonomous, D=differential).
                        GGA:    Satellites in view > 2, Fix quality '1'|'2' (1 = GPS fix (SPS) 2 = DGPS fix).
                        GSA:    Selection = 'A' (Automatic), 3Dfix = '2'|'3' (2 = 2D fix 3 = 3D fix).
                        GSV:    Satellites in view > 2.
                        VTG:    Mode = 'A'|'D' (A=autonomous, D=differential).
                The navigation sentence is converted to an array and the elements to be scrutinized
                are defined in a dictionary.
params          GPS navigation sentence, Sentence type, FAA mode flag (since NMEA standard 2.3).
returns         True if criteria is met, else False.
version         0.1 - 20150314
'''
def NMEA_validate_data(s,t,m=True):
        spos = {'RMC': {'status': 2,'FAAmode': 12},
                'GGA': {'fixquality': 6,'satsinview': 7},
                'GSA': {'selection': 1,'3Dfix': 2},
                'GSV': {'satsinview': 3},
                'VTG': {'FAAmode': 9}}
        result = False
        s = s[s.find("$")+1:s.find("*")].split(',')

        if(t in spos):
                if(m == True):
                        if(t == 'RMC' and (s[spos[t]['status']] == 'A' and (s[spos[t]['FAAmode']] == 'A' or s[spos[t]['FAAmode']] == 'D'))):
                                result = True
                        elif(t == 'GGA' and (int(s[spos[t]['satsinview']]) > 2 and (int(s[spos[t]['fixquality']]) == 1 or int(s[spos[t]['fixquality']]) == 2))):
                                result = True
                        elif(t == 'GSA' and s[spos[t]['selection']] == 'A' and (s[spos[t]['3Dfix']] == '2' or s[spos[t]['3Dfix']] == '3')):
                                result = True
                        elif(t == 'GSV' and int(s[spos[t]['satsinview']]) > 2):
                                result = True
                        elif(t == 'VTG' and (s[spos[t]['FAAmode']] == 'A' or s[spos[t]['FAAmode']] == 'D')):
                                result = True
                else:
                        if(t == 'RMC' and s[spos[t]['status']] == 'A'):
                                result = True
                        elif(t == 'GGA' and (int(s[spos[t]['satsinview']]) > 2 and (int(s[spos[t]['fixquality']]) == 1 or int(s[spos[t]['fixquality']]) == 2))):
                                result = True
                        elif(t == 'GSA' and s[spos[t]['selection']] == 'A' and (s[spos[t]['3Dfix']] == '2' or s[spos[t]['3Dfix']] == '3')):
                                result = True
                        elif(t == 'GSV' and int(s[spos[t]['satsinview']]) > 2):
                                result = True
                        elif(t == 'VTG'):
                                result = True

        return result

