
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
    
    for i in range (0,100):
        s = str(page[i].profile_image_url_https).replace("_normal.",".")
        form = ""
        flag = 0
        if (s[len(s)-2]=="e"):
            form = ".jpeg"
        else:
            form = ".jpg"
        id = page[i].id
        print form
        image = name + "_" + index + "_" + str(i).zfill(2) + "_" + str(id) + form
        image = "test/" + image
        if (s[8]=="p"):  # remove default images
            urllib.urlretrieve(s,image)

    f.close()

if __name__ == "__main__":
    main()