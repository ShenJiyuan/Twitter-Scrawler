
import googlemaps
import sys
import string
import pickle
import urllib
import json
from datetime import datetime
from collections import OrderedDict


#def main():
#if __name__ == "__main__":
#    main()


def main():
    name = "trump"
    
    gmaps = googlemaps.Client(key='AIzaSyDkhWA0sLFWwi5MY5fJJbH_sBv7eEQsgC4')

    # Geocoding an address
    infile = sys.argv[1]
    f = open(infile,'r')
    index = infile[5:11]
    page = pickle.load(f)
    
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    f_location = open('loc', 'a')
    for i in range (0,100):
        id = str(page[i].id)
        if (page[i].location):
            s = str(page[i].location.encode('utf-8'))
            geocode_result = gmaps.geocode(s)
            if (geocode_result):
                result = geocode_result[0]['address_components']
                num = len(result)
                if (num >= 3):
                    result1 = result[-3]['long_name']
                    result2 = result[-2]['long_name']
                    result3 = result[-1]['long_name']
                    print result1+'    '+result2+'    '+result3
                    if (result1=='United States' or result2=='United States' or result3=='United States'):
                        f_location.write(id+'   '+s+'   '+result1+'    '+result2+'    '+result3+'   '+'true'+'\n')
                    else:
                        f_location.write(id+'  '+s+'false'+'\n')

    f_location.close()
    f.close()

if __name__ == "__main__":
    main()
