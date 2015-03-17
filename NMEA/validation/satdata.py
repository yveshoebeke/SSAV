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

