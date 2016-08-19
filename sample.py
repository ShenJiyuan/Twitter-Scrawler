#!/usr/bin/env python
# usage: python sample.py k
# files:
#       list:     available indexes
#       index:    sampled indexes
#       id:       sampled ids

import sys
import random
import linecache

def main():
    k = int(sys.argv[1]) # input sample number
    
    # =============================read available  indexes======================______________________test okay
    f_list = open('list', 'r')
    ava_index = []
    for line in f_list.readlines():
        line = line[:-1]
        ava_index.append(line)
    f_list.close()

    # =============================check input parameter========================______________________test okay
    l = len(ava_index)
    if (k > l):
        error = 'Parameter is TOO LARGE. '+str(l)+' available now.'
        print error
        sys.exit(0)

    # ==========================randomly select some indexes====================
    # ======================delete and write both index and id==================______________________test okay
    f_index = open('index', 'a')
    f_id = open('id', 'a')
   
    for d in range(0,k):
        # index in list ava_index --> index
        i = random.randrange(0, l, 1)
        index = ava_index[i]
        del ava_index[i]
        l -= 1
        # write index, get original file name and file line number, write id
        f_index.write(index+'\n')
        index = int(index)
        t1 = index / 5000
        t = index % 5000
        file = 'ids_'+str(t1)
        ident = str(linecache.getline(file, t))
        print ident
        f_id.write(ident+' '+t1+' '+t+'\n')

    f_index.close()
    f_id.close()

    # ================================rewrite the list===========================______________________test okay
    f_list = open('list', 'w')
    for i in ava_index:
        f_list.write(i+'\n')
    f_list.close()

if __name__ == '__main__':
    main()
