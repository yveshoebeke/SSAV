def NMEA_get_lat_long(s,t):
        sentence_pos = {'GGA':{'lat':2,'latNS':3,'long':4,'longEW':5},
                                        'RMC':{'lat':3,'latNS':4,'long':5,'longEW':6}}
        e = s.split(',')
        longlat_tup = e[sentence_pos[t]['lat']]+e[sentence_pos[t]['latNS']],e[sentence_pos[t]['long']]+e[sentence_pos[t]['longEW']]
        return longlat_tup

