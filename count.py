# location: /and/count.py
# aboout: number of common followers of trump and hillary

import sys
import string

def main():
    
    # open files
    infile1 = sys.argv[1]
    infile2 = sys.argv[2]
    hillary = open(infile1,'r')
    trump = open(infile2,'r')
    
    # readlines
    hf = []
    tf = []
    for line in hillary:
        hf.append(line)
    for linee in trump:
        tf.append(linee)

    # close files
    hillary.close()
    trump.close()

    # write and number to 'common'
    hf = set(hf)
    tf = set(tf)
    num = len(hf & tf)
    outfile = open('common','a')
    outfile.write(str(num)+'\n')
    outfile.close()

    print 'done '+infile1+' '+infile2+' '+str(num)


if __name__ == "__main__":
    main()
