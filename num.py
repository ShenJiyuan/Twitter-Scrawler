#!/usr/bin/env python

import sys

def main():
    
    hillary_total = 2793 + 1656*5000
    trump_total = 1683 + 2150*5000
    
    fin = open('common','r')
    num = 0
    for line in fin:
        num += int(line)
        print 'run\n'
    fin.close()

    fout = open('result','w')
    fout.write('total followers of Hillary = '+str(hillary_total)+'\n')
    fout.write('total followers of Trump = '+str(trump_total)+'\n')
    fout.write('common followers = '+str(num))
    fout.close()

if __name__ == '__main__':
    main()
