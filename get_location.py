
import sys
import tweepy
import pickle
import string
import urllib

def main():
    name = "trump"
    
    # filename 'test000000.pkl' is used as input parameter
    # f = open('test000000.pkl','r')
    infile = sys.argv[1]
    f = open(infile,'r')
    index = infile[5:11]
    page = pickle.load(f)
    
    
    f_location = open('loc', 'w')
    for i in range (0,100):
        id = str(page[i].id)
        if (page[i].location):
            s = page[i].location.encode('utf-8')
            f_location.write(id+'  '+s+'\n')
        '''
            print form
            image = name + "_" + index + "_" + str(i).zfill(2) + "_" + str(id)
            image = "test/" + image
            if (s[8]=="p"):  # remove default images
            urllib.urlretrieve(s,image)
            '''
    
    f_location.close()
    f.close()

if __name__ == "__main__":
    main()