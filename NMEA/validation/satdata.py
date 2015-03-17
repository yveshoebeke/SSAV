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

